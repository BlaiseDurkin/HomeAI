import pandas as pd
import re
#TODO
#check if token is known
# if token is unknown -> check if it exists as a hyphen
"""
command
 - look(direction): if left, forward | center | middle, right else speak('i cant move' + direction)
 - analyze
 - stop_looking: shutdown camera
 - 'find me' -> find_user()
 - 'what am i doing' -> speak(user_action)

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

everything_synonyms = ['everything', 'all', 'whole', 'hole', 'every']
accepted_verbs = ['want', 'need', 'give', 'tell', 'recommend', 'suggest', 'share', 'think', 'plan', 'what']
meal_words = ['eat', 'food', 'eating', 'dinner', 'meal', 'recipe', 'dish', 'cook', 'cooking']

look_verbs = ['turn', 'look']
look_directions = ['left', 'right', 'center', 'middle', 'forward']
time_units = ['hour', 'hours', 'minute', 'minutes', 'second', 'seconds']
#arrest of tea == recipe
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
KITCHEN_DIR = os.path.join(SCRIPT_DIR, "../kitchen")  # No more ../ !

data_dir = KITCHEN_DIR

food_df = pd.read_csv(os.path.join(KITCHEN_DIR,'NLP_flavor_clean.csv'))
food_ingredients = food_df['item'].tolist()
nation_adj_set = { "american", "canadian", "brazilian", "mexican", "argentine", "british", "german", "french",
                   "italian", "spanish", "russian", "polish", "dutch", "swedish", "swiss", "chinese", "japanese",
                   "south korean", "north korean", "korean", "mongolian", "indian", "pakistani", "bangladeshi",
                   "sri lankan", "nepalese", "indonesian", "thai", "vietnamese", "filipino", "malaysian", "singaporean",
                   "arabian", "saudi", "iranian", "persian", "iraqi", "turkish", "israeli", "emirati", "egyptian",
                   "nigerian", "south african", "zambian", "kenyan", "ethiopian", "algerian", "moroccan", "ghanaian",
                   "australian", "colombian", "chilean", "ukrainian", "greek", "european", "middle eastern", "african",
                   "asian" }
nations = {
    "united states", "america", "canada", "brazil", "mexico", "argentina",
    "united kingdom", "germany", "france", "italy", "spain", "russia",
    "poland", "netherlands", "sweden", "switzerland", "china", "japan",
    "south korea", "north korea", "korea", "mongolia", "india", "pakistan",
    "bangladesh", "sri lanka", "nepal", "indonesia", "thailand", "vietnam",
    "philippines", "malaysia", "singapore", "saudi arabia", "iran", "persian",
    "iraq", "turkey", "israel", "united arab emirates", "egypt", "nigeria",
    "south africa", "kenya", "ethiopia", "algeria", "morocco", "ghana",
    "australia", "colombia", "chile", "ukraine", "greece", "europe",
    "middle east", "africa", "asia", "central asia"
}

#print(food_ingredients)

class Message:
    def __init__(self, text, type, intent, params):
        self.text = text
        self.intent = intent
        self.type = type
        self.params = params


# WARNING -- stupid approach --
def parse_message(text, state):
    # assume concise easy messages
    # construct message object
    # check if message is recognized command
    if text == None:
        return text
    # print(text)
    # return command object
    # command : (computer) VP NP
    # who is the subject
    # what is the primary action, nested action; E.g. think of running <- primary: think, nested: run
    # what is the theme

    # assume
    # 1 clean message from .,()/|\-+*
    has_timer_trigger_1 = False
    has_timer_trigger_2 = False

    has_look_trigger_1 = False
    has_look_trigger_2 = False
    key_param = ''
    #todo -- EXPECTED WORDS -> synonyms -> expected_words
    expected_set = []
    if state.sub_in_action:
        expected_set = state.sub_graph.current_node.expected_words
        #todo -> check if expected set is empty... empty maps default function and new node or does nothing?
    expected_words = []

    has_food_trigger_1 = False
    has_food_trigger_2 = False

    food_item_list = []  # TODO - negate elements
    allergy_list = [] #     {without __, i dont want __, no __}
    region = ''
    is_vegan = False
    is_vegetarian = False
    is_allergic = False
    is_pescetarian = False
    nxt = ''

    message = text.split()
    i = 0
    previous_no = False
    while i < len(message):
        word = message[i] #todo check variations (s) or no s ending
        word = word.strip(" .,()/|-+*").lower()
        #if word in synonymUnion(expected_set): #todo check for all symantic synonyms -> representative key word
        if word in expected_set:
            expected_words.append(word)
        if word == "allergy" or word == "allergic":
            is_allergic = True
        if word == "vegetarian": #todo check for negation
            is_vegetarian = True
        if word == "vegan": #todo check for negation
            is_vegan = True
        if i > 0:
            if message[i-1] == 'no':
                previous_no = True
        if i < len(message) - 1:
            nxt = message[i + 1]
        if word == 'set' or word == 'start':
            has_timer_trigger_1 = True
        if word == 'timer' or word == 'time':
            has_timer_trigger_2 = True
        if word in accepted_verbs:
            has_food_trigger_1 = True
        if word in meal_words:
            has_food_trigger_2 = True

        if word in look_verbs:
            has_look_trigger_1 = True
        if word in look_directions:
            has_look_trigger_2 = True
            key_param = word
        if word + '_' + nxt in food_ingredients:
            if previous_no:
                allergy_list.append(word+ '_' + nxt)
                previous_no = False
            else:
                food_item_list.append(word + '_' + nxt)
            i += 2
            continue
        elif word in food_ingredients or word in nation_adj_set:
            if previous_no:
                allergy_list.append(word)
                previous_no = False
            else:
                food_item_list.append(word)
        elif word + " "+nxt in nation_adj_set:
            if previous_no:
                allergy_list.append(word+" "+nxt)
                previous_no = False
            else:
                food_item_list.append(word+" "+nxt)
            i += 2
            continue
        i += 1

    diet = {'ingredients': food_item_list, 'allergies': allergy_list, 'diet': {'vegan':is_vegan, 'vegetarian': is_vegetarian, 'pescetarian': is_pescetarian, 'allergic': is_allergic}, 'preference': region} #TODO add feature weights: {spicy, Asian, etc...
    if has_food_trigger_1 and has_food_trigger_2:
        # create message object = recommend_meal(user_input=food_item_list)
        # print('RecommendMeal()')
        # print(food_item_list)

        return Message(text, "command", "recommend_meal", diet)

    if has_look_trigger_1 and has_look_trigger_2:
        return Message(text, "command", "turn_camera", key_param)

    if state.sub_in_action:
        if state.active_sub == 'kitchen' and len(expected_words) > 0:
            params = {'expected': expected_words, 'diet': diet}
            return Message(text, "command", "update_kitchen_graph", params)
        elif state.active_sub == 'timer' and len(expected_words) > 0:
            key_param = ''#TODO - timeObj(text, total minutes)
            return Message(text, "command", "set_timer", key_param)
    if text == 'clear diet' or text == 'reset diet':
        return Message(text, "command", "clear_diet", diet)
    if text == 'hello':
        return Message(text, "command", "hello", diet)
    if text == 'bonjour':
        state.character_mode = "french"
        return Message(text, "command", "hello", diet)
    if text == 'who are you':
        return Message(text, "command", "state_name", diet)
    if text == 'i need advice' or text == 'i want help' or text == 'i need help' or text == 'i want advice':
        return Message(text, "command", "health_advice", diet)
    if has_timer_trigger_1 and has_timer_trigger_2:
        key_param = ''#five or 5???
        pattern = r'(\d+)\s*(minutes?|seconds?|hours?)\b'
        match = re.search(pattern, text, re.IGNORECASE)
        state.active_sub = 'timer'
        #todo if match missing --> ask question
        if not match:
            state.sub_graph = state.timer
            state.sub_graph.current_node = state.timer.all_nodes[0]
            return Message(text, "command", "set_timer_q", key_param)
        return Message(text, "command", "set_timer", key_param)
    if text == 'switch character mode':
        return Message(text, "command", "switch_character_mode", key_param)
    return Message(text, "idk", "idk", key_param)

