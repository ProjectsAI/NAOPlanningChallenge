import sys
import time
import numpy as np
from naoqi import ALProxy

start = time.time()

def main(robotIP, port, unit_time):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.48, 1, 1.44, 1.92, 2.4, 2.88, 3.36, 3.92])
    keys.append([[-0.635118, [3, -0.16, 0], [3, 0.173333, 0]], [0.268407, [3, -0.173333, -0.152286], [3, 0.146667, 0.128858]], [0.397265, [3, -0.146667, 0], [3, 0.16, 0]], [-0.547679, [3, -0.16, 0], [3, 0.16, 0]], [0.397265, [3, -0.16, -0.125788], [3, 0.16, 0.125788]], [0.523053, [3, -0.16, 0], [3, 0.16, 0]], [-0.389678, [3, -0.16, 0], [3, 0.186667, 0]], [-0.144238, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([0.48, 1, 1.44, 1.92, 2.4, 2.88, 3.36, 3.92])
    keys.append([[-0.52467, [3, -0.16, 0], [3, 0.173333, 0]], [0.658043, [3, -0.173333, -0.0997112], [3, 0.146667, 0.084371]], [0.742414, [3, -0.146667, 0], [3, 0.16, 0]], [0.115008, [3, -0.16, 0.247471], [3, 0.16, -0.247471]], [-0.742414, [3, -0.16, 0], [3, 0.16, 0]], [0.4034, [3, -0.16, 0], [3, 0.16, 0]], [-0.845275, [3, -0.16, 0], [3, 0.186667, 0]], [-0.032256, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([0.56, 1.52, 2.48, 3.44, 3.92])
    keys.append([[-0.155334, [3, -0.186667, 0], [3, 0.32, 0]], [-0.1309, [3, -0.32, 0], [3, 0.32, 0]], [-0.549725, [3, -0.32, 0.0454326], [3, 0.32, -0.0454326]], [-0.595157, [3, -0.32, 0], [3, 0.16, 0]], [0.093532, [3, -0.16, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([0.56, 1.52, 2.48, 3.44, 3.92])
    keys.append([[-0.00532477, [3, -0.186667, 0], [3, 0.32, 0]], [0.140405, [3, -0.32, 0], [3, 0.32, 0]], [-0.0927629, [3, -0.32, 0.0611044], [3, 0.32, -0.0611044]], [-0.226221, [3, -0.32, 0], [3, 0.16, 0]], [-0.116542, [3, -0.16, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0.52, 1.04, 1.48, 1.96, 2.44, 2.92, 3.4, 3.92])
    keys.append([[-0.585945, [3, -0.173333, 0], [3, 0.173333, 0]], [-0.223922, [3, -0.173333, 0], [3, 0.146667, 0]], [-0.271475, [3, -0.146667, 0.0475533], [3, 0.16, -0.0518763]], [-0.736278, [3, -0.16, 0.126555], [3, 0.16, -0.126555]], [-1.03081, [3, -0.16, 0], [3, 0.16, 0]], [-0.929562, [3, -0.16, 0], [3, 0.16, 0]], [-1.03541, [3, -0.16, 0], [3, 0.173333, 0]], [-0.427944, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.52, 1.04, 1.48, 1.96, 2.44, 2.92, 3.4, 3.92])
    keys.append([[-0.415757, [3, -0.173333, 0], [3, 0.173333, 0]], [-2.0944, [3, -0.173333, 0], [3, 0.146667, 0]], [-2.0944, [3, -0.146667, 0], [3, 0.16, 0]], [-1.76414, [3, -0.16, -0.287955], [3, 0.16, 0.287955]], [-0.366667, [3, -0.16, 0], [3, 0.16, 0]], [-1.92674, [3, -0.16, 0], [3, 0.16, 0]], [-0.337522, [3, -0.16, 0], [3, 0.173333, 0]], [-1.17509, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0.96, 3.92])
    keys.append([[0.577479, [3, -0.32, 0], [3, 0.986667, 0]], [0.3048, [3, -0.986667, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([0.56, 1.52, 2.48, 3.44, 3.92])
    keys.append([[0.306829, [3, -0.186667, 0], [3, 0.32, 0]], [0.424946, [3, -0.32, -0.0317025], [3, 0.32, 0.0317025]], [0.497044, [3, -0.32, 0], [3, 0.32, 0]], [0.223992, [3, -0.32, 0.0797648], [3, 0.16, -0.0398824]], [0.138102, [3, -0.16, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([0.56, 1.52, 2.48, 3.44, 3.92])
    keys.append([[0.0349279, [3, -0.186667, 0], [3, 0.32, 0]], [-0.179832, [3, -0.32, 0], [3, 0.32, 0]], [0.212873, [3, -0.32, -0.119396], [3, 0.32, 0.119396]], [0.536546, [3, -0.32, 0], [3, 0.16, 0]], [0.11816, [3, -0.16, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([0.56, 1.52, 2.48, 3.44, 3.92])
    keys.append([[-0.329768, [3, -0.186667, 0], [3, 0.32, 0]], [-0.489305, [3, -0.32, 0], [3, 0.32, 0]], [-0.277612, [3, -0.32, 0], [3, 0.32, 0]], [-0.354312, [3, -0.32, 0], [3, 0.16, 0]], [-0.171766, [3, -0.16, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([0.56, 1.52, 2.48, 3.44, 3.92])
    keys.append([[0.0315796, [3, -0.186667, 0], [3, 0.32, 0]], [0.183446, [3, -0.32, -0.0769557], [3, 0.32, 0.0769557]], [0.493314, [3, -0.32, -0.0971532], [3, 0.32, 0.0971532]], [0.766365, [3, -0.32, 0], [3, 0.16, 0]], [-0.090548, [3, -0.16, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0.52, 1.04, 1.48, 1.96, 2.44, 2.92, 3.4, 3.92])
    keys.append([[-1.37297, [3, -0.173333, 0], [3, 0.173333, 0]], [0.256136, [3, -0.173333, -0.357848], [3, 0.146667, 0.302795]], [0.608956, [3, -0.146667, 0], [3, 0.16, 0]], [-0.10282, [3, -0.16, 0.168484], [3, 0.16, -0.168484]], [-0.401949, [3, -0.16, 0], [3, 0.16, 0]], [0.312894, [3, -0.16, -0.290437], [3, 0.16, 0.290437]], [1.34067, [3, -0.16, -0.128855], [3, 0.173333, 0.139593]], [1.48027, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.52, 1.04, 1.48, 1.96, 2.44, 2.92, 3.4, 3.92])
    keys.append([[0.187106, [3, -0.173333, 0], [3, 0.173333, 0]], [0.831386, [3, -0.173333, 0], [3, 0.146667, 0]], [0.751617, [3, -0.146667, 0.034237], [3, 0.16, -0.0373494]], [0.616627, [3, -0.16, 0.119652], [3, 0.16, -0.119652]], [0.033706, [3, -0.16, 0], [3, 0.16, 0]], [0.613558, [3, -0.16, 0], [3, 0.16, 0]], [0.536858, [3, -0.16, 0.0767002], [3, 0.173333, -0.0830919]], [0.0873961, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0.96, 3.92])
    keys.append([[-0.673468, [3, -0.32, 0], [3, 0.986667, 0]], [0.145688, [3, -0.986667, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([0.56, 1.52, 2.48, 3.44, 3.92])
    keys.append([[-0.179769, [3, -0.186667, 0], [3, 0.32, 0]], [-0.1309, [3, -0.32, 0], [3, 0.32, 0]], [-0.509835, [3, -0.32, 0], [3, 0.32, 0]], [0.144862, [3, -0.32, 0], [3, 0.16, 0]], [0.107422, [3, -0.16, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([0.56, 1.52, 2.48, 3.44, 3.92])
    keys.append([[0.205949, [3, -0.186667, 0], [3, 0.32, 0]], [0.39968, [3, -0.32, 0], [3, 0.32, 0]], [0.0416498, [3, -0.32, 0], [3, 0.32, 0]], [0.179769, [3, -0.32, 0], [3, 0.16, 0]], [0.07214, [3, -0.16, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.52, 1.04, 1.48, 1.96, 2.44, 2.92, 3.4, 3.92])
    keys.append([[0.265424, [3, -0.173333, 0], [3, 0.173333, 0]], [1.17662, [3, -0.173333, -0.183102], [3, 0.146667, 0.154933]], [1.33155, [3, -0.146667, -0.0420625], [3, 0.16, 0.0458864]], [1.44047, [3, -0.16, 0], [3, 0.16, 0]], [0.443368, [3, -0.16, 0], [3, 0.16, 0]], [1.35303, [3, -0.16, 0], [3, 0.16, 0]], [0.823801, [3, -0.16, 0.154136], [3, 0.173333, -0.166981]], [0.389678, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.52, 1.04, 1.48, 1.96, 2.44, 2.92, 3.4, 3.92])
    keys.append([[0.825249, [3, -0.173333, 0], [3, 0.173333, 0]], [0.33437, [3, -0.173333, 0.158982], [3, 0.146667, -0.134523]], [-0.055266, [3, -0.146667, 0.220585], [3, 0.16, -0.240638]], [-1.0493, [3, -0.16, 0], [3, 0.16, 0]], [1.31153, [3, -0.16, 0], [3, 0.16, 0]], [0.793036, [3, -0.16, 0.238537], [3, 0.16, -0.238537]], [-0.119694, [3, -0.16, 0], [3, 0.173333, 0]], [1.17654, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0.96, 3.92])
    keys.append([[0.814206, [3, -0.32, 0], [3, 0.986667, 0]], [0.3068, [3, -0.986667, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([0.56, 1.52, 2.48, 3.44, 3.92])
    keys.append([[0.317285, [3, -0.186667, 0], [3, 0.32, 0]], [0.435402, [3, -0.32, -0.0301686], [3, 0.32, 0.0301686]], [0.498297, [3, -0.32, 0], [3, 0.32, 0]], [0.337227, [3, -0.32, 0.0814255], [3, 0.16, -0.0407128]], [0.131882, [3, -0.16, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([0.56, 1.52, 2.48, 3.44, 3.92])
    keys.append([[-0.178942, [3, -0.186667, 0], [3, 0.32, 0]], [-0.531762, [3, -0.32, 0], [3, 0.32, 0]], [-0.119116, [3, -0.32, -0.0902502], [3, 0.32, 0.0902502]], [0.00973951, [3, -0.32, 0], [3, 0.16, 0]], [-0.06592, [3, -0.16, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([3.92])
    keys.append([[-0.171766, [3, -1.30667, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([0.56, 1.52, 2.48, 3.44, 3.92])
    keys.append([[0.0399984, [3, -0.186667, 0], [3, 0.32, 0]], [0.173456, [3, -0.32, -0.0726094], [3, 0.32, 0.0726094]], [0.475655, [3, -0.32, 0], [3, 0.32, 0]], [0.0630085, [3, -0.32, 0.126145], [3, 0.16, -0.0630725]], [-0.091998, [3, -0.16, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.52, 1.04, 1.48, 1.96, 2.44, 2.92, 3.4, 3.92])
    keys.append([[-1.19801, [3, -0.173333, 0], [3, 0.173333, 0]], [-0.507713, [3, -0.173333, -0.00181308], [3, 0.146667, 0.00153415]], [-0.506179, [3, -0.146667, -0.00153415], [3, 0.16, 0.00167362]], [-0.361981, [3, -0.16, -0.140361], [3, 0.16, 0.140361]], [0.335988, [3, -0.16, -0.0291453], [3, 0.16, 0.0291453]], [0.365133, [3, -0.16, 0], [3, 0.16, 0]], [-1.44959, [3, -0.16, 0], [3, 0.173333, 0]], [1.49569, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.52, 1.04, 1.48, 1.96, 2.44, 2.92, 3.4, 3.92])
    keys.append([[-0.544613, [3, -0.173333, 0], [3, 0.173333, 0]], [-0.285367, [3, -0.173333, -0.0656426], [3, 0.146667, 0.0555437]], [-0.181053, [3, -0.146667, 0], [3, 0.16, 0]], [-0.972599, [3, -0.16, 0.177944], [3, 0.16, -0.177944]], [-1.24872, [3, -0.16, 0], [3, 0.16, 0]], [-0.846809, [3, -0.16, -0.128345], [3, 0.16, 0.128345]], [-0.47865, [3, -0.16, -0.118793], [3, 0.173333, 0.128692]], [-0.104354, [3, -0.173333, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0.96, 3.92])
    keys.append([[0.984786, [3, -0.32, 0], [3, 0.986667, 0]], [0.0720561, [3, -0.986667, 0], [3, 0, 0]]])

    mul = unit_time/4
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

    main(robotIP, port, unit_time)

end = time.time()
print(end-start)
