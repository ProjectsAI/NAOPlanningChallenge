import argparse
from naoqi import ALProxy
import imp
from pygame import mixer

parser = argparse.ArgumentParser(description='Argument parser')
parser.add_argument('--IP_ADDRESS', type=str, default='127.0.0.1')
parser.add_argument('--PORT', type=str, default=34719)
parser.add_argument('--SONG', type=str, default='Poker Face')
args = parser.parse_args()

def main(arguments):
    ipAddress = arguments.IP_ADDRESS
    port = int(arguments.PORT)
    song = arguments.SONG

    motion = ALProxy("ALMotion", ipAddress, port)
    posture = ALProxy("ALRobotPosture", ipAddress, port)

    motion.wakeUp()
    posture.goToPosture("StandInit", 1)

    songFile = "Songs/" + song + ".mp3"
    mixer.init()
    mixer.music.load(songFile)
    mixer.music.play()

    moves = []
    file = open("GeneratedDanceMoves.txt", "r")
    for i in file:
        moves.append(i.rstrip())
    file.close()

    for i in range(len(moves)):
        move = moves[i]
        module = imp.load_source(move, 'RobotPositions/' + move + '.py')
        module.main(ipAddress, port)

if __name__ == "__main__":
    main(args)
