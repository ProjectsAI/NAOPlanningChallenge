# -*- encoding: UTF-8 -*-

''' Walk: Small example to make Nao walk '''
'''       with jerky head                '''
''' This example is only compatible with NAO '''
import sys
import argparse
import time
import random
from naoqi import ALProxy

def main(robotIP, PORT=9559):

    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    postureProxy = ALProxy("ALRobotPosture", robotIP, PORT)

    # Wake up robot
    motionProxy.wakeUp()

    # Send robot to Stand Init
    postureProxy.goToPosture("StandInit", 0.5)

    # Initialize the move process.
    # Check the robot pose and take a right posture.
    # This is blocking called.
    motionProxy.moveInit()

    testTime = 2.0 # seconds
    t  = 0.0
    dt = 0.2

    while t<testTime:
        # WALK
        X         = random.uniform(0.4, 1.0)
        Y         = random.uniform(-0.4, 0.4)
        Theta     = random.uniform(-0.4, 0.4)
        Frequency = random.uniform(0.5, 1.0)
        try:
            motionProxy.moveToward(X, Y, Theta, [["Frequency", Frequency]])
        except Exception, errorMsg:
            print str(errorMsg)
            print "This example is not allowed on this robot."
            exit()

        # JERKY HEAD
        motionProxy.setAngles("HeadYaw", random.uniform(-1.0, 1.0), 0.6)
        motionProxy.setAngles("HeadPitch", random.uniform(-0.5, 0.5), 0.6)

        t = t + dt
        time.sleep(dt)

    # stop move on the next double support
    motionProxy.stopMove()
    
    # Send robot to Stand Init
    postureProxy.goToPosture("StandInit", 0.3)

    # Go to rest position
    #motionProxy.rest()

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
