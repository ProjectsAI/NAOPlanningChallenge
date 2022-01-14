from naoqi import ALProxy
import Poses_names
import sys

ballet = []
#open text file with choreography
file = open("ballet.txt", "r")

#for loop on file to append all steps in an array
for f in file:
    ballet.append(f.rstrip())
file.close()
print(ballet)

initial_steps = ["Crouch","StandZero", "Stand", "StandInit", "Sit", "SitRelax"]
all_possible_poses = ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "SitRelax",
                      "WipeForehead","Guitar","DiagonalRight","RotationRightFoot",
                        "RotationLeftFoot","RotationHandgunObject","RotationRightArm",
                        "DoubleMovement","ArmsOpening","UnionArms","MoveForward","MoveBackward",
                        "DiagonalLeft","HappyBirthday","Workout","SprinklerLeft","SprinklerRight","Hello"]

#nao ip and port
NAOIP = "127.0.0.1"
PORT =44237
robot_pst = ALProxy("ALRobotPosture", NAOIP, PORT)
audio = ALProxy("ALAudioPlayer", NAOIP, PORT)
movement = ALProxy("ALMotion", NAOIP, PORT)

#music file
music = audio.post.playFile("/home/nao/Scrivania/SML/bensound-ukulele.wav", 0.5, -1.0)


for i in range(len(ballet)):
    step = ballet[i]
    print(step)
    if step not in initial_steps:
        mtd_move = Poses_names.func_steps(step)
        mtd_move(movement, NAOIP, PORT)
    else:
        robot_pst.applyPosture(step, 3.0)
audio.stop(music)
