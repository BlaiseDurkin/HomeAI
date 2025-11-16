#from kitchen.cooking_flow import start_diet
from kitchen.recipes import *
import random
import math

print('recommender.py loaded...')

def test_rec_file():
    print('recommender.py test')

#functions for processing user input related to food
#user data is formatted in previous parsing and processing function

#-------- herlper _----------------
def list_to_print_string(sequence):
    string = ""
    for i in range(len(sequence)):
        if i < len(sequence) - 1:
            string += sequence[i] + ', '
        elif i == len(sequence) - 1 and len(sequence) > 1:
            string += ' and '+sequence[i]

    return string

def statistics(scores):
    if not scores:  # Handle empty list
        return None, None

        # Calculate mean
    mean = sum(scores) / len(scores)

    # Calculate standard deviation
    variance = sum((x - mean) ** 2 for x in scores) / len(scores)
    standard_deviation = math.sqrt(variance)


    minimum = min(scores)
    maximum = max(scores)

    return minimum, maximum, mean, standard_deviation

def mean_and_deviation(scores):
    if not scores:  # Handle empty list
        return None, None

    # Calculate mean
    mean = sum(scores) / len(scores)

    # Calculate standard deviation
    variance = sum((x - mean) ** 2 for x in scores) / len(scores)
    standard_deviation = math.sqrt(variance)
    return mean, standard_deviation
#

def clean_list(list_of_recs):
    for r in range(len( list_of_recs)):
        nr = len(list_of_recs[r])
        for i in range(nr):
            list_of_recs[r][i] = list_of_recs[r][i].strip()
    return list_of_recs

"""
User interaction handling...

Ex: "recommend me a meal"
    -> ask user for additional data
    
    
    
  - recommend multiple meals from list of vegetables  
  - recommend sauce
"""


country_to_region = {
    "United States": "America",
    "America": "America",
    "Canada": "America",
    "Brazil": "America",
    "Mexico": "America",
    "Argentina": "America",
    "United Kingdom": "Europe",
    "Germany": "Europe",
    "France": "Europe",
    "Italy": "Europe",
    "Spain": "Europe",
    "Russia": "Europe",
    "Poland": "Europe",
    "Netherlands": "Europe",
    "Sweden": "Europe",
    "Switzerland": "Europe",
    "China": "EastAsia",
    "Japan": "EastAsia",
    "South Korea": "EastAsia",
    "North Korea": "EastAsia",
    "Korea": "EastAsia",
    "Mongolia": "EastAsia",
    "India": "SouthAsia",
    "Pakistan": "SouthAsia",
    "Bangladesh": "SouthAsia",
    "Sri Lanka": "SouthAsia",
    "Nepal": "SouthAsia",
    "Indonesia": "SouthEastAsia",
    "Thailand": "SouthEastAsia",
    "Vietnam": "SouthEastAsia",
    "Philippines": "SouthEastAsia",
    "Malaysia": "SouthEastAsia",
    "Singapore": "SouthEastAsia",
    "Saudi Arabia": "WestAsia",
    "Iran": "WestAsia",
    "Persian": "WestAsia",
    "Iraq": "WestAsia",
    "Turkey": "WestAsia",
    "Israel": "WestAsia",
    "United Arab Emirates": "WestAsia",
    "Egypt": "WestAsia",
    "Nigeria": "Africa",
    "South Africa": "Africa",
    "Kenya": "Africa",
    "Ethiopia": "Africa",
    "Algeria": "WestAsia",
    "Morocco": "WestAsia",
    "Ghana": "Africa",
    "Australia": "America",  # Note: Australia is often considered its own region but grouped here as per request
    "Colombia": "America",
    "Chile": "America",
    "Ukraine": "Europe",
    "Greece": "Europe",
    "Europe": "Europe",
    "Middle East": "WestAsia",
    "Africa": "Africa",
    "Asia": "EastAsia",
    "Central Asia": "WestAsia",

}


