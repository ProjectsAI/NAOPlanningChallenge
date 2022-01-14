import sys
import time

from naoqi import ALProxy


def main(robotIP, port):
	try:
		ttsProxy = ALProxy("ALTextToSpeech", robotIP, port)
	except Exception, e:
		print("Could not create a proxy to ALTextToSpeech")

	ttsProxy.say("STAND INIT")

	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([1])
	keys.append([[-0.00723003, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("HeadYaw")
	times.append([1])
	keys.append([[0, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LAnklePitch")
	times.append([1])
	keys.append([[-0.35977, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LAnkleRoll")
	times.append([1])
	keys.append([[-0.00342701, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LElbowRoll")
	times.append([1])
	keys.append([[-1.00708, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LElbowYaw")
	times.append([1])
	keys.append([[-1.38708, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LHand")
	times.append([1])
	keys.append([[0.251307, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LHipPitch")
	times.append([1])
	keys.append([[-0.459146, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LHipRoll")
	times.append([1])
	keys.append([[0.00473462, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LHipYawPitch")
	times.append([1])
	keys.append([[-0.00938212, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LKneePitch")
	times.append([1])
	keys.append([[0.699999, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LShoulderPitch")
	times.append([1])
	keys.append([[1.40935, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LShoulderRoll")
	times.append([1])
	keys.append([[0.303286, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LWristYaw")
	times.append([1])
	keys.append([[-0.00943111, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RAnklePitch")
	times.append([1])
	keys.append([[-0.355675, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RAnkleRoll")
	times.append([1])
	keys.append([[0.000261785, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RElbowRoll")
	times.append([1])
	keys.append([[1.00756, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RElbowYaw")
	times.append([1])
	keys.append([[1.38907, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RHand")
	times.append([1])
	keys.append([[0.251295, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RHipPitch")
	times.append([1])
	keys.append([[-0.455985, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RHipRoll")
	times.append([1])
	keys.append([[-0.0013073, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RHipYawPitch")
	times.append([1])
	keys.append([[-0.00938212, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RKneePitch")
	times.append([1])
	keys.append([[0.709895, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RShoulderPitch")
	times.append([1])
	keys.append([[1.39696, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RShoulderRoll")
	times.append([1])
	keys.append([[-0.301146, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RWristYaw")
	times.append([1])
	keys.append([[0.00896677, [3, -0.333333, 0], [3, 0, 0]]])

	try:
		motion = ALProxy("ALMotion",robotIP,port)
		motion.angleInterpolationBezier(names, times, keys)
	except BaseException, err:
		print err
	  
  
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
