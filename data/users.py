#create profiles on different users
# write to data/models/users/
#   read/write to model
#       -> update adjectives : add adjectives, remove contrasting adjectives

#colin
# adjectives = [vegan,...]

# Blaise
# adjectives = [,...]
"""
Schedule:
    8:30 wake
    9:00 study
    9:30 record
    10:30 run
    11:30 lunch
    12:30 work

** reality -- wake -> doom scroll for 1 hour +
(((*@*))) solution -- read ode in bedc

Target Schedule
    wake
    garden - quick from garden_todo_list
    quick workout { 1 min handstand, 40 squat, 100 pushup, 3 min meditate stretch}
    video lecture + arm work out {curl, shoulder circles}
    math/CS challenge - AI generated schedule
     - study & record
     - code
    run
    lunch
    work

** objective : optimize productivity via atmospheric variables (music), reminders, doom scroll blocker
music schedule: morning (rise) late morning (grind) early afternoon (sprint) late afternoon (locked in) evening (ponder)
rise = {andor, halo, vivaldi}
grind = {house, doom}
sprint = {dnb, dubstep}
locked in = {binural beats}
ponder = {dune, interstellar, oppenheimer, the king}
"""
# -------- tasks -----------
"""
class Task
    - sub tasks
    ex: to start mushroom, drill holes in log, and put spores in wood, and seal with wax
    
    
    
    garden_tasks = [gt1, gt2,... ]
    gt1 = {name: cut tree, location: in back yard, details: cut the tree pushing over the fence, score: 15, expected_time: 1 hour}
    
    garage...
    wst1 = {name: organize stuff, location: in garage, details: parts like wires and switches need to be organized, score: 7}
    
    
    
"""

# -- garden --
garden_tasks = ['start mushroom', 'prune shrub', 'plant seeds', 'water plants', 'cut down tree']
garden_tasks_desc = ['name: start mushroom. description: drill holes in log, put spores in wood, seal with wax. time: 2 hours. location: side yard.',
                     'name: cut tree. description: cut the tree pushing over the fence. score: 15. time: 1 hour.',
                     'name: plant seeds. description: put seeds in wet paper, put tumeric in ground. time: 2 minutes.',
                     'name: water plants. description: water fig clones, water pea seeds. time: 30 minutes.'
                     ]

# -- core tasks --
tasks_2_do = ['apply to jobs', 'fix resumay', 'work on certifications']

projects = ['buy raspberry pi 5', 'record audio', 'build smart home']

audio_projects = ['dustups video', 'water harvesting video', 'machine learning lesson']
core_tasks_desc = [
    'name: apply to jobs. description: apply to fitting jobs, and take notes on where to upskill. time: 1 hour. score: 10.',
    'name: tailor resumay. description: remake several resumays for each job. time: 3 hours. score: 40.',
    'name: buy raspberry pi 5. time: 30 minutes',
    'name: record audio. description: record machine learning lesson. time: 1 hour. score: 30.',
    'name: build smart home. description: implement functions and fix bugs. time: 30 minutes. score: 15.'
]


# -- garage projects --
garage_tasks = ['organize stuff', 'build helping hand', 'buy chair']
garage_tasks_desc = [
    'name: organize stuff. description: organize stuff. time: 3 hours',
    'name: build helping hand. description: get wire and clips to build a helping hand. time: 2 hours',
    'name: buy chair. description: find an office chair. time: 30 minutes'
]

# ----- all tasks -----------
#all_tasks = {'garden' : garden_tasks_desc, 'garage': garage_tasks_desc, 'main': core_tasks_desc}

def process_tasks_f(file):
    garden_tasks = []
    garage_tasks = []
    core_tasks = []
    add_2_garden = False
    add_2_garage = False
    add_2_core = False
    try:
        with open(file) as f:
            for line in f:

                if line == '\n':
                    #print('new line')
                    pass
                elif line.startswith('__'):
                    #print(line[2:-3])
                    if line[2:-3] == 'garden':
                        #print('gardennnn')
                        add_2_garden = True
                        add_2_garage = False
                        add_2_core = False
                    elif line[2:-3] == 'core':
                        #print('coreeee')
                        add_2_core = True
                        add_2_garden = False
                        add_2_garage = False
                    elif line[2:-3] == 'garage':
                        #print('gargeeee')
                        add_2_garage = True
                        add_2_core = False
                        add_2_garden = False
                else:
                    #print(line[0:-1])
                    if add_2_core:
                        core_tasks.append(line[0:-1])
                    elif add_2_garden:
                        garden_tasks.append(line[0:-1])
                    elif add_2_garage:
                        garage_tasks.append(line[0:-1])



    except:
        print('error reading file')
    #print('tasks')
    #print(core_tasks)
    #print(garden_tasks)
    #print(garage_tasks)
    all_tasks = {'garden': garden_tasks, 'core': core_tasks, 'garage': garage_tasks}
    return all_tasks



all_tasks = process_tasks_f('data/tasks.txt')








# garage -> stuff -> tools, parts,... build shelves
#   - sub tasks: find scap for garage

# ----- accountability schedule tracker ------------
# saves data for a week and then compresses -> rolling average
#   accomplishment rate, productivity level - points score, happiness, area of focus,



# -------- food ------------

#maman
# food preference: Europe, WestAsia, SouthAsia, Mex, SouthEastAsia, EastAsia, Africa

#papa
# food preference: Europe, WestAsia, SouthAsia, Mex, SouthEastAsia, EastAsia, Africa

#Blaise
# food preference: WestAsia, SouthAsia, EastAsia, Mex, SouthEastAsia, Europe,  Africa

#TODO get user data from file
# - write to file if new user added or user user data changes