country_to_region = {
    "united states": "America",
    "america": "America",
    "canada": "America",
    "brazil": "America",
    "mexico": "America",
    "argentina": "America",
    "united kingdom": "Europe",
    "germany": "Europe",
    "france": "Europe",
    "italy": "Europe",
    "spain": "Europe",
    "russia": "Europe",
    "poland": "Europe",
    "netherlands": "Europe",
    "sweden": "Europe",
    "switzerland": "Europe",
    "china": "EastAsia",
    "japan": "EastAsia",
    "south korea": "EastAsia",
    "north korea": "EastAsia",
    "korea": "EastAsia",
    "mongolia": "EastAsia",
    "india": "SouthAsia",
    "pakistan": "SouthAsia",
    "bangladesh": "SouthAsia",
    "sri lanka": "SouthAsia",
    "nepal": "SouthAsia",
    "indonesia": "SouthEastAsia",
    "thailand": "SouthEastAsia",
    "vietnam": "SouthEastAsia",
    "philippines": "SouthEastAsia",
    "malaysia": "SouthEastAsia",
    "singapore": "SouthEastAsia",
    "saudi arabia": "WestAsia",
    "iran": "WestAsia",
    "persian": "WestAsia",
    "iraq": "WestAsia",
    "turkey": "WestAsia",
    "israel": "WestAsia",
    "united arab emirates": "WestAsia",
    "egypt": "WestAsia",
    "nigeria": "Africa",
    "south africa": "Africa",
    "kenya": "Africa",
    "ethiopia": "Africa",
    "algeria": "WestAsia",
    "morocco": "WestAsia",
    "ghana": "Africa",
    "australia": "America",  # Note: Australia is often considered its own region but grouped here as per request
    "colombia": "America",
    "chile": "America",
    "ukraine": "Europe",
    "greece": "Europe",
    "europe": "Europe",
    "middle east": "WestAsia",
    "africa": "Africa",
    "asia": "EastAsia",
    "central asia": "WestAsia",
}

adjective_to_region = {
    "american": "America",  # United States
    "canadian": "America",
    "brazilian": "America",
    "mexican": "America",
    "argentine": "America",  # or Argentinian
    "british": "Europe",  # United Kingdom
    "german": "Europe",
    "french": "Europe",
    "italian": "Europe",
    "spanish": "Europe",
    "russian": "Europe",
    "polish": "Europe",
    "dutch": "Europe",  # Netherlands
    "swedish": "Europe",
    "swiss": "Europe",  # Switzerland
    "chinese": "EastAsia",
    "japanese": "EastAsia",
    "south korean": "EastAsia",
    "north korean": "EastAsia",
    "korean": "EastAsia",
    "mongolian": "EastAsia",
    "indian": "SouthAsia",
    "pakistani": "SouthAsia",
    "bangladeshi": "SouthAsia",
    "sri lankan": "SouthAsia",
    "nepalese": "SouthAsia",
    "indonesian": "SouthEastAsia",
    "thai": "SouthEastAsia",
    "vietnamese": "SouthEastAsia",
    "filipino": "SouthEastAsia",  # or Philippine
    "malaysian": "SouthEastAsia",
    "singaporean": "SouthEastAsia",
    "arabian": "WestAsia",
    "saudi": "WestAsia",  # or Saudi Arabian
    "iranian": "WestAsia",  # Persian also used, but "Iranian" is the standard demonym
    "persian": "WestAsia",
    "iraqi": "WestAsia",
    "turkish": "WestAsia",
    "israeli": "WestAsia",
    "emirati": "WestAsia",  # United Arab Emirates
    "egyptian": "WestAsia",
    "nigerian": "Africa",
    "south african": "Africa",
    "zambian": "Africa",
    "kenyan": "Africa",
    "ethiopian": "Africa",
    "algerian": "WestAsia",
    "moroccan": "WestAsia",
    "ghanaian": "Africa",
    "australian": "America",  # Grouped as per previous request
    "colombian": "America",
    "chilean": "America",
    "ukrainian": "Europe",
    "greek": "Europe",
    "european": "Europe",
    "middle eastern": "WestAsia",
    "african": "Africa",
    "asian": "EastAsia",
    "central asian": "WestAsia"
}
region_reps = {'EastAsia': ['chinese'],
               'SouthEastAsia': ['thai'],
               'SouthAsia': ['indian'],
               'WestAsia': ['persian'],
               'Europe': ['italian'],
               'Africa': ['african'],
               'America': ['mexican']}

