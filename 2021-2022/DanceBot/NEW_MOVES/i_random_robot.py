# Choregraphe bezier export in Python.

import sys
import time

from naoqi import ALProxy


def main(robotIP, port):

    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.26667, 3.46667, 4.26667, 6.4, 7.46667])
    keys.append([[-0.012314, [3, -0.422222, 0], [3, 0.733333, 0]], [0.00609404, [3, -0.733333, 0], [3, 0.266667, 0]],
                 [0.00609404, [3, -0.266667, 0], [3, 0.711111, 0]],
                 [-0.00136232, [3, -0.711111, 0.00745636], [3, 0.355556, -0.00372818]],
                 [-0.166523, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([1.26667, 3.46667, 4.26667, 6.4, 7.46667])
    keys.append([[0.00762803, [3, -0.422222, 0], [3, 0.733333, 0]], [0.00762803, [3, -0.733333, 0], [3, 0.266667, 0]],
                 [0.00762803, [3, -0.266667, 0], [3, 0.711111, 0]], [0.0097998, [3, -0.711111, 0], [3, 0.355556, 0]],
                 [0, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([1.26667, 2, 3.46667, 4.26667, 6.4, 7.46667])
    keys.append([[0.191576, [3, -0.422222, 0], [3, 0.244444, 0]], [0.205383, [3, -0.244444, 0], [3, 0.488889, 0]],
                 [0.183907, [3, -0.488889, 0], [3, 0.266667, 0]], [0.183907, [3, -0.266667, 0], [3, 0.711111, 0]],
                 [0.191801, [3, -0.711111, 0], [3, 0.355556, 0]], [0.0920989, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([1.26667, 2, 3.46667, 4.26667, 6.4, 7.46667])
    keys.append([[0.0659823, [3, -0.422222, 0], [3, 0.244444, 0]],
                 [0.0613804, [3, -0.244444, 0.00460191], [3, 0.488889, -0.00920382]],
                 [-0.0107176, [3, -0.488889, 0], [3, 0.266667, 0]], [-0.0107176, [3, -0.266667, 0], [3, 0.711111, 0]],
                 [-0.0080834, [3, -0.711111, 0], [3, 0.355556, 0]], [-0.125916, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([1.26667, 2.73333, 3.46667, 4.26667, 5, 5.73333, 6.4, 7.46667])
    keys.append([[-1.4772, [3, -0.422222, 0], [3, 0.488889, 0]], [-1.55697, [3, -0.488889, 0], [3, 0.244444, 0]],
                 [-0.010696, [3, -0.244444, 0], [3, 0.266667, 0]], [-0.010696, [3, -0.266667, 0], [3, 0.244444, 0]],
                 [-1.55697, [3, -0.244444, 0], [3, 0.244444, 0]], [-0.0194955, [3, -0.244444, 0], [3, 0.222222, 0]],
                 [-1.11663, [3, -0.222222, 0], [3, 0.355556, 0]], [-0.41238, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([1.26667, 2.73333, 3.46667, 4.26667, 5, 6.4, 7.46667])
    keys.append(
        [[-1.71812, [3, -0.422222, 0], [3, 0.488889, 0]], [-1.29627, [3, -0.488889, -0.33373], [3, 0.244444, 0.166865]],
         [-0.216335, [3, -0.244444, 0], [3, 0.266667, 0]], [-0.216335, [3, -0.266667, 0], [3, 0.244444, 0]],
         [-1.29627, [3, -0.244444, 0], [3, 0.466667, 0]],
         [-1.29382, [3, -0.466667, -0.00245037], [3, 0.355556, 0.00186695]], [-1.19378, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([1.26667, 3.46667, 4.26667, 6.4, 7.46667])
    keys.append([[0.997114, [3, -0.422222, 0], [3, 0.733333, 0]], [0.995296, [3, -0.733333, 0], [3, 0.266667, 0]],
                 [0.995296, [3, -0.266667, 0], [3, 0.711111, 0]],
                 [0.518533, [3, -0.711111, 0.15432], [3, 0.355556, -0.07716]],
                 [0.300856, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([1.26667, 2, 3.46667, 4.26667, 6.4, 7.46667])
    keys.append([[0.179256, [3, -0.422222, 0], [3, 0.244444, 0]],
                 [0.162382, [3, -0.244444, 0.0168733], [3, 0.488889, -0.0337466]],
                 [-0.24106, [3, -0.488889, 0], [3, 0.266667, 0]], [-0.24106, [3, -0.266667, 0], [3, 0.711111, 0]],
                 [-0.23925, [3, -0.711111, -0.0018099], [3, 0.355556, 0.00090495]],
                 [0.122387, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([1.26667, 2, 3.46667, 4.26667, 6.4, 7.46667])
    keys.append([[0.0580999, [3, -0.422222, 0], [3, 0.244444, 0]], [0.07344, [3, -0.244444, 0], [3, 0.488889, 0]],
                 [-0.145922, [3, -0.488889, 0], [3, 0.266667, 0]], [-0.145922, [3, -0.266667, 0], [3, 0.711111, 0]],
                 [-0.141748, [3, -0.711111, -0.00417377], [3, 0.355556, 0.00208689]],
                 [0.0919027, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([1.26667, 2, 3.46667, 4.26667, 6.4, 7.46667])
    keys.append([[-0.730228, [3, -0.422222, 0], [3, 0.244444, 0]], [-0.739431, [3, -0.244444, 0], [3, 0.488889, 0]],
                 [-0.487856, [3, -0.488889, 0], [3, 0.266667, 0]], [-0.487856, [3, -0.266667, 0], [3, 0.711111, 0]],
                 [-0.487856, [3, -0.711111, 0], [3, 0.355556, 0]], [-0.170141, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([1.26667, 2, 3.46667, 4.26667, 6.4, 7.46667])
    keys.append([[0.185295, [3, -0.422222, 0], [3, 0.244444, 0]],
                 [0.169954, [3, -0.244444, 0.00153397], [3, 0.488889, -0.00306794]],
                 [0.166886, [3, -0.488889, 0], [3, 0.266667, 0]], [0.166886, [3, -0.266667, 0], [3, 0.711111, 0]],
                 [0.172421, [3, -0.711111, 0], [3, 0.355556, 0]], [-0.0889719, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([1.26667, 2.73333, 3.46667, 4.26667, 5, 6.4, 7.46667])
    keys.append([[1.53089, [3, -0.422222, 0], [3, 0.488889, 0]], [0.179436, [3, -0.488889, 0], [3, 0.244444, 0]],
                 [1.7073, [3, -0.244444, 0], [3, 0.266667, 0]], [1.7073, [3, -0.266667, 0], [3, 0.244444, 0]],
                 [0.179436, [3, -0.244444, 0.0916945], [3, 0.466667, -0.175053]],
                 [0.00438252, [3, -0.466667, 0], [3, 0.355556, 0]], [1.4681, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([1.26667, 2.73333, 3.46667, 4.26667, 5, 5.73333, 6.4, 7.46667])
    keys.append([[0.039842, [3, -0.422222, 0], [3, 0.488889, 0]], [0, [3, -0.488889, 0], [3, 0.244444, 0]],
                 [1.35601, [3, -0.244444, 0], [3, 0.266667, 0]],
                 [1.34374, [3, -0.266667, 0.0122714], [3, 0.244444, -0.0112488]],
                 [0, [3, -0.244444, 0], [3, 0.244444, 0]],
                 [0.00207139, [3, -0.244444, -0.00207139], [3, 0.222222, 0.00188308]],
                 [0.119643, [3, -0.222222, -0.0227104], [3, 0.355556, 0.0363367]],
                 [0.179213, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([1.26667, 3.46667, 4.26667, 6.4, 7.46667])
    keys.append([[-0.277696, [3, -0.422222, 0], [3, 0.733333, 0]], [-0.289967, [3, -0.733333, 0], [3, 0.266667, 0]],
                 [-0.289967, [3, -0.266667, 0], [3, 0.711111, 0]],
                 [-0.280886, [3, -0.711111, -0.00908095], [3, 0.355556, 0.00454047]],
                 [0.0920903, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([1.26667, 2, 3.46667, 4.26667, 6.4, 7.46667])
    keys.append([[-0.411138, [3, -0.422222, 0], [3, 0.244444, 0]],
                 [-0.401935, [3, -0.244444, -0.00920312], [3, 0.488889, 0.0184062]],
                 [0.352792, [3, -0.488889, 0], [3, 0.266667, 0]], [0.352792, [3, -0.266667, 0], [3, 0.711111, 0]],
                 [0.349192, [3, -0.711111, 0.00360059], [3, 0.355556, -0.0018003]],
                 [0.0910154, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([1.26667, 2, 3.46667, 4.26667, 6.4, 7.46667])
    keys.append([[0.0322537, [3, -0.422222, 0], [3, 0.244444, 0]],
                 [0.0337877, [3, -0.244444, -0.00153397], [3, 0.488889, 0.00306794]],
                 [0.248547, [3, -0.488889, 0], [3, 0.266667, 0]], [0.248547, [3, -0.266667, 0], [3, 0.711111, 0]],
                 [0.244517, [3, -0.711111, 0.00402996], [3, 0.355556, -0.00201498]],
                 [0.130051, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([1.26667, 2.73333, 3.46667, 4.26667, 5, 6.4, 7.46667])
    keys.append([[1.46348, [3, -0.422222, 0], [3, 0.488889, 0]], [1.56319, [3, -0.488889, 0], [3, 0.244444, 0]],
                 [1.54171, [3, -0.244444, 0], [3, 0.266667, 0]], [1.54171, [3, -0.266667, 0], [3, 0.244444, 0]],
                 [1.56319, [3, -0.244444, 0], [3, 0.466667, 0]], [0.0379192, [3, -0.466667, 0], [3, 0.355556, 0]],
                 [0.407595, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([1.26667, 2.73333, 3.46667, 4.26667, 5, 5.73333, 6.4, 7.46667])
    keys.append([[1.52015, [3, -0.422222, 0], [3, 0.488889, 0]], [1.44499, [3, -0.488889, 0], [3, 0.244444, 0]],
                 [1.65821, [3, -0.244444, 0], [3, 0.266667, 0]],
                 [1.65668, [3, -0.266667, 0.00153411], [3, 0.244444, -0.00140627]],
                 [1.44499, [3, -0.244444, 0.211693], [3, 0.244444, -0.211693]],
                 [-0.0253746, [3, -0.244444, 0.506704], [3, 0.222222, -0.46064]],
                 [-1.45704, [3, -0.222222, 0], [3, 0.355556, 0]], [1.19234, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([1.26667, 3.46667, 4.26667, 6.4, 7.46667])
    keys.append([[1, [3, -0.422222, 0], [3, 0.733333, 0]], [1, [3, -0.733333, 0], [3, 0.266667, 0]],
                 [1, [3, -0.266667, 0], [3, 0.711111, 0]],
                 [0.99275, [3, -0.711111, 0.00725001], [3, 0.355556, -0.00362501]],
                 [0.302714, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([1.26667, 2, 3.46667, 4.26667, 6.4, 7.46667])
    keys.append([[0.489289, [3, -0.422222, 0], [3, 0.244444, 0]], [0.490823, [3, -0.244444, 0], [3, 0.488889, 0]],
                 [-0.279246, [3, -0.488889, 0], [3, 0.266667, 0]], [-0.279246, [3, -0.266667, 0], [3, 0.711111, 0]],
                 [-0.275481, [3, -0.711111, -0.00376468], [3, 0.355556, 0.00188234]],
                 [0.12164, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([1.26667, 2, 3.46667, 4.26667, 6.4, 7.46667])
    keys.append([[-0.148778, [3, -0.422222, 0], [3, 0.244444, 0]],
                 [-0.15338, [3, -0.244444, 0.00460191], [3, 0.488889, -0.00920382]],
                 [-0.257691, [3, -0.488889, 0], [3, 0.266667, 0]], [-0.257691, [3, -0.266667, 0], [3, 0.711111, 0]],
                 [-0.257691, [3, -0.711111, 0], [3, 0.355556, 0]], [-0.103251, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([1.26667, 2, 3.46667, 4.26667, 6.4, 7.46667])
    keys.append([[0.47666, [3, -0.422222, 0], [3, 0.244444, 0]],
                 [0.455184, [3, -0.244444, 0.0214763], [3, 0.488889, -0.0429526]],
                 [0.0195278, [3, -0.488889, 0], [3, 0.266667, 0]], [0.0195278, [3, -0.266667, 0], [3, 0.711111, 0]],
                 [0.0214506, [3, -0.711111, 0], [3, 0.355556, 0]], [-0.0835382, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([1.26667, 2.73333, 3.46667, 4.26667, 5, 6.4, 7.46667])
    keys.append([[0.00464395, [3, -0.422222, 0], [3, 0.488889, 0]], [2.07247, [3, -0.488889, 0], [3, 0.244444, 0]],
                 [1.56779, [3, -0.244444, 0], [3, 0.266667, 0]], [1.56779, [3, -0.266667, 0], [3, 0.244444, 0]],
                 [2.07247, [3, -0.244444, 0], [3, 0.466667, 0]], [0.0341683, [3, -0.466667, 0], [3, 0.355556, 0]],
                 [1.46813, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([1.26667, 2.73333, 3.46667, 4.26667, 5, 5.73333, 6.4, 7.46667])
    keys.append([[-0.11816, [3, -0.422222, 0], [3, 0.488889, 0]],
                 [-0.154976, [3, -0.488889, 0.0143172], [3, 0.244444, -0.00715862]],
                 [-0.182588, [3, -0.244444, 0], [3, 0.266667, 0]], [-0.182588, [3, -0.266667, 0], [3, 0.244444, 0]],
                 [-0.154976, [3, -0.244444, -0.0265728], [3, 0.244444, 0.0265728]],
                 [-0.0231509, [3, -0.244444, 0], [3, 0.222222, 0]], [-1.32332, [3, -0.222222, 0], [3, 0.355556, 0]],
                 [-0.190512, [3, -0.355556, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([1.26667, 3.46667, 4.26667, 6.4, 7.46667])
    keys.append([[0.408002, [3, -0.422222, 0], [3, 0.733333, 0]], [0.41107, [3, -0.733333, 0], [3, 0.266667, 0]],
                 [0.41107, [3, -0.266667, 0], [3, 0.711111, 0]], [-0.0270139, [3, -0.711111, 0], [3, 0.355556, 0]],
                 [0.0941091, [3, -0.355556, 0], [3, 0, 0]]])

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
