import sys
from naoqi import ALProxy


def main(robotIP, port):
	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([1, 3])
	keys.append([[-0.0321816, [3, -0.333333, 0], [3, 0.666667, 0]], [-0.00623845, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("HeadYaw")
	times.append([1, 3])
	keys.append([[-0.0347254, [3, -0.333333, 0], [3, 0.666667, 0]], [-0.00283518, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LAnklePitch")
	times.append([1, 3])
	keys.append([[0.831606, [3, -0.333333, 0], [3, 0.666667, 0]], [-0.343994, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LAnkleRoll")
	times.append([1, 3])
	keys.append([[-0.00811709, [3, -0.333333, 0], [3, 0.666667, 0]], [-0.00811709, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LElbowRoll")
	times.append([1, 3])
	keys.append([[-1.20996, [3, -0.333333, 0], [3, 0.666667, 0]], [-1.01104, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LElbowYaw")
	times.append([1, 3])
	keys.append([[-0.447832, [3, -0.333333, 0], [3, 0.666667, 0]], [-1.38528, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LHand")
	times.append([1, 3])
	keys.append([[0.292938, [3, -0.333333, 0], [3, 0.666667, 0]], [0.254393, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LHipPitch")
	times.append([1, 3])
	keys.append([[-1.5309, [3, -0.333333, 0], [3, 0.666667, 0]], [-0.4555, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LHipRoll")
	times.append([1, 3])
	keys.append([[0.275376, [3, -0.333333, 0], [3, 0.666667, 0]], [0.00140617, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LHipYawPitch")
	times.append([1, 3])
	keys.append([[-0.617496, [3, -0.333333, 0], [3, 0.666667, 0]], [-0.00312241, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LKneePitch")
	times.append([1, 3])
	keys.append([[1.3959, [3, -0.333333, 0], [3, 0.666667, 0]], [0.703523, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LShoulderPitch")
	times.append([1, 3])
	keys.append([[0.871816, [3, -0.333333, 0], [3, 0.666667, 0]], [1.39018, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LShoulderRoll")
	times.append([1, 3])
	keys.append([[0.256008, [3, -0.333333, 0], [3, 0.666667, 0]], [0.298455, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("LWristYaw")
	times.append([1, 3])
	keys.append([[0.0278425, [3, -0.333333, 0], [3, 0.666667, 0]], [0.00613747, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RAnklePitch")
	times.append([1, 3])
	keys.append([[0.845574, [3, -0.333333, 0], [3, 0.666667, 0]], [-0.343924, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RAnkleRoll")
	times.append([1, 3])
	keys.append([[0.0271249, [3, -0.333333, 0], [3, 0.666667, 0]], [0.00583771, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RElbowRoll")
	times.append([1, 3])
	keys.append([[1.25067, [3, -0.333333, 0], [3, 0.666667, 0]], [1.01282, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RElbowYaw")
	times.append([1, 3])
	keys.append([[0.506379, [3, -0.333333, 0], [3, 0.666667, 0]], [1.38557, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RHand")
	times.append([1, 3])
	keys.append([[0.297186, [3, -0.333333, 0], [3, 0.666667, 0]], [0.252217, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RHipPitch")
	times.append([1, 3])
	keys.append([[-1.53051, [3, -0.333333, 0], [3, 0.666667, 0]], [-0.4555, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RHipRoll")
	times.append([1, 3])
	keys.append([[-0.266126, [3, -0.333333, 0], [3, 0.666667, 0]], [-0.00135914, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RHipYawPitch")
	times.append([1, 3])
	keys.append([[-0.617496, [3, -0.333333, 0], [3, 0.666667, 0]], [-0.00312241, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RKneePitch")
	times.append([1, 3])
	keys.append([[1.3957, [3, -0.333333, 0], [3, 0.666667, 0]], [0.70357, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RShoulderPitch")
	times.append([1, 3])
	keys.append([[0.930711, [3, -0.333333, 0], [3, 0.666667, 0]], [1.39142, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RShoulderRoll")
	times.append([1, 3])
	keys.append([[-0.29676, [3, -0.333333, 0], [3, 0.666667, 0]], [-0.297813, [3, -0.666667, 0], [3, 0, 0]]])

	names.append("RWristYaw")
	times.append([1, 3])
	keys.append([[-0.0270029, [3, -0.333333, 0], [3, 0.666667, 0]], [-0.00512736, [3, -0.666667, 0], [3, 0, 0]]])

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