import pandas as pd
#TODO
#check if token is known
# if token is unknown -> check if it exists as a hyphen
"""
command
 - look(direction): if left, forward | center | middle, right else speak('i cant move' + direction)
 - analyze
 - stop_looking: shutdown camera

 TODO Plan:
    - 1) brute force, naive ungeneralizable hardcoded approach
    - 2) abstract
    - 3) profit

"""
# --- Simple lexicons (extendable) ---
PN = {"he", "she", "they", "it", "i", "you", "we", "him", "her", "us", "them", "me"}
DT = {"the","a","an","this","that","these","those","my","your","his","her","its","our","their"}
PREPS = {"in","on","at","with","by","for","to","from","of","about","into","over","under","near","through","between"}
CONJ = {"and","or","but","so","because","if","when","while", "although"}  # includes subordinating words we treat as CP trigger
W_SET = {"that","who","whose","whom","which"}  # complementizers / relative markers
AUX = {"is","are","was","were","have","has","had","do","does","did","will","would","shall","should","can","could","may","might","must","be","being","been"}
# small adjective & adverb lists; treat words ending with -ly as adverb; others can be assumed
ADJ = {"big","small","red","blue","green","old","young","happy","fast","slow","delicious","new","hot","cold","bright","dark","wooden"}
ADV = {"peacefully","quickly","slowly","quietly","loudly","well","badly","recently","already","soon","now","then","here","there", "that"}

# small verb lexicon; if word not present we'll accept it heuristically as a verb when parsing VP
VERBS = {"walked","eat","eats","ate","run","runs","ran","chase","chased","see","saw","think","thinks","said","say","says","be","am","is","are","have","has","make","made","go","went","sleep","slept","work","works","study","studies","know","knows","like","likes"}#left

accepted_verbs = ['want', 'need', 'give', 'tell', 'recommend', 'suggest', 'share', 'think', 'plan', 'what']
meal_words = ['eat', 'food', 'eating', 'dinner', 'meal', 'recipe', 'dish', 'cook', 'cooking']

look_verbs = ['turn', 'look']
look_directions = ['left', 'right', 'center', 'middle', 'forward']
#arrest of tea == recipe
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
KITCHEN_DIR = os.path.join(SCRIPT_DIR, "../kitchen")  # No more ../ !

data_dir = KITCHEN_DIR

food_df = pd.read_csv(os.path.join(KITCHEN_DIR,'NLP_flavor_clean.csv'))
food_ingredients = food_df['item'].tolist()
#print(food_ingredients)

# WARNING -- stupid approach --
def parse_message(text):
    #assume concise easy messages
    #construct message object
    #check if message is recognized command
    if text == None:
        return text
    #print(text)
    #return command object
    # command : (computer) VP NP
    # who is the subject
    # what is the primary action, nested action; E.g. think of running <- primary: think, nested: run
    # what is the theme

    #assume
    #1 clean message from .,()/|\-+*
    has_look_trigger_1 = False
    has_look_trigger_2 = False
    key_param = ''
    
    has_food_trigger_1 = False
    has_food_trigger_2 = False
    food_item_list = [] #TODO - negate elements
    message = text.split()
    for word in message:
        word = word.strip(" .,()/|-+*").lower()
        if word in accepted_verbs:
            has_food_trigger_1 = True
        if word in meal_words:
            has_food_trigger_2 = True
        if word in food_ingredients:
            food_item_list.append(word)
        
        if word in look_verbs:
            has_look_trigger_1 = True
        if word in look_directions:
            has_look_trigger_2 = True
            key_param = word
    if has_food_trigger_1 and has_food_trigger_2:
        #create message object = recommend_meal(user_input=food_item_list)
        #print('RecommendMeal()')
        #print(food_item_list)
        return Message(text, "command", "recommend_meal", key_param)
    if has_look_trigger_1 and has_look_trigger_2:
        return Message(text, "command", "turn_camera", key_param)
    return Message(text, "idk", "idk", key_param)



"""
    def parse_message(text):
        #tokenize each element of text
        #build groups: VP NP PP
        #   attach adjacent tokens: upBranch~parent, downBranch~nested phrase, family~same phrase
        #verb functions expect parameters. E.g. Give(to=NP, obj=NP, condition= Condition | PP)
"""



class Message:
    def __init__(self, text, type, intent, params):
        self.text = text
        self.intent = intent
        self.type = type
        self.params = params
        

"""
ft1 = 'I want a recipe with eggplant'
ft2 = 'Give me a dish'
ft3 = 'I need to know what to eat tonight'
ft4 = 'What should I eat for dinner'
ft5 = 'Tell me what to eat for dinner'
ft6 = 'Recommend me a meal'

parse_message(ft1)
parse_message(ft2)
parse_message(ft3)
parse_message(ft4)
parse_message(ft5)
parse_message(ft6)
"""