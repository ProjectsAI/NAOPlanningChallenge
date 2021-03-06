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
    times.append([1.2, 2.2, 3.1, 4, 5.2, 6.1, 6.9, 7.8])
    keys.append([[9.19019e-08, [3, -0.4, 0], [3, 0.333333, 0]], [-0.331613, [3, -0.333333, 0], [3, 0.3, 0]], [0.139626, [3, -0.3, 0], [3, 0.3, 0]], [-0.0872665, [3, -0.3, 0], [3, 0.4, 0]], [0.139626, [3, -0.4, -0.0897598], [3, 0.3, 0.0673198]], [0.383972, [3, -0.3, -0.0739198], [3, 0.266667, 0.0657065]], [0.558505, [3, -0.266667, 0], [3, 0.3, 0]], [0.00115463, [3, -0.3, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([1.2, 2.2, 3.1, 4, 5.2, 6.1, 6.9, 7.8])
    keys.append([[-1.18682, [3, -0.4, 0], [3, 0.333333, 0]], [-0.279253, [3, -0.333333, -0.244959], [3, 0.3, 0.220463]], [0.20944, [3, -0.3, -0.308341], [3, 0.3, 0.308341]], [1.5708, [3, -0.3, 0], [3, 0.4, 0]], [0.20944, [3, -0.4, 0.0930842], [3, 0.3, -0.0698132]], [0.139626, [3, -0.3, 0.0369599], [3, 0.266667, -0.0328533]], [0, [3, -0.266667, 0], [3, 0.3, 0]], [0.000982441, [3, -0.3, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([1.2, 2.2, 3.1, 4, 5.2, 6.1, 6.9, 7.8])
    keys.append([[-1.48353, [3, -0.4, 0], [3, 0.333333, 0]], [-1.01229, [3, -0.333333, 0], [3, 0.3, 0]], [-1.01229, [3, -0.3, 0], [3, 0.3, 0]], [0, [3, -0.3, 0], [3, 0.4, 0]], [-1.01229, [3, -0.4, 0], [3, 0.3, 0]], [-1.01229, [3, -0.3, 0], [3, 0.266667, 0]], [-0.890118, [3, -0.266667, -0.122173], [3, 0.3, 0.137445]], [-0.00156194, [3, -0.3, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([1.2, 2.2, 3.1, 4, 5.2, 6.1, 6.9, 7.8])
    keys.append([[0, [3, -0.4, 0], [3, 0.333333, 0]], [0, [3, -0.333333, 0], [3, 0.3, 0]], [0, [3, -0.3, 0], [3, 0.3, 0]], [0, [3, -0.3, 0], [3, 0.4, 0]], [0, [3, -0.4, 0], [3, 0.3, 0]], [0, [3, -0.3, 0], [3, 0.266667, 0]], [0.20944, [3, -0.266667, 0], [3, 0.3, 0]], [-1.56774, [3, -0.3, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([1.2, 2.2, 3.1, 4, 5.2, 6.1, 6.9, 7.8])
    keys.append([[0.191986, [3, -0.4, 0], [3, 0.333333, 0]], [-0.802851, [3, -0.333333, 0], [3, 0.3, 0]], [-0.174533, [3, -0.3, 0], [3, 0.3, 0]], [-0.296706, [3, -0.3, 0], [3, 0.4, 0]], [-0.174533, [3, -0.4, -0.122173], [3, 0.3, 0.0916298]], [0.523599, [3, -0.3, 0], [3, 0.266667, 0]], [0.471239, [3, -0.266667, 0], [3, 0.3, 0]], [1.57049, [3, -0.3, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([1.2, 2.2, 3.1, 4, 5.2, 6.1, 6.9, 7.8])
    keys.append([[0.0872665, [3, -0.4, 0], [3, 0.333333, 0]], [0.174533, [3, -0.333333, -0.0551157], [3, 0.3, 0.0496041]], [0.401426, [3, -0.3, -0.162897], [3, 0.3, 0.162897]], [1.15192, [3, -0.3, 0], [3, 0.4, 0]], [0.401426, [3, -0.4, 0], [3, 0.3, 0]], [0.401426, [3, -0.3, 0], [3, 0.266667, 0]], [0.174533, [3, -0.266667, 0], [3, 0.3, 0]], [0.175001, [3, -0.3, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([1.2, 2.2, 3.1, 4, 5.2, 6.1, 6.9, 7.8])
    keys.append([[0.0698132, [3, -0.4, 0], [3, 0.333333, 0]], [1.11701, [3, -0.333333, 0], [3, 0.3, 0]], [0.855211, [3, -0.3, 0], [3, 0.3, 0]], [1.25664, [3, -0.3, 0], [3, 0.4, 0]], [0.855211, [3, -0.4, 0], [3, 0.3, 0]], [0.855211, [3, -0.3, 0], [3, 0.266667, 0]], [0.890118, [3, -0.266667, 0], [3, 0.3, 0]], [0.00207301, [3, -0.3, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([1.2, 2.2, 3.1, 4, 5.2, 6.1, 6.9, 7.8])
    keys.append([[1.5708, [3, -0.4, 0], [3, 0.333333, 0]], [0.418879, [3, -0.333333, 0], [3, 0.3, 0]], [0.418879, [3, -0.3, 0], [3, 0.3, 0]], [0.0872665, [3, -0.3, 0], [3, 0.4, 0]], [0.418879, [3, -0.4, 0], [3, 0.3, 0]], [-0.191986, [3, -0.3, 0.019635], [3, 0.266667, -0.0174533]], [-0.20944, [3, -0.266667, 0], [3, 0.3, 0]], [1.56772, [3, -0.3, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([1.2, 2.2, 3.1, 4, 5.2, 6.1, 6.9, 7.8])
    keys.append([[1.0472, [3, -0.4, 0], [3, 0.333333, 0]], [-0.471239, [3, -0.333333, 0], [3, 0.3, 0]], [0.0698132, [3, -0.3, 0], [3, 0.3, 0]], [-0.0698132, [3, -0.3, 0], [3, 0.4, 0]], [0.0698132, [3, -0.4, -0.076462], [3, 0.3, 0.0573465]], [0.331613, [3, -0.3, -0.0708398], [3, 0.266667, 0.0629687]], [0.471239, [3, -0.266667, -0.139626], [3, 0.3, 0.15708]], [1.57046, [3, -0.3, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([1.2, 2.2, 3.1, 4, 5.2, 6.1, 6.9, 7.8])
    keys.append([[-1.51844, [3, -0.4, 0], [3, 0.333333, 0]], [-0.401426, [3, -0.333333, -0.266392], [3, 0.3, 0.239753]], [0, [3, -0.3, 0], [3, 0.3, 0]], [0, [3, -0.3, 0], [3, 0.4, 0]], [0, [3, -0.4, 0], [3, 0.3, 0]], [0, [3, -0.3, 0], [3, 0.266667, 0]], [-0.174533, [3, -0.266667, 0], [3, 0.3, 0]], [-0.174152, [3, -0.3, 0], [3, 0, 0]]])

    ###

    names.append("LAnklePitch")
    times.append([1.2, 2.2, 3.1, 4, 5.2, 6.1, 6.9, 7.8])
    keys.append([[-1.0472, [3, -0.4, 0], [3, 0.333333, 0]], [-1.0472, [3, -0.333333, 0], [3, 0.3, 0]], [-1.0472, [3, -0.3, 0], [3, 0.3, 0]], [-1.0472, [3, -0.3, 0], [3, 0.4, 0]], [-1.0472, [3, -0.4, 0], [3, 0.3, 0]], [-1.0472, [3, -0.3, 0], [3, 0.266667, 0]], [-0.872665, [3, -0.266667, -0.163818], [3, 0.3, 0.184295]], [-0.00285703, [3, -0.3, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([1.2, 2.2, 3.1, 4, 5.2, 6.1, 6.9, 7.8])
    keys.append([[0.174533, [3, -0.4, 0], [3, 0.333333, 0]], [0.174533, [3, -0.333333, 0], [3, 0.3, 0]], [0.0872665, [3, -0.3, 0], [3, 0.3, 0]], [0.0872665, [3, -0.3, 0], [3, 0.4, 0]], [0.0872665, [3, -0.4, 0], [3, 0.3, 0]], [0.174533, [3, -0.3, 0], [3, 0.266667, 0]], [0, [3, -0.266667, 0], [3, 0.3, 0]], [0.0494904, [3, -0.3, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([1.2, 2.2, 3.1, 4, 5.2, 6.1, 6.9, 7.8])
    keys.append([[-1.0472, [3, -0.4, 0], [3, 0.333333, 0]], [-1.0472, [3, -0.333333, 0], [3, 0.3, 0]], [-1.0472, [3, -0.3, 0], [3, 0.3, 0]], [-1.0472, [3, -0.3, 0], [3, 0.4, 0]], [-1.0472, [3, -0.4, 0], [3, 0.3, 0]], [-1.0472, [3, -0.3, 0], [3, 0.266667, 0]], [-0.872665, [3, -0.266667, -0.163817], [3, 0.3, 0.184294]], [-0.0028622, [3, -0.3, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([1.2, 2.2, 3.1, 4, 5.2, 6.1, 6.9, 7.8])
    keys.append([[0.420624, [3, -0.4, 0], [3, 0.333333, 0]], [0.528835, [3, -0.333333, -0.0333756], [3, 0.3, 0.030038]], [0.610865, [3, -0.3, 0], [3, 0.3, 0]], [0.610865, [3, -0.3, 0], [3, 0.4, 0]], [0.610865, [3, -0.4, 0], [3, 0.3, 0]], [0.349066, [3, -0.3, 0.1078], [3, 0.266667, -0.095822]], [0, [3, -0.266667, 0.0439303], [3, 0.3, -0.0494216]], [-0.0494216, [3, -0.3, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([1.2, 2.2, 3.1, 4, 5.2, 6.1, 6.9, 7.8])
    keys.append([[0, [3, -0.4, 0], [3, 0.333333, 0]], [0, [3, -0.333333, 0], [3, 0.3, 0]], [0, [3, -0.3, 0], [3, 0.3, 0]], [0, [3, -0.3, 0], [3, 0.4, 0]], [0, [3, -0.4, 0], [3, 0.3, 0]], [0, [3, -0.3, 0], [3, 0.266667, 0]], [0, [3, -0.266667, 0], [3, 0.3, 0]], [-0.001571, [3, -0.3, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([1.2, 2.2, 3.1, 4, 5.2, 6.1, 6.9, 7.8])
    keys.append([[2.0944, [3, -0.4, 0], [3, 0.333333, 0]], [2.0944, [3, -0.333333, 0], [3, 0.3, 0]], [2.0944, [3, -0.3, 0], [3, 0.3, 0]], [2.0944, [3, -0.3, 0], [3, 0.4, 0]], [2.0944, [3, -0.4, 0], [3, 0.3, 0]], [2.1101, [3, -0.3, 0], [3, 0.266667, 0]], [1.74533, [3, -0.266667, 0.330488], [3, 0.3, -0.371799]], [0.00324066, [3, -0.3, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([1.2, 2.2, 3.1, 4, 5.2, 6.1, 6.9, 7.8])
    keys.append([[0, [3, -0.4, 0], [3, 0.333333, 0]], [0, [3, -0.333333, 0], [3, 0.3, 0]], [1.00403e-07, [3, -0.3, -1.00403e-07], [3, 0.3, 1.00403e-07]], [0.523599, [3, -0.3, 0], [3, 0.4, 0]], [1.00403e-07, [3, -0.4, 0.241022], [3, 0.3, -0.180766]], [-0.741765, [3, -0.3, 0.147262], [3, 0.266667, -0.1309]], [-0.872665, [3, -0.266667, 0], [3, 0.3, 0]], [-0.00275212, [3, -0.3, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([1.2, 2.2, 3.1, 4, 5.2, 6.1, 6.9, 7.8])
    keys.append([[0.397935, [3, -0.4, 0], [3, 0.333333, 0]], [0.397935, [3, -0.333333, 0], [3, 0.3, 0]], [0.397935, [3, -0.3, 0], [3, 0.3, 0]], [0, [3, -0.3, 0], [3, 0.4, 0]], [0.349066, [3, -0.4, 0], [3, 0.3, 0]], [0.261799, [3, -0.3, 0.0615999], [3, 0.266667, -0.0547554]], [0, [3, -0.266667, 0.0439783], [3, 0.3, -0.0494755]], [-0.0494755, [3, -0.3, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([1.2, 2.2, 3.1, 4, 5.2, 6.1, 6.9, 7.8])
    keys.append([[-0.10472, [3, -0.4, 0], [3, 0.333333, 0]], [-0.122173, [3, -0.333333, 0.0174533], [3, 0.3, -0.015708]], [-0.872665, [3, -0.3, 0], [3, 0.3, 0]], [0, [3, -0.3, 0], [3, 0.4, 0]], [-0.872665, [3, -0.4, 0], [3, 0.3, 0]], [-0.741765, [3, -0.3, 0], [3, 0.266667, 0]], [-0.872665, [3, -0.266667, 0], [3, 0.3, 0]], [-0.00302314, [3, -0.3, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([1.2, 2.2, 3.1, 4, 5.2, 6.1, 6.9, 7.8])
    keys.append([[-0.541052, [3, -0.4, 0], [3, 0.333333, 0]], [-0.139626, [3, -0.333333, 0], [3, 0.3, 0]], [-0.139626, [3, -0.3, 0], [3, 0.3, 0]], [-0.698132, [3, -0.3, 0], [3, 0.4, 0]], [-0.139626, [3, -0.4, -0.182844], [3, 0.3, 0.137133]], [0.261799, [3, -0.3, 0], [3, 0.266667, 0]], [0, [3, -0.266667, 0], [3, 0.3, 0]], [0.0494939, [3, -0.3, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([1.2, 2.2, 3.1, 4, 5.2, 6.1, 6.9, 7.8])
    keys.append([[0.122173, [3, -0.4, 0], [3, 0.333333, 0]], [0.122173, [3, -0.333333, 0], [3, 0.3, 0]], [1.74533, [3, -0.3, 0], [3, 0.3, 0]], [0, [3, -0.3, 0], [3, 0.4, 0]], [1.74533, [3, -0.4, 0], [3, 0.3, 0]], [1.48353, [3, -0.3, 0], [3, 0.266667, 0]], [1.74533, [3, -0.266667, 0], [3, 0.3, 0]], [0.00291069, [3, -0.3, 0], [3, 0, 0]]])

    mul = unit_time/8
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