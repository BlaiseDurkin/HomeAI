
from kitchen.recommender import *
from kitchen.recipes import *
#test_rec_file()


# ------- helper function --------
def diet_union(d1, d2):
    print('diet union...')
    print('og diet: ', d2)
    print('new diet: ', d1)
    d3 = {'ingredients': [], 'allergies': [], 'diet': {'vegan': False, 'vegetarian': False, 'pescetarian': False, 'allergic': False}, 'preference':''}
    for key in d1.keys():
        if key in d2.keys():
            if type(d1[key]) == list:
                #d2[key] = set(d1[key]) | set(d2[key]) #union
                #d2[key] = list(d2[key])
                d3[key] = list(set(d1[key]) | set(d2[key]))
            elif type(d1[key]) == dict:
                for label in d1[key].keys():
                    d3[key][label] = d2[key][label] or d1[key][label]


            elif type(d1[key]) == str:
                if d1[key] != '':
                    d3[key] = d1[key]
                else:
                    d3[key] = d2[key]
    #print('newer diet: ', d2)
    return d3

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
        self.parent_recipe = None
        self.all_nodes = []
        self.recipe_index = 0
        self.holiday_themed = False
        self.holiday_name = ""


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
        #print('update response: ',response)
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
        self.graph.diet = self.graph.update_diet(diet) #bugggggggggggggggggggggggggggggggggggg
        print('d1: ', hex(id(diet)))
        print('gd2: ', hex(id(self.graph.diet)))
        print('gd: ',self.graph.diet['ingredients'])

        expected_words = params['expected'] #todo : create map: senitment to expected words
        print('processing input...')
        print('key words: ',expected_words)
        key = ''
        for word in expected_words:
            if word in self.map.keys():
                key = word
        return key, diet

    def update(self, message):
        key, diet = self.process_input(message.params)
        #print('node update: ',key)
        if not key in self.map.keys():
            if '' in self.map.keys():
                key = ''
            else:
                return ''

        self.graph.current_node = self.map[key][1]
        response = self.map[key][0](diet, self.graph)
        #print('node update: ',response)
        return response


# ----------------- init --------------------------
is_vegan = False
is_vegetarian = False
is_allergic = False
is_pescetarian = False

start_diet = {'ingredients': [], 'allergies': [], 'diet': {'vegan':is_vegan, 'vegetarian': is_vegetarian, 'pescetarian': is_pescetarian, 'allergic': is_allergic}, 'preference':''} #TODO add: feature_weight = {'meat' : -10 }
KAG = KitchenAssistantGraph(start_diet)


# --------------- Create Nodes ---------------------------------------

# TODO
#   - output recipe name!
#   --> name = bread, pie, dumplinmg, carb+veg+protein
#   - hungry hello " i want to eat" --> hungryHello() {self.graph = kag; response = "what ingredients do you have" | "what are you in the mood for"


asked_user_if_invent_meal = SubNode(['yes', 'no'], {'yes': [invent_meal], 'no': [give_random_meal]}, KAG)

gave_meal = SubNode(['change', 'explain', 'repeat', 'add', 'back'], {'change': [change_meal], 'explain': [explain_meal], 'repeat': [repeat_meal], 'add': [add_shit], 'back': [recipe_back]}, KAG)

asked_user_to_compare = SubNode([], {'': [recommend_meal]}, KAG) #todo change function -> update

asked_for_ingredients = SubNode([''], {'': [recommend_meal]}, KAG) #todo : add default_key maps to recommend meal, default_key triggered by any ingredient or adjective{country, diet...}

explaining_recipe = SubNode(['next', 'back', 'repeat', 'everything', 'explain', 'add', 'change'], {'next': [say_next_item], 'back': [say_previous_item], 'repeat': [say_same_item], 'everything': [repeat_meal], 'explain': [explain_item], 'add': [add_shit], 'change': [asking_swap_item]}, KAG)

recommend_meal_node = SubNode([''], {'': [recommend_meal]}, KAG)

asked_user_if_swap_item = SubNode(['yes', 'no'], {'yes': [ask_user_for_new_item], 'no': [sassy_response]}, KAG)

asked_for_new_item = SubNode([''], {'': [say_modified_recipe]}, KAG)

asked_if_holiday = SubNode(['yes', 'no'], {'yes': [recommend_holiday_meal], 'no': [recommend_meal_no_holiday]}, KAG)

# ----- edges ---------------
asked_user_if_invent_meal.map['yes'].append(gave_meal) #next node
asked_user_if_invent_meal.map['no'].append(gave_meal)  #next node

gave_meal.map['change'].append(gave_meal) #next node
gave_meal.map['explain'].append(explaining_recipe) # next node
gave_meal.map['repeat'].append(gave_meal) # next node
gave_meal.map['add'].append(gave_meal) # next node
gave_meal.map['back'].append(gave_meal)


asked_user_to_compare.map[''].append(recommend_meal_node) #next node

asked_for_ingredients.map[''].append(recommend_meal_node) #next node

explaining_recipe.map['next'].append(explaining_recipe)
explaining_recipe.map['back'].append(explaining_recipe)
explaining_recipe.map['repeat'].append(explaining_recipe)
explaining_recipe.map['everything'].append(gave_meal)
explaining_recipe.map['explain'].append(explaining_recipe)
explaining_recipe.map['add'].append(explaining_recipe)
explaining_recipe.map['change'].append(asked_user_if_swap_item)



recommend_meal_node.map[''].append(recommend_meal_node)

asked_user_if_swap_item.map['yes'].append(asked_for_new_item) # new node
asked_user_if_swap_item.map['no'].append(gave_meal) #new node

asked_for_new_item.map[''].append(gave_meal) #new node

asked_if_holiday.map['yes'].append(gave_meal)
asked_if_holiday.map['no'].append(gave_meal)
#-------------------------------------------------------------------

all_nodes = [gave_meal, asked_user_if_invent_meal, asked_for_ingredients, asked_user_to_compare, asked_for_new_item, asked_if_holiday]
KAG.all_nodes = all_nodes

#-----------------------------------------------------------------
#TODO explain sauce or processed item
# - same as explain recipe

"""
european pesto = ['nut', 'olive_oil', 'salt', 'garlic', 'basil']
west asia ['lemon', 'garlic', 'parsley', 'salt']
south asia ['cashew', ''] 
"""



#recommend_sauce - random or ask_for_country or ask_for_compliment

