import sys
import time
import numpy as np
from naoqi import ALProxy

start = time.time()

def main(robotIP, port, unit_time, stand):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.68, 1.2, 1.96])
    keys.append([[-0.635118, [3, -0.226667, 0], [3, 0.173333, 0]], [0.268407, [3, -0.173333, 0], [3, 0.253333, 0]], [-0.144238, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([0.68, 1.2, 1.96])
    keys.append([[-0.52467, [3, -0.226667, 0], [3, 0.173333, 0]], [0.658043, [3, -0.173333, 0], [3, 0.253333, 0]], [-0.032256, [3, -0.253333, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0.72, 1.24, 1.96])
    keys.append([[-0.585945, [3, -0.24, 0], [3, 0.173333, 0]], [-0.223922, [3, -0.173333, 0], [3, 0.24, 0]], [-0.427944, [3, -0.24, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.72, 1.24, 1.96])
    keys.append([[-0.415757, [3, -0.24, 0], [3, 0.173333, 0]], [-2.0944, [3, -0.173333, 0], [3, 0.24, 0]], [-1.17509, [3, -0.24, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([1.16, 1.96])
    keys.append([[0.577479, [3, -0.386667, 0], [3, 0.266667, 0]], [0.3048, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0.72, 1.24, 1.96])
    keys.append([[-1.37297, [3, -0.24, 0], [3, 0.173333, 0]], [0.256136, [3, -0.173333, -0.39884], [3, 0.24, 0.55224]], [1.48027, [3, -0.24, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.72, 1.24, 1.96])
    keys.append([[0.187106, [3, -0.24, 0], [3, 0.173333, 0]], [0.831386, [3, -0.173333, 0], [3, 0.24, 0]], [0.0873961, [3, -0.24, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([1.16, 1.96])
    keys.append([[-0.673468, [3, -0.386667, 0], [3, 0.266667, 0]], [0.145688, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.72, 1.24, 1.96])
    keys.append([[0.265424, [3, -0.24, 0], [3, 0.173333, 0]], [1.17662, [3, -0.173333, 0], [3, 0.24, 0]], [0.389678, [3, -0.24, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.72, 1.24, 1.96])
    keys.append([[0.825249, [3, -0.24, 0], [3, 0.173333, 0]], [0.33437, [3, -0.173333, 0], [3, 0.24, 0]], [1.17654, [3, -0.24, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([1.16, 1.96])
    keys.append([[0.814206, [3, -0.386667, 0], [3, 0.266667, 0]], [0.3068, [3, -0.266667, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.72, 1.24, 1.96])
    keys.append([[-1.19801, [3, -0.24, 0], [3, 0.173333, 0]], [-0.507713, [3, -0.173333, -0.376539], [3, 0.24, 0.521362]], [1.49569, [3, -0.24, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.72, 1.24, 1.96])
    keys.append([[-0.544613, [3, -0.24, 0], [3, 0.173333, 0]], [-0.285367, [3, -0.173333, -0.0615415], [3, 0.24, 0.0852114]], [-0.104354, [3, -0.24, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([1.16, 1.96])
    keys.append([[0.984786, [3, -0.386667, 0], [3, 0.266667, 0]], [0.0720561, [3, -0.266667, 0], [3, 0, 0]]])

    if stand:
        names.append("LAnklePitch")
        times.append([0.76, 1.96])
        keys.append([[-0.155334, [3, -0.253333, 0], [3, 0.4, 0]], [0.093532, [3, -0.4, 0], [3, 0, 0]]])

        names.append("LAnkleRoll")
        times.append([0.76, 1.96])
        keys.append([[-0.00532477, [3, -0.253333, 0], [3, 0.4, 0]], [-0.116542, [3, -0.4, 0], [3, 0, 0]]])

        names.append("LHipPitch")
        times.append([0.76, 1.96])
        keys.append([[0.306829, [3, -0.253333, 0], [3, 0.4, 0]], [0.138102, [3, -0.4, 0], [3, 0, 0]]])

        names.append("LHipRoll")
        times.append([0.76, 1.96])
        keys.append([[0.0349279, [3, -0.253333, 0], [3, 0.4, 0]], [0.11816, [3, -0.4, 0], [3, 0, 0]]])

        names.append("LHipYawPitch")
        times.append([0.76, 1.96])
        keys.append([[-0.329768, [3, -0.253333, 0], [3, 0.4, 0]], [-0.171766, [3, -0.4, 0], [3, 0, 0]]])

        names.append("LKneePitch")
        times.append([0.76, 1.96])
        keys.append([[0.0315796, [3, -0.253333, 0], [3, 0.4, 0]], [-0.090548, [3, -0.4, 0], [3, 0, 0]]])

        names.append("RAnklePitch")
        times.append([0.76, 1.96])
        keys.append([[-0.179769, [3, -0.253333, 0], [3, 0.4, 0]], [0.107422, [3, -0.4, 0], [3, 0, 0]]])

        names.append("RAnkleRoll")
        times.append([0.76, 1.96])
        keys.append([[0.205949, [3, -0.253333, 0], [3, 0.4, 0]], [0.07214, [3, -0.4, 0], [3, 0, 0]]])

        names.append("RHipPitch")
        times.append([0.76, 1.96])
        keys.append([[0.317285, [3, -0.253333, 0], [3, 0.4, 0]], [0.131882, [3, -0.4, 0], [3, 0, 0]]])

        names.append("RHipRoll")
        times.append([0.76, 1.96])
        keys.append([[-0.178942, [3, -0.253333, 0], [3, 0.4, 0]], [-0.06592, [3, -0.4, 0], [3, 0, 0]]])

        names.append("RHipYawPitch")
        times.append([1.96])
        keys.append([[-0.171766, [3, -0.653333, 0], [3, 0, 0]]])

        names.append("RKneePitch")
        times.append([0.76, 1.96])
        keys.append([[0.0399984, [3, -0.253333, 0], [3, 0.4, 0]], [-0.091998, [3, -0.4, 0], [3, 0, 0]]])

    mul = unit_time/2.1
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