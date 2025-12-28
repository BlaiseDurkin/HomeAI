
#TODO: add themes {thanksgiving, christmas, etc..}
import pandas as pd
import random

food_df = pd.read_csv('kitchen/NLP_flavor_clean.csv')
food_ingredients = food_df['item'].tolist()

vegetables_set = food_df.loc[food_df['plant'] > 0, 'item']
vegetables_list = vegetables_set.tolist()


# ----------- recipe ----------------
class Recipe:
    def __init__(self, list_of_ingredients):
        self.list_of_ingredients = list_of_ingredients
        self.region = None
        self.vegetables = self.parseVeg()
    def parseVeg(self):
        vegetables = []
        for ingredient in self.list_of_ingredients:
            if ingredient in vegetables_list:
                vegetables.append(ingredient)
        self.vegetables = vegetables




#use spider graph to visualize

#East Asia
EA1 = ['rice', 'shrimp', 'ginger', 'garlic', 'carrot', 'broccoli', 'soy_sauce', 'sesame_oil', 'white_pepper', 'green_onion'] #shrim and broccoli with rice
EA2 = ['rice', 'steak', 'ginger', 'garlic', 'bell_pepper', 'broccoli', 'vinegar', 'soy_sauce', ' sesame_oil', 'white_pepper', 'green_onion'] #steak and broccoli with rice
EA3 = ['rice', 'pork', 'ginger', 'garlic', 'cabbage', 'onion', 'carrot', 'soy_sauce', 'sesame_oil', 'white_pepper', 'green_onion'] #pork with rice
EA4 = ['rice', 'shrimp', 'ginger', 'garlic', 'carrot', 'bell_pepper', 'walnut', 'soy_sauce', 'sesame_oil', 'white_pepper', 'green_onion'] #shrimp and walnut with rice
EA5 = ['noodles', 'shrimp', 'ginger', 'garlic', 'carrot', 'broccoli', 'seaweed', 'soy_sauce', 'sesame_oil', 'white_pepper', 'green_onion'] #
EA6 = ['rice', 'chicken', 'garlic', 'chili_pepper', 'soy_sauce', 'sesame_oil', 'ginger', 'green_onion', 'vinegar', 'peanut'] #peanut chicken with rice
EA7 = ['rice', 'steak', 'soy_sauce', 'sesame_oil', 'garlic', 'green_onion', 'spinach', 'carrot', 'zucchini', 'shiitake_mushroom', 'sprouts', 'egg', 'sesame_seed'] #stir fry with rice
EA8 = ['rice', 'carrot', 'cabbage', 'green_onion', 'sesame_seed', 'soy_sauce', 'sesame_oil', 'chili_pepper', 'shiitake_mushroom'] #spicy mushroom with rice
EA9 = ['noodles', 'cabbage', 'celery', 'onion', 'soy_sauce', 'oyster_sauce'] #chow mein

EA_meals = [EA1, EA2, EA3, EA4, EA5, EA6, EA7, EA8, EA9]

#South East Asia
SEA1 = ['rice', 'steak','garlic', 'cilantro', 'peanut', 'soy_sauce', 'vinegar', 'mint', 'peanut', 'bell_pepper', 'green_onion'] #steak with rice
SEA2 = ['rice','shrimp', 'carrot','lettuce', 'sprouts', 'cilantro', 'mint', 'vinegar', 'peanut'] #shrimp with rice
SEA3 = ['noodles', 'chicken', 'peanut','egg', 'sprouts', 'garlic', 'lime', 'vinegar', 'pepper', 'soy_sauce', 'basil', 'fish_sauce', 'green_onion'] #pad thai
SEA4 = ['rice', 'chicken', 'onion', 'ginger', 'garlic', 'carrot', 'coriander', 'coconut', 'chili_pepper','turmeric','lemongrass', 'basil', 'green_beans'] #red curry
SEA5 = ['rice', 'ginger', 'garlic', 'lemongrass', 'curry', 'eggplant', 'peas', 'coconut', 'basil', 'white_pepper']#green curry
SEA6 = ['rice', 'zucchini', 'curry', 'coconut', 'turmeric', 'lemongrass', 'carrot', 'onion', 'coriander', 'cumin', 'white_pepper', 'ginger', 'garlic', 'cilantro', 'lime']#yellow curry
SEA7 = ['rice', 'shrimp', 'chicken', 'egg', 'garlic', 'soy_sauce', 'fish_sauce', 'green_onion', 'chili_pepper', 'cucumber'] #fried rice with chicken
SEA8 = ['rice', 'steak', 'garlic', 'chili_pepper', 'coconut', 'lemongrass', 'clove', 'cinnamon', 'coriander', 'star_anise', 'cumin'] #steak with rice and coconut sauce


