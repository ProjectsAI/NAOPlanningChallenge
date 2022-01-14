from naoqi import ALProxy
import sys
import time

def main(robotIP, port):

	print "Let's play some music!"
	
	aup = ALProxy("ALAudioPlayer", robotIP, port)
	aup.post.playFile("/home/nao/PycharmProjects/Don_t_Stop_Me_NAO/music/bee_gees_stayin_alive.wav")

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