# Choregraphe simplified export in Python.
from naoqi import ALProxy
import sys

def main(robotIP, port):
	names = list()
	times = list()
	keys = list()

	names.append("HeadPitch")
	times.append([1, 3, 4.06667, 5.26667, 7.26667, 8.33333])
	keys.append([-0.01078, -0.01078, -0.112024, -0.01078, -0.01078, -0.112024])

	names.append("HeadYaw")
	times.append([1, 3, 4.06667, 5.26667, 7.26667, 8.33333])
	keys.append([0.010696, 0.010696, 0.338973, 0.010696, 0.010696, 0.338973])

	names.append("LAnklePitch")
	times.append([1.2, 5.46667])
	keys.append([-0.359129, -0.359129])

	names.append("LAnkleRoll")
	times.append([1.2, 5.46667])
	keys.append([-0.0797476, -0.0797476])

	names.append("LElbowRoll")
	times.append([1, 1.66667, 3, 3.53333, 4.06667, 5.26667, 5.93333, 7.26667, 7.8, 8.33333])
	keys.append([-1.56617, -0.658043, -1.56617, -0.658043, -0.305225, -1.56617, -0.658043, -1.56617, -0.658043, -0.305225])

	names.append("LElbowYaw")
	times.append([1, 1.66667, 3, 3.53333, 4.06667, 5.26667, 5.93333, 7.26667, 7.8, 8.33333])
	keys.append([-0.624379, -1.26866, -0.624379, -1.26866, -2.07862, -0.624379, -1.26866, -0.624379, -1.26866, -2.07862])

	names.append("LHand")
	times.append([1, 1.66667, 3, 3.53333, 4.06667, 5.26667, 5.93333, 7.26667, 7.8, 8.33333])
	keys.append([0.917114, 1, 0.917114, 1, 0.997478, 0.917114, 1, 0.917114, 1, 0.997478])

	names.append("LHipPitch")
	times.append([1.2, 5.46667])
	keys.append([-0.27941, -0.27941])

	names.append("LHipRoll")
	times.append([1.2, 5.46667])
	keys.append([0.168548, 0.168548])

	names.append("LHipYawPitch")
	times.append([1.2, 5.46667])
	keys.append([-0.170318, -0.170318])

	names.append("LKneePitch")
	times.append([1.2, 5.46667])
	keys.append([0.680776, 0.680776])

	names.append("LShoulderPitch")
	times.append([1, 1.66667, 3, 3.53333, 4.06667, 5.26667, 5.93333, 7.26667, 7.8, 8.33333])
	keys.append([0.496974, 0.225456, 0.496974, 0.225456, 0.4034, 0.496974, 0.225456, 0.496974, 0.225456, 0.4034])

	names.append("LShoulderRoll")
	times.append([1, 1.66667, 3, 3.53333, 4.06667, 5.26667, 5.93333, 7.26667, 7.8, 8.33333])
	keys.append([0, 0.05058, 0, 0.05058, 0.77923, 0, 0.05058, 0, 0.05058, 0.77923])

	names.append("LWristYaw")
	times.append([1, 1.66667, 3, 3.53333, 4.06667, 5.26667, 5.93333, 7.26667, 7.8, 8.33333])
	keys.append([-1.00941, -1.00941, -1.00941, -1.00941, -1.01095, -1.00941, -1.00941, -1.00941, -1.00941, -1.01095])

	names.append("RAnklePitch")
	times.append([1.2, 5.46667])
	keys.append([-0.184108, -0.184108])

	names.append("RAnkleRoll")
	times.append([1.2, 5.46667])
	keys.append([0.0675357, 0.0675357])

	names.append("RElbowRoll")
	times.append([1, 1.66667, 3, 3.53333, 4.06667, 5.26667, 5.93333, 7.26667, 7.8, 8.33333])
	keys.append([0.504728, 0.431096, 0.504728, 0.431096, 0.596768, 0.504728, 0.431096, 0.504728, 0.431096, 0.596768])

	names.append("RElbowYaw")
	times.append([1, 1.66667, 3, 3.53333, 4.06667, 5.26667, 5.93333, 7.26667, 7.8, 8.33333])
	keys.append([0.42641, 0.41107, 0.42641, 0.41107, 0.196309, 0.42641, 0.41107, 0.42641, 0.41107, 0.196309])

	names.append("RHand")
	times.append([1, 3, 4.06667, 5.26667, 7.26667, 8.33333])
	keys.append([0.630909, 0.630909, 0.572727, 0.630909, 0.630909, 0.572727])

	names.append("RHipPitch")
	times.append([1.2, 5.46667])
	keys.append([-0.336004, -0.336004])

	names.append("RHipRoll")
	times.append([1.2, 5.46667])
	keys.append([0.0015544, 0.0015544])

	names.append("RKneePitch")
	times.append([1.2, 5.46667])
	keys.append([0.556428, 0.556428])

	names.append("RShoulderPitch")
	times.append([1, 1.66667, 3, 3.53333, 4.06667, 5.26667, 5.93333, 7.26667, 7.8, 8.33333])
	keys.append([1.14441, 1.10912, 1.14441, 1.10912, 1.27173, 1.14441, 1.10912, 1.14441, 1.10912, 1.27173])

	names.append("RShoulderRoll")
	times.append([1, 1.66667, 3, 3.53333, 4.06667, 5.26667, 5.93333, 7.26667, 7.8, 8.33333])
	keys.append([-0.271559, -0.253151, -0.271559, -0.253151, -0.579894, -0.271559, -0.253151, -0.271559, -0.253151, -0.579894])

	names.append("RWristYaw")
	times.append([1, 3, 4.06667, 5.26667, 7.26667, 8.33333])
	keys.append([0.958708, 0.958708, 0.944902, 0.958708, 0.958708, 0.944902])

	try:
		ttsProxy = ALProxy("ALTextToSpeech", robotIP, port)
		motion = ALProxy("ALMotion", robotIP, port)
		motion.angleInterpolation(names, keys, times, True)
		ttsProxy.say("You're amazing!")
	except BaseException, err:
		print err
	
	try:
		postureProxy = ALProxy("ALRobotPosture", robotIP, port)
		postureProxy.goToPosture("Stand", 0.5)
	except  Exception, e:
		print "Could not create proxy to ALRobotPosture"
	

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
