# Choregraphe simplified export in Python.
from naoqi import ALProxy
import sys

def main(robotIP, port):
	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([0.96, 1.36, 1.52, 1.68, 2.88, 3.04, 3.2, 3.88, 4.44, 5])
	keys.append([-0.0261199, -0.00204094, 0.000822467, -0.0010357, -0.00137078, 0.00137078, 0.00127939, 0.11194, -0.013848, 0.061318])

	names.append("HeadYaw")
	times.append([0.96, 1.36, 1.52, 1.68, 2.88, 3.04, 3.2, 3.88, 4.44, 5])
	keys.append([0.00140124, 0.0014317, 0.000852928, 0.000852928, 0.00365541, 0.00365541, 0.00426464, -0.00617796, -0.027654, -0.036858])

	names.append("LElbowRoll")
	times.append([0.8, 1.52, 3.04, 3.72, 4.28, 4.84])
	keys.append([-0.866668, -0.868202, -0.822183, -0.992455, -0.966378, -0.990923])

	names.append("LElbowYaw")
	times.append([0.8, 1.52, 3.04, 3.72, 4.28, 4.84])
	keys.append([-0.957257, -0.823801, -1.00788, -0.925044, -1.24412, -0.960325])

	names.append("LHand")
	times.append([1.52, 3.04, 3.72, 4.84])
	keys.append([0.132026, 0.132026, 0.132026, 0.132026])

	names.append("LShoulderPitch")
	times.append([0.8, 1.52, 3.04, 3.72, 4.28, 4.84])
	keys.append([0.863599, 0.858999, 0.888144, 0.929562, 1.017, 0.977116])

	names.append("LShoulderRoll")
	times.append([0.8, 1.52, 3.04, 3.72, 4.28, 4.84])
	keys.append([0.286815, 0.230059, 0.202446, 0.406468, 0.360449, 0.31903])

	names.append("LWristYaw")
	times.append([1.52, 3.04, 3.72, 4.84])
	keys.append([0.386526, 0.386526, 0.386526, 0.386526])

	names.append("RElbowRoll")
	times.append([0.64, 1.36, 2.88, 3.56, 4.12, 4.64])
	keys.append([1.28093, 1.39752, 1.57239, 1.24105, 1.22571, 0.840674])

	names.append("RElbowYaw")
	times.append([0.64, 1.36, 2.88, 3.56, 4.12, 4.64])
	keys.append([-0.128898, -0.285367, -0.15651, 0.754686, 1.17193, 0.677985])

	names.append("RHand")
	times.append([0.64, 0.8, 0.96, 1.36, 1.52, 1.68, 2.88, 3.04, 3.56, 3.72, 4.64])
	keys.append([1, 1, 1, 1, 1, 1, 1, 1, 0.98, 1, 0.166208])

	names.append("RShoulderPitch")
	times.append([0.64, 1.36, 2.88, 3.56, 4.12, 4.64])
	keys.append([0.0767419, -0.59515, -0.866668, -0.613558, 0.584497, 0.882091])

	names.append("RShoulderRoll")
	times.append([0.64, 1.36, 2.88, 3.56, 4.12, 4.64])
	keys.append([-0.019984, -0.019984, -0.615176, -0.833004, -0.224006, -0.214801])

	names.append("RWristYaw")
	times.append([1.36, 2.88, 3.56, 4.64])
	keys.append([-0.058334, -0.0521979, -0.067538, -0.038392])

	try:
		motion = ALProxy("ALMotion", robotIP, port)
		motion.angleInterpolation(names, keys, times, True)
	except BaseException, err:
		print err
	try:
		postureProxy = ALProxy("ALRobotPosture", robotIP, port)
		postureProxy.goToPosture("Stand", 0.5)
	except  Exception, e:
		print "Could not create proxy to ALRobotPosture"

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
