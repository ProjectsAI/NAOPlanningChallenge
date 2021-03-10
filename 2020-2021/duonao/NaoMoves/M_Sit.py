''' NAO va in una posizione seduta'''
import sys
import time

from naoqi import ALProxy


#def StiffnessOn(proxy):
#    # We use the "Body" name to signify the collection of all joints
#    pNames = "Body"
#    pStiffnessLists = 1.0
#    pTimeLists = 1.0
#    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def main(robotIP, port):
    try:
        ttsProxy = ALProxy("ALTextToSpeech", robotIP, port)
    except Exception, e:
        print("Could not create a proxy to ALTextToSpeech")

    ttsProxy.say("SIT")

    # Init proxies.
    """
    try:
        motionProxy = ALProxy("ALMotion", robotIP, port)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e
    """

    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, port)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e

    # Set NAO in Stiffness On
    #    StiffnessOn(motionProxy)
    # NAO:
    # time.sleep(1)

    # Set NAO in Stiffness On
    #    StiffnessOn(motionProxy)

    # Send NAO to Pose Crouch
    postureProxy.goToPosture("Sit", 1)


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

	start = time.time()
	main(robotIP, port)
	end = time.time()
	print ("%.2f seconds elapsed" % (end-start))

