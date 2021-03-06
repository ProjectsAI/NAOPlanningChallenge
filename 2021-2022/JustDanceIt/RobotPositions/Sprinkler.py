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
    times.append([1, 2.48, 7, 7.92])
    keys.append([[-0.12583, [3, -0.333333, 0], [3, 0.493333, 0]], [-0.233874, [3, -0.493333, 0], [3, 1.50667, 0]], [-0.173384, [3, -1.50667, 0], [3, 0.306667, 0]], [-0.173384, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([1, 2.48, 7, 7.92])
    keys.append([[-0.0107799, [3, -0.333333, 0], [3, 0.493333, 0]], [0.912807, [3, -0.493333, 0], [3, 1.50667, 0]], [0.21932, [3, -1.50667, 0], [3, 0.306667, 0]], [0.21932, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([1, 2.32, 7, 7.92])
    keys.append([[0.095066, [3, -0.333333, 0], [3, 0.44, 0]], [-0.214803, [3, -0.44, 0.0367853], [3, 1.56, -0.130421]], [-0.406552, [3, -1.56, 0], [3, 0.306667, 0]], [-0.406552, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([1, 2.32, 7, 7.92])
    keys.append([[-0.116542, [3, -0.333333, 0], [3, 0.44, 0]], [-0.14262, [3, -0.44, 0], [3, 1.56, 0]], [-0.11961, [3, -1.56, 0], [3, 0.306667, 0]], [-0.11961, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([1, 2.4, 3, 7, 7.92])
    keys.append([[-0.400331, [3, -0.333333, 0], [3, 0.466667, 0]], [-0.0349066, [3, -0.466667, 0], [3, 0.2, 0]], [-0.0459781, [3, -0.2, 0.0110715], [3, 1.33333, -0.07381]], [-0.358915, [3, -1.33333, 0], [3, 0.306667, 0]], [-0.358915, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([1, 2.4, 3, 7, 7.92])
    keys.append([[-1.21037, [3, -0.333333, 0], [3, 0.466667, 0]], [-1.48956, [3, -0.466667, 0], [3, 0.2, 0]], [-1.48035, [3, -0.2, -0.00920482], [3, 1.33333, 0.0613654]], [-1.26099, [3, -1.33333, 0], [3, 0.306667, 0]], [-1.26099, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([1, 2.4, 3, 7, 7.92])
    keys.append([[0.3056, [3, -0.333333, 0], [3, 0.466667, 0]], [0.9616, [3, -0.466667, 0], [3, 0.2, 0]], [0.9592, [3, -0.2, 0], [3, 1.33333, 0]], [0.9616, [3, -1.33333, 0], [3, 0.306667, 0]], [0.9616, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([1, 2.32, 7, 7.92])
    keys.append([[0.136568, [3, -0.333333, 0], [3, 0.44, 0]], [-0.144154, [3, -0.44, 0.0296982], [3, 1.56, -0.105294]], [-0.268407, [3, -1.56, 0], [3, 0.306667, 0]], [-0.268407, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([1, 2.32, 7, 7.92])
    keys.append([[0.115092, [3, -0.333333, 0], [3, 0.44, 0]], [0.233211, [3, -0.44, 0], [3, 1.56, 0]], [0.173384, [3, -1.56, 0], [3, 0.306667, 0]], [0.173384, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([1, 2.32, 7, 7.92])
    keys.append([[-0.1733, [3, -0.333333, 0], [3, 0.44, 0]], [-0.288349, [3, -0.44, 0], [3, 1.56, 0]], [-0.28068, [3, -1.56, 0], [3, 0.306667, 0]], [-0.28068, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([1, 2.32, 7, 7.92])
    keys.append([[-0.090548, [3, -0.333333, 0], [3, 0.44, 0]], [0.539926, [3, -0.44, -0.0668211], [3, 1.56, 0.236911]], [0.820649, [3, -1.56, 0], [3, 0.306667, 0]], [0.820649, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([1, 2.4, 2.48, 3, 7, 7.92])
    keys.append([[1.53089, [3, -0.333333, 0], [3, 0.466667, 0]], [-0.420357, [3, -0.466667, 0.659368], [3, 0.0266667, -0.0376782]], [-0.560251, [3, -0.0266667, 0], [3, 0.173333, 0]], [-0.417134, [3, -0.173333, -0.0177769], [3, 1.33333, 0.136745]], [-0.0966839, [3, -1.33333, 0], [3, 0.306667, 0]], [-0.0966839, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([1, 2.4, 3, 3.44, 3.8, 4.2, 4.6, 4.96, 5.4, 5.8, 6.16, 6.6, 7, 7.92])
    keys.append([[0.13495, [3, -0.333333, 0], [3, 0.466667, 0]], [0.819114, [3, -0.466667, 0], [3, 0.2, 0]], [0.461692, [3, -0.2, 0], [3, 0.146667, 0]], [0.610865, [3, -0.146667, 0], [3, 0.12, 0]], [0.223402, [3, -0.12, 0], [3, 0.133333, 0]], [0.460767, [3, -0.133333, 0], [3, 0.133333, 0]], [0.0436332, [3, -0.133333, 0], [3, 0.12, 0]], [0.312414, [3, -0.12, 0], [3, 0.146667, 0]], [-0.0610865, [3, -0.146667, 0], [3, 0.133333, 0]], [0.207694, [3, -0.133333, 0], [3, 0.12, 0]], [-0.195477, [3, -0.12, 0], [3, 0.146667, 0]], [0.0593412, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.159578, [3, -0.133333, 0], [3, 0.306667, 0]], [-0.159578, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([1, 2.4, 3, 3.44, 3.8, 7, 7.92])
    keys.append([[0.121144, [3, -0.333333, 0], [3, 0.466667, 0]], [0.312894, [3, -0.466667, 0], [3, 0.2, 0]], [0.131882, [3, -0.2, 0.0474176], [3, 0.146667, -0.0347729]], [0.0663225, [3, -0.146667, 0], [3, 0.12, 0]], [0.0663225, [3, -0.12, 0], [3, 1.06667, 0]], [-0.29457, [3, -1.06667, 0], [3, 0.306667, 0]], [-0.29457, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([1, 2.32, 7, 7.92])
    keys.append([[0.10282, [3, -0.333333, 0], [3, 0.44, 0]], [-0.0199001, [3, -0.44, 0.0268859], [3, 1.56, -0.0953229]], [-0.263807, [3, -1.56, 0], [3, 0.306667, 0]], [-0.263807, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([1, 2.32, 7, 7.92])
    keys.append([[0.07214, [3, -0.333333, 0], [3, 0.44, 0]], [0.116626, [3, -0.44, 0], [3, 1.56, 0]], [0.0828778, [3, -1.56, 0], [3, 0.306667, 0]], [0.0828778, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([1, 2.44, 2.96, 3.4, 3.8, 4.24, 4.6, 5, 5.48, 5.8, 6.2, 6.56, 7, 7.92])
    keys.append([[0.385075, [3, -0.333333, 0], [3, 0.48, 0]], [1.54462, [3, -0.48, 0], [3, 0.173333, 0]], [1.53864, [3, -0.173333, 0], [3, 0.146667, 0]], [1.54462, [3, -0.146667, 0], [3, 0.133333, 0]], [1.53864, [3, -0.133333, 0], [3, 0.146667, 0]], [1.54462, [3, -0.146667, 0], [3, 0.12, 0]], [1.53864, [3, -0.12, 0], [3, 0.133333, 0]], [1.54462, [3, -0.133333, 0], [3, 0.16, 0]], [1.53864, [3, -0.16, 0], [3, 0.106667, 0]], [1.54462, [3, -0.106667, 0], [3, 0.133333, 0]], [1.53864, [3, -0.133333, 0], [3, 0.12, 0]], [1.54462, [3, -0.12, 0], [3, 0.146667, 0]], [1.53558, [3, -0.146667, 0], [3, 0.306667, 0]], [1.53558, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([1, 2.44, 2.96, 3.4, 3.8, 4.24, 4.6, 5, 5.48, 5.8, 6.2, 6.56, 7, 7.92])
    keys.append([[1.18421, [3, -0.333333, 0], [3, 0.48, 0]], [0.966378, [3, -0.48, 0], [3, 0.173333, 0]], [1.38823, [3, -0.173333, 0], [3, 0.146667, 0]], [0.966378, [3, -0.146667, 0], [3, 0.133333, 0]], [1.38823, [3, -0.133333, 0], [3, 0.146667, 0]], [0.966378, [3, -0.146667, 0], [3, 0.12, 0]], [1.38823, [3, -0.12, 0], [3, 0.133333, 0]], [0.966378, [3, -0.133333, 0], [3, 0.16, 0]], [1.38823, [3, -0.16, 0], [3, 0.106667, 0]], [0.966378, [3, -0.106667, 0], [3, 0.133333, 0]], [1.38823, [3, -0.133333, 0], [3, 0.12, 0]], [0.966378, [3, -0.12, 0], [3, 0.146667, 0]], [1.36982, [3, -0.146667, 0], [3, 0.306667, 0]], [1.36982, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([1, 2.44, 2.96, 3.4, 3.8, 4.24, 4.6, 5, 5.48, 5.8, 6.2, 6.56, 7, 7.92])
    keys.append([[0.3068, [3, -0.333333, 0], [3, 0.48, 0]], [0.7708, [3, -0.48, 0], [3, 0.173333, 0]], [0.7696, [3, -0.173333, 0], [3, 0.146667, 0]], [0.7708, [3, -0.146667, 0], [3, 0.133333, 0]], [0.7696, [3, -0.133333, 0], [3, 0.146667, 0]], [0.7708, [3, -0.146667, 0], [3, 0.12, 0]], [0.7696, [3, -0.12, 0], [3, 0.133333, 0]], [0.7708, [3, -0.133333, 0], [3, 0.16, 0]], [0.7696, [3, -0.16, 0], [3, 0.106667, 0]], [0.7708, [3, -0.106667, 0], [3, 0.133333, 0]], [0.7696, [3, -0.133333, 0], [3, 0.12, 0]], [0.7708, [3, -0.12, 0], [3, 0.146667, 0]], [0.7692, [3, -0.146667, 0], [3, 0.306667, 0]], [0.7692, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([1, 2.32, 7, 7.92])
    keys.append([[0.130348, [3, -0.333333, 0], [3, 0.44, 0]], [0.138018, [3, -0.44, 0], [3, 1.56, 0]], [-0.251617, [3, -1.56, 0], [3, 0.306667, 0]], [-0.251617, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([1, 2.32, 7, 7.92])
    keys.append([[-0.06592, [3, -0.333333, 0], [3, 0.44, 0]], [-0.0383082, [3, -0.44, -0.00259605], [3, 1.56, 0.00920417]], [-0.0291041, [3, -1.56, 0], [3, 0.306667, 0]], [-0.0291041, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([1, 2.32, 7, 7.92])
    keys.append([[-0.1733, [3, -0.333333, 0], [3, 0.44, 0]], [-0.288349, [3, -0.44, 0], [3, 1.56, 0]], [-0.28068, [3, -1.56, 0], [3, 0.306667, 0]], [-0.28068, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([1, 2.32, 7, 7.92])
    keys.append([[-0.0904641, [3, -0.333333, 0], [3, 0.44, 0]], [0.0798099, [3, -0.44, -0.0562467], [3, 1.56, 0.19942]], [0.676537, [3, -1.56, 0], [3, 0.306667, 0]], [0.676537, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([1, 2.44, 2.96, 3.4, 3.8, 4.24, 4.6, 5, 5.48, 5.8, 6.2, 6.56, 7, 7.92])
    keys.append([[1.51103, [3, -0.333333, 0], [3, 0.48, 0]], [-0.742414, [3, -0.48, 0], [3, 0.173333, 0]], [-0.566003, [3, -0.173333, 0], [3, 0.146667, 0]], [-0.742414, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.566003, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.742414, [3, -0.146667, 0], [3, 0.12, 0]], [-0.566003, [3, -0.12, 0], [3, 0.133333, 0]], [-0.742414, [3, -0.133333, 0], [3, 0.16, 0]], [-0.566003, [3, -0.16, 0], [3, 0.106667, 0]], [-0.742414, [3, -0.106667, 0], [3, 0.133333, 0]], [-0.566003, [3, -0.133333, 0], [3, 0.12, 0]], [-0.742414, [3, -0.12, 0], [3, 0.146667, 0]], [-0.544529, [3, -0.146667, 0], [3, 0.306667, 0]], [-0.544529, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([1, 2.44, 2.96, 3.4, 3.8, 4.24, 4.6, 5, 5.48, 5.8, 6.2, 6.56, 7, 7.92])
    keys.append([[-0.113558, [3, -0.333333, 0], [3, 0.48, 0]], [-0.43263, [3, -0.48, 0], [3, 0.173333, 0]], [-0.0614019, [3, -0.173333, 0], [3, 0.146667, 0]], [-0.43263, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.0614019, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.43263, [3, -0.146667, 0], [3, 0.12, 0]], [-0.0614019, [3, -0.12, 0], [3, 0.133333, 0]], [-0.43263, [3, -0.133333, 0], [3, 0.16, 0]], [-0.0614019, [3, -0.16, 0], [3, 0.106667, 0]], [-0.43263, [3, -0.106667, 0], [3, 0.133333, 0]], [-0.0614019, [3, -0.133333, 0], [3, 0.12, 0]], [-0.43263, [3, -0.12, 0], [3, 0.146667, 0]], [-0.075208, [3, -0.146667, 0], [3, 0.306667, 0]], [-0.075208, [3, -0.306667, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([1, 2.44, 2.96, 3.4, 3.8, 4.24, 4.6, 5, 5.48, 5.8, 6.2, 6.56, 7, 7.92])
    keys.append([[0.105804, [3, -0.333333, 0], [3, 0.48, 0]], [1.30539, [3, -0.48, 0], [3, 0.173333, 0]], [0.803775, [3, -0.173333, 0], [3, 0.146667, 0]], [1.30539, [3, -0.146667, 0], [3, 0.133333, 0]], [0.803775, [3, -0.133333, 0], [3, 0.146667, 0]], [1.30539, [3, -0.146667, 0], [3, 0.12, 0]], [0.803775, [3, -0.12, 0], [3, 0.133333, 0]], [1.30539, [3, -0.133333, 0], [3, 0.16, 0]], [0.803775, [3, -0.16, 0], [3, 0.106667, 0]], [1.30539, [3, -0.106667, 0], [3, 0.133333, 0]], [0.803775, [3, -0.133333, 0], [3, 0.12, 0]], [1.30539, [3, -0.12, 0], [3, 0.146667, 0]], [0.820649, [3, -0.146667, 0], [3, 0.306667, 0]], [0.820649, [3, -0.306667, 0], [3, 0, 0]]])

    mul = unit_time/16.8
    times_unit = [list(np.array(t, dtype=float)*mul) for t in times]

    try:
        motion = ALProxy("ALMotion", robotIP, port)
        motion.angleInterpolationBezier(names, times_unit, keys)
        motion.waitUntilMoveIsFinished()
    except BaseException, err:
        print err

    end = time.time()
    print(end-start)
    start1 = time.time()


    #Other side
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([2.48, 7, 7.44, 8.76])
    keys.append([[-0.233874, [3, -0.826667, 0], [3, 1.50667, 0]], [-0.173384, [3, -1.50667, 0], [3, 0.146667, 0]], [-0.173384, [3, -0.146667, 0], [3, 0.44, 0]], [-0.173384, [3, -0.44, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([2.48, 7, 7.44, 8.76])
    keys.append([[-0.912807, [3, -0.826667, 0], [3, 1.50667, 0]], [-0.21932, [3, -1.50667, 0], [3, 0.146667, 0]], [-0.21932, [3, -0.146667, 0], [3, 0.44, 0]], [0.0107799, [3, -0.44, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([2.32, 7, 7.44, 8.76])
    keys.append([[-0.0199001, [3, -0.773333, 0], [3, 1.56, 0]], [-0.263807, [3, -1.56, 0], [3, 0.146667, 0]], [-0.263807, [3, -0.146667, 0], [3, 0.44, 0]], [0.107422, [3, -0.44, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([2.32, 7, 7.44, 8.76])
    keys.append([[-0.116626, [3, -0.773333, 0], [3, 1.56, 0]], [-0.0828778, [3, -1.56, 0], [3, 0.146667, 0]], [-0.0828778, [3, -0.146667, 0], [3, 0.44, 0]], [-0.073674, [3, -0.44, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([2.44, 2.96, 3.4, 3.8, 4.24, 4.6, 5, 5.48, 5.8, 6.2, 6.56, 7, 7.44, 8.76])
    keys.append([[-1.54462, [3, -0.813333, 0], [3, 0.173333, 0]], [-1.53864, [3, -0.173333, 0], [3, 0.146667, 0]], [-1.54462, [3, -0.146667, 0], [3, 0.133333, 0]], [-1.53864, [3, -0.133333, 0], [3, 0.146667, 0]], [-1.54462, [3, -0.146667, 0], [3, 0.12, 0]], [-1.53864, [3, -0.12, 0], [3, 0.133333, 0]], [-1.54462, [3, -0.133333, 0], [3, 0.16, 0]], [-1.53864, [3, -0.16, 0], [3, 0.106667, 0]], [-1.54462, [3, -0.106667, 0], [3, 0.133333, 0]], [-1.53864, [3, -0.133333, 0], [3, 0.12, 0]], [-1.54462, [3, -0.12, 0], [3, 0.146667, 0]], [-1.53558, [3, -0.146667, 0], [3, 0.146667, 0]], [-1.53558, [3, -0.146667, 0], [3, 0.44, 0]], [-0.412688, [3, -0.44, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([2.44, 2.96, 3.4, 3.8, 4.24, 4.6, 5, 5.48, 5.8, 6.2, 6.56, 7, 7.44, 8.76])
    keys.append([[-0.966378, [3, -0.813333, 0], [3, 0.173333, 0]], [-1.38823, [3, -0.173333, 0], [3, 0.146667, 0]], [-0.966378, [3, -0.146667, 0], [3, 0.133333, 0]], [-1.38823, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.966378, [3, -0.146667, 0], [3, 0.12, 0]], [-1.38823, [3, -0.12, 0], [3, 0.133333, 0]], [-0.966378, [3, -0.133333, 0], [3, 0.16, 0]], [-1.38823, [3, -0.16, 0], [3, 0.106667, 0]], [-0.966378, [3, -0.106667, 0], [3, 0.133333, 0]], [-1.38823, [3, -0.133333, 0], [3, 0.12, 0]], [-0.966378, [3, -0.12, 0], [3, 0.146667, 0]], [-1.36982, [3, -0.146667, 0], [3, 0.146667, 0]], [-1.36982, [3, -0.146667, 0], [3, 0.44, 0]], [-1.19494, [3, -0.44, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([2.44, 2.96, 3.4, 3.8, 4.24, 4.6, 5, 5.48, 5.8, 6.2, 6.56, 7, 7.44, 8.76])
    keys.append([[0.7708, [3, -0.813333, 0], [3, 0.173333, 0]], [0.7696, [3, -0.173333, 0], [3, 0.146667, 0]], [0.7708, [3, -0.146667, 0], [3, 0.133333, 0]], [0.7696, [3, -0.133333, 0], [3, 0.146667, 0]], [0.7708, [3, -0.146667, 0], [3, 0.12, 0]], [0.7696, [3, -0.12, 0], [3, 0.133333, 0]], [0.7708, [3, -0.133333, 0], [3, 0.16, 0]], [0.7696, [3, -0.16, 0], [3, 0.106667, 0]], [0.7708, [3, -0.106667, 0], [3, 0.133333, 0]], [0.7696, [3, -0.133333, 0], [3, 0.12, 0]], [0.7708, [3, -0.12, 0], [3, 0.146667, 0]], [0.7692, [3, -0.146667, 0], [3, 0.146667, 0]], [0.7692, [3, -0.146667, 0], [3, 0.44, 0]], [0.3068, [3, -0.44, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([2.32, 7, 7.44, 8.76])
    keys.append([[0.138018, [3, -0.773333, 0], [3, 1.56, 0]], [-0.251617, [3, -1.56, 0], [3, 0.146667, 0]], [-0.251617, [3, -0.146667, 0], [3, 0.44, 0]], [0.133416, [3, -0.44, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([2.32, 7, 7.44, 8.76])
    keys.append([[0.0383082, [3, -0.773333, 0], [3, 1.56, 0]], [0.0291041, [3, -1.56, 0], [3, 0.146667, 0]], [0.0291041, [3, -0.146667, 0], [3, 0.44, 0]], [0.0643861, [3, -0.44, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([2.32, 7, 7.44, 8.76])
    keys.append([[-0.288349, [3, -0.773333, 0], [3, 1.56, 0]], [-0.28068, [3, -1.56, 0], [3, 0.146667, 0]], [-0.28068, [3, -0.146667, 0], [3, 0.44, 0]], [-0.168698, [3, -0.44, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([2.32, 7, 7.44, 8.76])
    keys.append([[0.0798099, [3, -0.773333, 0], [3, 1.56, 0]], [0.676537, [3, -1.56, 0], [3, 0.146667, 0]], [0.676537, [3, -0.146667, 0], [3, 0.44, 0]], [-0.091998, [3, -0.44, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([2.44, 2.96, 3.4, 3.8, 4.24, 4.6, 5, 5.48, 5.8, 6.2, 6.56, 7, 7.44, 8.76])
    keys.append([[-0.742414, [3, -0.813333, 0], [3, 0.173333, 0]], [-0.566003, [3, -0.173333, 0], [3, 0.146667, 0]], [-0.742414, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.566003, [3, -0.133333, 0], [3, 0.146667, 0]], [-0.742414, [3, -0.146667, 0], [3, 0.12, 0]], [-0.566003, [3, -0.12, 0], [3, 0.133333, 0]], [-0.742414, [3, -0.133333, 0], [3, 0.16, 0]], [-0.566003, [3, -0.16, 0], [3, 0.106667, 0]], [-0.742414, [3, -0.106667, 0], [3, 0.133333, 0]], [-0.566003, [3, -0.133333, 0], [3, 0.12, 0]], [-0.742414, [3, -0.12, 0], [3, 0.146667, 0]], [-0.544529, [3, -0.146667, 0], [3, 0.146667, 0]], [-0.544529, [3, -0.146667, 0], [3, 0.44, 0]], [1.48189, [3, -0.44, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([2.44, 2.96, 3.4, 3.8, 4.24, 4.6, 5, 5.48, 5.8, 6.2, 6.56, 7, 7.44, 8.76])
    keys.append([[0.43263, [3, -0.813333, 0], [3, 0.173333, 0]], [0.0614019, [3, -0.173333, 0], [3, 0.146667, 0]], [0.43263, [3, -0.146667, 0], [3, 0.133333, 0]], [0.0614019, [3, -0.133333, 0], [3, 0.146667, 0]], [0.43263, [3, -0.146667, 0], [3, 0.12, 0]], [0.0614019, [3, -0.12, 0], [3, 0.133333, 0]], [0.43263, [3, -0.133333, 0], [3, 0.16, 0]], [0.0614019, [3, -0.16, 0], [3, 0.106667, 0]], [0.43263, [3, -0.106667, 0], [3, 0.133333, 0]], [0.0614019, [3, -0.133333, 0], [3, 0.12, 0]], [0.43263, [3, -0.12, 0], [3, 0.146667, 0]], [0.075208, [3, -0.146667, 0], [3, 0.146667, 0]], [0.075208, [3, -0.146667, 0], [3, 0.44, 0]], [0.0813439, [3, -0.44, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([2.44, 2.96, 3.4, 3.8, 4.24, 4.6, 5, 5.48, 5.8, 6.2, 6.56, 7, 7.44, 8.76])
    keys.append([[-1.30539, [3, -0.813333, 0], [3, 0.173333, 0]], [-0.803775, [3, -0.173333, 0], [3, 0.146667, 0]], [-1.30539, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.803775, [3, -0.133333, 0], [3, 0.146667, 0]], [-1.30539, [3, -0.146667, 0], [3, 0.12, 0]], [-0.803775, [3, -0.12, 0], [3, 0.133333, 0]], [-1.30539, [3, -0.133333, 0], [3, 0.16, 0]], [-0.803775, [3, -0.16, 0], [3, 0.106667, 0]], [-1.30539, [3, -0.106667, 0], [3, 0.133333, 0]], [-0.803775, [3, -0.133333, 0], [3, 0.12, 0]], [-1.30539, [3, -0.12, 0], [3, 0.146667, 0]], [-0.820649, [3, -0.146667, 0], [3, 0.146667, 0]], [-0.820649, [3, -0.146667, 0], [3, 0.44, 0]], [-0.167164, [3, -0.44, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([2.32, 7, 7.44, 8.76])
    keys.append([[-0.214803, [3, -0.773333, 0], [3, 1.56, 0]], [-0.406552, [3, -1.56, 0], [3, 0.146667, 0]], [-0.406552, [3, -0.146667, 0], [3, 0.44, 0]], [0.101202, [3, -0.44, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([2.32, 7, 7.44, 8.76])
    keys.append([[0.14262, [3, -0.773333, 0], [3, 1.56, 0]], [0.11961, [3, -1.56, 0], [3, 0.146667, 0]], [0.11961, [3, -0.146667, 0], [3, 0.44, 0]], [0.118076, [3, -0.44, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([2.4, 3, 7, 7.44, 8.76])
    keys.append([[0.0349066, [3, -0.8, 0], [3, 0.2, 0]], [0.0459781, [3, -0.2, -0.0110715], [3, 1.33333, 0.07381]], [0.358915, [3, -1.33333, 0], [3, 0.146667, 0]], [0.358915, [3, -0.146667, 0], [3, 0.44, 0]], [0.38806, [3, -0.44, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([2.4, 3, 7, 7.44, 8.76])
    keys.append([[1.48956, [3, -0.8, 0], [3, 0.2, 0]], [1.48035, [3, -0.2, 0.00920482], [3, 1.33333, -0.0613654]], [1.26099, [3, -1.33333, 0], [3, 0.146667, 0]], [1.26099, [3, -0.146667, 0], [3, 0.44, 0]], [1.21497, [3, -0.44, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([2.4, 3, 7, 7.44, 8.76])
    keys.append([[0.9616, [3, -0.8, 0], [3, 0.2, 0]], [0.9592, [3, -0.2, 0], [3, 1.33333, 0]], [0.9616, [3, -1.33333, 0], [3, 0.146667, 0]], [0.9616, [3, -0.146667, 0], [3, 0.44, 0]], [0.3052, [3, -0.44, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([2.32, 7, 7.44, 8.76])
    keys.append([[-0.144154, [3, -0.773333, 0], [3, 1.56, 0]], [-0.268407, [3, -1.56, 0], [3, 0.146667, 0]], [-0.268407, [3, -0.146667, 0], [3, 0.44, 0]], [0.142704, [3, -0.44, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([2.32, 7, 7.44, 8.76])
    keys.append([[-0.233211, [3, -0.773333, 0], [3, 1.56, 0]], [-0.173384, [3, -1.56, 0], [3, 0.146667, 0]], [-0.173384, [3, -0.146667, 0], [3, 0.44, 0]], [-0.115092, [3, -0.44, 0], [3, 0, 0]]])

    names.append("RHipYawPitch")
    times.append([2.32, 7, 7.44, 8.76])
    keys.append([[-0.288349, [3, -0.773333, 0], [3, 1.56, 0]], [-0.28068, [3, -1.56, 0], [3, 0.146667, 0]], [-0.28068, [3, -0.146667, 0], [3, 0.44, 0]], [-0.168698, [3, -0.44, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([2.32, 7, 7.44, 8.76])
    keys.append([[0.539926, [3, -0.773333, 0], [3, 1.56, 0]], [0.820649, [3, -1.56, 0], [3, 0.146667, 0]], [0.820649, [3, -0.146667, 0], [3, 0.44, 0]], [-0.0923279, [3, -0.44, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([2.4, 2.48, 3, 7, 7.44, 8.76])
    keys.append([[-0.420357, [3, -0.8, 0], [3, 0.0266667, 0]], [-0.560251, [3, -0.0266667, 0], [3, 0.173333, 0]], [-0.417134, [3, -0.173333, -0.0177769], [3, 1.33333, 0.136745]], [-0.0966839, [3, -1.33333, 0], [3, 0.146667, 0]], [-0.0966839, [3, -0.146667, 0], [3, 0.44, 0]], [1.48794, [3, -0.44, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([2.4, 3, 3.44, 3.8, 4.2, 4.6, 4.96, 5.4, 5.8, 6.16, 6.6, 7, 7.44, 8.76])
    keys.append([[-0.819114, [3, -0.8, 0], [3, 0.2, 0]], [-0.461692, [3, -0.2, 0], [3, 0.146667, 0]], [-0.610865, [3, -0.146667, 0], [3, 0.12, 0]], [-0.223402, [3, -0.12, 0], [3, 0.133333, 0]], [-0.460767, [3, -0.133333, 0], [3, 0.133333, 0]], [-0.0436332, [3, -0.133333, 0], [3, 0.12, 0]], [-0.312414, [3, -0.12, 0], [3, 0.146667, 0]], [0.0610865, [3, -0.146667, 0], [3, 0.133333, 0]], [-0.207694, [3, -0.133333, 0], [3, 0.12, 0]], [0.195477, [3, -0.12, 0], [3, 0.146667, 0]], [-0.0593412, [3, -0.146667, 0], [3, 0.133333, 0]], [0.159578, [3, -0.133333, 0], [3, 0.146667, 0]], [0.159578, [3, -0.146667, 0], [3, 0.44, 0]], [-0.0889301, [3, -0.44, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([2.4, 3, 3.44, 3.8, 7, 7.44, 8.76])
    keys.append([[-0.312894, [3, -0.8, 0], [3, 0.2, 0]], [-0.131882, [3, -0.2, -0.0474176], [3, 0.146667, 0.0347729]], [-0.0663225, [3, -0.146667, 0], [3, 0.12, 0]], [-0.0663225, [3, -0.12, 0], [3, 1.06667, 0]], [0.29457, [3, -1.06667, 0], [3, 0.146667, 0]], [0.29457, [3, -0.146667, 0], [3, 0.44, 0]], [-0.161028, [3, -0.44, 0], [3, 0, 0]]])

    mul = unit_time/16.8
    times_unit = [list(np.array(t, dtype=float)*mul) for t in times]

    try:
        motion = ALProxy("ALMotion", robotIP, port)
        motion.angleInterpolationBezier(names, times_unit, keys)
    except BaseException, err:
        print err

    end1 = time.time()
    print(end1-start1)

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
