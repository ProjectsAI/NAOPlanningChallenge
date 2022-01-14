# Choregraphe simplified export in Python.
from naoqi import ALProxy
import sys

def main(robotIP, port):
	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([1.44, 2.04, 2.6, 3.2, 3.76, 4.92])
	keys.append([0.343573, 0.361981, -0.04913, -0.380475, 0.240796, 0.516916])

	names.append("HeadYaw")
	times.append([1.44, 2.04, 2.6, 3.2, 3.76, 4.92])
	keys.append([0.5568, -0.411154, -0.0537319, 0.0720561, 0.493905, -0.39428])

	names.append("LAnklePitch")
	times.append([0.96, 1.52, 2.12, 2.68, 3.28, 3.84, 4.44, 5])
	keys.append([-0.682424, -0.781907, -0.357974, -0.425471, -0.256563, -0.280998, -0.518363, -0.167552])

	names.append("LAnkleRoll")
	times.append([0.96, 1.52, 2.12, 2.68, 3.28, 3.84, 4.44, 5])
	keys.append([-0.137881, -0.0558505, -0.165806, -0.0268008, 0.0279253, 0.0558505, 0.179769, 0.219911])

	names.append("LElbowRoll")
	times.append([0.92, 1.48, 2.08, 2.64, 3.24, 3.8, 4.4, 4.96])
	keys.append([-1.06149, -0.455555, -0.952573, -0.492371, -1.06149, -0.83147, -1.36837, -1.14594])

	names.append("LElbowYaw")
	times.append([0.92, 1.48, 2.08, 2.64, 3.24, 3.8, 4.4, 4.96])
	keys.append([-1.6629, -0.918907, 0.075124, -0.553816, -1.6629, -0.941834, -0.523053, -2.08007])

	names.append("LHand")
	times.append([0.84, 2, 3.72])
	keys.append([0.295298, 0.295298, 0.296389])

	names.append("LHipPitch")
	times.append([0.96, 1.52, 2.12, 2.68, 3.28, 3.84, 4.44, 5])
	keys.append([-0.168712, -0.329782, 0.0567862, 0.262342, -0.185867, 0.107127, -0.139847, 0.186895])

	names.append("LHipRoll")
	times.append([0.96, 1.52, 2.12, 2.68, 3.28, 3.84, 4.44, 5])
	keys.append([0.39235, 0.226678, 0.16225, 0.0870839, -0.0496235, -0.419317, -0.345685, -0.255179])

	names.append("LHipYawPitch")
	times.append([0.96, 1.52, 2.12, 2.68, 3.28, 3.84, 4.44, 5])
	keys.append([-0.391128, -0.340507, -0.303691, -0.354312, -0.483168, -0.391128, -0.340507, -0.303691])

	names.append("LKneePitch")
	times.append([0.96, 1.52, 2.12, 2.68, 3.28, 3.84, 4.44, 5])
	keys.append([1.14373, 1.33343, 0.497419, 0.494848, 0.699619, 0.540082, 1.00949, 0.268564])

	names.append("LShoulderPitch")
	times.append([0.92, 1.48, 2.08, 2.64, 3.24, 3.8, 4.4, 4.96])
	keys.append([1.3913, 2.05704, 2.0944, 1.73491, 1.3913, 1.40058, 0.704148, 0.808459])

	names.append("LShoulderRoll")
	times.append([0.92, 1.48, 2.08, 2.64, 3.24, 3.8, 4.4, 4.96])
	keys.append([0.481634, 0.51845, 0.461692, 0.719404, 0.481634, 0.01078, 0.016916, 0.00771196])

	names.append("LWristYaw")
	times.append([0.84, 2, 3.72])
	keys.append([0.676451, 0.839057, 0.118076])

	names.append("RAnklePitch")
	times.append([0.96, 1.52, 2.12, 2.68, 3.28, 3.84, 4.44, 5])
	keys.append([-0.293215, -0.518363, -0.207637, -0.456145, -0.293215, -0.670206, -0.681649, -0.305433])

	names.append("RAnkleRoll")
	times.append([0.96, 1.52, 2.12, 2.68, 3.28, 3.84, 4.44, 5])
	keys.append([-0.0558505, -0.137881, -0.151844, 0.0278439, 0.0139626, 0.137881, 0.109637, 0.179769])

	names.append("RElbowRoll")
	times.append([0.92, 1.48, 2.08, 2.64, 3.24, 3.8, 4.4, 4.96])
	keys.append([0.980268, 0.83147, 1.36837, 1.14594, 0.980268, 0.455555, 0.952573, 0.492371])

	names.append("RElbowYaw")
	times.append([0.92, 1.48, 2.08, 2.64, 3.24, 3.8, 4.4, 4.96])
	keys.append([2.08007, 0.941834, 0.523053, 2.08007, 2.08007, 0.918907, -0.075124, 0.553816])

	names.append("RHand")
	times.append([0.84, 2, 3.72])
	keys.append([0.340389, 0.340389, 0.340753])

	names.append("RHipPitch")
	times.append([0.96, 1.52, 2.12, 2.68, 3.28, 3.84, 4.44, 5])
	keys.append([0.107127, -0.139847, 0.186895, 0.21144, -0.13343, -0.168712, -0.329782, 0.0567862])

	names.append("RHipRoll")
	times.append([0.96, 1.52, 2.12, 2.68, 3.28, 3.84, 4.44, 5])
	keys.append([0.419317, 0.345685, 0.255179, -0.131389, 0.0555781, -0.39235, -0.226678, -0.16225])

	names.append("RKneePitch")
	times.append([0.96, 1.52, 2.12, 2.68, 3.28, 3.84, 4.44, 5])
	keys.append([0.540082, 1.00949, 0.268564, 0.561558, 0.671257, 1.14373, 1.33343, 0.497419])

	names.append("RShoulderPitch")
	times.append([0.92, 1.48, 2.08, 2.64, 3.24, 3.8, 4.4, 4.96])
	keys.append([1.40979, 1.40058, 0.704148, 0.808459, 1.40979, 2.05704, 2.0944, 1.73491])

	names.append("RShoulderRoll")
	times.append([0.92, 1.48, 2.08, 2.64, 3.24, 3.8, 4.4, 4.96])
	keys.append([-0.401949, -0.01078, -0.016916, -0.00771196, -0.401949, -0.51845, -0.461692, -0.719404])

	names.append("RWristYaw")
	times.append([0.84, 2, 3.72])
	keys.append([-0.421891, 0.604353, -0.366667])

	try:
		motion = ALProxy("ALMotion", robotIP, port)
		motion.angleInterpolation(names, keys, times, True)
	except BaseException, err:
		print err

if __name__ == "__main__":
	robotIP = "127.0.0.1"
	port = 9559

	if len(sys.argv) <= 1:
		print "(robotIP default: 127.0.0.1)"
	elif len(sys.argv) <= 2:
		robotIP = sys.argv[1]
	else:
		port = int(sys.argv[2])
		robotIP = sys.argv[1]

	main(robotIP, port)
