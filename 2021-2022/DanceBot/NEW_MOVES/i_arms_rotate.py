import sys
import time

from naoqi import ALProxy


def main(robotIP, port):
    names = list()
    times = list()
    keys = list()

    names.append("LElbowRoll")
    times.append([0.16, 0.72, 1.28, 1.88, 2.44, 3.08, 3.64, 4.28])
    keys.append([[-0.162316, [3, -0.0533333, 0], [3, 0.186667, 0]], [-1.53985, [3, -0.186667, 0], [3, 0.186667, 0]],
                 [-0.162316, [3, -0.186667, 0], [3, 0.2, 0]], [-1.53985, [3, -0.2, 0], [3, 0.186667, 0]],
                 [-0.162316, [3, -0.186667, 0], [3, 0.213333, 0]], [-1.53985, [3, -0.213333, 0], [3, 0.186667, 0]],
                 [-0.162316, [3, -0.186667, 0], [3, 0.213333, 0]], [-0.415553, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.16, 0.72, 1.28, 1.88, 2.44, 3.08, 3.64, 4.28])
    keys.append([[-1.32645, [3, -0.0533333, 0], [3, 0.186667, 0]], [-1.32736, [3, -0.186667, 0], [3, 0.186667, 0]],
                 [-1.32645, [3, -0.186667, 0], [3, 0.2, 0]], [-1.32736, [3, -0.2, 0], [3, 0.186667, 0]],
                 [-1.32645, [3, -0.186667, 0], [3, 0.213333, 0]], [-1.32736, [3, -0.213333, 0], [3, 0.186667, 0]],
                 [-1.32645, [3, -0.186667, -0.000911067], [3, 0.213333, 0.00104122]],
                 [-1.19376, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0.72, 1.88, 3.08, 4.28])
    keys.append([[0.04, [3, -0.24, 0], [3, 0.386667, 0]], [0.04, [3, -0.386667, 0], [3, 0.4, 0]],
                 [0.04, [3, -0.4, 0], [3, 0.4, 0]], [0.3, [3, -0.4, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0.72, 1.88, 3.08, 4.28])
    keys.append([[0.00844208, [3, -0.24, 0], [3, 0.386667, 0]], [0.00844209, [3, -0.386667, 0], [3, 0.4, 0]],
                 [0.00844209, [3, -0.4, 0], [3, 0.4, 0]], [1.47002, [3, -0.4, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.72, 1.88, 3.08, 4.28])
    keys.append([[0.051226, [3, -0.24, 0], [3, 0.386667, 0]], [0.0512259, [3, -0.386667, 0], [3, 0.4, 0]],
                 [0.0512259, [3, -0.4, 0], [3, 0.4, 0]], [0.182978, [3, -0.4, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0.16, 0.72, 1.28, 1.88, 2.44, 3.08, 3.64, 4.28])
    keys.append([[-1.82387, [3, -0.0533333, 0], [3, 0.186667, 0]], [-1.82293, [3, -0.186667, 0], [3, 0.186667, 0]],
                 [-1.82387, [3, -0.186667, 0], [3, 0.2, 0]], [-1.82293, [3, -0.2, 0], [3, 0.186667, 0]],
                 [-1.82387, [3, -0.186667, 0], [3, 0.213333, 0]], [-1.82293, [3, -0.213333, 0], [3, 0.186667, 0]],
                 [-1.82387, [3, -0.186667, 0], [3, 0.213333, 0]], [0.090121, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.16, 0.72, 1.28, 1.88, 2.44, 3.08, 3.64, 4.28])
    keys.append([[0.162316, [3, -0.0533333, 0], [3, 0.186667, 0]], [0.0377185, [3, -0.186667, 0], [3, 0.186667, 0]],
                 [1.54462, [3, -0.186667, 0], [3, 0.2, 0]], [0.0377185, [3, -0.2, 0], [3, 0.186667, 0]],
                 [1.54462, [3, -0.186667, 0], [3, 0.213333, 0]], [0.0377185, [3, -0.213333, 0], [3, 0.186667, 0]],
                 [1.54462, [3, -0.186667, 0], [3, 0.213333, 0]], [0.414032, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.16, 0.72, 1.28, 1.88, 2.44, 3.08, 3.64, 4.28])
    keys.append([[1.32645, [3, -0.0533333, 0], [3, 0.186667, 0]], [1.31706, [3, -0.186667, 0], [3, 0.186667, 0]],
                 [1.32645, [3, -0.186667, 0], [3, 0.2, 0]], [1.31706, [3, -0.2, 0], [3, 0.186667, 0]],
                 [1.32645, [3, -0.186667, 0], [3, 0.213333, 0]], [1.31706, [3, -0.213333, 0], [3, 0.186667, 0]],
                 [1.32645, [3, -0.186667, 0], [3, 0.213333, 0]], [1.19674, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0.72, 1.88, 3.08, 4.28])
    keys.append(
        [[0, [3, -0.24, 0], [3, 0.386667, 0]], [0, [3, -0.386667, 0], [3, 0.4, 0]], [0, [3, -0.4, 0], [3, 0.4, 0]],
         [0.3, [3, -0.4, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.72, 1.88, 3.08, 4.28])
    keys.append([[0.00844208, [3, -0.24, 0], [3, 0.386667, 0]], [0.00844209, [3, -0.386667, 0], [3, 0.4, 0]],
                 [0.00844209, [3, -0.4, 0], [3, 0.4, 0]], [1.47161, [3, -0.4, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.72, 1.28, 1.88, 2.44, 3.08, 3.64, 4.28])
    keys.append([[-0.192931, [3, -0.24, 0], [3, 0.186667, 0]], [-0.197222, [3, -0.186667, 0], [3, 0.2, 0]],
                 [-0.192932, [3, -0.2, 0], [3, 0.186667, 0]], [-0.197222, [3, -0.186667, 0], [3, 0.213333, 0]],
                 [-0.192932, [3, -0.213333, 0], [3, 0.186667, 0]], [-0.197222, [3, -0.186667, 0], [3, 0.213333, 0]],
                 [-0.177582, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0.16, 0.72, 1.28, 1.88, 2.44, 3.08, 3.64, 4.28])
    keys.append([[1.82387, [3, -0.0533333, 0], [3, 0.186667, 0]], [1.82293, [3, -0.186667, 0], [3, 0.186667, 0]],
                 [1.82387, [3, -0.186667, 0], [3, 0.2, 0]], [1.82293, [3, -0.2, 0], [3, 0.186667, 0]],
                 [1.82387, [3, -0.186667, 0], [3, 0.213333, 0]], [1.82293, [3, -0.213333, 0], [3, 0.186667, 0]],
                 [1.82387, [3, -0.186667, 0], [3, 0.213333, 0]], [0.108852, [3, -0.213333, 0], [3, 0, 0]]])

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