#key features
"""
    - spicy -> drop all items with spice > 2
    - vegan -> drop all items not vegan
"""
def extrapolate_user_input():
    vague_items = ['meat', 'fish']


def RecipeVariations(region, meal, diet):
    #TODO - change diet to -> set_of_user_inputs and set_of_allergies

    # when is the meal essentially the same?
    # - meat exchange
    #   if (EAsia or SEAsia) and vegan --> create tofu variation
    #   if (WAsia) --> steak = lamb = chicken = fish = shrimp = chickpeas = lentils
    #   if (Europe) --> pork = steak = lamb = chicken = fish = shrimp
    #
    #
    meat_exchanges = {'WestAsia': ['steak', 'lamb', 'chicken', 'fish', 'shrimp'],
                      'SouthAsia': ['lamb', 'chicken', 'fish', 'shrimp'],
                      'SouthEastAsia': ['chicken', 'fish', 'shrimp', 'steak', 'pork'],
                      'EastAsia': ['chicken', 'fish', 'shrimp', 'steak', 'pork', 'lamb'],
                      'Europe': ['chicken', 'fish', 'shrimp', 'steak', 'pork', 'lamb'],
                      'Africa': ['chicken', 'fish', 'shrimp', 'steak', 'pork', 'lamb'],
                      'America': ['chicken', 'fish', 'shrimp', 'steak', 'pork', 'lamb'],
                      }
    meat_subsitutes = {'WestAsia': ['lentils', 'chickpeas'],
                       'SouthAsia': ['lentils', 'chickpeas', 'cheese', 'mushroom'],
                       'SouthEastAsia': ['lentils', 'green_beans', 'tofu', 'soy_beans', 'mushroom'],
                       'EastAsia': ['green_beans', 'tofu', 'soy_beans', 'mushroom'],
                       'Europe': ['green_beans', 'cheese', 'mushroom'],
                       'Africa': ['soy_meat', 'beans'],
                       'America': ['beans', 'mushroom']
                       }

    animal_products = ['lard', 'ghee', 'butter', 'egg', 'chicken', 'steak','beef', 'pork', 'lamb', 'fish', 'shrimp', 'tuna', 'salmon', 'clam', 'cheese', 'yogurt', 'honey']
    not_vegetarian_products = ['lard', 'chicken', 'steak', 'beef', 'pork', 'lamb']
    dairy = ['yogurt', 'cheese']
    meats = ['chicken', 'fish', 'shrimp', 'steak', 'pork', 'lamb', 'salmon', 'tuna']
    cooking_mediums = ['butter', 'ghee', 'lard']

    vegan = False
    vegetarian = False
    meat_lover = False

    if diet != None:
        if diet['vegan']:
            vegan = True
        elif diet['vegetarian']:
            vegetarian = True
        elif diet['meat_lover']:
            meat_lover = True
    og_meal = []
    omitted_ingredients = []
    variations = []
    for ing in meal:
        if (vegetarian and ing in not_vegetarian_products) or (vegan and ing in animal_products):
            #add to list of
            omitted_ingredients.append(ing)
        else:
            if ing in meats:
                if meat_lover:
                    og_meal.append(ing)
            else:
                og_meal.append(ing)

    num_vars = 0
    new_ingredients = []
    for ing in omitted_ingredients:
        #swap for? dairy -> sauce, cooking_medium -> oil, meat -> meat_subs
        if ing in dairy:
            #add sauce
            new_ingredients.append('sauce')
        elif ing in cooking_mediums:
            #add oil
            new_ingredients.append('oil')
        elif ing in meats:
            for meat_sub in meat_subsitutes[region]:
                if not(vegan and meat_sub == 'cheese'):
                    variations.append(meat_sub)

    if not (vegetarian or vegan):
        #was there meat in
        for meat in meat_exchanges[region]:
                variations.append([meat])
            #for each subsitutue
                #make variation

    for variation in variations:
        variation += new_ingredients + og_meal

    return variations


