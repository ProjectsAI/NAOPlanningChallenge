''' Movimento Completo Movimento Doppio '''
import sys
import motion
import almath
import time
from naoqi import ALProxy

#def StiffnessOn(proxy):
#    # We use the "Body" name to signify the collection of all joints
#    pNames = "Body"
#    pStiffnessLists = 1.0
#    pTimeLists = 1.0
#    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


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

    try:
        ttsProxy = ALProxy("ALTextToSpeech", robotIP, port)
    except Exception, e:
        print "Could not create proxy to ALTextToSpeech"
        print "Error was: ", e

    # Set NAO in Stiffness On
    # StiffnessOn(motionProxy)
    # NAO:
    #ttsProxy.say("Ora eseguiro un secondo movimento piu breve con entrambe le braccia mantenedo sempre il ventaglio aperto")
    #time.sleep(1)

    # Moving

    ########## Start position ###########
    start = time.time()

    RShoulderPitch = 78.0
    RShoulderRoll = -39.9
    RElbowYaw = 68.3
    RElbowRoll = 57.2
    RWristYaw = 95
    RHand = 0.10

    LShoulderPitch = 78.0
    LShoulderRoll = 39.9
    LElbowYaw = -68.3
    LElbowRoll = -57.2
    LWristYaw = 4.3
    LHand = 0.0

    names = "LArm"
    angleLists = [  LShoulderPitch * almath.TO_RAD,
                    LShoulderRoll * almath.TO_RAD,
                    LElbowYaw * almath.TO_RAD,
                    LElbowRoll * almath.TO_RAD,
                    LWristYaw * almath.TO_RAD,
                    LHand ]
    timeLists = unit_time/6*5
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, True)
    
    names = "RArm"
    angleLists = [  RShoulderPitch * almath.TO_RAD,
                    RShoulderRoll * almath.TO_RAD,
                    RElbowYaw * almath.TO_RAD,
                    RElbowRoll * almath.TO_RAD,
                    RWristYaw * almath.TO_RAD,
                    RHand ]
    timeLists = unit_time/6*5
    motionProxy.angleInterpolation(names, angleLists, timeLists, True)

    time.sleep(unit_time/6) # Waiting between the two movements
    end1 = time.time()
    ########## Movement arms ###########
    # Start rotation movement
    RShoulderPitch = 77.7
    RShoulderRoll = -39.5
    RElbowYaw = 33.7
    RElbowRoll = 70
    RWristYaw = 95
    RHand = 0.10

    LShoulderPitch = 77.8
    LShoulderRoll = 49.2
    LElbowYaw = -68.5
    LElbowRoll = -9.4
    LWristYaw = 4.5
    LHand = 0.0

    names = "RArm"
    angleLists = [  RShoulderPitch * almath.TO_RAD,
                    RShoulderRoll * almath.TO_RAD,
                    RElbowYaw * almath.TO_RAD,
                    RElbowRoll * almath.TO_RAD,
                    RWristYaw * almath.TO_RAD,
                    RHand * almath.TO_RAD ]
    motionProxy.setAngles(names, angleLists, 0.05*(1/unit_time))

    time.sleep(unit_time/7)
    end2 = time.time()
    names = "LArm"
    angleLists = [  LShoulderPitch * almath.TO_RAD,
                    LShoulderRoll * almath.TO_RAD,
                    LElbowYaw * almath.TO_RAD,
                    LElbowRoll * almath.TO_RAD,
                    LWristYaw * almath.TO_RAD,
                    LHand * almath.TO_RAD ]
    motionProxy.setAngles(names, angleLists, 0.08*(1/unit_time))

    time.sleep(unit_time/7*6)
    end3 = time.time()
    # Arms parallel to the floor
    RShoulderPitch = 15.1
    RShoulderRoll = -10.6
    RElbowYaw = 9.5
    RElbowRoll = 70
    RWristYaw = 95
    RHand = 0.10

    LShoulderPitch = 77.8
    LShoulderRoll = 75.8
    LElbowYaw = -68.5
    LElbowRoll = -2.5
    LWristYaw = 4.5
    LHand = 0.0

    names = "RArm"
    angleLists = [  RShoulderPitch * almath.TO_RAD,
                    RShoulderRoll * almath.TO_RAD,
                    RElbowYaw * almath.TO_RAD,
                    RElbowRoll * almath.TO_RAD,
                    RWristYaw * almath.TO_RAD,
                    RHand * almath.TO_RAD ]
    motionProxy.setAngles(names, angleLists, 0.15*(1/unit_time))
    time.sleep(unit_time/3)
    end4 = time.time()
    names = "LArm"
    angleLists = [  LShoulderPitch * almath.TO_RAD,
                    LShoulderRoll * almath.TO_RAD,
                    LElbowYaw * almath.TO_RAD,
                    LElbowRoll * almath.TO_RAD,
                    LWristYaw * almath.TO_RAD,
                    LHand * almath.TO_RAD ]
    motionProxy.setAngles(names, angleLists, 0.1*(1/unit_time))

    time.sleep(unit_time/3*2)
    end5 = time.time()
    # Go to final position
    RShoulderPitch = 62.4
    RShoulderRoll = -15.7
    RElbowYaw = 51.7
    RElbowRoll = 81
    RWristYaw = 105
    RHand = 0.10

    LShoulderPitch = 40.0
    LShoulderRoll = 29.8
    LElbowYaw = -72.9
    LElbowRoll = -27.2
    LWristYaw = 4.5
    LHand = 0.0

    names = "RArm"
    angleLists = [  RShoulderPitch * almath.TO_RAD,
                    RShoulderRoll * almath.TO_RAD,
                    RElbowYaw * almath.TO_RAD,
                    RElbowRoll * almath.TO_RAD,
                    RWristYaw * almath.TO_RAD,
                    RHand * almath.TO_RAD ]
    motionProxy.post.angleInterpolation(names, angleLists, unit_time*0.83, True)

    time.sleep(unit_time*0.17)
    end6 = time.time()
    names = "LArm"
    angleLists = [  LShoulderPitch * almath.TO_RAD,
                    LShoulderRoll * almath.TO_RAD,
                    LElbowYaw * almath.TO_RAD,
                    LElbowRoll * almath.TO_RAD,
                    LWristYaw * almath.TO_RAD,
                    LHand * almath.TO_RAD ]
    motionProxy.angleInterpolation(names, angleLists, unit_time*0.83, True)

    end = time.time()
    print(end1-start)
    print(end2-start)
    print(end3-start)
    print(end4-start)
    print(end5-start)
    print(end6-start)
    print(end-start)


if __name__ == "__main__":
    robotIP = "127.0.0.1" #"192.168.1.11"
    port = 9559 # Insert NAO port

    if len(sys.argv) <= 1:
        print "(robotIP default: 127.0.0.1)"
    elif len(sys.argv) <= 2:
        robotIP = sys.argv[1]
    else:
        port = int(sys.argv[2])
        robotIP = sys.argv[1]

    unit_time = float(sys.argv[3])/4

    main(robotIP, port, unit_time)
