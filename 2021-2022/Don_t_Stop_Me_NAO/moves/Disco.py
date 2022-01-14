# Choregraphe simplified export in Python.
from naoqi import ALProxy
import sys

def main(robotIP, port):
	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([0.88, 2.24, 3.6, 5])
	keys.append([-0.268493, 0.118076, -0.268493, 0.118076])

	names.append("HeadYaw")
	times.append([0.88, 2.24, 3.6, 5])
	keys.append([0.384992, -0.214803, 0.384992, -0.214803])

	names.append("LAnklePitch")
	times.append([0.88, 2.24, 3.6, 5])
	keys.append([0.174835, 0.179436, 0.174835, 0.179436])

	names.append("LAnkleRoll")
	times.append([0.88, 2.24, 3.6, 5])
	keys.append([-0.0720561, -0.141086, -0.0720561, -0.141086])

	names.append("LElbowRoll")
	times.append([0.36, 0.88, 1.56, 2.24, 2.88, 3.6, 4.28, 5])
	keys.append([-1.22562, -0.199378, -1.22562, -0.391128, -1.22562, -0.199378, -1.22562, -0.391128])

	names.append("LElbowYaw")
	times.append([0.36, 0.88, 1.56, 2.24, 2.88, 3.6, 4.28, 5])
	keys.append([-0.803859, -1.56165, -0.803859, -0.337522, -0.803859, -1.56165, -0.803859, -0.337522])

	names.append("LHand")
	times.append([0.36, 0.88, 1.56, 2.24, 2.88, 3.6, 4.28, 5])
	keys.append([0.8592, 0.8592, 0.8592, 0.8592, 0.8592, 0.8592, 0.8592, 0.8592])

	names.append("LHipPitch")
	times.append([0.88, 2.24, 3.6, 5])
	keys.append([-0.243864, 0.0552659, -0.243864, 0.0552659])

	names.append("LHipRoll")
	times.append([0.88, 2.24, 3.6, 5])
	keys.append([0.066004, 0.142704, 0.066004, 0.142704])

	names.append("LHipYawPitch")
	times.append([0.88, 2.24, 3.6, 5])
	keys.append([-0.371186, -0.538392, -0.371186, -0.538392])

	names.append("LKneePitch")
	times.append([0.88, 2.24, 3.6, 5])
	keys.append([0.223922, -0.00310993, 0.223922, -0.00310993])

	names.append("LShoulderPitch")
	times.append([0.36, 0.88, 1.56, 2.24, 2.88, 3.6, 4.28, 5])
	keys.append([0.759288, -1.08611, 0.759288, 0.960242, 0.759288, -1.08611, 0.759288, 0.960242])

	names.append("LShoulderRoll")
	times.append([0.36, 0.88, 1.56, 2.24, 2.88, 3.6, 4.28, 5])
	keys.append([0.228525, 0.636569, 0.228525, -0.314159, 0.228525, 0.636569, 0.228525, -0.314159])

	names.append("LWristYaw")
	times.append([0.36, 0.88, 1.56, 2.24, 2.88, 3.6, 4.28, 5])
	keys.append([1.23176, 0.900415, 1.23176, 0.730143, 1.23176, 0.900415, 1.23176, 0.730143])

	names.append("RAnklePitch")
	times.append([0.88, 2.24, 3.6, 5])
	keys.append([0.11049, 0.108956, 0.11049, 0.108956])

	names.append("RAnkleRoll")
	times.append([0.88, 2.24, 3.6, 5])
	keys.append([0.277696, -0.0168321, 0.277696, -0.0168321])

	names.append("RElbowRoll")
	times.append([0.88, 2.24, 3.6, 5])
	keys.append([0.392746, 0.194861, 0.392746, 0.194861])

	names.append("RElbowYaw")
	times.append([0.88, 2.24, 3.6, 5])
	keys.append([1.18114, 1.16887, 1.18114, 1.16887])

	names.append("RHand")
	times.append([0.88, 2.24, 3.6, 5])
	keys.append([0.3068, 0.684, 0.3068, 0.684])

	names.append("RHipPitch")
	times.append([0.88, 2.24, 3.6, 5])
	keys.append([0.131882, -0.073674, 0.131882, -0.073674])

	names.append("RHipRoll")
	times.append([0.88, 2.24, 3.6, 5])
	keys.append([-0.292952, 0.00771189, -0.292952, 0.00771189])

	names.append("RHipYawPitch")
	times.append([0.88, 2.24, 3.6, 5])
	keys.append([-0.371186, -0.538392, -0.371186, -0.538392])

	names.append("RKneePitch")
	times.append([0.88, 2.24, 3.6, 5])
	keys.append([-0.0923279, 0.196393, -0.0923279, 0.196393])

	names.append("RShoulderPitch")
	times.append([0.88, 2.24, 3.6, 5])
	keys.append([1.51563, 1.49262, 1.51563, 1.49262])

	names.append("RShoulderRoll")
	times.append([0.88, 2.24, 3.6, 5])
	keys.append([-0.10282, -0.158044, -0.10282, -0.158044])

	names.append("RWristYaw")
	times.append([0.88, 2.24, 3.6, 5])
	keys.append([0.06592, -0.530805, 0.06592, -0.530805])

	try:
		motion = ALProxy("ALMotion", robotIP, port)
		motion.angleInterpolation(names, keys, times, True)
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

	main(robotIP, port)
