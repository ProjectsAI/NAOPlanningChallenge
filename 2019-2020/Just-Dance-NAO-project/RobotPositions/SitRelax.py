import sys
from naoqi import ALProxy


def main(robotIP, port):
	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([1, 3])
	keys.append([[0.0280607, [3, -0.333333, 0], [3, 0.666667, 0]], [0.00730429, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("HeadYaw")
	times.append([1, 3])
	keys.append([[-0.0239594, [3, -0.333333, 0], [3, 0.666667, 0]], [-0.000940801, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LAnklePitch")
	times.append([1, 3])
	keys.append([[0.92063, [3, -0.333333, 0], [3, 0.666667, 0]], [-0.344285, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LAnkleRoll")
	times.append([1, 3])
	keys.append([[7.49291e-05, [3, -0.333333, 0], [3, 0.666667, 0]], [7.49291e-05, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LElbowRoll")
	times.append([1, 3])
	keys.append([[-0.196903, [3, -0.333333, 0], [3, 0.666667, 0]], [-1.00579, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LElbowYaw")
	times.append([1, 3])
	keys.append([[-2.08111, [3, -0.333333, 0], [3, 0.666667, 0]], [-1.39128, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LHand")
	times.append([1, 3])
	keys.append([[0.138198, [3, -0.333333, 0], [3, 0.666667, 0]], [0.24573, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LHipPitch")
	times.append([1, 3])
	keys.append([[-1.12294, [3, -0.333333, 0], [3, 0.666667, 0]], [-0.452988, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LHipRoll")
	times.append([1, 3])
	keys.append([[0.137523, [3, -0.333333, 0], [3, 0.666667, 0]], [0.00059293, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LHipYawPitch")
	times.append([1, 3])
	keys.append([[-0.51759, [3, -0.333333, 0], [3, 0.666667, 0]], [-0.00234321, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LKneePitch")
	times.append([1, 3])
	keys.append([[-0.0376436, [3, -0.333333, 0], [3, 0.666667, 0]], [0.696669, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LShoulderPitch")
	times.append([1, 3])
	keys.append([[2.07748, [3, -0.333333, 0], [3, 0.666667, 0]], [1.40451, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LShoulderRoll")
	times.append([1, 3])
	keys.append([[0.0891677, [3, -0.333333, 0], [3, 0.666667, 0]], [0.293116, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LWristYaw")
	times.append([1, 3])
	keys.append([[-0.941568, [3, -0.333333, 0], [3, 0.666667, 0]], [-0.00420263, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RAnklePitch")
	times.append([1, 3])
	keys.append([[0.912261, [3, -0.333333, 0], [3, 0.666667, 0]], [-0.344285, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RAnkleRoll")
	times.append([1, 3])
	keys.append([[0.00475415, [3, -0.333333, 0], [3, 0.666667, 0]], [0.00475415, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RElbowRoll")
	times.append([1, 3])
	keys.append([[0.0412083, [3, -0.333333, 0], [3, 0.666667, 0]], [1.0016, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RElbowYaw")
	times.append([1, 3])
	keys.append([[2.07326, [3, -0.333333, 0], [3, 0.666667, 0]], [1.3913, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RHand")
	times.append([1, 3])
	keys.append([[0.138231, [3, -0.333333, 0], [3, 0.666667, 0]], [0.245775, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RHipPitch")
	times.append([1, 3])
	keys.append([[-1.06657, [3, -0.333333, 0], [3, 0.666667, 0]], [-0.45274, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RHipRoll")
	times.append([1, 3])
	keys.append([[-0.217257, [3, -0.333333, 0], [3, 0.666667, 0]], [-0.00099231, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RHipYawPitch")
	times.append([1, 3])
	keys.append([[-0.51759, [3, -0.333333, 0], [3, 0.666667, 0]], [-0.00234321, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RKneePitch")
	times.append([1, 3])
	keys.append([[-0.0827457, [3, -0.333333, 0], [3, 0.666667, 0]], [0.696442, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RShoulderPitch")
	times.append([1, 3])
	keys.append([[2.07822, [3, -0.333333, 0], [3, 0.666667, 0]], [1.40423, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RShoulderRoll")
	times.append([1, 3])
	keys.append([[-0.155254, [3, -0.333333, 0], [3, 0.666667, 0]], [-0.300624, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RWristYaw")
	times.append([1, 3])
	keys.append([[0.958376, [3, -0.333333, 0], [3, 0.666667, 0]], [0.00420263, [3, -0.666667, 0], [3, 0, 0]]])

	try:
	  motion = ALProxy("ALMotion",robotIP,port)
	  motion.angleInterpolationBezier(names, times, keys)
	except BaseException, err:
	  print err

  
if __name__ == "__main__":

    robotIP = "127.0.0.1"#"192.168.11.3"

    port = 55691 #9559 # Insert NAO port


    if len(sys.argv) <= 1:
        print "(robotIP default: 127.0.0.1)"
    elif len(sys.argv) <= 2:
        robotIP = sys.argv[1]
    else:
        port = int(sys.argv[2])
        robotIP = sys.argv[1]

    main(robotIP, port)