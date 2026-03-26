
from coach.coach_ass import *



# coach
#   - data : task_lists { easy_task, hard_task
#   - mantras: internal narrative hacking
class Task:
    def __init__(self, raw):
        self.name = ""
        self.description = ""
        self.time = 0
        self.score = 0
        self.raw = raw
        self.process_self(raw)

    def process_self(self, raw):
        for x in raw:
            x = x.split(":")
            if x[0].strip() == "name":
                self.name = x[1].strip()
            elif x[0].strip() == "description":
                self.description = x[1].strip()
            elif x[0].strip() == "time":
                self.time = x[1].strip()
            elif x[0].strip() == "score":
                self.score = x[1].strip()

class CoachAssistantGraph:
    def __init__(self):
        self.current_node = None
        self.all_nodes = []
        self.workout = ""
        self.task = None
        self.task_name = ""
        self.temp_t_name = ""
        self.temp_t_desc = ""
        self.temp_text = ""
        self.task_index = 0
        self.task_category = "core"
        self.feat_2_change = "name"

    def update(self, message):
        response = self.current_node.update(message)
        #TODO
        # - check if response is string
        return response

    def update_task(self, task):
        new_task = Task(task)
        self.task = new_task
        self.task_name = new_task.name



class CoachNode:
    def __init__(self, expected_words, function_map, graph):
        self.expected_words = expected_words
        # TODO expected words gets reduced by sentiment
        self.map = function_map
        self.graph = graph

    def process_input(self, params):

        expected_words = params['expected'] #todo : create map: senitment to expected words
        print('processing input...')
        print('key words: ',expected_words)
        key = ''
        for word in expected_words:
            if word in self.map.keys():
                key = word
        return key

    def update(self, message):
        key = self.process_input(message.params)
        #print('node update: ',key)
        if not key in self.map.keys():
            if '' in self.map.keys():
                key = ''
            else:
                return ''


        self.graph.current_node = self.map[key][1]
        if key == 'RAT':
            response = self.map[key][0](self.graph, message.text)
        else:
            response = self.map[key][0](self.graph)
        #print('node update: ',response)
        return response

# ----------- Nodes -----------------------
CAG = CoachAssistantGraph()

said_good_morning = CoachNode(["good","fine", "bad"], {"good": [slept_good],"fine": [slept_fine], "bad": [slept_bad]}, CAG)

asked_to_start_workout = CoachNode(["start"], {"start": [start_workout]}, CAG)

said_workout = CoachNode(["repeat", "done"], {"repeat": [repeat_workout], "done": [finished_workout]}, CAG)

asked_if_say_task = CoachNode(["yes"], {"yes": [repeat_task]}, CAG)

said_task = CoachNode(["repeat", "done", "explain"], {"repeat": [repeat_task], "done": [finished_workout], "explain": [explain_task]}, CAG)




asked_for_task_name = CoachNode(['RAT'], {'RAT': [check_input]}, CAG)
checked_task_name = CoachNode(['yes', 'no'], {'yes': [ask_task_desc], 'no': [try_again]}, CAG)

asked_for_task_desc = CoachNode(['RAT'],{'RAT': [check_input]}, CAG)
checked_task_desc = CoachNode(['yes', 'no'], {'yes': [ask_task_priority], 'no': [try_again]}, CAG)

asked_for_task_priority = CoachNode(['low', 'medium', 'high', 'hi'], {'low': [low_t_added], 'medium': [med_t_added], 'high': [high_t_added], 'hi': [high_t_added]}, CAG)



manage_tasks = CoachNode(['edit','delete'],{'edit': [ask_user_edit_task], 'delete': [ask_user_delete_task]}, CAG) #map to limbo_node


limbo_node = CoachNode(['read'], {'read':[read_task_name]}, CAG) #add 'next' and 'back'

delete_task = CoachNode(['yes', 'no', 'cancel'], {'yes': [remove_task], 'no': [cancel_action], 'cancel': [cancel_action]}, CAG)

edit_task_feat = CoachNode(['name', 'description', 'priority', 'cancel', 'back'],{'name': [edit_task_name], 'description': [edit_task_desc], 'priority': [edit_task_priority], 'cancel': [cancel_action], 'back': [cancel_action]}, CAG)

asked_for_task_feat = CoachNode(['RAT'], {'RAT': [change_task_feat]}, CAG)

read_task = CoachNode(['next', 'repeat', 'back', 'edit','delete', 'explain', 'garden', 'garage', 'main'],
                      {'next': [read_next_task], 'repeat': [read_task_name], 'back': [read_prev_task], 'edit': [ask_user_edit_task],'explain': [read_task_desc], 'delete': [ask_user_delete_task], 'garden':[task_category_garden], 'garage': [task_category_garage], 'main':[task_category_core]}, CAG)

#gaeden, garage, main, core
# switch to category and read_task_name

#----------------------------------------------------------
nodes = [said_good_morning, asked_to_start_workout, said_workout, asked_if_say_task, said_task, asked_for_task_name, read_task]
CAG.all_nodes = nodes
# ------------- Edges ---------------------

said_good_morning.map["good"].append(asked_to_start_workout)
said_good_morning.map["fine"].append(asked_to_start_workout)
said_good_morning.map["bad"].append(asked_to_start_workout)

asked_to_start_workout.map["start"].append(said_workout)

said_workout.map["repeat"].append(said_workout)
said_workout.map["done"].append(said_task) #default next node

asked_if_say_task.map["yes"].append(said_task)

said_task.map["repeat"].append(said_task)
said_task.map["done"].append(said_task)
said_task.map["explain"].append(said_task)

asked_for_task_name.map['RAT'].append(checked_task_name)

checked_task_name.map['yes'].append(asked_for_task_desc)
checked_task_name.map['no'].append(asked_for_task_name)

asked_for_task_desc.map['RAT'].append(checked_task_desc)

checked_task_desc.map['yes'].append(asked_for_task_priority)
checked_task_desc.map['no'].append(asked_for_task_desc)

asked_for_task_priority.map['low'].append(read_task) #change to limbo node
asked_for_task_priority.map['medium'].append(read_task)
asked_for_task_priority.map['high'].append(read_task)
asked_for_task_priority.map['hi'].append(read_task)

#TODO
# - go through all tasks
#       'read all tasks' or 'read 2do list' --> read_todo() --> read_list_element = Node('next', 'repeat', 'back', 'edit', 'delete')

manage_tasks.map['edit'].append(edit_task_feat)
manage_tasks.map['delete'].append(delete_task)

limbo_node.map['read'].append(read_task)

delete_task.map['yes'].append(limbo_node)
delete_task.map['no'].append(limbo_node)
delete_task.map['cancel'].append(read_task)

edit_task_feat.map['name'].append(asked_for_task_feat)
edit_task_feat.map['description'].append(asked_for_task_feat)
edit_task_feat.map['priority'].append(asked_for_task_feat)
edit_task_feat.map['back'].append(read_task)
edit_task_feat.map['cancel'].append(read_task)

asked_for_task_feat.map['RAT'].append(read_task)

read_task.map['next'].append(read_task)
read_task.map['repeat'].append(read_task)
read_task.map['back'].append(read_task)
read_task.map['edit'].append(edit_task_feat)
read_task.map['explain'].append(read_task)
read_task.map['delete'].append(delete_task)
read_task.map['garden'].append(read_task)
read_task.map['garage'].append(read_task)
read_task.map['main'].append(read_task)


#__task list__
#-apply to jobs
#-code
#-project
#-record