def coverage(user_set, meal):
    #return % of user_set in meal
    cov = 0
    for ing in user_set:
        if ing in meal:
            cov += 1/len(user_set)
    return cov

# (1) find best match given user data
def find_suggestions_from_food_list(diet):
    #score each region with user_list : list of <str> ingredients
    # meal : list of <str> ingredients
    user_set = diet['ingredients']
    country = diet['preference']
    favorite_region = ''
    if country in country_to_region:
        favorite_region = country_to_region[country]
    if country in adjective_to_region:
        favorite_region = adjective_to_region[country]
    canidates = []
    scores = []

    region_scores = {}
    region_perfect_scores = {}
    top_meal = None
    top_meal_region = None
    top_score = 0
    max_region_score = 0
    for region, region_list in RegionRecipes.items():
        region_list = clean_list(region_list)
        region_perfect_scores[region] = 0
        region_score = 0
        for OG_meal in region_list:
            #meal_variations = RecipeVariations(OG_meal)

            score = coverage(user_set, OG_meal) # ~(0,1)
            if score >.75:
                region_perfect_scores[region] = 1

            if region == favorite_region:
                score += 0.15

            region_score += score**2
            if score > top_score:
                top_score = score
                top_meal = OG_meal
                top_meal_region = region
            canidates.append(OG_meal)
            scores.append(score)
        region_scores[region] = region_score
        if region_score > max_region_score:
            max_region_score = region_score
    #print(top_meal)
    #print(region_scores)
    f_l = math.sqrt(len(diet['ingredients']))
    if len(diet['ingredients']) < 1:
        f_l = 1
    n = sum(region_perfect_scores.values())#number of regions with perfect match
    #print(n)
    g_n = ((n - 1.15 )** 2)/1.5 + .8
    confinence = max(scores) / (f_l * g_n)
    #print('confidence: ',confinence)
    return region_scores, top_meal,top_meal_region, canidates, scores, confinence


def kosherize(meal, diet):
    print('kosherizing...')
    #check if allergies
    meat_subsitutes = {'WestAsia': ['lentils', 'chickpeas'],
                       'SouthAsia': ['lentils', 'chickpeas', 'cheese', 'mushroom'],
                       'SouthEastAsia': ['lentils', 'green_beans', 'tofu', 'soy_beans', 'mushroom'],
                       'EastAsia': ['green_beans', 'tofu', 'soy_beans', 'mushroom'],
                       'Europe': ['green_beans', 'cheese', 'mushroom'],
                       'Africa': ['soy_meat', 'beans'],
                       'America': ['beans', 'mushroom']
                       }
    animal_products = ['lard', 'ghee', 'butter', 'egg', 'chicken', 'steak','goat', 'beef', 'pork', 'lamb', 'fish', 'shrimp',
                       'tuna', 'salmon', 'clam', 'cheese', 'yogurt', 'honey']
    not_vegetarian_products = ['lard', 'chicken', 'steak', 'goat', 'beef', 'pork', 'lamb']
    dairy = ['yogurt', 'cheese']
    meats = ['chicken', 'fish', 'shrimp', 'steak', 'goat', 'pork', 'lamb', 'salmon', 'tuna']
    cooking_mediums = ['butter', 'ghee', 'lard']

    vegan = diet['diet']['vegan']
    vegetarian = diet['diet']['vegetarian']
    meat_lover = False

    final_recipe = []
    omitted_ingredients = []
    for word in meal:
        if not word in diet['allergies'] and not (vegan and word in animal_products) and not (vegetarian and word in not_vegetarian_products):
            final_recipe.append(word)
        else:
            omitted_ingredients.append(word)
    region = get_region_from_meal(meal)
    for word in omitted_ingredients:
        if word in dairy:
            final_recipe.append('sauce')
        elif word in cooking_mediums:
            final_recipe.append('oil')
        elif word in meats:
            meat_sub = random.choice(meat_subsitutes[region])
            if not (vegan and meat_sub == 'cheese'):
                final_recipe.append(meat_sub)
            else:
                final_recipe.append((meat_subsitutes[region].index(meat_sub) + 1)%len(meat_subsitutes))


    return final_recipe

