#estimate
def estimate_activity(pose_results, state):
    #estimate activity given pose
    #if short time has surpassed since last pose estimation -> smooth~moving average analog

    return "idk"


"""
camera default position is middle

if user enters sight and moves to right, turn to right.
if user enters sight and moves to left, turn to left.

if all the way right and user disapears -> user in backyard
if center and user disapears -> user in stairs or front
if all the way left and user disapears in right or center -> user in stairs or front


"""

"""
0 - nose
1 - left eye (inner)
2 - left eye
3 - left eye (outer)
4 - right eye (inner)
5 - right eye
6 - right eye (outer)
7 - left ear
8 - right ear
9 - mouth (left)
10 - mouth (right)
11 - left shoulder
12 - right shoulder
13 - left elbow
14 - right elbow
15 - left wrist
16 - right wrist
17 - left pinky
18 - right pinky
19 - left index
20 - right index
21 - left thumb
22 - right thumb
23 - left hip
24 - right hip
25 - left knee
26 - right knee
27 - left ankle
28 - right ankle
29 - left heel
30 - right heel
31 - left foot index
32 - right foot index

"""