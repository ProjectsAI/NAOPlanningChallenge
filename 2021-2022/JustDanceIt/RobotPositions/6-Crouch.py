''' NAO va in una posizione simile a quella in ginocchio
    ma con entrambi i piedi attaccati al suolo (Crouch) '''
import sys
import motion
import almath
import math
import time
from naoqi import ALProxy

start =time.time()

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
    #ttsProxy.say("Infine termino nella posizione in ginocchio.")
    #time.sleep(1)

    # Set NAO in Stiffness On
    # StiffnessOn(motionProxy)

    # Send NAO to Pose Crouch
    postureProxy.goToPosture("Crouch", 1/unit_time)


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

    unit_time = float(sys.argv[3])

    main(robotIP, port, unit_time)

end = time.time()
print(end-start)
