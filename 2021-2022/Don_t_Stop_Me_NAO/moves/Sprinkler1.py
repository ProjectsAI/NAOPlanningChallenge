# Choregraphe simplified export in Python.
from naoqi import ALProxy
import sys

def main(robotIP, port):
	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([0.48, 5])
	keys.append([-0.233874, -0.173384])

	names.append("HeadYaw")
	times.append([0.48, 5])
	keys.append([0.912807, 0.21932])

	names.append("LAnklePitch")
	times.append([0.32, 5])
	keys.append([-0.214803, -0.406552])

	names.append("LAnkleRoll")
	times.append([0.32, 5])
	keys.append([-0.14262, -0.11961])

	names.append("LElbowRoll")
	times.append([0.4, 1, 5])
	keys.append([-0.0349066, -0.0459781, -0.358915])

	names.append("LElbowYaw")
	times.append([0.4, 1, 5])
	keys.append([-1.48956, -1.48035, -1.26099])

	names.append("LHand")
	times.append([0.4, 1, 5])
	keys.append([0.9616, 0.9592, 0.9616])

	names.append("LHipPitch")
	times.append([0.32, 5])
	keys.append([-0.144154, -0.268407])

	names.append("LHipRoll")
	times.append([0.32, 5])
	keys.append([0.233211, 0.173384])

	names.append("LHipYawPitch")
	times.append([0.32, 5])
	keys.append([-0.288349, -0.28068])

	names.append("LKneePitch")
	times.append([0.32, 5])
	keys.append([0.539926, 0.820649])

	names.append("LShoulderPitch")
	times.append([0.4, 0.48, 1, 5])
	keys.append([-0.420357, -0.560251, -0.417134, -0.0966839])

	names.append("LShoulderRoll")
	times.append([0.4, 1, 1.44, 1.8, 2.2, 2.6, 2.96, 3.4, 3.8, 4.16, 4.6, 5])
	keys.append([0.819114, 0.461692, 0.610865, 0.223402, 0.460767, 0.0436332, 0.312414, -0.0610865, 0.207694, -0.195477, 0.0593412, -0.159578])

	names.append("LWristYaw")
	times.append([0.4, 1, 1.44, 1.8, 5])
	keys.append([0.312894, 0.131882, 0.0663225, 0.0663225, -0.29457])

	names.append("RAnklePitch")
	times.append([0.32, 5])
	keys.append([-0.0199001, -0.263807])

	names.append("RAnkleRoll")
	times.append([0.32, 5])
	keys.append([0.116626, 0.0828778])

	names.append("RElbowRoll")
	times.append([0.44, 0.96, 1.4, 1.8, 2.24, 2.6, 3, 3.48, 3.8, 4.2, 4.56, 5])
	keys.append([1.54462, 1.53864, 1.54462, 1.53864, 1.54462, 1.53864, 1.54462, 1.53864, 1.54462, 1.53864, 1.54462, 1.53558])

	names.append("RElbowYaw")
	times.append([0.44, 0.96, 1.4, 1.8, 2.24, 2.6, 3, 3.48, 3.8, 4.2, 4.56, 5])
	keys.append([0.966378, 1.38823, 0.966378, 1.38823, 0.966378, 1.38823, 0.966378, 1.38823, 0.966378, 1.38823, 0.966378, 1.36982])

	names.append("RHand")
	times.append([0.44, 0.96, 1.4, 1.8, 2.24, 2.6, 3, 3.48, 3.8, 4.2, 4.56, 5])
	keys.append([0.7708, 0.7696, 0.7708, 0.7696, 0.7708, 0.7696, 0.7708, 0.7696, 0.7708, 0.7696, 0.7708, 0.7692])

	names.append("RHipPitch")
	times.append([0.32, 5])
	keys.append([0.138018, -0.251617])

	names.append("RHipRoll")
	times.append([0.32, 5])
	keys.append([-0.0383082, -0.0291041])

	names.append("RHipYawPitch")
	times.append([0.32, 5])
	keys.append([-0.288349, -0.28068])

	names.append("RKneePitch")
	times.append([0.32, 5])
	keys.append([0.0798099, 0.676537])

	names.append("RShoulderPitch")
	times.append([0.44, 0.96, 1.4, 1.8, 2.24, 2.6, 3, 3.48, 3.8, 4.2, 4.56, 5])
	keys.append([-0.742414, -0.566003, -0.742414, -0.566003, -0.742414, -0.566003, -0.742414, -0.566003, -0.742414, -0.566003, -0.742414, -0.544529])

	names.append("RShoulderRoll")
	times.append([0.44, 0.96, 1.4, 1.8, 2.24, 2.6, 3, 3.48, 3.8, 4.2, 4.56, 5])
	keys.append([-0.43263, -0.0614019, -0.43263, -0.0614019, -0.43263, -0.0614019, -0.43263, -0.0614019, -0.43263, -0.0614019, -0.43263, -0.075208])

	names.append("RWristYaw")
	times.append([0.44, 0.96, 1.4, 1.8, 2.24, 2.6, 3, 3.48, 3.8, 4.2, 4.56, 5])
	keys.append([1.30539, 0.803775, 1.30539, 0.803775, 1.30539, 0.803775, 1.30539, 0.803775, 1.30539, 0.803775, 1.30539, 0.820649])

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
