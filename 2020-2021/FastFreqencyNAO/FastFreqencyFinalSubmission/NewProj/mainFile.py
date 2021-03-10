import numpy as np
from naoqi import ALProxy

# import the optionalActions here
import m_StandInit, m_Hello, m_StandZero, m_Sit, m_SitRelax, m_Stand, m_WIpeForehead, m_Crouch
import o_Waving_Arms, o_unleashing, o_two, o_three, o_tampa02,o_tampa01, o_take_energy, o_snap, o_raising_arms,o_arms_movement, o_arms_rotation, o_bowing,o_clap,o_giving_rhythm, o_moving_hips, o_one

# lists that contains the optionalActions/ MandatoryAction
mandatoryPos = [m_StandInit, m_Hello, m_StandZero, m_Sit, m_SitRelax, m_Stand, m_WIpeForehead, m_Crouch]
availablePos = [o_Waving_Arms, o_unleashing, o_two, o_three, o_tampa02, o_tampa01, o_take_energy, o_snap, o_raising_arms, o_arms_movement, o_arms_rotation,o_bowing, o_clap, o_giving_rhythm, o_moving_hips, o_one]

# this functionn executes the action according to the given action file
def execute_performance(x):
    try:
        motion = ALProxy("ALMotion", "127.0.0.1", 43891)
        motion.angleInterpolation(x.names, x.keys, x.times, True)
    except BaseException as err:
        print(err)


# calculates the weight differences
def costDifference(coreValues1, coreValues2, coreValues3):
    return np.sum(np.abs(coreValues3-coreValues2) + np.abs(coreValues1-coreValues2))


def findTheNextNode():
    optimum = 100
    index = 0
    # picks up the most efficient position  & index
    for i in range(len(availablePos)):
        cost = costDifference(mandatoryPos[0], availablePos[i], mandatoryPos[1])
        if optimum > cost:
            optimum, index = cost, i
    print("Action chosen at index - ", index)
    execute_performance(availablePos[index])
    availablePos.pop(index)


def mainFunctionToRun():
    # get the initial positions
    while len(mandatoryPos) != 1:
        execute_performance(mandatoryPos[0])
        findTheNextNode()
        mandatoryPos.pop(0)

mainFunctionToRun()

"""
# copy paste from here to below and leave the two lists below. This code is used to calculate the values of position which are most important from each action file
import numpy as np
# randomness for the movements
data = list()
data.append(np.std(keys[5]))
data.append(np.std(keys[6]))
data.append(np.std(keys[8]))
data.append(np.std(keys[10]))
data.append(np.std(keys[11]))
data.append(np.std(keys[12]))
data.append(np.std(keys[13]))
print("KeyValue ", data)
keysValue = list()

# ending positions for the moves
tempPositionValue = list()
tempPositionValue.append(keys[5][-1])
tempPositionValue.append(keys[6][-1])
tempPositionValue.append(keys[8][-1])
tempPositionValue.append(keys[10][-1])
tempPositionValue.append(keys[11][-1])
tempPositionValue.append(keys[12][-1])
tempPositionValue.append(keys[13][-1])
print("tempPosition ", tempPositionValue)
finalPositionValue = list()

x = np.hstack(times)
print("time taken", np.sum(times[0]))

# copy paste the printed value and uncomment
# keysValue = []
# finalPositionValue = []
"""
