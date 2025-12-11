
from coach.coach_ass import *



# coach
#   - data : task_lists { easy_task, hard_task
#   - mantras: internal narrative hacking


class CoachAssistantGraph:
    def __init__(self):
        self.current_node = None
        self.all_nodes = []
        self.workout = ""

    def update(self, message):
        response = self.current_node.update(message)
        #TODO
        # - check if response is string
        return response



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
        response = self.map[key][0](self.graph)
        #print('node update: ',response)
        return response

# ----------- Nodes -----------------------
CAG = CoachAssistantGraph()

said_good_morning = CoachNode(["good","fine", "bad"], {"good": [slept_good],"fine": [slept_fine], "bad": [slept_bad]}, CAG)

asked_to_start_workout = CoachNode(["start"], {"start": [start_workout]}, CAG)

said_workout = CoachNode(["repeat", "done"], {"repeat": [repeat_workout], "done": [finished_workout]}, CAG)

said_task = CoachNode(["repeat", "done"], {"repeat": [repeat_task], "done": [finished_workout]}, CAG)

#----------------------------------------------------------
nodes = [said_good_morning, asked_to_start_workout, said_workout, said_task]
CAG.all_nodes = nodes
# ------------- Edges ---------------------

said_good_morning.map["good"].append(asked_to_start_workout)
said_good_morning.map["fine"].append(asked_to_start_workout)
said_good_morning.map["bad"].append(asked_to_start_workout)

asked_to_start_workout.map["start"].append(said_workout)

said_workout.map["repeat"].append(said_workout)
said_workout.map["done"].append(said_task) #default next node

said_task.map["repeat"].append(said_task)

#__task list__
#-apply to jobs
#-code
#-project
#-record

