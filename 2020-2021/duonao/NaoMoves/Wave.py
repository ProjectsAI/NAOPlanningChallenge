# Choregraphe bezier export in Python.
import sys
import time

from naoqi import ALProxy


def main(robotIP, port):
    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("LElbowRoll")
    times.append([0.6, 1.2, 1.8, 2.4, 3, 3.6])
    keys.append([-0.0385809, -0.0385809, -0.0385809, -0.0385809, -0.0385809, -1.20686])

    names.append("LElbowYaw")
    times.append([0.6, 1.2, 1.8, 2.4, 3, 3.6])
    keys.append([-0.0580294, -0.0580294, -0.0580294, -0.0580294, -0.0580294, -0.449089])

    names.append("LHand")
    times.append([0.6, 1.2, 1.8, 2.4, 3, 3.6])
    keys.append([0.999057, 0.999057, 0.999057, 0.999057, 0.999057, 0.292776])

    names.append("LShoulderPitch")
    times.append([0.6, 1.2, 1.8, 2.4, 3, 3.6])
    keys.append([-1.13408, -1.09507, -1.1302, -1.09592, -1.12881, 0.869991])

    names.append("LShoulderRoll")
    times.append([0.6, 1.2, 1.8, 2.4, 3, 3.6])
    keys.append([0.0281089, -0.203226, 0.571384, -0.208213, 0.570628, 0.253432])

    names.append("LWristYaw")
    times.append([0.6, 1.2, 1.8, 2.4, 3, 3.6])
    keys.append([-0.497478, -0.497478, -0.497478, -0.497478, -0.497478, 0.0340756])

    names.append("RElbowRoll")
    times.append([0.6, 1.2, 1.8, 2.4, 3, 3.6])
    keys.append([0.0385964, 0.0385964, 0.0385964, 0.0385964, 0.0385964, 1.25389])

    names.append("RElbowYaw")
    times.append([0.6, 1.2, 1.8, 2.4, 3, 3.6])
    keys.append([0.0594192, 0.0594192, 0.0594192, 0.0594192, 0.0594192, 0.5143])

    names.append("RHand")
    times.append([0.6, 1.2, 1.8, 2.4, 3, 3.6])
    keys.append([0.999057, 0.999057, 0.999057, 0.999057, 0.999057, 0.296343])

    names.append("RShoulderPitch")
    times.append([0.6, 1.2, 1.8, 2.4, 3, 3.6])
    keys.append([-1.13415, -1.13415, -1.09282, -1.14402, -1.09261, 0.930716])

    names.append("RShoulderRoll")
    times.append([0.6, 1.2, 1.8, 2.4, 3, 3.6])
    keys.append([-0.0270566, -0.578711, 0.213113, -0.576468, 0.216522, -0.297706])

    names.append("RWristYaw")
    times.append([0.6, 1.2, 1.8, 2.4, 3, 3.6])
    keys.append([0.499836, 0.499836, 0.499836, 0.499836, 0.499836, -0.0207239])

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
