'''
***************************** N.B. **************************************
This move unifies two moves, 'rotation_foot_LLeg' and 'rotation_foot_RLeg'
'''

import sys
import motion
from naoqi import ALProxy

def main(robotIP, port):
    # Init proxies.
    try:
        motionProxy = ALProxy("ALMotion", robotIP, port)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e
    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, port)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e

    # *** rotation_foot_RLeg ***
    postureProxy.goToPosture("StandInit", 0.5)
    motionProxy.wbEnable(True)

    # Legs/Feet Configuration
    stateName = "Plane"
    supportLeg = "RLeg"
    motionProxy.wbFootState(stateName, supportLeg)
    stateName = "Fixed"
    supportLeg = "LLeg"
    motionProxy.wbFootState(stateName, supportLeg)

    # Cartesian foot trajectory
    # Warning: Needs a PoseInit before executing
    space = motion.FRAME_ROBOT
    axisMask = 63  # control all the effector's axes
    isAbsolute = False

    # Lower the Torso and move to the side
    effector = "Torso"
    path = [0.0, 0.00, 0.00, 0.0, 0.0, 0.05]
    timeList = 1.0  # seconds
    motionProxy.positionInterpolation(effector, space, path,
                                        axisMask, timeList, isAbsolute)

    # Back to the inizial position
    postureProxy.goToPosture("StandInit", 0.5)
    motionProxy.wbEnable(False)

    # *** rotation_foot_LLeg ***
    # Send NAO to Pose Init
    postureProxy.goToPosture("StandInit", 0.5)
    motionProxy.wbEnable(True)

    # Legs/Feet configuration
    stateName = "Fixed"
    supportLeg = "RLeg"
    motionProxy.wbFootState(stateName, supportLeg)
    stateName = "Plane"
    supportLeg = "LLeg"
    motionProxy.wbFootState(stateName, supportLeg)

    # Cartesian foot trajectory
    # Warning: Needs a PoseInit before executing
    space = motion.FRAME_ROBOT
    axisMask = 63  # control all the effector's axes
    isAbsolute = False

    # Lower the Torso and move to the side
    effector = "Torso"
    path = [0.0, 0.0, 0.15, 0.0, 0.0, 0.05]
    timeList = 1.0  # seconds
    motionProxy.positionInterpolation(effector, space, path,
                                      axisMask, timeList, isAbsolute)

    postureProxy.goToPosture("StandInit", 0.5)
    motionProxy.wbEnable(False)

if __name__ == "__main__":
	robotIP = "127.0.0.1"
	port = 9559

	if len(sys.argv) <= 1:
		print "(robotIP default: 127.0.0.1)"
	elif len(sys.argv) <= 2:
		robotIP = sys.argv[1]
	else:
		port = int(sys.argv[2])
		robotIP = sys.argv[1]

	main(robotIP, port)