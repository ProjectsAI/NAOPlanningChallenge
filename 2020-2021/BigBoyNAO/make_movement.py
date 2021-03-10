from naoqi import ALProxy
import exported_poses
import sys

NAO_IP = sys.argv[1]
PORT = int(sys.argv[2])
print(NAO_IP)
print(PORT)

#NAO_IP = "127.0.0.1"
#PORT = 37439

plan = []
f = open("choreography.txt", "r")
for x in f:
    plan.append(x.rstrip())
f.close()
print(plan)
#plan = ["Workout"]
predefined_poses = ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "SitRelax"]
all_possible_poses = ["StandInit", "StandZero", "Stand", "Crouch", "Sit", "SitRelax",
                      "WipeForehead","Guitar","DiagonalRight","RotationRightFoot",
                        "RotationLeftFoot","RotationHandgunObject","RotationRightArm",
                        "DoubleMovement","ArmsOpening","UnionArms","MoveForward","MoveBackward",
                        "DiagonalLeft","HappyBirthday","Workout","SprinklerLeft","SprinklerRight","Hello"]
#plan = all_possible_poses

posture = ALProxy("ALRobotPosture", NAO_IP, PORT)
player = ALProxy("ALAudioPlayer", NAO_IP, PORT)
motion = ALProxy("ALMotion", NAO_IP, PORT)

song = player.post.playFile("/home/nao/PycharmProjects/project/YBBN.wav", 0.5, -1.0)


for i in range(len(plan)):

    pose = plan[i]
    print(pose)

    if pose not in predefined_poses:
        specific_func = exported_poses.pose_to_func(pose)
        specific_func(motion, NAO_IP, PORT)

    else:
        posture.applyPosture(pose, 3.0)

player.stop(song)
