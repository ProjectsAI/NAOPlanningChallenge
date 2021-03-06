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
    times.append([0.52, 1, 1.36, 1.92])
    keys.append([[-0.084412, [3, -0.173333, 0], [3, 0.16, 0]], [-0.082878, [3, -0.16, -0.00153397], [3, 0.12, 0.00115048]], [0.325165, [3, -0.12, 0], [3, 0.186667, 0]], [-0.144238, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([0.52, 1, 1.36, 1.92])
    keys.append([[-0.917375, [3, -0.173333, 0], [3, 0.16, 0]], [-0.021518, [3, -0.16, 0], [3, 0.12, 0]], [-1.126, [3, -0.12, 0], [3, 0.186667, 0]], [-0.032256, [3, -0.186667, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([0.6, 0.8, 1.08, 1.4, 1.72, 1.92])
    keys.append([[-1.05995, [3, -0.2, 0], [3, 0.0666667, 0]], [-0.743948, [3, -0.0666667, -0.0722259], [3, 0.0933333, 0.101116]], [-0.539926, [3, -0.0933333, -0.0625189], [3, 0.106667, 0.0714502]], [-0.342041, [3, -0.106667, 0], [3, 0.106667, 0]], [-0.710201, [3, -0.106667, 0], [3, 0.0666667, 0]], [-0.427944, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([0.6, 0.8, 1.08, 1.4, 1.72, 1.92])
    keys.append([[-0.667332, [3, -0.2, 0], [3, 0.0666667, 0]], [-1.2932, [3, -0.0666667, 0.198203], [3, 0.0933333, -0.277485]], [-2.0944, [3, -0.0933333, 0], [3, 0.106667, 0]], [-2.08782, [3, -0.106667, -0.00657987], [3, 0.106667, 0.00657987]], [-1.11066, [3, -0.106667, 0], [3, 0.0666667, 0]], [-1.17509, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([0.44, 0.96, 1.92])
    keys.append([[0.258935, [3, -0.146667, 0], [3, 0.173333, 0]], [0.256753, [3, -0.173333, 0], [3, 0.32, 0]], [0.3048, [3, -0.32, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([0.6, 0.8, 1.08, 1.4, 1.72, 1.92])
    keys.append([[1.35601, [3, -0.2, 0], [3, 0.0666667, 0]], [1.37135, [3, -0.0666667, 0], [3, 0.0933333, 0]], [1.31613, [3, -0.0933333, 0], [3, 0.106667, 0]], [1.55697, [3, -0.106667, -0.0383501], [3, 0.106667, 0.0383501]], [1.59532, [3, -0.106667, 0], [3, 0.0666667, 0]], [1.48027, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([0.6, 0.8, 1.08, 1.4, 1.72, 1.92])
    keys.append([[0.021434, [3, -0.2, 0], [3, 0.0666667, 0]], [0.021434, [3, -0.0666667, 0], [3, 0.0933333, 0]], [0.075124, [3, -0.0933333, 0], [3, 0.106667, 0]], [0.0260361, [3, -0.106667, 0], [3, 0.106667, 0]], [0.199378, [3, -0.106667, 0], [3, 0.0666667, 0]], [0.0873961, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([0.44, 0.96, 1.32, 1.92])
    keys.append([[0.265341, [3, -0.146667, 0], [3, 0.173333, 0]], [1.10904, [3, -0.173333, 0], [3, 0.12, 0]], [-0.570723, [3, -0.12, 0], [3, 0.2, 0]], [0.145688, [3, -0.2, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([0.6, 0.8, 1.08, 1.4, 1.72, 1.92])
    keys.append([[1.55245, [3, -0.2, 0], [3, 0.0666667, 0]], [1.09685, [3, -0.0666667, 0], [3, 0.0933333, 0]], [1.46501, [3, -0.0933333, 0], [3, 0.106667, 0]], [0.446436, [3, -0.106667, 0], [3, 0.106667, 0]], [0.687274, [3, -0.106667, 0], [3, 0.0666667, 0]], [0.389678, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([0.6, 0.8, 1.08, 1.4, 1.72, 1.92])
    keys.append([[0.569072, [3, -0.2, 0], [3, 0.0666667, 0]], [1.38209, [3, -0.0666667, -0.211351], [3, 0.0933333, 0.295892]], [2.0908, [3, -0.0933333, 0], [3, 0.106667, 0]], [2.08773, [3, -0.106667, 0.00307182], [3, 0.106667, -0.00307182]], [1.18881, [3, -0.106667, 0.0196343], [3, 0.0666667, -0.0122714]], [1.17654, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([0.44, 0.96, 1.92])
    keys.append([[0.382207, [3, -0.146667, 0], [3, 0.173333, 0]], [0.382207, [3, -0.173333, 0], [3, 0.32, 0]], [0.3068, [3, -0.32, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([0.6, 0.8, 1.08, 1.4, 1.72, 1.92])
    keys.append([[0.664264, [3, -0.2, 0], [3, 0.0666667, 0]], [1.2119, [3, -0.0666667, 0], [3, 0.0933333, 0]], [0.952657, [3, -0.0933333, 0], [3, 0.106667, 0]], [1.68591, [3, -0.106667, 0], [3, 0.106667, 0]], [1.67977, [3, -0.106667, 0.00613659], [3, 0.0666667, -0.00383537]], [1.49569, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([0.6, 0.8, 1.08, 1.4, 1.72, 1.92])
    keys.append([[-0.00771196, [3, -0.2, 0], [3, 0.0666667, 0]], [-0.0798099, [3, -0.0666667, 0.00657428], [3, 0.0933333, -0.00920399]], [-0.0890139, [3, -0.0933333, 0], [3, 0.106667, 0]], [-0.029188, [3, -0.106667, 0], [3, 0.106667, 0]], [-0.22554, [3, -0.106667, 0], [3, 0.0666667, 0]], [-0.104354, [3, -0.0666667, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([0.44, 0.96, 1.92])
    keys.append([[0.85593, [3, -0.146667, 0], [3, 0.173333, 0]], [1.03387, [3, -0.173333, 0], [3, 0.32, 0]], [0.0720561, [3, -0.32, 0], [3, 0, 0]]])

    if stand:
        names.append("LAnklePitch")
        times.append([0.48, 1.44, 1.92])
        keys.append([[-0.0281642, [3, -0.16, 0], [3, 0.32, 0]], [-0.0158923, [3, -0.32, -0.0122719], [3, 0.16, 0.00613596]], [0.093532, [3, -0.16, 0], [3, 0, 0]]])

        names.append("LAnkleRoll")
        times.append([0.48, 1.44, 1.92])
        keys.append([[0.154211, [3, -0.16, 0], [3, 0.32, 0]], [-0.0973648, [3, -0.32, 0.0383547], [3, 0.16, -0.0191773]], [-0.116542, [3, -0.16, 0], [3, 0, 0]]])

        names.append("LHipPitch")
        times.append([0.48, 1.44, 1.92])
        keys.append([[0.343645, [3, -0.16, 0], [3, 0.32, 0]], [0.274614, [3, -0.32, 0.0456762], [3, 0.16, -0.0228381]], [0.138102, [3, -0.16, 0], [3, 0, 0]]])

        names.append("LHipRoll")
        times.append([0.48, 1.44, 1.92])
        keys.append([[-0.127676, [3, -0.16, 0], [3, 0.32, 0]], [0.134638, [3, -0.32, 0], [3, 0.16, 0]], [0.11816, [3, -0.16, 0], [3, 0, 0]]])

        names.append("LHipYawPitch")
        times.append([0.48, 1.44, 1.92])
        keys.append([[-0.455555, [3, -0.16, 0], [3, 0.32, 0]], [-0.289883, [3, -0.32, -0.0630643], [3, 0.16, 0.0315321]], [-0.171766, [3, -0.16, 0], [3, 0, 0]]])

        names.append("LKneePitch")
        times.append([0.48, 1.44, 1.92])
        keys.append([[0.0116376, [3, -0.16, 0], [3, 0.32, 0]], [0.0346476, [3, -0.32, 0], [3, 0.16, 0]], [-0.090548, [3, -0.16, 0], [3, 0, 0]]])

        names.append("RAnklePitch")
        times.append([0.48, 1.44, 1.92])
        keys.append([[-0.00668269, [3, -0.16, 0], [3, 0.32, 0]], [0.00098731, [3, -0.32, -0.00767], [3, 0.16, 0.003835]], [0.107422, [3, -0.16, 0], [3, 0, 0]]])

        names.append("RAnkleRoll")
        times.append([0.48, 1.44, 1.92])
        keys.append([[0.233874, [3, -0.16, 0], [3, 0.32, 0]], [0.179769, [3, -0.32, 0.0359409], [3, 0.16, -0.0179705]], [0.07214, [3, -0.16, 0], [3, 0, 0]]])

        names.append("RHipPitch")
        times.append([0.48, 1.44, 1.92])
        keys.append([[0.202235, [3, -0.16, 0], [3, 0.32, 0]], [0.277401, [3, -0.32, 0], [3, 0.16, 0]], [0.131882, [3, -0.16, 0], [3, 0, 0]]])

        names.append("RHipRoll")
        times.append([0.48, 1.44, 1.92])
        keys.append([[-0.221894, [3, -0.16, 0], [3, 0.32, 0]], [-0.159001, [3, -0.32, -0.0346609], [3, 0.16, 0.0173305]], [-0.06592, [3, -0.16, 0], [3, 0, 0]]])

        names.append("RHipYawPitch")
        times.append([1.92])
        keys.append([[-0.171766, [3, -0.64, 0], [3, 0, 0]]])

        names.append("RKneePitch")
        times.append([0.48, 1.44, 1.92])
        keys.append([[0.0844844, [3, -0.16, 0], [3, 0.32, 0]], [0.0277265, [3, -0.32, 0.0392183], [3, 0.16, -0.0196092]], [-0.091998, [3, -0.16, 0], [3, 0, 0]]])

    mul = unit_time/2.05
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