SEA_meals = [SEA1, SEA2, SEA3, SEA4, SEA5, SEA6, SEA7, SEA8]

#South Asia
SA1 = ['rice', 'lentils', 'turmeric','cumin','cardamom', 'curry', 'carrot', 'onion'] #dahl
SA2 = ['rice', 'chicken', 'yogurt', 'turmeric', 'cumin', 'coriander', 'ginger', 'garlic', 'butter', 'onion', 'tomato', 'cashew', 'cilantro']
SA3 = ['rice', 'spinach', 'paneer', 'onion', 'ginger', 'garlic', 'bell_pepper', 'cumin', 'turmeric', 'chili_pepper', 'cream', 'butter'] #palak paneer
SA4 = ['rice', 'chickpeas', 'onion', 'tomato', 'ginger', 'garlic', 'chili_pepper', 'cumin', 'coriander', 'turmeric', 'cilantro']
SA5 = ['rice', 'lamb', 'yogurt', 'onion', 'ginger', 'garlic', 'tomato', 'chili_pepper', 'coriander', 'turmeric', 'clove', 'cardamom', 'cinnamon', 'cilantro']
SA6 = ['rice', 'cauliflower', 'carrot', 'green_beans', 'potato', 'peas', 'onion', 'ginger', 'garlic', 'chili_pepper', 'yogurt', 'mint', 'cilantro', 'saffron', 'cumin', 'coriander', 'turmeric', 'cardamom', 'clove', 'cinnamon', 'butter', 'cashew']
SA7 = ['rice', 'eggplant', 'onion', 'tomato', 'ginger', 'garlic', 'chili_pepper', 'cumin', 'turmeric', 'coriander', 'peas', 'cilantro']
SA8 = ['rice', 'carrot', 'peas', 'potato', 'onion', 'tomato', 'ginger', 'garlic', 'coconut', 'cashew', 'chili_pepper', 'cumin', 'coriander', 'turmeric', 'cilantro', 'clove', 'cardamom']

SA_meals = [SA1, SA2, SA3, SA4, SA5, SA6, SA7, SA8]

#West Asia
WA1 = ['rice','turmeric', 'cinnamon', 'onion', 'bell_pepper', 'lentils', 'lemon', 'mint']
WA2 = ['rice', 'saffron', 'chickpeas', 'lemon', 'garlic', 'olive_oil', 'cumin', 'parsley']
WA3 = ['cucumber', 'lemon', 'garlic', 'olive_oil', 'mint', 'chickpeas']
WA4 = ['rice', 'lemon', 'olive_oil', 'parsley', 'onion', 'tomato', 'lamb']
WA5 = ['rice', 'turmeric', 'black_pepper', 'parsley', 'onion', 'bell_pepper', 'lamb']
WA6 = ['rice', 'chicken', 'turmeric', 'black_pepper', 'parsley', 'onion', 'pomegranate', 'walnut','olive_oil']
WA7 = ['rice', 'eggplant', 'tomato', 'garlic', 'onion', 'turmeric', 'olive_oil', 'black_pepper', 'parsley', 'egg']
WA8 = ['rice','turmeric', 'cinnamon', 'onion', 'cumin', 'lentils', 'lemon', 'parsley', 'garlic', 'black_pepper', 'olive_oil']