def get_region_from_meal(meal):
    regions = ['Wasia', 'Easia', 'SEAsia', 'SAsia', 'Mex', 'Africa', 'Europe']
    print('getting region from meal...')
    print('list???',meal)
    subset = food_df[food_df['item'].isin(meal)]

    region_sums = subset[regions].sum()
    reg_map = {'Wasia': 'WestAsia', 'Easia': 'EastAsia', 'SEAsia': 'SouthEastAsia', 'SAsia': 'SouthAsia', 'Mex': 'America', 'Africa': 'Africa', 'Europe': 'Europe'}
    print('region???',reg_map[region_sums.idxmax()])
    # Return the region with the maximum sum
    return reg_map[region_sums.idxmax()]

#TODO fix this
def make_meal_with_diet(diet, graph):

    region_scores, top_meal, top_meal_region, candidates, scores, confidence = find_suggestions_from_food_list(diet)

    # if change --> select 2nd choice

    if top_meal_region == None:
        graph.current_node = graph.all_nodes[0]
        recipe = give_super_random_meal()
        recipe = kosherize(recipe, diet)
        graph.recipe = recipe
        return recipe


    graph.current_node = graph.all_nodes[0]
    top_meal = kosherize(top_meal, diet)
    graph.recipe = top_meal
    return top_meal

# (2) suggest meal recommendation given minimal data
def give_random_meal(diet, graph):
    print('Giving random meal...')

    region = ''
    if diet['preference'] != '':
        if diet['preference'] in adjective_to_region.keys():
            region = adjective_to_region[diet['preference']]
        if diet['preference'] in country_to_region.keys():
            region = country_to_region[diet['preference']]
    if region != '':
        return give_random_meal_from_(region)
    return give_super_random_meal()

def give_random_meal_from_(region):
    print('Giving random meal from',region,'...')
    return random.choice(RegionRecipes[region])



# (3) create meal using flavor model
def invent_meal(diet, graph):
    print('Inventing meal...')
    # which direction given data? region, ingredients, both?
    recipe = make_meal_with_diet(diet, graph)
    # TODO recipe probably returns None or empty list
    return recipe


def change_meal(diet, KAG):
    #if new data --> recommend_meal(data += data) & hope the same meal doesnt get chosen
    print('Changing meal...')
    og_meal = KAG.recipe
    #print('og_meal: ', og_meal)
    #diet = KAG.diet   !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! the bug
    new_meal = recommend_meal(diet, KAG, change=True)
    if new_meal == og_meal:
        return kosherize(give_random_meal(diet, KAG), diet)
    #print('should be different:', new_meal)
    return new_meal

def explain_item(diet, graph):
    print('Explaining item')
    return 'what, do you not, understand, just, add, ' + graph.recipe[graph.recipe_index]

def explain_meal(diet, KAG):
    print('Explaining meal...')
    # item = read ingredient[0]
    KAG.recipe_index = 0
    #return 'first add the ' + item
    return 'first, add, '+ KAG.recipe[KAG.recipe_index]

