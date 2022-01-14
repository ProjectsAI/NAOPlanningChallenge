# Choregraphe simplified export in Python.
import sys
import time

from naoqi import ALProxy


def main(robotIP, port):
	# Choregraphe simplified export in Python.
	names = list()
	times = list()
	keys = list()

	names.append("LElbowRoll")
	times.append([0.48, 0.92, 1.32, 1.76, 2.2, 2.64, 3.08, 3.52, 4.4])
	keys.append([-0.0380787, -1.51158, -0.044138, -1.51158, -0.044138, -1.51158, -0.044138, -1.51158, -1.21306])

	names.append("LElbowYaw")
	times.append([0.48, 0.92, 1.32, 1.76, 2.2, 2.64, 3.08, 3.52, 4.4])
	keys.append([0.0602687, 0.0663552, 0.0602687, 0.0663552, 0.0602687, 0.0663552, 0.0602687, 0.0663552, -0.447262])

	names.append("LHand")
	times.append([0.48, 0.92, 1.32, 1.76, 2.2, 2.64, 3.08, 3.52, 4.4])
	keys.append([1, 1, 1, 1, 1, 1, 1, 1, 0.294])

	names.append("LShoulderPitch")
	times.append([0.48, 0.92, 1.32, 1.76, 2.2, 2.64, 3.08, 3.52, 4.4])
	keys.append([-1.48104, -1.48104, -1.48104, -1.48104, -1.48104, -1.48104, -1.48104, -1.48104, 0.871741])

	names.append("LShoulderRoll")
	times.append([0.48, 0.92, 1.32, 1.76, 2.2, 2.64, 3.08, 3.52, 4.4])
	keys.append([0.753904, 0.74713, 0.74632, 0.74713, 0.74632, 0.74713, 0.74632, 0.74713, 0.246531])

	names.append("LWristYaw")
	times.append([0.48, 0.92, 1.32, 1.76, 2.2, 2.64, 3.08, 3.52, 4.4])
	keys.append([-1.8212, -1.8212, -1.8212, -1.8212, -1.8212, -1.8212, -1.8212, -1.8212, 0.0398731])

	names.append("RElbowRoll")
	times.append([0.48, 0.92, 1.32, 1.76, 2.2, 2.64, 3.08, 3.52, 4.4])
	keys.append([0.155987, 0.0358367, 1.50865, 0.0358367, 1.50865, 0.0358367, 1.50865, 0.0358367, 1.2531])

	names.append("RElbowYaw")
	times.append([0.48, 0.92, 1.32, 1.76, 2.2, 2.64, 3.08, 3.52, 4.4])
	keys.append(
		[-0.0694713, -0.0694713, -0.0694713, -0.0694713, -0.0694713, -0.0694713, -0.0694713, -0.0694713, 0.514931])

	names.append("RHand")
	times.append([0.48, 0.92, 1.32, 1.76, 2.2, 2.64, 3.08, 3.52, 4.4])
	keys.append([1, 1, 1, 1, 1, 1, 1, 1, 0.3016])

	names.append("RShoulderPitch")
	times.append([0.48, 0.92, 1.32, 1.76, 2.2, 2.64, 3.08, 3.52, 4.4])
	keys.append([-1.48103, -1.48103, -1.48103, -1.48103, -1.48103, -1.48103, -1.48103, -1.48103, 0.930718])

	names.append("RShoulderRoll")
	times.append([0.48, 0.92, 1.32, 1.76, 2.2, 2.64, 3.08, 3.52, 4.4])
	keys.append([-0.729118, -0.725818, -0.743114, -0.725818, -0.743114, -0.725818, -0.743114, -0.725818, -0.28714])

	names.append("RWristYaw")
	times.append([0.48, 0.92, 1.32, 1.76, 2.2, 2.64, 3.08, 3.52, 4.4])
	keys.append([1.8212, 1.8212, 1.8212, 1.8212, 1.8212, 1.8212, 1.8212, 1.8212, -0.0228942])

	try:
		# uncomment the following line and modify the IP if you use this script outside Choregraphe.
		# motion = ALProxy("ALMotion", IP, 9559)
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

	start = time.time()
	main(robotIP, port)
	end = time.time()
	print ("%.2f seconds elapsed" % (end-start))
