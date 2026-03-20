import random
from datetime import datetime
import calendar
from http.client import responses

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
        if time_2_day <2:
            holiday_greet = 'happy, '+day_name+", "
            if day_name == "Christmas":
                holiday_greet = 'ho, ho, ho, merry, christmas, '
    hr = datetime.now().hour
    time_greet = "good, morning, "
    time_greet_end = ". do not, look, at, your phone. do not, look, at, your screen. go, splash, water, on your, face. go, chug, water. how, did, you, sleep."
    if hr > 11 and hr < 18:
        time_greet = "good, afternoon, "
        time_greet_end = ". stop, gooning. go, splash, water, on your, face. go, chug, water. how, is, the day, so far."
    if hr >= 18:
        time_greet = "good, evening, "
        time_greet_end = ". stop, gooning. how, was, your, day"
    if hr > 21:
        time_greet = "good, night, "
        time_greet_end = "go to sleep"
        #todo change next state
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


"""def select_tasks(graph):
    pass

def parse_task():
    pass
"""
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
        return max_score_task(all_tasks['core'])
    elif 11 < datetime.now().hour < 14:
        #return top score garden task
        return max_score_task(all_tasks['garden'])

    #p(garage) = .15
    if random.random() < 0.15:
        #garage\
        return max_score_task(all_tasks['garage'])
    return weighted_random_task(all_tasks['core'])


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

        discipline_lecture = "remember, no, pleasure, eating, because, your, dopamine, crashes after. "
        respo = "now, are you, ready, for, the next task."
        if random.random() > 0.4:
            response = discipline_lecture + respo
        else:
            response = respo
        graph.update_task(select_top_task())
        return response

def repeat_task(graph):
    return graph.task_name
def explain_task(graph):
    return graph.task.description #TODO figure out why graph.task = none


def read_all_tasks(graph):
    pass


def check_input(graph, text):
    graph.temp_text = text
    return 'did you say, '+ text

def try_again(graph):
    graph.temp_text = ""
    return 'try again'

def ask_task_desc(graph):
    graph.temp_t_name = graph.temp_text
    return 'describe the task'

def ask_task_priority(graph):
    graph.temp_t_desc = graph.temp_text
    return 'is the priority, high, medium, or low'

def who_cares(graph):
    return 'yeah, i, do not care'


def add_2_tasks_f(new_t, file='data/tasks.txt'):
    #new_t = ['subject_area', 'task....']
    print('add_2_tasks_f()')
    if not new_t[1].endswith('\n'):
        new_t[1] = new_t[1] + '\n'
    indx = -1
    with open(file) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.startswith('__'):
                # print(line[2:-3])
                if line[2:-3] == new_t[0]:
                    indx = i
    if indx == -1:
        if not lines[len(lines)-1].endswith('\n'):
            lines[len(lines)-1] = lines[len(lines)-1] + '\n'
        lines.append(new_t[1])
    else:
        lines.insert(indx+1, new_t[1])

    out = open(file, 'w')
    out.writelines(lines)
    out.close()
    


def remove_from_tasks_f(tt, file='data/tasks.txt'):
    new_lines = []
    with open(file) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.split(".")[0].split(":")[1].strip() != tt.split(".")[0].split(":")[1].strip():
                new_lines.append(line)
    out = open(file, 'w')
    out.writelines(new_lines)
    out.close()

def replace_task_in_f(tt, new_t, file='data/tasks.txt'):
    new_lines = []
    with open(file) as f:
        lines = f.readlines()
        for i, line in enumerate(lines):
            if line.split(".")[0].split(":")[1].strip() != tt.split(".")[0].split(":")[1].strip(): # if name = name
                new_lines.append(line)
            else:
                new_lines.append(new_t+'\n')
    out = open(file, 'w')
    out.writelines(new_lines)
    out.close()


#todo: add task to current category
def new_t_added(graph, score):
    new_t = 'name: ' + graph.temp_t_name + '. description: ' + graph.temp_t_desc + '. score: ' + str(score) + '. '
    print(new_t)
    add_2_tasks_f(['core', new_t])
    #todo add to list all_tasks or reset with file read
    all_tasks['core'].append(new_t) #alltask not in graph

    response = 'task' + graph.temp_t_name + '. ' + graph.temp_t_desc + '. added'
    graph.temp_t_name, graph.temp_t_desc, graph.temp_text = "", "", ""
    graph.task_category = "core"
    graph.task_index = len(all_tasks['core']) - 1
    return response

def low_t_added(graph):
    #todo make score low = 4
    score = 4
    return new_t_added(graph, score)