WA_meals = [WA1, WA2, WA3, WA4, WA5, WA6, WA7, WA8]

#Europe
E1 = ['bread','eggplant', 'zucchini', 'bell_pepper', 'onion', 'tomato', 'garlic', 'olive_oil', 'thyme', 'basil', 'black_pepper']
E2 = ['pasta','mushroom', 'onion', 'carrot', 'garlic', 'wine', 'tomato', 'butter', 'thyme', 'black_pepper']
E3 = ['pasta', 'cheese', 'black_pepper', 'parsley', 'garlic', 'cream', 'mushroom']
E4 = ['pasta', 'garlic', 'broccoli', 'parsley', 'salmon', 'black_pepper']
E5 = ["pork", "pasta", "tomato", "garlic"]
E6 = ["chicken", "potato", "rosemary"]
E7 = ['pasta', 'tomato', 'garlic', 'eggplant', 'oregano']
E8 = ['pasta', 'zucchini', 'garlic', 'pork']
E9 = ['pasta', "pesto", "chicken"]
E_meals = [E1, E2, E3, E4, E5, E6, E7, E8, E9]


#Africa
A1 = ["lamb", "couscous", "cucumber"]
A2 = ["fish", "yam", "peanut"]
A3 = ["fish", "peanut", "spinach", "yam"]
A4 = ["oil", "onion", "tomato", "cabbage", "shima"]
A5 = ["goat", "oil", "tomato", "shima"]
A6 = ["okra", "peanut", "shima"]
Af_meals = [A1, A2, A3, A4, A5, A6]

#Mex America
Mx1 = ["corn", "beans", "quinoa", "chipotle_pepper", "paprika"]
Mx2 = ["beans", "pepper", "quinoa", "tomato"]
Mx3 = ["tortilla", "chicken", "lettuce", "salsa"]
Mx4 = ["tortilla","lard", "beans", "lettuce", "salsa"]
Mx5 = ["tortilla", "pork", "onion", "cilantro", "chipotle_pepper"]
Mx6 = ["tortilla", "steak", "cheese", "cream", "salsa"]
Mx_meals = [Mx1, Mx2, Mx3, Mx4, Mx5, Mx6]

RegionRecipes = {'EastAsia': EA_meals, 'SouthEastAsia': SEA_meals, 'SouthAsia': SA_meals, 'WestAsia': WA_meals, "Europe": E_meals, "Africa": Af_meals, "America": Mx_meals}

#Maman
M1 = ['rice', 'zucchini', 'celery', 'onion', 'tofu', 'spinach', 'soy_sauce']

#ThanksGiving
T1 = ['squash', 'rice', 'bell_pepper','onion', 'pumpkin_seed', 'chipotle_pepper','paprika', 'black_sage', 'cranberries']
T2 = ['corn', 'beans', 'tomato', 'onion', 'lime', 'cilantro', 'avocado']
T3 = ['turkey', 'garlic', 'walnut', 'onion', 'chipotle_pepper', 'paprika', 'black_sage']
T4 = ['beans', 'squash', 'chipotle_pepper', 'black_sage']
T5 = ['pumpkin', 'nutmeg', 'cinnamon', 'sugar']
T6 = ['apple', 'nutmeg', 'cinnamon', 'honey']
T7 = ['pie_dough', 'apple_filling'] #apple_filling = T6
T8 = ['pie_dough', 'pumpkin_filling'] #pumpkin_filling = T5
T9 = ['turkey', 'turkey_filling'] #turkey_filling = T3
Thanksgiving_meals = [T1, T2, T3, T4, T7, T8, T9]

