import random

def good_morning():
    txt = "Good, morning, today is, monday, december, 8. time is 8:15. do not, look, at, your phone. do not, look, at, your screen. go, splash, water, on your, face. go, chug, water. how, did, you, sleep."
    return txt


def slept_good(graph):
    workout = "300, push ups. 100, squats. 200, flutter kicks"
    graph.workout = workout
    response = 'good, i made, a workout, tell me, when, to start'
    return response

def slept_bad(graph):
    workout = "300, push ups. 200, lunge walks. 100, donkey kicks. 1, minute, hand, stand"
    graph.workout = workout
    response = 'lets, do, a workout, tell me, when, to start'
    return response

def slept_fine(graph):
    workout = "300, push ups. 100, donkey kicks. 200, flutter kicks"
    graph.workout = workout
    response = 'fine, fine, tell me, when, to start, workout'
    return response

def start_workout(graph):
    return graph.workout

def repeat_workout(graph):
    return graph.workout

def finished_workout(graph):
    #congrats
    response = 'good, job'
    #random choose another workout
    if random.random() > 0.5:
        graph.workout = "50, hand, stand, push ups"
        graph.current_node = graph.all_nodes[2]
        return response + " now, do, "+graph.workout
    else:
        graph.current_node = graph.all_nodes[3]
    # or pick task from list
    # set graph.current_node = graph.all_nodes[i]
    pass

def repeat_task(graph):
    pass