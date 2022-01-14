import sys
import motion
import almath
import math
import time
from naoqi import ALProxy
import sys

def main(robotIP, port):
    # Init proxies.
    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, port)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e
    try:
        ttsProxy = ALProxy("ALTextToSpeech", robotIP, port)
    except Exception, e:
        print "Could not create proxy to ALTextToSpeech"

    # NAO speaks:
    ttsProxy.say("I'm tired...")
    #time.sleep(1)

    # Send NAO to Pose Sit
    postureProxy.goToPosture("Sit", 3.0)

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

