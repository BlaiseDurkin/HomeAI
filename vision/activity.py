#estimate
def estimate_activity(pose_results, state):
    #estimate activity given pose
    #if short time has surpassed since last pose estimation -> smooth~moving average analog
    print("Estimating activity...")
    if state.orientation == "center":
        print("Orientation is center")
    if state.orientation == "left":
        print("Orientation is left")
    if state.orientation == "right":
        print("Orientation is right")
    return "idk"



"""
camera default position is middle

if user enters sight and moves to right, turn to right.
if user enters sight and moves to left, turn to left.

if all the way right and user disapears -> user in backyard
if center and user disapears -> user in stairs or front
if all the way left and user disapears in right or center -> user in stairs or front


"""