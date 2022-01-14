import os
import time
import imp
import json
import argparse
from naoqi import ALProxy

parser = argparse.ArgumentParser(description='Argument parser')
parser.add_argument('--IP_ADDRESS', type=str, default='127.0.0.1')
parser.add_argument('--PORT', type=str, default=34719)
args = parser.parse_args()

def main(arguments):
    robotIP = arguments.IP_ADDRESS
    robotPort = int(arguments.PORT)

    audio = ALProxy("ALAudioPlayer", robotIP, robotPort)
    motion = ALProxy("ALMotion", robotIP, robotPort)
    posture = ALProxy("ALRobotPosture", robotIP, robotPort)

    fileName = "movement_times.json"
    if not(os.path.exists(fileName)):
        movementsDict = {}
        Path = 'RobotPositions/'
        for Position in os.listdir(os.path.dirname(Path)):
            if Position == '__init__.py' or Position[-3:] != '.py':
                continue
            ModuleName = Position[:-3]
            Module = imp.load_source(ModuleName, Path + Position)
            prev_time = time.time()
            Module.main(robotIP, robotPort)
            current_time = time.time()
            movementsDict[ModuleName] = current_time - prev_time

        with open(fileName, 'w') as f:
            json.dump(movementsDict, f)

if __name__ == "__main__":
    main(args)