def say_next_item(diet, graph):
    if graph.recipe_index < len(graph.recipe) - 1:
        graph.recipe_index += 1
    return 'then, add, ' + graph.recipe[graph.recipe_index]

def say_previous_item(diet, graph):
    if graph.recipe_index > 0:
        graph.recipe_index -= 1
    return 'add, ' + graph.recipe[graph.recipe_index]

def say_same_item(diet, graph):
    return 'add, ' + graph.recipe[graph.recipe_index]

def asking_swap_item(diet, graph):
    return 'do you, want, me to, replace, '  + graph.recipe[graph.recipe_index]

def add_shit(diet, graph):
    return "no, i, will not, add, "+list_to_print_string(diet['ingredients'])
def sorry_dave(diet, graph):
    return "sorry, but, i, can not, do, that"

def repeat_meal(diet, KAG):
    print('Repeating meal...')
    print('KAG: ', KAG)
    print('recipe: ',KAG.recipe)
    return KAG.recipe

def say_modified_recipe(diet, graph):
    graph.recipe[graph.recipe_index] = diet['ingredients'][0]
    return "here, is your, new recipe, "+list_to_print_string(graph.recipe)

def ask_user_for_new_item(diet, graph):
    graph.all_nodes[4].expected_words = food_ingredients
    return "tell me, the, new, item"

def ask_user_for_ingredients(diet, graph):
    print('asking for ingredients...')
    graph.all_nodes[2].expected_words = food_ingredients
    response = 'do you, want, to use, certain ingredients'
    return response

def ask_user_max_separability(region_scores):
    print("asking question to compare")
    pair = get_compair_pair(region_scores)
    response = 'do you, prefer, '+pair[0]+', or, '+pair[1]+' food'
    return response, pair

def set_preference(pair, graph):
    expected_words = pair
    node_index = 3
    graph.all_nodes[node_index].expected_words = expected_words

def asking_to_compair(graph, region_scores):
    response, pair = ask_user_max_separability(region_scores)
    set_preference(pair, graph)
    return response




def ask_user_to_invent_meal(user_data):
    print("asking to invent meal...")
    print('user_data: ', user_data, type(user_data))
    bad = ''
    good = ''
    if len(user_data['allergies']) > 0:
        i = 0
        while i < len(user_data['allergies']):
            bad += 'no '+user_data['allergies'][i]
            if i < len(user_data['allergies']) - 1:
                bad += ' and, '
            i += 1
    if len(user_data['ingredients']) > 0:
        i = 0
        while i < len(user_data['ingredients']):
            good += user_data['ingredients'][i]
            if i < len(user_data['ingredients']) - 1:
                good += ' and, '
            i += 1
    res = "do you, want me, to create one "
    has_good = False
    if len(good) > 0:
        res += 'with, '+good
        has_good = True
    if len(bad) > 0:
        if has_good:
            res += ' and, '
        res += 'with, '+bad

    return res


def give_super_random_meal():
    print('giving super random meal...')
    random_key = random.choice(list(RegionRecipes.keys()))
    random_recipe = random.choice(RegionRecipes[random_key])
    print('random recipe: ',random_recipe)
    return random_recipe

def get_compair_pair(region_scores):
    #top 2 regions
    top_2 = sorted(region_scores, key=region_scores.get, reverse=True)[:2]
    canidate1 =random.choice(region_reps[top_2[0]])
    canidate2 = random.choice(region_reps[top_2[1]])
    return [canidate1, canidate2]

#fulfill user request

