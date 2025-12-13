import random
from datetime import datetime
import calendar
from data.users import *

def good_morning():
    #todo fix date time
    # afternoon
    # evening
    hr = datetime.now().hour
    time_greet = "good, morning, "
    if hr > 11 and hr < 18:
        time_greet = "good, afternoon, "
    if hr >= 18:
        time_greet = "good, evening, "
    txt = time_greet+"today is, "+datetime.now().strftime("%A")+", "+calendar.month_name[datetime.now().month]+", "+str(datetime.now().day)+". time is "+str(datetime.now().hour)+", "+str(datetime.now().minute)+". do not, look, at, your phone. do not, look, at, your screen. go, splash, water, on your, face. go, chug, water. how, did, you, sleep."
    return txt


def slept_good(graph):
    workout = "200, push ups. 100, squats. 500, flutter kicks"
    graph.workout = workout
    response = 'good, i made, a workout, tell me, when, to start'
    return response

def slept_bad(graph):
    workout = "200, push ups. 200, lunge walks. 100, donkey kicks. 1, minute, hand, stand"
    graph.workout = workout
    response = 'lets, do, a workout, tell me, when, to start'
    return response

def slept_fine(graph):
    workout = "200, push ups. 100, donkey kicks. 400, flutter kicks"
    graph.workout = workout
    response = 'fine, just, fine, tell me, when, to start, workout'
    return response

def start_workout(graph):
    return graph.workout

def repeat_workout(graph):
    return graph.workout


def select_tasks(graph):
    pass

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
        # discipline lecture
        # - no weed because get stoned faded and forgetful, time skips forward, too much day dreaming,
        # - no food because, dopamine drop after eating
        # - must do exercise snack
        # or pick task from list
        # set graph.current_node = graph.all_nodes[i]
        return response

def repeat_task(graph):
    pass

def read_all_tasks(graph):