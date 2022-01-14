import sys
import time
import numpy as np
from naoqi import ALProxy

start = time.time()

def StiffnessOn(proxy):
    # We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = unit_time/2
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

def main(robotIP, port, unit_time, stand):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.52, 0.88, 1.28, 1.96])
    keys.append([[0.447886, [3, -0.173333, 0], [3, 0.12, 0]], [0.340507, [3, -0.12, 0.0697567], [3, 0.133333, -0.0775074]], [0.00609404, [3, -0.133333, 0.059845], [3, 0.226667, -0.101737]], [-0.144238, [3, -0.226667, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([0.52, 0.88, 1.28, 1.96])
    keys.append([[0.366584, [3, -0.173333, 0], [3, 0.12, 0]], [0.642704, [3, -0.12, -0.0441802], [3, 0.133333, 0.0490891]], [0.691793, [3, -0.133333, 0], [3, 0.226667, 0]], [-0.032256, [3, -0.226667, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0.56, 0.92, 1.32, 1.96])
    keys.append([[-0.906552, [3, -0.186667, 0], [3, 0.12, 0]], [-1.23943, [3, -0.12, 0], [3, 0.133333, 0]], [-0.742414, [3, -0.133333, -0.104037], [3, 0.213333, 0.166459]], [-0.427944, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.56, 0.92, 1.32, 1.96])
    keys.append([[-0.259288, [3, -0.186667, 0], [3, 0.12, 0]], [0.207048, [3, -0.12, -0.111659], [3, 0.133333, 0.124066]], [0.447886, [3, -0.133333, 0], [3, 0.213333, 0]], [-1.17509, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([1.24, 1.96])
    keys.append([[0.577479, [3, -0.413333, 0], [3, 0.24, 0]], [0.3048, [3, -0.24, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0.56, 0.92, 1.32, 1.96])
    keys.append([[0.926494, [3, -0.186667, 0], [3, 0.12, 0]], [0.555266, [3, -0.12, 0.124254], [3, 0.133333, -0.13806]], [0.139552, [3, -0.133333, 0], [3, 0.213333, 0]], [1.48027, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.56, 0.92, 1.32, 1.96])
    keys.append([[0.977116, [3, -0.186667, 0], [3, 0.12, 0]], [0.668782, [3, -0.12, 0], [3, 0.133333, 0]], [1.43118, [3, -0.133333, 0], [3, 0.213333, 0]], [0.0873961, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([1.24, 1.96])
    keys.append([[-0.22554, [3, -0.413333, 0], [3, 0.24, 0]], [0.145688, [3, -0.24, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.56, 0.92, 1.32, 1.96])
    keys.append([[0.503194, [3, -0.186667, 0], [3, 0.12, 0]], [0.582963, [3, -0.12, -0.0666078], [3, 0.133333, 0.0740087]], [0.925044, [3, -0.133333, 0], [3, 0.213333, 0]], [0.389678, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.56, 0.92, 1.32, 1.96])
    keys.append([[-0.217869, [3, -0.186667, 0], [3, 0.12, 0]], [0.282215, [3, -0.12, 0], [3, 0.133333, 0]], [-0.214801, [3, -0.133333, 0], [3, 0.213333, 0]], [1.17654, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([1.24, 1.96])
    keys.append([[0.81166, [3, -0.413333, 0], [3, 0.24, 0]], [0.3068, [3, -0.24, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.56, 0.92, 1.32, 1.96])
    keys.append([[0.728692, [3, -0.186667, 0], [3, 0.12, 0]], [0.90817, [3, -0.12, 0], [3, 0.133333, 0]], [0.211735, [3, -0.133333, 0], [3, 0.213333, 0]], [1.49569, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.56, 0.92, 1.32, 1.96])
    keys.append([[-0.00924597, [3, -0.186667, 0], [3, 0.12, 0]], [-0.303775, [3, -0.12, 0], [3, 0.133333, 0]], [-0.047596, [3, -0.133333, 0], [3, 0.213333, 0]], [-0.104354, [3, -0.213333, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([1.24, 1.96])
    keys.append([[0.733209, [3, -0.413333, 0], [3, 0.24, 0]], [0.0720561, [3, -0.24, 0], [3, 0, 0]]])

    if stand:
        names.append("LAnklePitch")
        times.append([0.96, 1.36, 1.96])
        keys.append([[-0.308887, [3, -0.32, 0], [3, 0.133333, 0]], [0.0101913, [3, -0.133333, -0.0536558], [3, 0.2, 0.0804837]], [0.093532, [3, -0.2, 0], [3, 0, 0]]])

        names.append("LAnkleRoll")
        times.append([0.96, 1.36, 1.96])
        keys.append([[-0.0139626, [3, -0.32, 0], [3, 0.133333, 0]], [0.139362, [3, -0.133333, 0], [3, 0.2, 0]], [-0.116542, [3, -0.2, 0], [3, 0, 0]]])

        names.append("LHipPitch")
        times.append([0.96, 1.36, 1.96])
        keys.append([[0.162632, [3, -0.32, 0], [3, 0.133333, 0]], [0.289672, [3, -0.133333, 0], [3, 0.2, 0]], [0.138102, [3, -0.2, 0], [3, 0, 0]]])

        names.append("LHipRoll")
        times.append([0.96, 1.36, 1.96])
        keys.append([[-0.397659, [3, -0.32, 0], [3, 0.133333, 0]], [-0.195353, [3, -0.133333, -0.0687759], [3, 0.2, 0.103164]], [0.11816, [3, -0.2, 0], [3, 0, 0]]])

        names.append("LHipYawPitch")
        times.append([0.96, 1.36, 1.96])
        keys.append([[-0.674919, [3, -0.32, 0], [3, 0.133333, 0]], [-0.582879, [3, -0.133333, -0.067087], [3, 0.2, 0.100631]], [-0.171766, [3, -0.2, 0], [3, 0, 0]]])

        names.append("LKneePitch")
        times.append([0.96, 1.36, 1.96])
        keys.append([[0.849202, [3, -0.32, 0], [3, 0.133333, 0]], [0.181127, [3, -0.133333, 0.1253], [3, 0.2, -0.18795]], [-0.090548, [3, -0.2, 0], [3, 0, 0]]])

        names.append("RAnklePitch")
        times.append([0.96, 1.36, 1.96])
        keys.append([[-0.86879, [3, -0.32, 0], [3, 0.133333, 0]], [-0.176962, [3, -0.133333, -0.130162], [3, 0.2, 0.195242]], [0.107422, [3, -0.2, 0], [3, 0, 0]]])

        names.append("RAnkleRoll")
        times.append([0.96, 1.36, 1.96])
        keys.append([[0.106078, [3, -0.32, 0], [3, 0.133333, 0]], [0.328998, [3, -0.133333, 0], [3, 0.2, 0]], [0.07214, [3, -0.2, 0], [3, 0, 0]]])

        names.append("RHipPitch")
        times.append([0.96, 1.36, 1.96])
        keys.append([[-0.366879, [3, -0.32, 0], [3, 0.133333, 0]], [0.139622, [3, -0.133333, 0], [3, 0.2, 0]], [0.131882, [3, -0.2, 0], [3, 0, 0]]])

        names.append("RHipRoll")
        times.append([0.96, 1.36, 1.96])
        keys.append([[-0.734251, [3, -0.32, 0], [3, 0.133333, 0]], [-0.631654, [3, -0.133333, -0.0891108], [3, 0.2, 0.133666]], [-0.06592, [3, -0.2, 0], [3, 0, 0]]])

        names.append("RHipYawPitch")
        times.append([1.96])
        keys.append([[-0.171766, [3, -0.653333, 0], [3, 0, 0]]])

        names.append("RKneePitch")
        times.append([0.96, 1.36, 1.96])
        keys.append([[1.52951, [3, -0.32, 0], [3, 0.133333, 0]], [0.408943, [3, -0.133333, 0.216201], [3, 0.2, -0.324302]], [-0.091998, [3, -0.2, 0], [3, 0, 0]]])

    mul = unit_time/2.05
    times_unit = [list(np.array(t, dtype=float)*mul) for t in times]

    try:
        motion = ALProxy("ALMotion", robotIP, port)
        postureProxy = ALProxy("ALRobotPosture", robotIP, port)
        motion.angleInterpolationBezier(names, times_unit, keys)
    except BaseException, err:
        print err


if __name__ == "__main__":
    robotIP = "127.0.0.1" #"192.168.1.11"
    port = 9559 # Insert NAO port

    if len(sys.argv) <= 1:
        print "(robotIP default: 127.0.0.1)"
    elif len(sys.argv) <= 2:
        robotIP = sys.argv[1]
    else:
        port = int(sys.argv[2])
        robotIP = sys.argv[1]

    unit_time = float(sys.argv[3])
    stand = bool(int(sys.argv[4]))

    main(robotIP, port, unit_time, stand)

end = time.time()
print(end-start)


