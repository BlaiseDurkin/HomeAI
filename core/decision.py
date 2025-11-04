from kitchen.recommender import recommend_meal
#process command
#command functions
#increase volume
#decrease volume


"""
recognized commands:
 - recommend meal
 - turn {left, center, right}
 - look {left, center, right}
 - set a timer
 - set a reminder
 - 
"""
def is_question(text):
    if text.startswith('do you'):
        return True
    else:
        return False
#todo -> if in sub routine, continue sub routine
#   ex: kitchen module
def process_command(command, state):
    """
    if command.intent == "RECOMMEND_MEAL":
        meal = recommend_meal(state)
        response = f"How about {meal}?"
        state.meal_state = flow.start_recipe(meal)



    elif command.intent == "STOP":
        state.running = False
        response = "Goodbye!


      elif command.intent == "NEXT_STEP":
        step = flow.next_step()
        response = step



    """
    response = None
    
    if command.intent == "shut_down":
        state.running = False
        response = "Ending program, Goodbye!"
        return state, response
    elif command.intent == "recommend_meal":
        state.active_sub = "kitchen"
        state.sub_in_action = True
        state.sub_in_action = state.kitchen_graph
        #what if the active sub is allready kitchen????
        preamble = "You sound, hungry, here you go,"
        response = recommend_meal(command.params, state.kitchen_graph) # return function response & direction... update node = direction
        if is_question(response):
            preamble = "you sound, hungry, but,"
        response = preamble + response

    elif command.intent == "turn_camera":
        direction = command.params
        response = "camera turning "+direction
        state.camera.turn_(direction)
        

    elif command.intent == "update_kitchen_graph":
       response = state.sub_graph.update(command)
    

        
    return state, response