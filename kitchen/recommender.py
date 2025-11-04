from kitchen.cooking_flow import list_to_print_string, KAG
from recipes import *
import random
import math

#functions for processing user input related to food
#user data is formatted in previous parsing and processing function

#-------- herlper _----------------
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
                if not(vegan and meat_subsitutes[region][meat_sub] == 'cheese'):
                    variations.append([meat_subsitutes[region][meat_sub]])

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
def find_suggestions_from_food_list(user_set):
    #score each region with user_list : list of <str> ingredients
    # meal : list of <str> ingredients

    canidates = []
    scores = []

    region_scores = {}
    top_meal = None
    top_meal_region = None
    top_score = 0
    max_region_score = 0
    for region, region_list in RegionRecipes.items():
        region_list = clean_list(region_list)

        region_score = 0
        for OG_meal in region_list:
            #meal_variations = RecipeVariations(OG_meal)
            score = coverage(user_set, OG_meal)
            region_score += score
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
    return region_scores, top_meal,top_meal_region, canidates, scores

def make_meal_with_diet(diet):
    region_scores, top_meal, top_meal_region, canidates, scores = find_suggestions_from_food_list(diet["ingredients"])
    #use top_meal
    final_recipe = []
    for word in top_meal:
        if not word in diet["allergies"]:
            final_recipe.append(word)
    return final_recipe


# (2) suggest meal recommendation given minimal data
def give_random_meal(diet):
    print('Giving random meal...')

    #TODO - move current_node to gave_random
    """
    give random meal if allergies -> swap
    current_node = gave_meal
    """
    #this is not super random... should have region

def give_random_meal_from_(region):
    return random.choice(RegionRecipes[region])



# (3) create meal using flavor model
def invent_meal(diet):
    print('Inventing meal...')
    # which direction given data? region, ingredients, both?
    recipe = make_meal_with_diet(diet)
    # TODO recipe probably returns None or empty list
    return recipe


def change_meal(diet):
    #if new data --> recommend_meal(data += data) & hope the same meal doesnt get chosen
    og_meal = KAG.recipe
    new_meal = just_call_recommend(diet)
    if new_meal == og_meal:
        return
    pass

def explain_meal(diet):
    pass

def repeat_meal(diet):
    return list_to_print_string(KAG.recipe)

def just_call_recommend(diet):
    return recommend_meal(diet, KAG)

def say_next_item(diet):
    pass
def say_previous_item(diet):
    pass


def ask_user_for_ingredients(diet):
    print('asking for ingredients...')
    #TODO move node on graph
    response = 'do you, want, to use, certain ingredients'
    return response


def ask_user_max_separability(pair):
    print("asking question to compare")
    #Ex: results = SEAsia + EAsia  --> ask: "SEAsia or EAsia"
    #   -> do you prefer thai and vietnamese or indian
    response = 'do you, prefer'


def ask_user_to_invent_meal(user_data):
    print("asking to invent meal...")
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
            good += user_data['ingredients']
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
    random_key = random.choice(RegionRecipes.keys())
    random_recipe = random.choice(RegionRecipes[random_key])
    return random_recipe


#fulfill user request

#TODO -- change user_set to user_data
def recommend_meal(diet, graph):
    #TODO move node????????????????????????????????????????????????????????????????????????????

    region_scores, top_meal, top_meal_region, canidates, scores = find_suggestions_from_food_list(diet["ingredients"])
    #if many canidates with similar scores -> low confidence prediction
    #prediction_confidence = g(results)
    scores_mean, scores_standev = mean_and_deviation(scores)
    prob_ask_for_ingredients = 0
    prediction_confidence = 0

    if scores_mean == None:
        prob_ask_for_ingredients = 0.6
    else:
        prediction_confidence = max(scores) - scores_mean

    if random.random() <= prob_ask_for_ingredients:
        # TODO move node to asked for ingred
        graph.current_node = graph.all_nodes[2]
        return ask_user_for_ingredients()

    if top_meal_region == None:
        graph.current_node = graph.all_nodes[0]
        recipe = give_super_random_meal()
        graph.recipe = recipe
        return list_to_print_string(recipe)

    #meal = give_random_meal_from_(top_meal_region)
    #print(meal)
    #return list_to_print_string(meal)
    if random.random() <= prediction_confidence:
        graph.current_node = graph.all_nodes[0]
        graph.recipe = top_meal
        return list_to_print_string(top_meal)
    else:
        #ask questions
        # probability_invent = f1(results)
        # probability_split = f2(results)
        graph.current_node = graph.all_nodes[1]
        return ask_user_to_invent_meal(diet)



#nodes: all_nodes = [gave_meal, asked_user_if_invent_meal, asked_for_ingredients, asked_user_to_compare]











# -------------------test--------------------------
"""
test RecipeVariations(region, meal, diet)

test give_random_meal function
test ask_user_for_ingredients function
test recommend_meal function
"""


user_list = ['ginger', 'soy_sauce']
test_diet = {'ingredients': user_list, 'allergies': []}
recommend_meal(test_diet)
#todo - apply user preference weights to regions
#   - if user known -> use their preferences, else use average preferences
#
# todo
#   - diet = {include, allergy, preference



# ??????
# users state in food recommender program - where is user in assembly line?