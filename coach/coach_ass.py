import random
from datetime import datetime
import calendar
from data.users import *
from kitchen.seasonal import *

def good_morning():
    #todo fix date time
    # afternoon
    # evening
    # holiday
    #if holiday = 0
    is_near_day, time_2_day, day_name = is_near_holiday(date.today(),5)
    holiday_greet = ''
    if is_near_day:
        if time_2_day <6:
            holiday_greet = 'happy, '+day_name+", "
    hr = datetime.now().hour
    time_greet = "good, morning, "
    time_greet_end = ". do not, look, at, your phone. do not, look, at, your screen. go, splash, water, on your, face. go, chug, water. how, did, you, sleep."
    if hr > 11 and hr < 18:
        time_greet = "good, afternoon, "
        time_greet_end = ". stop, gooning. go, splash, water, on your, face. go, chug, water. how, is, the day, so far."
    if hr >= 18:
        time_greet = "good, evening, "
        time_greet_end = ". stop, gooning. how, was, your, day"
    txt = time_greet+holiday_greet+"today is, "+datetime.now().strftime("%A")+", "+calendar.month_name[datetime.now().month]+", "+str(datetime.now().day)+". time is "+str(datetime.now().hour)+", "+str(datetime.now().minute)+time_greet_end
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

def parse_task():
    pass

#TODO future
# create tasks score = {priority, important, etc}
# ask user for details: [score, expected time, description]
def weighted_random_task(tasks):
    scores = {}
    total = 0
    for i, task in enumerate(tasks):
        task = task.split(".")
        scores[i] = 0
        for x in task:
            x = x.split(":")
            if x[0].strip() == "score":
                scores[i] = int(x[1].strip())
                total += int(x[1].strip())

    if total > 0:
        rx = random.random()
        LB = 0
        UB = 0
        j = 0
        while j < len(scores.keys()):
            UB += scores[j]/total
            if LB <= rx < UB:
                break
            LB = UB
            j += 1
        return tasks[j].split(".")
    return random.choice(tasks).split(".")



def max_score_task(tasks):
    max_score = 0
    max_t = ""
    for task in tasks:
        task = task.split(".")
        for x in task:
            x = x.split(":")
            if x[0].strip() == "score":

                if int(x[1].strip()) > max_score:
                    max_score = int(x[1].strip())
                    max_t = task
    if max_t == "":
        max_t = random.choice(tasks).split(".")
    return max_t

def select_top_task():
   #TODO keep track of completed tasks for next task recommender
    if datetime.now().hour <= 11:
        #return top score core task
        return max_score_task(core_tasks_desc)
    elif 11 < datetime.now().hour < 14:
        #return top score garden task
        return max_score_task(garden_tasks_desc)

    #p(garage) = .15
    if random.random() < 0.15:
        #garage\
        return max_score_task(garage_tasks_desc)
    return weighted_random_task(core_tasks_desc)


def finished_workout(graph):
    #congrats
    response = 'good, job'
    #random choose another workout
    if random.random() > 0.5:
        graph.workout = "50, hand, stand, push ups"
        graph.current_node = graph.all_nodes[2]
        return response + " now, do, "+graph.workout
    else:
        #-->give lecture, ask to receive lecture,
        graph.current_node = graph.all_nodes[3]

        discipline_lecture = "no, weed, because, you, get, stoned, and space, out. no, pleasure, eating, because, your, dopamine, crashes after. remember, to ask, for, snacks. "
        respo = "are you, ready, for, next task."
        if random.random() > 0.3:
            response = discipline_lecture + respo
        else:
            response = respo
        graph.task = graph.update_task(select_top_task())
        return response

def repeat_task(graph):
    return graph.task_name
def explain_task(graph):
    return graph.task.description


def read_all_tasks(graph):
    pass


"""

task list

start_of_day - easy task: fun activity = drink tea outside
    - first task: work out & discipline lecture
    - next task: easy task: garden task
    - next task: record 1 short micro lesson
    - next task: core_work 2 to 4 hours
    - gym -- 4pm
    - garage or core_work 








"""