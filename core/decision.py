#process command
#command functions
#increase volume
#decrease volume

def process_command(command, state):
    """
    if command.intent == "RECOMMEND_MEAL":
        meal = recommend_meal(state)
        response = f"How about {meal}?"
        state.meal_state = flow.start_recipe(meal)

    elif command.intent == "NEXT_STEP":
        step = flow.next_step()
        response = step

    elif command.intent == "STOP":
        state.running = False
        response = "Goodbye!
    """
    if command.intent == "STOP":
        state.running = False
        response = "Ending program, Goodbye!"
        return state, response