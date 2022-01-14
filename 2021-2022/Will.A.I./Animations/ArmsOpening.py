''' Movimento Completo Apertura Braccia con Rotazione '''

import sys
import time

import almath
from naoqi import ALProxy


#def StiffnessOn(proxy):
#    # We use the "Body" name to signify the collection of all joints
#    pNames = "Body"
#    pStiffnessLists = 1.0
#    pTimeLists = 1.0
#    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def main(robotIP, port):
    # Init proxies.
    try:
        motionProxy = ALProxy("ALMotion", robotIP, port)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e

    # Set NAO in Stiffness On

#    StiffnessOn(motionProxy)
    # NAO:
    #ttsProxy.say("Ora invece eseguiro due movimenti con entrambe le braccia e cerchero il piu possibile di mantenere il ventaglio aperto.")
    #time.sleep(1)

    # Moving

    ########## Start position ###########

    RShoulderPitch = 78.0
    RShoulderRoll = -16.6
    RElbowYaw = 68.3
    RElbowRoll = 49.2
    RWristYaw = 4.3
    RHand = 0.10
    LShoulderPitch = 78.0
    LShoulderRoll = 16.6
    LElbowYaw = -68.3
    LElbowRoll = -49.2
    LWristYaw = 4.3
    LHand = 0.0


    names = "LArm"
    angleLists = [ LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,
                   LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand ]
    timeLists = 2
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, True)


    names = "RArm"
    angleLists = [ RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,
                   RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand ]
    timeLists = 2
    motionProxy.angleInterpolation(names, angleLists, timeLists, True)

    #time.sleep(0.2) # Waiting between the two movements

    ########## Movement arms  ###########

    RShoulderPitch = 24.9
    RShoulderRoll = 8.0
    RElbowYaw = 67.8
    RElbowRoll = 14.7
    RWristYaw = 79.3
    RHand = 0.35
    LShoulderPitch = 68.8
    LShoulderRoll = 14.3
    LElbowYaw = -68.4
    LElbowRoll = -53.9
    LWristYaw = 4.5
    LHand = 0.0


    names = "LArm"
    angleLists = [ LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,
                   LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand * almath.TO_RAD ]
    motionProxy.setAngles(names, angleLists, 0.08)


    names = "RArm"
    angleLists = [ RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,
                   RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD ]
    motionProxy.setAngles(names, angleLists, 0.08)

    #time.sleep(1.2)

    # Close arms
    RShoulderPitch = 24.5
    RShoulderRoll = 16.9
    RElbowYaw = 67.4
    RElbowRoll = 14.9
    RWristYaw = 79.1
    RHand = 0.35
    LShoulderPitch = 66.7
    LShoulderRoll = -12.3
    LElbowYaw = -69.0
    LElbowRoll = -53.7
    LWristYaw = 4.6
    LHand = 0.0


    names = "LArm"
    angleLists = [ LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,
                   LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand * almath.TO_RAD ]
    motionProxy.setAngles(names, angleLists, 0.1)


    names = "RArm"
    angleLists = [ RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,
                   RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD ]
    motionProxy.setAngles(names, angleLists, 0.15)

    #time.sleep(0.4)

    # Stretch and raise arms
    RShoulderPitch = 24.7
    RShoulderRoll = -51.8
    RElbowYaw = 45.6
    RElbowRoll = 14.7
    RWristYaw = 78.9
    RHand = 0.35
    LShoulderPitch = 24.7
    LShoulderRoll = 51.8
    LElbowYaw = -45.6
    LElbowRoll = -14.7
    LWristYaw = -78.9
    LHand = 0.0


    names = "RArm"

    angleLists = [ RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,
                   RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD ]
    motionProxy.setAngles(names, angleLists, 0.1)

    time.sleep(0.2)


    names = "LArm"
    angleLists = [ LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,
                   LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand * almath.TO_RAD ]
    motionProxy.setAngles(names, angleLists, 0.1)

    #time.sleep(2.2)

    # Final position
    RShoulderPitch = 66.4
    RShoulderRoll = -26.1
    RElbowYaw = 106.0
    RElbowRoll = 80
    RWristYaw = 85
    RHand = 0.35
    LShoulderPitch = 66.4
    LShoulderRoll = 26.1
    LElbowYaw = -106.0
    LElbowRoll = -44.2
    LWristYaw = 4.6
    LHand = 0.0


    names = "LArm"
    angleLists = [ LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,
                   LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand * almath.TO_RAD ]
    timeLists = 1.5
    motionProxy.post.angleInterpolation(names, angleLists, timeLists, True)


    names = "RArm"
    angleLists = [ RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,
                   RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD ]
    timeLists = 1.5
    motionProxy.angleInterpolation(names, angleLists, timeLists, True)


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
