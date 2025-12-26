import numpy as np


from enum import Enum


class Activity(Enum):
    STANDING = "standing"
    SITTING = "sitting"
    LYING = "lying_down"
    UNKNOWN = "unknown"


def estimate_activity(pose_results, state, height_threshold_ratio=0.15, angle_threshold=25):
    """
    Estimates whether the person is standing, sitting, or lying down.

    Args:
        pose_results: MediaPipe Pose solution output
        state: Optional previous state for temporal smoothing (not used here but kept for compatibility)
        height_threshold_ratio: Fraction of shoulder height to consider heights "similar"
        angle_threshold: Degrees around 180° to consider torso "straight"

    Returns:
        Activity enum and confidence dict
    """
    if pose_results.pose_landmarks is None:
        return Activity.UNKNOWN

    landmarks = pose_results.pose_landmarks.landmark

    # Key points (MediaPipe Pose landmark indices)
    shoulder_l = landmarks[11]  # left_shoulder
    shoulder_r = landmarks[12]  # right_shoulder
    hip_l = landmarks[23]  # left_hip
    hip_r = landmarks[24]  # right_hip
    knee_l = landmarks[25]  # left_knee
    knee_r = landmarks[26]  # right_knee

    # Use midpoints for robustness
    mid_shoulder = np.array([(shoulder_l.x + shoulder_r.x) / 2,
                             (shoulder_l.y + shoulder_r.y) / 2])
    mid_hip = np.array([(hip_l.x + hip_r.x) / 2,
                        (hip_l.y + hip_r.y) / 2])
    mid_knee = np.array([(knee_l.x + knee_r.x) / 2,
                         (knee_l.y + knee_r.y) / 2])

    # Vector from shoulder → hip → knee
    vec_shoulder_to_hip = mid_hip - mid_shoulder
    vec_hip_to_knee = mid_knee - mid_hip

    # Calculate angle at the hip (shoulder-hip-knee angle)
    def angle_between(v1, v2):
        dot = np.dot(v1, v2)
        norm1 = np.linalg.norm(v1)
        norm2 = np.linalg.norm(v2)
        if norm1 == 0 or norm2 == 0:
            return 180.0
        cos_theta = np.clip(dot / (norm1 * norm2), -1.0, 1.0)
        return np.degrees(np.arccos(cos_theta))

    body_angle = angle_between(vec_shoulder_to_hip, vec_hip_to_knee)

    # Average Y positions (in image coordinates: y increases downward)
    y_shoulder = (shoulder_l.y + shoulder_r.y) / 2
    y_hip = (hip_l.y + hip_r.y) / 2
    y_knee = (knee_l.y + knee_r.y) / 2

    x_shoulder = (shoulder_l.x + shoulder_r.x) / 2
    x_hip = (hip_l.x + hip_r.x) / 2
    x_knee = (knee_l.x + knee_r.x) / 2

    dy_shoulder_to_hip = abs(y_shoulder - y_hip)
    dy_hip_to_knee = abs(y_hip - y_knee)
    height_shoulder_avg = y_shoulder  # reference height from top

    # Threshold: if vertical differences are small → person is horizontal (lying)
    dx_shoulder_to_hip = abs(x_shoulder - x_hip)
    dx_hip_to_knee = abs(x_hip - x_knee)

    is_horizontal = (dy_shoulder_to_hip < dx_shoulder_to_hip and
                     dy_hip_to_knee < dx_hip_to_knee)

    # Decision logic
    if is_horizontal:
        return Activity.LYING

    elif abs(body_angle - 180) < angle_threshold or abs(body_angle - 0) < angle_threshold:
        # Torso and legs are straight → standing (or upright plank, but rare)
        return Activity.STANDING

    elif 60 < body_angle < 130 or 230 < body_angle < 300:
        # Hip angle around 90° → sitting
        return Activity.SITTING

    else:
        return Activity.UNKNOWN


# Example usage:
# activity, info = estimate_activity(pose_results)
# print(activity.value, info)





# pose category
"""
stance
- squat
- sitting
- lying down
- standing

action
- walking
- sitting
- squating
- pushups
- arm circles
- flutter kicks
"""
#location


#if short time has surpassed since last pose estimation -> smooth~moving average


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