def med_t_added(graph):
    #todo score = 8
    score = 8
    return new_t_added(graph, score)

def high_t_added(graph):
    #todo score = 35
    score = 35
    return new_t_added(graph, score)

"""def process_task(raw_task):
    pass"""

def ask_user_edit_task(graph):
    response = 'do you want, to edit, the name, or the description, or the priority, level'
    return response

def ask_user_delete_task(graph):
    #double check index not out of bounds
    if graph.task_index > len(all_tasks[graph.task_category]) - 1:
        graph.task_index = len(all_tasks[graph.task_category]) - 1
    response = 'are you sure, you want, to delete task, ' + all_tasks[graph.task_category][graph.task_index].split('.')[0][6:] + ', from list'
    return response

def read_task_name(graph):
    if graph.task_index > len(all_tasks[graph.task_category]) - 1:
        graph.task_index = len(all_tasks[graph.task_category]) - 1
    response = all_tasks[graph.task_category][graph.task_index].split('.')[0][6:]
    if len(all_tasks[graph.task_category]) == 0:
        response = graph.task_category + " list, is empty"
    return response

def remove_task(graph):
    #remove all_tasks[graph.task_category][graph.task_index] from data then remake all_task
    task = all_tasks[graph.task_category][graph.task_index]
    all_tasks[graph.task_category].pop(graph.task_index)
    remove_from_tasks_f(task)


def cancel_action(graph):
    response = "ok, sorry "
    return response

def edit_task_name(graph):
    graph.feat_2_change = 'name'
    response = "say, the new, name"
    return response

def edit_task_desc(graph):
    graph.feat_2_change = 'description'
    response = "say, the new, description"
    return response

def edit_task_priority(graph):
    graph.feat_2_change = 'priority'
    response = "say, the new, priority"
    return response

def read_next_task(graph):
    if len(all_tasks[graph.task_category]) == 0:
        return "list is empty"
    graph.task_index += 1
    if graph.task_index >= len(all_tasks[graph.task_category]):
        graph.task_index = 0
    response = read_task_name(graph)
    return response

def read_prev_task(graph):
    if len(all_tasks[graph.task_category]) == 0:
        return "list is empty"
    graph.task_index -= 1
    if graph.task_index < 0:
        graph.task_index = len(all_tasks[graph.task_category]) - 1
    response = read_task_name(graph)
    return response




def change_task_feat(graph, text):
    old_task = all_tasks[graph.task_category][graph.task_index]
    new_task = old_task
    if graph.feat_2_change == 'name':
        #new name + old
        new_task = "name: "+text+"."+".".join(old_task.split('.')[1:])
    elif graph.feat_2_change == 'description':
        new_task = old_task.split('.')[0]+". description: "+text+"."+".".join(old_task.split('.')[2:])
    elif graph.feat_2_change == 'priority':
        key_words = ['hi', 'high', 'medium', 'low', 'minimum', 'max', 'now', 'immediate', 'important']
        normal_map = {'hi': 35, 'high': 35,'medium': 8, 'low': 4, 'minimum': 2, 'max': 40, 'now': 40, 'immediate': 40, 'important': 36}
        negative_map = {'hi': 8, 'high': 8, 'medium': 25, 'low': 8, 'minimum': 6, 'max': 6, 'now': 6, 'immediate': 6, 'important': 6}
        is_negated = False
        has_key = False
        key = ''
        score = 5
        for i, word in enumerate(text.split()):
            if word in key_words:
                has_key = True
                key = word
                if i > 0:
                    if text.split()[i-1] == 'not':
                        is_negated = True
        if has_key:
            if is_negated:
                score = negative_map[key]
            else:
                score = normal_map[key]

        new_parts = []
        add_score = True
        parts = old_task.split('.')
        for i, part in enumerate(parts):

            if part.split(':')[0].strip() == "score":
                new_parts.append(" score: " + str(score))
                add_score = False
            else:
                new_parts.append(part)
        if add_score:
            new_parts.append(" score: " + str(score))

        new_task = ".".join(new_parts)

    #replace all_tasks
    all_tasks[graph.task_category][graph.task_index] = new_task
    replace_task_in_f(old_task, new_task)
    response = "task, replaced"
    return response


def task_category_garden(graph):
    #index = 0
    #category = garden
    # response = repeat_task(graph)
    graph.task_index = 0
    graph.task_category = 'garden'
    return read_task_name(graph)


def task_category_garage(graph):
    graph.task_index = 0
    graph.task_category = 'garage'
    return read_task_name(graph)

def task_category_core(graph):
    graph.task_index = 0
    graph.task_category = 'core'
    return read_task_name(graph)








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