#ChineeseNewYear
EAny1 = ['dumpling_dough', 'dumpling_filling']
EAny2 = ['cabbage','carrot','green_onion','sesame_oil', 'white_pepper', 'soy_sauce']
EAny3 = ['pork','cabbage','carrot','green_onion','sesame_oil', 'white_pepper', 'soy_sauce']

dough = ['flour', 'water', 'salt']
pie_dough = ['flour', 'butter', 'water', 'salt']
bread_dough = ['flour', 'yeast', 'water']

# christmas
"""
roman honey fritters
stuffed dates
roasted boar, ham, lamb, chicken, turkey, salmon
beetroot soup
Panettone: Italian sweet bread with fruits and nuts / Stollen: German fruit bread
ginger bread
roasted root veg: turnips, carrots
clam chowder


"""
christmas_bread = ['bread_dough', 'nuts', 'fruit']
ginger_bread = ['flour', 'water', 'cinnamon', 'clove', 'ginger', 'sugar', 'egg', 'butter']
mushroom_pie = ['pie_dough', 'mushroom', 'onion', 'thyme', 'garlic', 'salt']
roasted_root_veg = ['carrot', 'turnip', 'garlic', 'lavender']
apple_bread = ['flour', 'water', 'salt', 'cinnamon', 'apple', 'honey']

def random_christmas_meat():
    options = ['ham', 'lamb', 'chicken', 'turkey', 'salmon']
    return random.choice(options)

Christmas_meals = [christmas_bread, mushroom_pie, roasted_root_veg, apple_bread, random_christmas_meat()]

#---------------- salad ----------------------------
S1 = ['broccoli', 'sauce']



#
def random_dumpling_filling():
    options = [EAny2, EAny3]
    return random.choice(options)

processed_recipes = {'apple_filling': T6, 'pumpkin_filling': T5, 'turkey_filling': T3,
                     'dumpling_filling': random_dumpling_filling, 'dumpling_dough': dough, 'pie_dough': pie_dough,
                        'bread_dough': bread_dough, 'christmas_bread': christmas_bread, 'ginger_bread': ginger_bread}

# ------------------- sauces ------------------------

# nut + liquid + flavor + salt
# flavor ~ {herb spice or seasoning}

salsa = ['tomato', 'onion', 'jalapeno_pepper', 'cilantro', 'lime', 'salt']
pesto = ['basil', 'garlic', 'nut', 'olive_oil', 'salt', 'cheese']
nut_sauce_euro1 = ['walnut', 'garlic', 'salt', 'basil', 'tomato', 'water']
nut_sauce_euro2 = ['walnut', 'garlic', 'salt', 'onion', 'tomato', 'water']
nut_sauce_sasia1 = ['walnut', 'garlic', 'salt', 'cashew', 'tomato', 'cumin', 'turmeric', 'clove','water']
nut_sauce_easia = ['almond', 'seaweed', 'garlic', 'salt', 'water', 'ginger', 'white_pepper']
nut_sauce_mex1 = ['walnut', 'chipotle_pepper', 'garlic', 'black_sage', 'tomato', 'salt', 'water']
nut_sauce_wasia1 = ['walnut', 'pomegranate', 'olive_oil', 'salt', 'water', 'saffron', 'black_pepper']
sauce_easia1 = ['soy_sauce', 'vinegar', 'sesame_oil', 'white_pepper']
sauce_seasia1 = ['soy_sauce', 'vinegar', 'sesame_oil', 'peanut', 'mint']




Newyears_meals = []
July4_meals = []
Easter_meals = []
Asianewyears_meals = []
Bday_meals = []

holiday_meals = {
    "Thanksgiving": Thanksgiving_meals,
    "Christmas": Christmas_meals,
    "New Years": Newyears_meals,
    "July 4th": July4_meals,
    "Easter": Easter_meals,
    "Asian New Year": Asianewyears_meals,
    "Birthday": Bday_meals
}




