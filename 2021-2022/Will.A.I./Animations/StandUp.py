import sys
import time

from naoqi import ALProxy


def main(robotIP, port):
	nTries = 3
	postureProxy = ALProxy("ALRobotPosture", robotIP, port)
	postureProxy.setMaxTryNumber(nTries)

	postureProxy.goToPosture("Stand", 1.0)

  
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

	start = time.time()
	main(robotIP, port)
	end = time.time()
	print ("%.2f seconds elapsed" % (end-start))
