# Choregraphe simplified export in Python.
from naoqi import ALProxy
import sys

def main(robotIP, port):
	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([0.64, 1.16, 1.64, 2.16, 2.64, 3.16, 3.64, 5])
	keys.append([-0.0782759, -0.50166, -0.0782759, -0.50166, -0.0782759, -0.50166, -0.656595, -0.0245859])

	names.append("HeadYaw")
	times.append([0.64, 1.16, 1.64, 2.16, 2.64, 3.16, 3.64, 5])
	keys.append([-0.0859459, -0.0706059, -0.0859459, -0.0706059, -0.0859459, -0.0706059, -0.0782759, 0.00609404])

	names.append("LAnklePitch")
	times.append([0.72, 1.72, 3.24, 3.72, 5])
	keys.append([-0.0910584, -0.298148, -0.298148, -0.293215, -0.104485])

	names.append("LAnkleRoll")
	times.append([0.72, 1.72, 3.24, 3.72, 5])
	keys.append([-0.0329368, 0.0192192, 0.0192192, 0.0667732, 0.0092244])

	names.append("LElbowRoll")
	times.append([0.68, 1.2, 1.68, 2.2, 2.68, 3.2, 3.68, 5])
	keys.append([0, -0.612024, 0, -0.612024, 0, -0.612024, -0.523053, -0.326699])

	names.append("LElbowYaw")
	times.append([0.68, 1.2, 1.68, 2.2, 2.68, 3.2, 3.68, 5])
	keys.append([-0.420357, -0.374338, -0.420357, -0.374338, -0.420357, -0.374338, -0.819198, -0.759372])

	names.append("LHand")
	times.append([1.12, 3.12, 4.12, 5])
	keys.append([0.796751, 0.796751, 0.295298, 0.918933])

	names.append("LHipPitch")
	times.append([0.72, 1.72, 3.24, 3.72, 5])
	keys.append([0.340577, 0.25774, 0.25774, -0.13343, 0.0596046])

	names.append("LHipRoll")
	times.append([0.72, 1.72, 3.24, 3.72, 5])
	keys.append([0.090152, 0.0671419, 0.0671419, -0.0555781, -0.0324061])

	names.append("LHipYawPitch")
	times.append([0.72, 1.72, 3.24, 3.72, 5])
	keys.append([-0.360449, -0.384992, -0.384992, -0.483168, 0.0183645])

	names.append("LKneePitch")
	times.append([0.72, 1.72, 3.24, 3.72, 5])
	keys.append([0.0714636, 0.405876, 0.405876, 0.671257, 0.0702441])

	names.append("LShoulderPitch")
	times.append([0.68, 1.2, 1.68, 2.2, 2.68, 3.2, 3.68, 5])
	keys.append([-1.05237, -0.823801, -1.05237, -0.823801, -1.05237, -0.823801, -0.510863, 1.56771])

	names.append("LShoulderRoll")
	times.append([0.68, 1.2, 1.68, 2.2, 2.68, 3.2, 3.68, 5])
	keys.append([0.432547, 0.0352401, 0.432547, 0.0352401, 0.432547, 0.0352401, 0.507713, 0.329768])

	names.append("LWristYaw")
	times.append([1.12, 3.12, 4.12, 5])
	keys.append([-1.30394, -1.30394, 0.676451, -1.02629])

	names.append("RAnklePitch")
	times.append([0.72, 1.72, 3.24, 3.72, 5])
	keys.append([-0.0787807, -0.292008, -0.292008, -0.256563, -0.0951351])

	names.append("RAnkleRoll")
	times.append([0.72, 1.72, 3.24, 3.72, 5])
	keys.append([0.165806, 0.0680678, 0.0558505, -0.0933421, -0.00302827])

	names.append("RElbowRoll")
	times.append([0.68, 1.2, 1.68, 2.2, 2.68, 3.2, 3.68, 5])
	keys.append([4.19617e-05, 0.656595, 4.19617e-05, 0.656595, 4.19617e-05, 0.656595, 0.598302, 0.291501])

	names.append("RElbowYaw")
	times.append([0.68, 1.2, 1.68, 2.2, 2.68, 3.2, 3.68, 5])
	keys.append([0.233125, 0.170232, 0.233125, 0.170232, 0.233125, 0.170232, 0.984786, 0.77923])

	names.append("RHand")
	times.append([1.12, 3.12, 4.12, 5])
	keys.append([0.849115, 0.849115, 0.340389, 0.918205])

	names.append("RHipPitch")
	times.append([0.72, 1.72, 3.24, 3.72, 5])
	keys.append([0.355635, 0.26973, 0.26973, -0.185867, 0.0367591])

	names.append("RHipRoll")
	times.append([0.72, 1.72, 3.24, 3.72, 5])
	keys.append([-0.119116, -0.0853684, -0.0853684, 0.0496235, 0.0107584])

	names.append("RKneePitch")
	times.append([0.72, 1.72, 3.24, 3.72, 5])
	keys.append([0.0476684, 0.388217, 0.388217, 0.699619, 0.0839559])

	names.append("RShoulderPitch")
	times.append([0.68, 1.2, 1.68, 2.2, 2.68, 3.2, 3.68, 5])
	keys.append([-1.11978, -0.926494, -1.11978, -0.926494, -1.11978, -0.926494, -0.404934, 1.56779])

	names.append("RShoulderRoll")
	times.append([0.68, 1.2, 1.68, 2.2, 2.68, 3.2, 3.68, 5])
	keys.append([-0.454107, -0.0245859, -0.454107, -0.0245859, -0.454107, -0.0245859, -0.604437, -0.320648])

	names.append("RWristYaw")
	times.append([1.12, 3.12, 4.12, 5])
	keys.append([1.31153, 1.31153, -0.421891, 0.967912])

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
