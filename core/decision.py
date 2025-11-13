import random

from kitchen.recommender import recommend_meal
#process command
#command functions
#increase volume
#decrease volume



def random_health_advice():
    health_activities = ['to do, 500, push ups', 'to do, 100, squats', 'to run', 'to do, a, hand stand, for one, minute', 'to meditate', 'to stop, eating', 'god']
    y = random.choice(health_activities)
    return y
def list_to_print_string(sequence):
    string = ""
    for i in range(len(sequence)):
        if i < len(sequence) - 1:
            string += sequence[i] + ', '
        elif i == len(sequence) - 1 and len(sequence) > 1:
            string += ' and '+sequence[i]

    return string

def is_question(text):
    print('check if question...')
    #print(type(text), ' should be string')
    if text.startswith('do you'):
        return True
    else:
        return False
#todo -> if in sub routine, continue sub routine
#   ex: kitchen module
def process_command(command, state):

    response = None
    
    if command.intent == "shut_down":
        state.running = False
        response = "Ending program, Goodbye!"
        return state, response
    elif command.intent == "recommend_meal":
        state.active_sub = "kitchen"
        state.sub_in_action = True
        state.sub_graph = state.kitchen_graph
        #what if the active sub is allready kitchen????
        preamble = "You sound, hungry, here you go,"
        response = recommend_meal(command.params, state.kitchen_graph, fresh=True) # return function response & direction... update node = direction
        if type(response) == list:
            response = list_to_print_string(response)
        if is_question(response):
            preamble = "you sound, hungry, but,"

        #TODO change preamble to not be repetitive
        response = preamble + response

    elif command.intent == "turn_camera":
        direction = command.params
        response = "camera turning "+direction
        state.camera.turn_(direction)
        

    elif command.intent == "update_kitchen_graph":
       response = state.sub_graph.update(command)
    elif command.intent == "clear_diet":
        state.kitchen_graph.diet = {'ingredients': [], 'allergies': [], 'diet': {'vegan':False, 'vegetarian': False, 'pescetarian': False, 'allergic': False}, 'preference': ''} #TODO add feature weights: {spicy, Asian, etc...
        response = 'diet, is, reset'

    elif command.intent == "hello":
        response = "uh, hey there"
    elif command.intent == "state_name":
        response = "uh, i am, the, kitchen assistant"
    elif command.intent == "health_advice":
        response = "listen, bro, you need, "+ random_health_advice()
    elif command.intent == "set_timer": #or node = set_time_q
        response = "no, i am, not, the, time keeper"
    elif command.intent == "set_timer_q":
        #todo set node to set_time_q
        response = "ah, and, for, how long"
        state.active_timer = True

    elif command.intent == "weather_forecast":
        response = "uh, i think, it will, be sunny"
    elif command.intent == "switch_character_mode":
        #if no key_param
        state.character_mode = state.all_characters[(state.all_characters.index(state.character_mode)+1)%len(state.all_characters)]
        response = "changing, "+state.character_mode + ", mode, activated"
    

        
    return state, response