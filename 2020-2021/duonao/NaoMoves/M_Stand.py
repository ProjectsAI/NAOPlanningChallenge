import sys
import time

from naoqi import ALProxy


def main(robotIP, port):
	try:
		ttsProxy = ALProxy("ALTextToSpeech", robotIP, port)
	except Exception, e:
		print("Could not create a proxy to ALTextToSpeech")

	ttsProxy.say("STAND")

	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([1, 2])
	keys.append([[-0.169063, [3, -0.333333, 0], [3, 0.333333, 0]], [0, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("HeadYaw")
	times.append([1, 2])
	keys.append([[-0.00843369, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.00843369, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LAnklePitch")
	times.append([1, 2])
	keys.append([[0.0895551, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.345059, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LAnkleRoll")
	times.append([1, 2])
	keys.append([[-0.13, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.00852969, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LElbowRoll")
	times.append([1, 2])
	keys.append([[-0.413308, [3, -0.333333, 0], [3, 0.333333, 0]], [-1.00499, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LElbowYaw")
	times.append([1, 2])
	keys.append([[-1.19139, [3, -0.333333, 0], [3, 0.333333, 0]], [-1.38293, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LHand")
	times.append([1, 2])
	keys.append([[0.298421, [3, -0.333333, 0], [3, 0.333333, 0]], [0.257813, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LHipPitch")
	times.append([1, 2])
	keys.append([[0.13, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.443486, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LHipRoll")
	times.append([1, 2])
	keys.append([[0.0959189, [3, -0.333333, 0], [3, 0.333333, 0]], [0.00112305, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LHipYawPitch")
	times.append([1, 2])
	keys.append([[-0.16912, [3, -0.333333, 0], [3, 0.333333, 0]], [0, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LKneePitch")
	times.append([1, 2])
	keys.append([[-0.0860816, [3, -0.333333, 0], [3, 0.333333, 0]], [0.691128, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LShoulderPitch")
	times.append([1, 2])
	keys.append([[1.46258, [3, -0.333333, 0], [3, 0.333333, 0]], [1.40681, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LShoulderRoll")
	times.append([1, 2])
	keys.append([[0.175502, [3, -0.333333, 0], [3, 0.333333, 0]], [0.297247, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LWristYaw")
	times.append([1, 2])
	keys.append([[0.0994729, [3, -0.333333, 0], [3, 0.333333, 0]], [0.00303542, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RAnklePitch")
	times.append([1, 2])
	keys.append([[0.0895548, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.345059, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RAnkleRoll")
	times.append([1, 2])
	keys.append([[0.120349, [3, -0.333333, 0], [3, 0.333333, 0]], [0.00852969, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RElbowRoll")
	times.append([1, 2])
	keys.append([[0.413489, [3, -0.333333, 0], [3, 0.333333, 0]], [1.00499, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RElbowYaw")
	times.append([1, 2])
	keys.append([[1.19159, [3, -0.333333, 0], [3, 0.333333, 0]], [1.38293, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RHand")
	times.append([1, 2])
	keys.append([[0.298421, [3, -0.333333, 0], [3, 0.333333, 0]], [0.257813, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RHipPitch")
	times.append([1, 2])
	keys.append([[0.13, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.443486, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RHipRoll")
	times.append([1, 2])
	keys.append([[-0.0958409, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.00112305, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RHipYawPitch")
	times.append([1, 2])
	keys.append([[-0.16912, [3, -0.333333, 0], [3, 0.333333, 0]], [0, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RKneePitch")
	times.append([1, 2])
	keys.append([[-0.0895528, [3, -0.333333, 0], [3, 0.333333, 0]], [0.691128, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RShoulderPitch")
	times.append([1, 2])
	keys.append([[1.46238, [3, -0.333333, 0], [3, 0.333333, 0]], [1.40681, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RShoulderRoll")
	times.append([1, 2])
	keys.append([[-0.185298, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.297247, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RWristYaw")
	times.append([1, 2])
	keys.append([[0.0995004, [3, -0.333333, 0], [3, 0.333333, 0]], [0.00303542, [3, -0.333333, 0], [3, 0, 0]]])

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
