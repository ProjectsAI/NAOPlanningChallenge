import sys
import time
import numpy as np
from naoqi import ALProxy

start = time.time()

def main(robotIP, port, unit_time, sit):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.96, 1.48, 1.96])
    keys.append([[-0.50166, [3, -0.32, 0], [3, 0.173333, 0]], [-0.0782759, [3, -0.173333, 0], [3, 0.16, 0]], [-0.144238, [3, -0.16, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([0.96, 1.48, 1.96])
    keys.append([[-0.0706059, [3, -0.32, 0], [3, 0.173333, 0]], [-0.0859459, [3, -0.173333, 0], [3, 0.16, 0]], [-0.032256, [3, -0.16, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0.52, 1, 1.52, 1.96])
    keys.append([[0, [3, -0.173333, 0], [3, 0.16, 0]], [-0.612024, [3, -0.16, 0], [3, 0.173333, 0]], [0, [3, -0.173333, 0], [3, 0.146667, 0]], [-0.427944, [3, -0.146667, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.52, 1, 1.52, 1.96])
    keys.append([[-0.420357, [3, -0.173333, 0], [3, 0.16, 0]], [-0.374338, [3, -0.16, 0], [3, 0.173333, 0]], [-0.420357, [3, -0.173333, 0.0460191], [3, 0.146667, -0.0389392]], [-1.17509, [3, -0.146667, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0.92, 1.96])
    keys.append([[0.796751, [3, -0.306667, 0], [3, 0.346667, 0]], [0.3048, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0.52, 1, 1.52, 1.96])
    keys.append([[-1.05237, [3, -0.173333, 0], [3, 0.16, 0]], [-0.823801, [3, -0.16, 0], [3, 0.173333, 0]], [-1.05237, [3, -0.173333, 0], [3, 0.146667, 0]], [1.48027, [3, -0.146667, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.52, 1, 1.52, 1.96])
    keys.append([[0.432547, [3, -0.173333, 0], [3, 0.16, 0]], [0.0352401, [3, -0.16, 0], [3, 0.173333, 0]], [0.432547, [3, -0.173333, 0], [3, 0.146667, 0]], [0.0873961, [3, -0.146667, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0.92, 1.96])
    keys.append([[-1.30394, [3, -0.306667, 0], [3, 0.346667, 0]], [0.145688, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.52, 1, 1.52, 1.96])
    keys.append([[4.19617e-05, [3, -0.173333, 0], [3, 0.16, 0]], [0.656595, [3, -0.16, 0], [3, 0.173333, 0]], [4.19617e-05, [3, -0.173333, 0], [3, 0.146667, 0]], [0.389678, [3, -0.146667, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.52, 1, 1.52, 1.96])
    keys.append([[0.233125, [3, -0.173333, 0], [3, 0.16, 0]], [0.170232, [3, -0.16, 0], [3, 0.173333, 0]], [0.233125, [3, -0.173333, -0.0628933], [3, 0.146667, 0.0532174]], [1.17654, [3, -0.146667, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0.92, 1.96])
    keys.append([[0.849115, [3, -0.306667, 0], [3, 0.346667, 0]], [0.3068, [3, -0.346667, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.52, 1, 1.52, 1.96])
    keys.append([[-1.11978, [3, -0.173333, 0], [3, 0.16, 0]], [-0.926494, [3, -0.16, 0], [3, 0.173333, 0]], [-1.11978, [3, -0.173333, 0], [3, 0.146667, 0]], [1.49569, [3, -0.146667, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.52, 1, 1.52, 1.96])
    keys.append([[-0.454107, [3, -0.173333, 0], [3, 0.16, 0]], [-0.0245859, [3, -0.16, 0], [3, 0.173333, 0]], [-0.454107, [3, -0.173333, 0], [3, 0.146667, 0]], [-0.104354, [3, -0.146667, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0.92, 1.96])
    keys.append([[1.31153, [3, -0.306667, 0], [3, 0.346667, 0]], [0.0720561, [3, -0.346667, 0], [3, 0, 0]]])

    if stand:
        names.append("LAnklePitch")
        times.append([0.56, 1.96])
        keys.append([[-0.0910584, [3, -0.186667, 0], [3, 0.466667, 0]], [0.093532, [3, -0.466667, 0], [3, 0, 0]]])

        names.append("LAnkleRoll")
        times.append([0.56, 1.96])
        keys.append([[-0.0329368, [3, -0.186667, 0], [3, 0.466667, 0]], [-0.116542, [3, -0.466667, 0], [3, 0, 0]]])

        names.append("LHipPitch")
        times.append([0.56, 1.96])
        keys.append([[0.340577, [3, -0.186667, 0], [3, 0.466667, 0]], [0.138102, [3, -0.466667, 0], [3, 0, 0]]])

        names.append("LHipRoll")
        times.append([0.56, 1.96])
        keys.append([[0.090152, [3, -0.186667, 0], [3, 0.466667, 0]], [0.11816, [3, -0.466667, 0], [3, 0, 0]]])

        names.append("LHipYawPitch")
        times.append([0.56, 1.96])
        keys.append([[-0.360449, [3, -0.186667, 0], [3, 0.466667, 0]], [-0.171766, [3, -0.466667, 0], [3, 0, 0]]])

        names.append("LKneePitch")
        times.append([0.56, 1.96])
        keys.append([[0.0714636, [3, -0.186667, 0], [3, 0.466667, 0]], [-0.090548, [3, -0.466667, 0], [3, 0, 0]]])

        names.append("RAnklePitch")
        times.append([0.56, 1.96])
        keys.append([[-0.0787807, [3, -0.186667, 0], [3, 0.466667, 0]], [0.107422, [3, -0.466667, 0], [3, 0, 0]]])

        names.append("RAnkleRoll")
        times.append([0.56, 1.96])
        keys.append([[0.165806, [3, -0.186667, 0], [3, 0.466667, 0]], [0.07214, [3, -0.466667, 0], [3, 0, 0]]])

        names.append("RHipPitch")
        times.append([0.56, 1.96])
        keys.append([[0.355635, [3, -0.186667, 0], [3, 0.466667, 0]], [0.131882, [3, -0.466667, 0], [3, 0, 0]]])

        names.append("RHipRoll")
        times.append([0.56, 1.96])
        keys.append([[-0.119116, [3, -0.186667, 0], [3, 0.466667, 0]], [-0.06592, [3, -0.466667, 0], [3, 0, 0]]])

        names.append("RHipYawPitch")
        times.append([1.96])
        keys.append([[-0.171766, [3, -0.653333, 0], [3, 0, 0]]])

        names.append("RKneePitch")
        times.append([0.56, 1.96])
        keys.append([[0.0476684, [3, -0.186667, 0], [3, 0.466667, 0]], [-0.091998, [3, -0.466667, 0], [3, 0, 0]]])
    
    mul = unit_time/2
    times_unit = [list(np.array(t, dtype=float)*mul) for t in times]

    try:
        motion = ALProxy("ALMotion", robotIP, port)
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
