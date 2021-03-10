import sys
import time

from naoqi import ALProxy


def main(robotIP, port):
	try:
		ttsProxy = ALProxy("ALTextToSpeech", robotIP, port)
	except Exception, e:
		print("Could not create a proxy to ALTextToSpeech")

	ttsProxy.say("CROUCH")

	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([1])
	keys.append([[0.099661, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("HeadYaw")
	times.append([1])
	keys.append([[-0.00711237, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LAnklePitch")
	times.append([1])
	keys.append([[-1.18, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LAnkleRoll")
	times.append([1])
	keys.append([[0.068992, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LElbowRoll")
	times.append([1])
	keys.append([[-1.07296, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LElbowYaw")
	times.append([1])
	keys.append([[-0.793177, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LHand")
	times.append([1])
	keys.append([[0.000844251, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LHipPitch")
	times.append([1])
	keys.append([[-0.699185, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LHipRoll")
	times.append([1])
	keys.append([[-0.073343, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LHipYawPitch")
	times.append([1])
	keys.append([[-0.249199, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LKneePitch")
	times.append([1])
	keys.append([[2.1054, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LShoulderPitch")
	times.append([1])
	keys.append([[1.40121, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LShoulderRoll")
	times.append([1])
	keys.append([[0.160449, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LWristYaw")
	times.append([1])
	keys.append([[0.142231, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RAnklePitch")
	times.append([1])
	keys.append([[-1.18, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RAnkleRoll")
	times.append([1])
	keys.append([[-0.068992, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RElbowRoll")
	times.append([1])
	keys.append([[1.07296, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RElbowYaw")
	times.append([1])
	keys.append([[0.793161, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RHand")
	times.append([1])
	keys.append([[0.000846233, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RHipPitch")
	times.append([1])
	keys.append([[-0.699185, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RHipRoll")
	times.append([1])
	keys.append([[0.0759977, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RHipYawPitch")
	times.append([1])
	keys.append([[-0.249199, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RKneePitch")
	times.append([1])
	keys.append([[2.1054, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RShoulderPitch")
	times.append([1])
	keys.append([[1.40122, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RShoulderRoll")
	times.append([1])
	keys.append([[-0.160239, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RWristYaw")
	times.append([1])
	keys.append([[-0.141808, [3, -0.333333, 0], [3, 0, 0]]])

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