#TODO --
# - if new diet has ingredients then replace old ingredients
# - else
def recommend_meal(diet, graph, change=False, fresh=False):
    print('recommending meal...')
    #print('diet: ', diet)
    #ToDO
    # 1) ask_for_ing
    # 2) if exist multiple region canidates --> ask preference
    region = ''
    if diet['preference'] != '':
        if diet['preference'] in adjective_to_region.keys():
            region = adjective_to_region[diet['preference']]
        if diet['preference'] in country_to_region.keys():
            region = country_to_region[diet['preference']]
    ask_preference_node_index = 3
    graph.all_nodes[ask_preference_node_index].expected_words = []
    prob_ask = 0
    if not change:
        #graph.diet = start_diet #reset diet ?????????? maybe dont do this ????????
        pass
    else:
        # clear diet ingredients if they dont align with preference
        if diet['preference'] != '':
            graph.diet['ingredients'] = []
        prob_ask += .2
    if len(diet['ingredients']) > 0 or fresh:
        print('clearing diet...')
        print('d1: ',hex(id(diet)))
        print('d2: ',hex(id(graph.diet)))
        graph.diet['ingredients'] = []

    #TODO:
    # - condition A: diet = update_diet
    # - condition B: graph.diet = update_diet
    diet = graph.update_diet(diet) #change to diet?????
    if len(diet['ingredients']) == 0 and len(graph.diet['ingredients']) == 0: #change to include graph.diet??????
        print('no ingredients')
        if diet['preference'] == '':
            prob_ask += .45

            if random.random() < prob_ask:
                # ask ingredients
                graph.current_node = graph.all_nodes[2]
                return ask_user_for_ingredients(diet, graph)
            else:
                #super random
                graph.current_node = graph.all_nodes[0]
                recipe = give_super_random_meal()
                recipe = kosherize(recipe, diet)
                graph.recipe = recipe
                return recipe
        else:
            if region != '':
                graph.current_node = graph.all_nodes[0]
                recipe = give_random_meal_from_(region)
                recipe = kosherize(recipe, diet)
                graph.recipe = recipe
                return recipe

    region_scores, top_meal, top_meal_region, candidates, scores, confidence = find_suggestions_from_food_list(diet)

    # if change --> select 2nd choice

    if random.random() > confidence:
        #ask question ~ invent or preferenace
        if diet['preference'] == '' and graph.diet['preference'] == '':
            graph.current_node = graph.all_nodes[3]
            return asking_to_compair(graph, region_scores)

        if len(diet['ingredients']) > 1 and max(scores) < .9:
            #ask to invent
            graph.current_node = graph.all_nodes[1]
            return ask_user_to_invent_meal(diet)



    if top_meal_region == None:
        graph.current_node = graph.all_nodes[0]
        recipe = give_super_random_meal()
        recipe = kosherize(recipe, diet)
        graph.recipe = recipe
        return recipe

    if change:
        graph.current_node = graph.all_nodes[0]
        top_3 = sorted(zip(scores, candidates), reverse=True)[:3]
        top_candidates = [candidate for score, candidate in top_3]
        if top_candidates[0] == graph.recipe:
            top_meal = top_candidates[1]
        else:
            top_meal = top_candidates[0]
        top_meal = kosherize(top_meal, diet)
        graph.recipe = top_meal
        return top_meal

    graph.current_node = graph.all_nodes[0]
    top_meal = kosherize(top_meal, diet)
    graph.recipe = top_meal
    return top_meal





#nodes: all_nodes = [gave_meal, asked_user_if_invent_meal, asked_for_ingredients, asked_user_to_compare]


def sassy_response(d, g):
    return "ok, maybe, think, before you, speak"








# -------------------test--------------------------
"""
test RecipeVariations(region, meal, diet)

test give_random_meal function
test ask_user_for_ingredients function
test recommend_meal function
"""


#user_list = ['ginger', 'soy_sauce']
#test_diet = {'ingredients': user_list, 'allergies': []}
#recommend_meal(test_diet, graph)
#todo - apply user preference weights to regions
#   - if user known -> use their preferences, else use average preferences
#
# todo
#   - diet = {include, allergy, preference



# ??????
# users state in food recommender program - where is user in assembly line?