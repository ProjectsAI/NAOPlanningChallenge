def main(nao_ip, nao_port):
    # Choregraphe bezier export in Python.
    from naoqi import ALProxy
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.75])
    keys.append([[-0.00310997, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("HeadYaw")
    times.append([1.75])
    keys.append([[0.00302603, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("LAnklePitch")
    times.append([1.75])
    keys.append([[-0.107422, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("LAnkleRoll")
    times.append([1.75])
    keys.append([[0.00924597, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("LElbowRoll")
    times.append([1.75])
    keys.append([[-1.45572, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("LElbowYaw")
    times.append([1.75])
    keys.append([[0.010696, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("LHand")
    times.append([1.75])
    keys.append([[0.918205, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("LHipPitch")
    times.append([1.75])
    keys.append([[0.055266, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("LHipRoll")
    times.append([1.75])
    keys.append([[-0.032172, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("LHipYawPitch")
    times.append([1.75])
    keys.append([[0.0184499, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("LKneePitch")
    times.append([1.75])
    keys.append([[0.0705221, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("LShoulderPitch")
    times.append([1.75])
    keys.append([[1.18574, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("LShoulderRoll")
    times.append([1.75])
    keys.append([[0.783833, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("LWristYaw")
    times.append([1.75])
    keys.append([[-0.374338, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("RAnklePitch")
    times.append([1.75])
    keys.append([[-0.095066, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("RAnkleRoll")
    times.append([1.75])
    keys.append([[-0.00302603, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("RElbowRoll")
    times.append([1.75])
    keys.append([[1.37604, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("RElbowYaw")
    times.append([1.75])
    keys.append([[-0.34826, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("RHand")
    times.append([1.75])
    keys.append([[0.912387, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("RHipPitch")
    times.append([1.75])
    keys.append([[0.0352401, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("RHipRoll")
    times.append([1.75])
    keys.append([[0.01078, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("RKneePitch")
    times.append([1.75])
    keys.append([[0.084412, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("RShoulderPitch")
    times.append([1.75])
    keys.append([[0.991007, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("RShoulderRoll")
    times.append([1.75])
    keys.append([[-0.639721, [3, -0.583333, 0], [3, 0, 0]]])

    names.append("RWristYaw")
    times.append([1.75])
    keys.append([[0.427944, [3, -0.583333, 0], [3, 0, 0]]])

    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        motion = ALProxy("ALMotion", nao_ip, nao_port)
        motion.angleInterpolationBezier(names, times, keys)
    except BaseException, err:
        print err
