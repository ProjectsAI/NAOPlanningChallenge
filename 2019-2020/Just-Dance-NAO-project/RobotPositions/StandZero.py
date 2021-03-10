import sys
from naoqi import ALProxy


def main(robotIP, port):
	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([1, 2])
	keys.append([[0.0074676, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0074676, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("HeadYaw")
	times.append([1, 2])
	keys.append([[-0.00843369, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.00843369, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LAnklePitch")
	times.append([1, 2])
	keys.append([[0.00570227, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.345127, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LAnkleRoll")
	times.append([1, 2])
	keys.append([[7.49291e-05, [3, -0.333333, 0], [3, 0.333333, 0]], [7.49291e-05, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LElbowRoll")
	times.append([1, 2])
	keys.append([[-0.0359292, [3, -0.333333, 0], [3, 0.333333, 0]], [-1.00742, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LElbowYaw")
	times.append([1, 2])
	keys.append([[-0.00195768, [3, -0.333333, 0], [3, 0.333333, 0]], [-1.38162, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LHand")
	times.append([1, 2])
	keys.append([[0.000855981, [3, -0.333333, 0], [3, 0.333333, 0]], [0.246519, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LHipPitch")
	times.append([1, 2])
	keys.append([[-0.00695538, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.443734, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LHipRoll")
	times.append([1, 2])
	keys.append([[0.0087634, [3, -0.333333, 0], [3, 0.333333, 0]], [0.0087634, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LHipYawPitch")
	times.append([1, 2])
	keys.append([[-0.00320589, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.00320589, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LKneePitch")
	times.append([1, 2])
	keys.append([[-0.00239876, [3, -0.333333, 0], [3, 0.333333, 0]], [0.690253, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LShoulderPitch")
	times.append([1, 2])
	keys.append([[0.00196107, [3, -0.333333, 0], [3, 0.333333, 0]], [1.39156, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LShoulderRoll")
	times.append([1, 2])
	keys.append([[0.0186958, [3, -0.333333, 0], [3, 0.333333, 0]], [0.295999, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("LWristYaw")
	times.append([1, 2])
	keys.append([[-0.00265636, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.00265636, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RAnklePitch")
	times.append([1, 2])
	keys.append([[0.00565043, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.345127, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RAnkleRoll")
	times.append([1, 2])
	keys.append([[0.00475415, [3, -0.333333, 0], [3, 0.333333, 0]], [0.00475415, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RElbowRoll")
	times.append([1, 2])
	keys.append([[0.0364184, [3, -0.333333, 0], [3, 0.333333, 0]], [1.00742, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RElbowYaw")
	times.append([1, 2])
	keys.append([[0.00195061, [3, -0.333333, 0], [3, 0.333333, 0]], [1.38162, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RHand")
	times.append([1, 2])
	keys.append([[0.000856186, [3, -0.333333, 0], [3, 0.333333, 0]], [0.246519, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RHipPitch")
	times.append([1, 2])
	keys.append([[-0.00660623, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.443734, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RHipRoll")
	times.append([1, 2])
	keys.append([[-0.00701631, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.00701631, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RHipYawPitch")
	times.append([1, 2])
	keys.append([[-0.00320589, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.00320589, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RKneePitch")
	times.append([1, 2])
	keys.append([[-0.00527281, [3, -0.333333, 0], [3, 0.333333, 0]], [0.690253, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RShoulderPitch")
	times.append([1, 2])
	keys.append([[0.00196013, [3, -0.333333, 0], [3, 0.333333, 0]], [1.39156, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RShoulderRoll")
	times.append([1, 2])
	keys.append([[-0.00914964, [3, -0.333333, 0], [3, 0.333333, 0]], [-0.295999, [3, -0.333333, 0], [3, 0, 0]]])

	names.append("RWristYaw")
	times.append([1, 2])
	keys.append([[0.00270378, [3, -0.333333, 0], [3, 0.333333, 0]], [0.00270378, [3, -0.333333, 0], [3, 0, 0]]])

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
