from recipes import *
import random

#functions for processing user input related to food
#user data is formatted in previous parsing and processing function
#

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
    "Greece": "Europe"
}

adjective_to_region = {
    "American": "America",  # United States
    "Canadian": "America",
    "Brazilian": "America",
    "Mexican": "America",
    "Argentine": "America",  # or Argentinian
    "British": "Europe",  # United Kingdom
    "German": "Europe",
    "French": "Europe",
    "Italian": "Europe",
    "Spanish": "Europe",
    "Russian": "Europe",
    "Polish": "Europe",
    "Dutch": "Europe",  # Netherlands
    "Swedish": "Europe",
    "Swiss": "Europe",  # Switzerland
    "Chinese": "EastAsia",
    "Japanese": "EastAsia",
    "South Korean": "EastAsia",
    "North Korean": "EastAsia",
    "Korean": "EastAsia",
    "Mongolian": "EastAsia",
    "Indian": "SouthAsia",
    "Pakistani": "SouthAsia",
    "Bangladeshi": "SouthAsia",
    "Sri Lankan": "SouthAsia",
    "Nepalese": "SouthAsia",
    "Indonesian": "SouthEastAsia",
    "Thai": "SouthEastAsia",
    "Vietnamese": "SouthEastAsia",
    "Filipino": "SouthEastAsia",  # or Philippine
    "Malaysian": "SouthEastAsia",
    "Singaporean": "SouthEastAsia",
    "Arabian": "WestAsia",
    "Saudi": "WestAsia",  # or Saudi Arabian
    "Iranian": "WestAsia",  # Persian also used, but "Iranian" is the standard demonym
    "Persian": "WestAsia",
    "Iraqi": "WestAsia",
    "Turkish": "WestAsia",
    "Israeli": "WestAsia",
    "Emirati": "WestAsia",  # United Arab Emirates
    "Egyptian": "WestAsia",
    "Nigerian": "Africa",
    "South African": "Africa",
    "Kenyan": "Africa",
    "Ethiopian": "Africa",
    "Algerian": "WestAsia",
    "Moroccan": "WestAsia",
    "Ghanaian": "Africa",
    "Australian": "America",  # Grouped as per previous request
    "Colombian": "America",
    "Chilean": "America",
    "Ukrainian": "Europe",
    "Greek": "Europe"
}

#key features
"""
    - spicy
    - vegan
"""
def RecipeVariations(region, meal, diet):
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


# (2) suggest meal recommendation given minimal data
def give_random_meal(region):
    #test with SE_meals
    #region = SEAsia
    print('Giving random meal')
    print(random.choice(SEA_meals))

#give_random_meal()


# (3) create meal using flavor model

def ask_user_for_ingredients():
    print('I can recommend me a meal, but first can you tell me what if there are any ingredients you want to use')
    #TODO - scan response for tokens (food ingredients)
    #return set of tokens

#fulfill user request
def recommend_meal(user_set):
    if len(user_set) == 0:
        user_data = ask_user_for_ingredients()
        user_set.update(user_data)
    region_scores, top_meal, top_meal_region, canidates, scores = find_suggestions_from_food_list(user_set)

def extrapolate_user_input():
    vague_items = ['meat', 'fish']

#test
"""
test RecipeVariations(region, meal, diet)

test give_random_meal function
test ask_user_for_ingredients function
test recommend_meal function
"""

"""
Interactions
B: 'I want a recipe with eggplant'
    'Give me a dish'
    'I need to know what to eat tonight'
    'What should I eat for dinner'
    'Tell me what to eat for dinner'
    'Recommend me a meal'

    verbs: give, tell, need, want, recommend
"""
"""
Special interactions
     analyze
     where can i plausibly add broccoli?
     
"""
user_list = ['ginger']
region_scores, top_meal, top_meal_region, canidates, scores = find_suggestions_from_food_list(user_list)
print(region_scores)
print(top_meal)
for pair in zip(canidates, scores):
    if pair[1] > .1:
        print(pair)
diet = {'vegan': False, 'vegetarian': False, 'meat_lover': False}

variations = RecipeVariations(top_meal_region, top_meal, diet)
print(variations)
#todo - apply user preference weights to regions
#   - if user known -> use their preferences, else use average preferences

# ??????
# users state in food recommender program - where is user in assembly line?