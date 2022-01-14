# Choregraphe bezier export in Python.

import sys
import time

from naoqi import ALProxy


def main(robotIP, port):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.04])
    keys.append([[-0.00043734, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([0.04])
    keys.append([[0.0033466, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([0.04])
    keys.append([[-0.00886088, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([0.04])
    keys.append([[-0.00768038, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0.04])
    keys.append([[-0.0374484, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.04])
    keys.append([[-0.00305847, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0.04])
    keys.append([[0.00580015, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([0.04])
    keys.append([[-0.00635093, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([0.04])
    keys.append([[0.00574582, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([0.04])
    keys.append([[-0.000115165, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([0.04])
    keys.append([[0.00102519, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0.04])
    keys.append([[-0.00648669, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.04])
    keys.append([[0.0182266, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0.04])
    keys.append([[-0.000388482, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([0.04])
    keys.append([[-0.00886088, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([0.04])
    keys.append([[0.00802482, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.04])
    keys.append([[0.0374523, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.04])
    keys.append([[0.00307293, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0.04])
    keys.append([[0.00580015, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([0.04])
    keys.append([[-0.00635093, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([0.04])
    keys.append([[-0.00574582, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([0.04])
    keys.append([[-0.000115165, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([0.04])
    keys.append([[0.00102519, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.04])
    keys.append([[-0.00340581, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.04])
    keys.append([[-0.0182518, [3, -0.0133333, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0.04])
    keys.append([[0.000388482, [3, -0.0133333, 0], [3, 0, 0]]])

    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        motion = ALProxy("ALMotion", robotIP, port)
        #  motion = ALProxy("ALMotion")
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
    duration = end - start
    print ("%.2f seconds elapsed" % duration)

