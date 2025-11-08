
from kitchen.recommender import *
from kitchen.recipes import *
#test_rec_file()


# ------- helper function --------
def diet_union(d1, d2):
    for key in d1.keys():
        if key in d2.keys():
            if type(d2[key]) == list:
                d2[key] = set(d1[key]) | set(d2[key]) #union
                d2[key] = list(d2[key])
    return d2

def list_to_print_string(sequence):
    string = ""
    for i in range(len(sequence)):
        if i < len(sequence) - 1:
            string += sequence[i] + ', '
        elif i == len(sequence) - 1 and len(sequence) > 1:
            string += ' and '+sequence[i]
    return string

# ----------------- Graph -------------------------
class KitchenAssistantGraph:
    #TODO: add timeout --> return to default node

    def __init__(self, diet):
        #TODO : current_node = start node <-- default: recommend meal
        self.diet = diet #TODO clear each day
        self.current_node = None
        self.recipe = None #TODO clear each day
        self.all_nodes = []
        self.recipe_index = 0


    def update_diet(self, diet):
        self.diet = diet_union(diet, self.diet)
        return self.diet

    def update_current_node(self, current_node):
        self.current_node = current_node

    def update(self, message):
        print("Updating Kitchen Assistant Graph")
        #   message.params = words in set of expected words
        response = self.current_node.update(message)
        # did this fix it??????
        #TODO fix this -> if response ~ recipe then self.recipe = response
        # if response type is recipe -> self.recipe = response
        if type(response) == list:
            self.recipe = response
            response = list_to_print_string(response)
        print('update response: ',response)
        return response

#  ------------------ Node --------------------

class SubNode:
    #TODO add timeout --> return time out to graph

    def __init__(self,expected_words, function_map, graph):
        self.expected_words = expected_words
        #TODO expected words gets reduced by sentiment
        self.map = function_map
        self.graph = graph

    def process_input(self, params):
        diet = params['diet']
        diet = self.graph.update_diet(diet)

        expected_words = params['expected'] #todo : create map: senitment to expected words
        print('processing input...')
        print('key words: ',expected_words)
        key = ''
        for word in expected_words:
            if word in self.map.keys():
                key = word
        return key

    def update(self, message):
        key = self.process_input(message.params)
        print('node update: ',key)
        if not key in self.map.keys():
            return ''

        self.graph.current_node = self.map[key][1]
        response = self.map[key][0](self.graph.diet, self.graph)
        print('node update: ',response)
        return response


# ----------------- init --------------------------
is_vegan = False
is_vegetarian = False
is_allergic = False
is_pescetarian = True #Todo fix this

start_diet = {'ingredients': [], 'allergies': [], 'diet': {'vegan':is_vegan, 'vegetarian': is_vegetarian, 'pescetarian': is_pescetarian, 'allergic': is_allergic}} #TODO add: feature_weight = {'meat' : -10 }
KAG = KitchenAssistantGraph(start_diet)


# --------------- Create Nodes ---------------------------------------
print('before fail')

asked_user_if_invent_meal = SubNode(['yes', 'no'], {'yes': [invent_meal], 'no': [give_random_meal]}, KAG)

gave_meal = SubNode(['change', 'explain', 'repeat'], {'change': [change_meal], 'explain': [explain_meal], 'repeat': [repeat_meal]}, KAG)

asked_user_to_compare = SubNode([''], {'': [recommend_meal]}, KAG) #todo change function -> update

asked_for_ingredients = SubNode([''], {'': [recommend_meal]}, KAG) #todo : add default_key maps to recommend meal, default_key triggered by any ingredient or adjective{country, diet...}

explaining_recipe = SubNode(['next', 'back'], {'next': [say_next_item], 'back': [say_previous_item]}, KAG)

recommend_meal_node = SubNode([''], {'': [recommend_meal]}, KAG)



# ----- edges ---------------
asked_user_if_invent_meal.map['yes'].append(gave_meal) #next node
asked_user_if_invent_meal.map['no'].append(gave_meal)  #next node

gave_meal.map['change'].append(gave_meal) #next node
gave_meal.map['explain'].append(explaining_recipe) # next node
gave_meal.map['repeat'].append(gave_meal) # next node

asked_user_to_compare.map[''].append(recommend_meal_node) #next node

asked_for_ingredients.map[''].append(recommend_meal_node) #next node

explaining_recipe.map['next'].append(explaining_recipe)
explaining_recipe.map['back'].append(explaining_recipe)

#recommend_meal_node.map[''].append(KAG.current_node) # this doesnt work
recommend_meal_node.map[''].append(recommend_meal_node)

#-------------------------------------------------------------------

all_nodes = [gave_meal, asked_user_if_invent_meal, asked_for_ingredients, asked_user_to_compare]
KAG.all_nodes = all_nodes


#TODO explain sauce

