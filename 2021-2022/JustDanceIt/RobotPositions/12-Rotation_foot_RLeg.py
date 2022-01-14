''' Rotazione piede RLeg e ritorno in posizione:
    NAO senza staccare i piedi da terra ruota internamente
    RLeg, attende qualche secondo,e poi lo ruota nuovamente
    per tornare alla posizione di partenza '''
import sys
import motion
import almath
import math
import time
from naoqi import ALProxy

start = time.time()

unit_time = float(sys.argv[3])/4
legs = bool(int(sys.argv[4]))

def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = unit_time/2
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

def main(robotIP, port, unit_time):
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

    # Set NAO in Stiffness On
    #StiffnessOn(motionProxy)

    # Send NAO to Pose Init
    postureProxy.goToPosture("StandInit", 0.3*(2/unit_time))

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

    space      =  motion.FRAME_ROBOT
    axisMask   = 63                     # control all the effector's axes
    isAbsolute = False

    # Lower the Torso and move to the side
    effector = "Torso"
    path     = [0.0, 0.00, 0.00, 0.0, 0.0, 0.05]
    timeList = unit_time/2*3
    motionProxy.positionInterpolation(effector, space, path, axisMask, timeList, isAbsolute)

    time.sleep(unit_time/2) # wait a few seconds

    # Back to the inizial position
    postureProxy.goToPosture("StandInit", 0.2*(2/unit_time))
    motionProxy.wbEnable(False)


if __name__ == "__main__":
    robotIP = "127.0.0.1"#"192.168.11.3"
    port = 9559 # Insert NAO port

    if len(sys.argv) <= 1:
        print "(robotIP default: 127.0.0.1)"
    elif len(sys.argv) <= 2:
        robotIP = sys.argv[1]
    else:
        port = int(sys.argv[2])
        robotIP = sys.argv[1]
    
    if not legs:
        unit_time = unit_time*(0.82)

    main(robotIP, port, unit_time)

end = time.time()
print(end-start)