import motion
import almath
import time
from naoqi import ALProxy


def func_steps(stp):

    list_steps = {
        "Hello": Hello,
        "WipeForehead": Wipe_Forehead,
        "DiagonalRight": Diagonal_Right,
        "RotationRightFoot": Rotation_right_foot,
        "MoveForward": Move_forward,
        "RotationLeftFoot": Rotation_left_foot,
        "HappyBirthday": Happy_birthday,
        "RotationRightArm" : Right_arm,
        "DoubleMovement" : Double_movement,
        "ArmsOpening" : Arms_opening,
        "RotationHandgunObject": Rotation_handgun_object,
        "UnionArms" : Union_arms,
        "Guitar": Guitar_modified,
        "MoveBackward": Move_backward,
        "DiagonalLeft": Diagonal_left,
        "Workout": Workout,
        "SprinklerLeft": Sprinkler_left,
        "SprinklerRight": Sprinkler_right
    }
    steps = list_steps.get(stp, lambda: "No step")
    return steps


def Guitar_modified(motion, NAO_IP, PORT):

    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.26667, 2.8, 3, 3.53333, 3.8, 4.46667, 4.66667, 5.26667, 5.46667])
    keys.append([0.0797261, -0.055266, 0.191709, -0.055266, 0.191709, -0.055266, 0.191709, -0.055266, 0.191709])

    names.append("HeadYaw")
    times.append([1.26667, 2.8, 3, 3.53333, 3.8, 4.46667, 4.66667, 5.26667, 5.46667])
    keys.append([-0.108956, -0.20253, -0.176453, -0.20253, -0.176453, -0.20253, -0.176453, -0.20253, -0.176453])

    names.append("LAnklePitch")
    times.append([1.26667, 1.66667])
    keys.append([-0.374338, -0.374338])

    names.append("LAnkleRoll")
    times.append([1.26667, 1.66667])
    keys.append([0.016916, 0.016916])

    names.append("LElbowRoll")
    times.append([1.26667, 1.93333, 2.13333, 2.33333, 2.8, 3, 3.53333, 3.8, 4.46667, 4.66667, 5.26667, 5.46667])
    keys.append(
        [-1.03541, -1.05688, -1.05688, -1.04461, -1.05688, -1.04461, -1.05688, -1.04461, -1.05688, -1.04461, -1.05688,
         -1.04461])

    names.append("LElbowYaw")
    times.append([1.26667, 1.93333, 2.13333, 2.33333, 2.8, 3, 3.53333, 3.8, 4.46667, 4.66667, 5.26667, 5.46667])
    keys.append(
        [-1.76261, -1.75341, -1.75495, -1.75034, -1.75495, -1.75034, -1.75495, -1.75034, -1.75495, -1.75034, -1.75495,
         -1.75034])

    names.append("LHand")
    times.append([1.26667])
    keys.append([0.920024])

    names.append("LHipPitch")
    times.append([1.26667, 1.66667])
    keys.append([-0.162562, -0.162562])

    names.append("LHipRoll")
    times.append([1.26667, 1.66667])
    keys.append([0.101286, 0.101286])

    names.append("LHipYawPitch")
    times.append([1.26667, 1.66667])
    keys.append([-0.395731, -0.395731])

    names.append("LKneePitch")
    times.append([1.26667, 1.66667])
    keys.append([0.789967, 0.789967])

    names.append("LShoulderPitch")
    times.append([1.26667, 1.93333, 2.13333, 2.33333, 2.8, 3, 3.53333, 3.8, 4.46667, 4.66667, 5.26667, 5.46667])
    keys.append(
        [0.745483, 0.733209, 0.743948, 0.760822, 0.743948, 0.760822, 0.743948, 0.760822, 0.743948, 0.760822, 0.743948,
         0.760822])

    names.append("LShoulderRoll")
    times.append([1.26667, 1.93333, 2.33333, 3, 3.8, 4.66667, 5.46667])
    keys.append([0.515382, 0.516916, 0.501576, 0.501576, 0.501576, 0.501576, 0.501576])

    names.append("LWristYaw")
    times.append([1.26667])
    keys.append([-1.01862])

    names.append("RAnklePitch")
    times.append([1.26667, 1.66667])
    keys.append([-0.207048, -0.207048])

    names.append("RAnkleRoll")
    times.append([1.26667, 1.66667])
    keys.append([0.032256, 0.032256])

    names.append("RElbowRoll")
    times.append([1.26667, 1.93333, 2.13333, 2.33333, 2.8, 3, 3.53333, 3.8, 4.46667, 4.66667, 5.26667, 5.46667])
    keys.append([1.03242, 0.523136, 1.22264, 0.681137, 1.22264, 0.681137, 1.22264, 0.681137, 1.22264, 0.681137, 1.22264,
                 0.681137])

    names.append("RElbowYaw")
    times.append([1.26667, 1.93333, 2.13333, 2.33333, 2.8, 3, 3.53333, 3.8, 4.46667, 4.66667, 5.26667, 5.46667])
    keys.append(
        [0.265341, -0.029188, 0.408002, -0.138102, 0.408002, -0.138102, 0.408002, -0.138102, 0.408002, -0.138102,
         0.408002, -0.138102])

    names.append("RHand")
    times.append([1.26667, 1.93333])
    keys.append([0.918933, 0.452752])

    names.append("RHipPitch")
    times.append([1.26667, 1.66667])
    keys.append([-0.032256, -0.032256])

    names.append("RHipRoll")
    times.append([1.26667, 1.66667])
    keys.append([-0.016832, -0.016832])

    names.append("RKneePitch")
    times.append([1.26667, 1.66667])
    keys.append([0.55535, 0.55535])

    names.append("RShoulderPitch")
    times.append([1.26667, 1.93333, 2.13333, 2.33333, 2.8, 3, 3.53333, 3.8, 4.46667, 4.66667, 5.26667, 5.46667])
    keys.append(
        [0.906636, 0.868286, 0.92351, 0.935783, 0.92351, 0.935783, 0.92351, 0.935783, 0.92351, 0.935783, 0.92351,
         0.935783])

    names.append("RShoulderRoll")
    times.append([1.26667, 1.93333, 2.13333, 2.33333, 2.8, 3, 3.53333, 3.8, 4.46667, 4.66667, 5.26667, 5.46667])
    keys.append(
        [-0.185656, -0.101286, -0.0782759, -0.16418, -0.0782759, -0.16418, -0.0782759, -0.16418, -0.0782759, -0.16418,
         -0.0782759, -0.16418])

    names.append("RWristYaw")
    times.append([1.26667, 1.93333])
    keys.append([0.961776, 0.682588])

    try:
        motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print
        err


def Wipe_Forehead(motion, NAO_IP, PORT):
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.96, 1.68, 3.28, 3.96, 4.52, 5.08])
    keys.append([-0.0261199, 0.427944, 0.308291, 0.11194, -0.013848, 0.061318])

    names.append("HeadYaw")
    times.append([0.96, 1.68, 3.28, 3.96, 4.52, 5.08])
    keys.append([-0.234743, -0.622845, -0.113558, -0.00617796, -0.027654, -0.036858])

    names.append("LElbowRoll")
    times.append([0.8, 1.52, 3.12, 3.8, 4.36, 4.92])
    keys.append([-0.866668, -0.868202, -0.822183, -0.992455, -0.966378, -0.990923])

    names.append("LElbowYaw")
    times.append([0.8, 1.52, 3.12, 3.8, 4.36, 4.92])
    keys.append([-0.957257, -0.823801, -1.00788, -0.925044, -1.24412, -0.960325])

    names.append("LHand")
    times.append([1.52, 3.12, 3.8, 4.92])
    keys.append([0.132026, 0.132026, 0.132026, 0.132026])

    names.append("LShoulderPitch")
    times.append([0.8, 1.52, 3.12, 3.8, 4.36, 4.92])
    keys.append([0.863599, 0.858999, 0.888144, 0.929562, 1.017, 0.977116])

    names.append("LShoulderRoll")
    times.append([0.8, 1.52, 3.12, 3.8, 4.36, 4.92])
    keys.append([0.286815, 0.230059, 0.202446, 0.406468, 0.360449, 0.31903])

    names.append("LWristYaw")
    times.append([1.52, 3.12, 3.8, 4.92])
    keys.append([0.386526, 0.386526, 0.386526, 0.386526])

    names.append("RElbowRoll")
    times.append([0.64, 1.36, 2.96, 3.64, 4.2, 4.76])
    keys.append([1.28093, 1.39752, 1.57239, 1.24105, 1.22571, 0.840674])

    names.append("RElbowYaw")
    times.append([0.64, 1.36, 2.96, 3.64, 4.2, 4.76])
    keys.append([-0.128898, -0.285367, -0.15651, 0.754686, 1.17193, 0.677985])

    names.append("RHand")
    times.append([1.36, 2.96, 3.64, 4.76])
    keys.append([0.166571, 0.166208, 0.166571, 0.166208])

    names.append("RShoulderPitch")
    times.append([0.64, 1.36, 2.96, 3.64, 4.2, 4.76])
    keys.append([0.0767419, -0.59515, -0.866668, -0.613558, 0.584497, 0.882091])

    names.append("RShoulderRoll")
    times.append([0.64, 1.36, 2.96, 3.64, 4.2, 4.76])
    keys.append([-0.019984, -0.019984, -0.615176, -0.833004, -0.224006, -0.214801])

    names.append("RWristYaw")
    times.append([1.36, 2.96, 3.64, 4.76])
    keys.append([-0.058334, -0.0521979, -0.067538, -0.038392])

    try:

        motion.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print err


def Diagonal_Right(motion, NAO_IP, PORT):


    distance_x_m = 0.03
    distance_y_m = -0.012
    theta_deg = 0.0
    # The command position estimation will be set to the sensor position when the robot starts moving, so we use sensors first and commands later.
    initPosition = almath.Pose2D(motion.getRobotPosition(True))
    targetDistance = almath.Pose2D(distance_x_m, distance_y_m, theta_deg * almath.PI / 180)
    #expectedEndPosition = initPosition * targetDistance
    enableArms = 0
    motion.setMoveArmsEnabled(enableArms, enableArms)
    motion.moveTo(distance_x_m, distance_y_m, theta_deg)

def StiffnessOn(proxy):

    # We use the "Body" name to signify the collection of all joints

    pNames = "Body"

    pStiffnessLists = 1.0

    pTimeLists = 0.1

    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)

def Rotation_right_foot(motionProxy, NAO_IP, PORT):

    try:

        postureProxy = ALProxy("ALRobotPosture", NAO_IP, PORT)

    except Exception, e:

        print
        "Could not create proxy to ALRobotPosture"

        print
        "Error was: ", e

    StiffnessOn(motionProxy)

    postureProxy.goToPosture("StandInit", 1.0)

    motionProxy.wbEnable(True)

    # Legs/Feet Configuration

    stateName = "Plane"

    supportLeg = "RLeg"

    motionProxy.wbEnable(True)

    # Legs/Feet Configuration

    stateName = "Plane"

    supportLeg = "RLeg"

    motionProxy.wbFootState(stateName, supportLeg)

    stateName = "Fixed"

    supportLeg = "LLeg"

    motionProxy.wbFootState(stateName, supportLeg)

    # Cartesian foot trajectory

    # Warning: Needs a PoseInit before executing

    space = motion.FRAME_ROBOT

    axisMask = 63  # control all the effector's axes

    isAbsolute = False

    # Lower the Torso and move to the side

    effector = "Torso"

    path = [0.0, 0.00, 0.00, 0.0, 0.0, 0.05]

    timeList = 0.5  # seconds

    motionProxy.positionInterpolation(effector, space, path,

                                      axisMask, timeList, isAbsolute)

    time.sleep(1)

    # Back to the initial position

    postureProxy.goToPosture("StandInit", 3.0)

    motionProxy.wbEnable(False)



def Rotation_handgun_object(motionProxy, NAO_IP, PORT):

    RShoulderPitch = 67.7

    RShoulderRoll = -26.4

    RElbowYaw = 90.9

    RElbowRoll = 88.5

    RWristYaw = 80

    RHand = 0.35

    LShoulderPitch = 78.0

    LShoulderRoll = 16.6

    LElbowYaw = -68.3

    LElbowRoll = -49.2

    LWristYaw = 4.3

    LHand = 0.0

    names = "LArm"

    angleLists = [LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,

                  LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand * almath.TO_RAD]

    timeLists = 0.5

    motionProxy.post.angleInterpolation(names, angleLists, timeLists, True)

    names = "RArm"

    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,

                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD]

    timeLists = 0.5

    motionProxy.post.angleInterpolation(names, angleLists, timeLists, True)

    #time.sleep(1)

    # Open RHand
    RHandAngle = 0.90

    names = "RHand"
    angleLists = [RHandAngle]
    timeLists = 0.5
    motionProxy.angleInterpolation(names, angleLists, timeLists, True)

    #time.sleep(1)

    # Close RHand
    names = "RHand"
    timeLists = 0.5
    RHandAngle = 0.05
    angleLists = [RHandAngle]
    motionProxy.angleInterpolation(names, angleLists, timeLists, True)


def Right_arm(motionProxy, NAO_IP, PORT):

    RShoulderPitch = 78.0

    RShoulderRoll = -16.6

    RElbowYaw = 68.3

    RElbowRoll = 49.2

    RWristYaw = 4.3

    RHand = 0.10

    LShoulderPitch = 78.0

    LShoulderRoll = 16.6

    LElbowYaw = -68.3

    LElbowRoll = -49.2

    LWristYaw = 4.3

    LHand = 0.0

    names = "LArm"

    angleLists = [LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,

                  LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand]

    timeLists = 0.5

    motionProxy.post.angleInterpolation(names, angleLists, timeLists, True)

    names = "RArm"

    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,

                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand]

    timeLists = 0.5

    motionProxy.angleInterpolation(names, angleLists, timeLists, True)

    # Not waiting because movement is fluid and without pause

    ########## Movement arms ###########

    # Open/extend RArm

    RShoulderPitch = -75.7

    RShoulderRoll = -79.8

    RElbowYaw = -57.6

    RElbowRoll = 2.2

    RWristYaw = 87.0

    RHand = 0.35

    names = "RArm"

    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,

                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD]

    motionProxy.setAngles(names, angleLists, 0.1)

    time.sleep(2)

    # Raise RArm sideways

    RShoulderPitch = -79.8

    RShoulderRoll = -26.2

    RElbowYaw = -57.6

    RElbowRoll = 2.2

    RWristYaw = 87.0

    RHand = 0.35

    names = "RArm"

    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,

                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD]

    motionProxy.setAngles(names, angleLists, 0.15)

    time.sleep(1)

    # Align RShoulder and move forward RArm

    RShoulderPitch = 11.0

    RShoulderRoll = 5.4

    RElbowYaw = 68.3

    RElbowRoll = 2.2

    RWristYaw = 88.5

    RHand = 0.35

    names = "RArm"

    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,

                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD]

    timeLists = 0.5

    motionProxy.angleInterpolation(names, angleLists, timeLists, True)

def Rotation_left_foot(motionProxy, NAO_IP, PORT):
    try:

        postureProxy = ALProxy("ALRobotPosture", NAO_IP, PORT)

    except Exception, e:

        print
        "Could not create proxy to ALRobotPosture"

        print
        "Error was: ", e

        # Set NAO in Stiffness On

    StiffnessOn(motionProxy)

    # Send NAO to Pose Init

    postureProxy.goToPosture("StandInit", 1.0)

    motionProxy.wbEnable(True)

    # Legs/Feet configuration

    stateName = "Fixed"

    supportLeg = "RLeg"

    motionProxy.wbFootState(stateName, supportLeg)

    stateName = "Plane"

    supportLeg = "LLeg"

    motionProxy.wbFootState(stateName, supportLeg)

    # Cartesian foot trajectory

    # Warning: Needs a PoseInit before executing

    space = motion.FRAME_ROBOT

    axisMask = 63  # control all the effector's axes

    isAbsolute = False

    # Lower the Torso and move to the side

    effector = "Torso"

    path = [0.0, 0.0, 0.15, 0.0, 0.0, 0.05]

    timeList = 0.5  # seconds

    motionProxy.positionInterpolation(effector, space, path,

                                      axisMask, timeList, isAbsolute)

    motionProxy.wbEnable(False)

    time.sleep(1)  # waiting a few seconds

    motionProxy.wbEnable(True)

    # New Legs/Feet configuration

    stateName = "Fixed"

    supportLeg = "LLeg"

    motionProxy.wbFootState(stateName, supportLeg)

    stateName = "Plane"

    supportLeg = "RLeg"

    motionProxy.wbFootState(stateName, supportLeg)

    postureProxy.goToPosture("StandInit", 1.0)

    motionProxy.wbEnable(False)

def Double_movement(motionProxy, NAO_IP, PORT):

    RShoulderPitch = 78.0

    RShoulderRoll = -39.9

    RElbowYaw = 68.3

    RElbowRoll = 57.2

    RWristYaw = 95

    RHand = 0.10

    LShoulderPitch = 78.0

    LShoulderRoll = 39.9

    LElbowYaw = -68.3

    LElbowRoll = -57.2

    LWristYaw = 4.3

    LHand = 0.0

    names = "LArm"

    angleLists = [LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,

                  LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand]

    timeLists = 0.5

    motionProxy.post.angleInterpolation(names, angleLists, timeLists, True)

    names = "RArm"

    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,

                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand]

    timeLists = 0.5

    motionProxy.angleInterpolation(names, angleLists, timeLists, True)

    time.sleep(0.5)  # Waiting between the two movements

    ########## Movement arms ###########

    # Start rotation movement

    RShoulderPitch = 77.7

    RShoulderRoll = -39.5

    RElbowYaw = 33.7

    RElbowRoll = 70

    RWristYaw = 95

    RHand = 0.10

    LShoulderPitch = 77.8

    LShoulderRoll = 49.2

    LElbowYaw = -68.5

    LElbowRoll = -9.4

    LWristYaw = 4.5

    LHand = 0.0

    names = "RArm"

    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,

                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD]

    motionProxy.setAngles(names, angleLists, 0.05)

    time.sleep(0.1)

    names = "LArm"

    angleLists = [LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,

                  LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand * almath.TO_RAD]

    motionProxy.setAngles(names, angleLists, 0.08)

    time.sleep(0.5)

    # Arms parallel to the floor

    RShoulderPitch = 15.1

    RShoulderRoll = -10.6

    RElbowYaw = 9.5

    RElbowRoll = 70

    RWristYaw = 95

    RHand = 0.10

    LShoulderPitch = 77.8

    LShoulderRoll = 75.8

    LElbowYaw = -68.5

    LElbowRoll = -2.5

    LWristYaw = 4.5

    LHand = 0.0

    names = "RArm"

    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,

                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD]

    motionProxy.setAngles(names, angleLists, 0.15)

    time.sleep(0.1)

    names = "LArm"

    angleLists = [LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,

                  LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand * almath.TO_RAD]

    motionProxy.setAngles(names, angleLists, 0.1)

    time.sleep(0.3)

    # Go to final position

    RShoulderPitch = 62.4

    RShoulderRoll = -15.7

    RElbowYaw = 51.7

    RElbowRoll = 81

    RWristYaw = 105

    RHand = 0.10

    LShoulderPitch = 27.0

    LShoulderRoll = 29.8

    LElbowYaw = -72.9

    LElbowRoll = -27.2

    LWristYaw = 4.5

    LHand = 0.0

    names = "RArm"

    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,

                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD]

    motionProxy.post.angleInterpolation(names, angleLists, 1.4, True)

    time.sleep(0.1)

    names = "LArm"

    angleLists = [LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,

                  LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand * almath.TO_RAD]

    motionProxy.angleInterpolation(names, angleLists, 1.4, True)


def Union_arms(motionProxy, NAO_IP, PORT):
    RShoulderPitch = 67.7

    RShoulderRoll = -26.4

    RElbowYaw = 90.9

    RElbowRoll = 88.5

    RWristYaw = 59.2

    RHand = 0.35

    LShoulderPitch = 80.2

    LShoulderRoll = 24.1

    LElbowYaw = -90.0

    LElbowRoll = -4.4

    LWristYaw = 0.5

    LHand = 0.0

    names = "LArm"

    angleLists = [LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,

                  LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand * almath.TO_RAD]

    timeLists = 0.5

    motionProxy.post.angleInterpolation(names, angleLists, timeLists, True)

    names = "RArm"

    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,

                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD]

    timeLists = 0.5

    motionProxy.angleInterpolation(names, angleLists, timeLists, True)

    time.sleep(0.2)  # Waiting between the two movements

    ####### Movement arms  ###########

    # Open/extend arms

    RShoulderPitch = 58.8

    RShoulderRoll = -25.9

    RElbowYaw = 90.6

    RElbowRoll = 25.0

    RWristYaw = 3.2

    RHand = 0.35

    LShoulderPitch = 58.8

    LShoulderRoll = 25.9

    LElbowYaw = -90.6

    LElbowRoll = -25.0

    LWristYaw = -59.4

    LHand = 0.0

    names = "LArm"

    angleLists = [LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,

                  LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand * almath.TO_RAD]

    timeLists = 0.5

    motionProxy.post.angleInterpolation(names, angleLists, timeLists, True)

    names = "RArm"

    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,

                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD]

    timeLists = 0.5

    motionProxy.angleInterpolation(names, angleLists, timeLists, True)

    RWristYaw = 59.4

    motionProxy.post.angleInterpolation("RWristYaw", RWristYaw * almath.TO_RAD, 1, True)

    time.sleep(0.5)  # For a better movements synchronization

    # Close arms

    RShoulderPitch = 45.9

    RShoulderRoll = 15.3

    RElbowRoll = 21.6

    LShoulderPitch = 45.9

    LShoulderRoll = -15.3

    LElbowRoll = -21.6

    names = "LArm"

    angleLists = [LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,

                  LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand * almath.TO_RAD]

    timeLists = 0.5

    motionProxy.post.angleInterpolation(names, angleLists, timeLists, True)

    names = "RArm"

    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,

                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD]

    timeLists = 0.5

    motionProxy.angleInterpolation(names, angleLists, timeLists, True)

    # Wait a few seconds

    time.sleep(1)

    # Go to final position

    RShoulderPitch = 78.0

    RShoulderRoll = -16.6

    RElbowYaw = 68.3

    RElbowRoll = 49.2

    RWristYaw = 4.3

    RHand = 0.35

    LShoulderPitch = 78.0

    LShoulderRoll = 16.6

    LElbowYaw = -68.3

    LElbowRoll = -49.2

    LWristYaw = 4.3

    LHand = 0.0

    names = "LArm"

    angleLists = [LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,

                  LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand * almath.TO_RAD]

    timeLists = 0.5

    motionProxy.post.angleInterpolation(names, angleLists, timeLists, True)

    names = "RArm"

    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,

                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD]

    timeLists = 0.5

    motionProxy.angleInterpolation(names, angleLists, timeLists, True)

def Move_forward(motionProxy, NAO_IP, PORT):

    distance_x_m = 0.08
    distance_y_m = 0.0
    theta_deg = 0.0
    # The command position estimation will be set to the sensor position when the robot starts moving, so we use sensors first and commands later.
    initPosition = almath.Pose2D(motionProxy.getRobotPosition(True))
    targetDistance = almath.Pose2D(distance_x_m, distance_y_m, theta_deg * almath.PI / 180)
    expectedEndPosition = initPosition * targetDistance
    enableArms = 0
    motionProxy.setMoveArmsEnabled(enableArms, enableArms)
    motionProxy.moveTo(distance_x_m, distance_y_m, theta_deg)

def Move_backward(motionProxy, NAO_IP, PORT):
    distance_x_m = -0.08
    distance_y_m = 0.0
    theta_deg = 0.0
    # The command position estimation will be set to the sensor position when the robot starts moving, so we use sensors first and commands later.
    initPosition = almath.Pose2D(motionProxy.getRobotPosition(True))
    targetDistance = almath.Pose2D(distance_x_m, distance_y_m, theta_deg * almath.PI / 180)
    expectedEndPosition = initPosition * targetDistance
    enableArms = 0
    motionProxy.setMoveArmsEnabled(enableArms, enableArms)
    motionProxy.moveTo(distance_x_m, distance_y_m, theta_deg)

def Arms_opening(motionProxy, NAO_IP, PORT):
    RShoulderPitch = 78.0

    RShoulderRoll = -16.6

    RElbowYaw = 68.3

    RElbowRoll = 49.2

    RWristYaw = 4.3

    RHand = 0.10

    LShoulderPitch = 78.0

    LShoulderRoll = 16.6

    LElbowYaw = -68.3

    LElbowRoll = -49.2

    LWristYaw = 4.3

    LHand = 0.0

    names = "LArm"

    angleLists = [LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,

                  LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand]

    timeLists = 0.1

    motionProxy.post.angleInterpolation(names, angleLists, timeLists, True)

    names = "RArm"

    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,

                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand]

    timeLists = 0.1

    motionProxy.angleInterpolation(names, angleLists, timeLists, True)

    time.sleep(0.1)  # Waiting between the two movements

    ########## Movement arms  ###########

    RShoulderPitch = 24.9

    RShoulderRoll = 8.0

    RElbowYaw = 67.8

    RElbowRoll = 14.7

    RWristYaw = 79.3

    RHand = 0.35

    LShoulderPitch = 68.8

    LShoulderRoll = 14.3

    LElbowYaw = -68.4

    LElbowRoll = -53.9

    LWristYaw = 4.5

    LHand = 0.0

    names = "LArm"

    angleLists = [LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,

                  LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand * almath.TO_RAD]

    motionProxy.setAngles(names, angleLists, 0.08)

    names = "RArm"

    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,

                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD]

    motionProxy.setAngles(names, angleLists, 0.08)

    #time.sleep(1.2)

    # Close arms

    RShoulderPitch = 24.5

    RShoulderRoll = 16.9

    RElbowYaw = 67.4

    RElbowRoll = 14.9

    RWristYaw = 79.1

    RHand = 0.35

    LShoulderPitch = 66.7

    LShoulderRoll = -12.3

    LElbowYaw = -69.0

    LElbowRoll = -53.7

    LWristYaw = 4.6

    LHand = 0.0

    names = "LArm"

    angleLists = [LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,

                  LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand * almath.TO_RAD]

    motionProxy.setAngles(names, angleLists, 0.1)

    names = "RArm"

    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,

                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD]

    motionProxy.setAngles(names, angleLists, 0.15)

    #time.sleep(0.4)

    # Stretch and raise arms

    RShoulderPitch = 24.7

    RShoulderRoll = -51.8

    RElbowYaw = 45.6

    RElbowRoll = 14.7

    RWristYaw = 78.9

    RHand = 0.35

    LShoulderPitch = 24.7

    LShoulderRoll = 51.8

    LElbowYaw = -45.6

    LElbowRoll = -14.7

    LWristYaw = -78.9

    LHand = 0.0

    names = "RArm"

    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,

                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD]

    motionProxy.setAngles(names, angleLists, 0.1)

    #time.sleep(0.2)

    names = "LArm"

    angleLists = [LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,

                  LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand * almath.TO_RAD]

    motionProxy.setAngles(names, angleLists, 0.1)

    #time.sleep(2.2)

    # Final position

    RShoulderPitch = 66.4

    RShoulderRoll = -26.1

    RElbowYaw = 106.0

    RElbowRoll = 80

    RWristYaw = 85

    RHand = 0.35

    LShoulderPitch = 66.4

    LShoulderRoll = 26.1

    LElbowYaw = -106.0

    LElbowRoll = -44.2

    LWristYaw = 4.6

    LHand = 0.0

    names = "LArm"

    angleLists = [LShoulderPitch * almath.TO_RAD, LShoulderRoll * almath.TO_RAD, LElbowYaw * almath.TO_RAD,

                  LElbowRoll * almath.TO_RAD, LWristYaw * almath.TO_RAD, LHand * almath.TO_RAD]

    timeLists = 0.1

    motionProxy.post.angleInterpolation(names, angleLists, timeLists, True)

    names = "RArm"

    angleLists = [RShoulderPitch * almath.TO_RAD, RShoulderRoll * almath.TO_RAD, RElbowYaw * almath.TO_RAD,

                  RElbowRoll * almath.TO_RAD, RWristYaw * almath.TO_RAD, RHand * almath.TO_RAD]

    timeLists = 0.1

    motionProxy.angleInterpolation(names, angleLists, timeLists, True)


def Diagonal_left(motionProxy, NAO_IP, PORT):

    distance_x_m = 0.03
    distance_y_m = 0.012
    theta_deg = 0.0
    # The command position estimation will be set to the sensor position when the robot starts moving, so we use sensors first and commands later.
    initPosition = almath.Pose2D(motionProxy.getRobotPosition(True))
    targetDistance = almath.Pose2D(distance_x_m, distance_y_m, theta_deg * almath.PI / 180)
    expectedEndPosition = initPosition * targetDistance
    enableArms = 0
    motionProxy.setMoveArmsEnabled(enableArms, enableArms)
    motionProxy.moveTo(distance_x_m, distance_y_m, theta_deg)

def Happy_birthday(motionProxy, NAO_IP, PORT):

    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append(
        [-0.0414599, -0.154976, -0.162646, -0.154976, -0.154976, -0.154976, -0.154976, -0.154976, -0.154976, -0.1335,
         -0.145772, -0.1335])

    names.append("HeadYaw")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append(
        [-0.00157596, -0.214801, -0.213269, -0.214801, -0.2102, -0.214801, -0.2102, -0.214801, -0.2102, -4.19617e-05,
         -4.19617e-05, -4.19617e-05])

    names.append("LAnklePitch")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append(
        [-0.113689, -0.340721, -0.244079, -0.340721, -0.00170743, -0.340721, -0.00170743, -0.340721, -0.00170743,
         -0.0139794, -0.0262515, -0.0139794])

    names.append("LAnkleRoll")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append([0.0168944, -0.0398637, -0.167186, -0.0398637, -0.265362, -0.0398637, -0.265362, -0.0398637, -0.265362,
                 -0.259225, -0.254624, -0.259225])

    names.append("LElbowRoll")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append([-0.340507, -1.54776, -1.54163, -1.54776, -1.54009, -1.54776, -1.54009, -1.54776, -1.54009, -0.814512,
                 -0.653443, -0.814512])

    names.append("LElbowYaw")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append(
        [-0.767043, -1.14441, -1.47882, -1.14441, -1.33155, -1.14441, -1.33155, -1.14441, -1.33155, -1.66903, -1.42666,
         -1.66903])

    names.append("LHand")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append([0.916387, 0.41748, 0.417116, 0.41748, 0.41748, 0.41748, 0.41748, 0.41748, 0.41748, 0.421116, 0.421116,
                 0.421116])

    names.append("LHipPitch")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append(
        [0.0749446, -0.242594, 0.438502, -0.242594, 0.271296, -0.242594, 0.271296, -0.242594, 0.271296, 0.286637,
         0.303511, 0.286637])

    names.append("LHipRoll")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append([-0.0477461, 0.17315, 0.185422, 0.17315, 0.24218, 0.17315, 0.24218, 0.17315, 0.24218, 0.22684, 0.211501,
                 0.22684])

    names.append("LHipYawPitch")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append(
        [0.0275685, -0.523138, -0.401951, -0.523138, -0.357466, -0.523138, -0.357466, -0.523138, -0.357466, -0.346727,
         -0.337524, -0.346727])

    names.append("LKneePitch")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append(
        [0.0886521, 0.775884, 0.133138, 0.775884, 0.00581614, 0.775884, 0.00581614, 0.775884, 0.00581614, 0.0226902,
         0.0380302, 0.0226902])

    names.append("LShoulderPitch")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append(
        [1.58765, 1.45266, 1.98343, 1.45266, 2.0187, 1.45266, 2.0187, 1.45266, 2.0187, -0.72409, 1.62907, -0.72409])

    names.append("LShoulderRoll")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append([0.303691, 0, 0.115008, 0, 0, 0, 0, 0, 0, 0.314428, 0.059784, 0.314428])

    names.append("LWristYaw")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append(
        [-1.00328, -0.694945, -0.65506, -0.694945, -0.688808, -0.694945, -0.688808, -0.694945, -0.688808, -0.690342,
         -0.681137, -0.690342])

    names.append("RAnklePitch")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append(
        [-0.104339, 0.0398569, -0.270011, 0.0398569, -0.451023, 0.0398569, -0.451023, 0.0398569, -0.451023, -0.458693,
         -0.466362, -0.458693])

    names.append("RAnkleRoll")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append(
        [-0.00456227, 0.108954, 0.0859437, 0.108954, 0.00464174, 0.108954, 0.00464174, 0.108954, 0.00464174, 0.00310773,
         0.00157374, 0.00310773])

    names.append("RElbowRoll")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append([0.305309, 1.12907, 1.1214, 1.12907, 1.126, 1.12907, 1.126, 1.12907, 1.126, 1.33616, 1.25485, 1.33616])

    names.append("RElbowYaw")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append(
        [0.786901, 1.52475, 1.18574, 1.52475, 1.51555, 1.52475, 1.51555, 1.52475, 1.51555, 1.26397, 1.27931, 1.26397])

    names.append("RHand")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append(
        [0.917842, 0.411661, 0.411661, 0.411661, 0.411661, 0.411661, 0.411661, 0.411661, 0.411661, 0.414571, 0.414571,
         0.414571])

    names.append("RHipPitch")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append(
        [0.039827, 0.315946, 0.010681, 0.315946, 0.042895, 0.315946, 0.042895, 0.315946, 0.042895, 0.047497, 0.0520989,
         0.047497])

    names.append("RHipRoll")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append([0.0153604, 0.0260984, -0.144176, 0.0260984, -0.0644075, 0.0260984, -0.0644075, 0.0260984, -0.0644075,
                 -0.0598056, -0.0552035, -0.0598056])

    names.append("RKneePitch")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append([0.103898, 0, 0.570234, 0, 0.665342, 0, 0.665342, 0, 0.665342, 0.686818, 0.708295, 0.686818])

    names.append("RShoulderPitch")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append([1.55859, 2.01572, 1.48035, 2.01572, 1.43893, 2.01572, 1.43893, 2.01572, 1.43893, 0.615176, -0.530721,
                 0.615176])

    names.append("RShoulderRoll")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append(
        [-0.296104, -0.082878, -0.01078, -0.082878, -0.081344, -0.082878, -0.081344, -0.082878, -0.081344, -0.460242,
         -0.679603, -0.460242])

    names.append("RWristYaw")
    times.append([0.733333, 1.2, 1.66667, 2.06667, 2.46667, 2.93333, 3.46667, 3.93333, 4.33333, 5, 5.53333, 6.2])
    keys.append(
        [0.946436, 0.76389, 0.766959, 0.76389, 0.760822, 0.76389, 0.760822, 0.76389, 0.760822, 0.77923, 0.777696,
         0.77923])

    try:
        motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print
        err



def Sprinkler_left(motionProxy, NAO_IP, PORT):

    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.714286, 1.77143, 5, 5.65714])
    keys.append([-0.12583, -0.233874, -0.173384, -0.173384])

    names.append("HeadYaw")
    times.append([0.714286, 1.77143, 5, 5.65714])
    keys.append([-0.0107799, 0.912807, 0.21932, 0.21932])

    names.append("LAnklePitch")
    times.append([0.714286, 1.65714, 5, 5.65714])
    keys.append([0.095066, -0.214803, -0.406552, -0.406552])

    names.append("LAnkleRoll")
    times.append([0.714286, 1.65714, 5, 5.65714])
    keys.append([-0.116542, -0.14262, -0.11961, -0.11961])

    names.append("LElbowRoll")
    times.append([0.714286, 1.71429, 2.14286, 5, 5.65714])
    keys.append([-0.400331, -0.0349066, -0.0459781, -0.358915, -0.358915])

    names.append("LElbowYaw")
    times.append([0.714286, 1.71429, 2.14286, 5, 5.65714])
    keys.append([-1.21037, -1.48956, -1.48035, -1.26099, -1.26099])

    names.append("LHand")
    times.append([0.714286, 1.71429, 2.14286, 5, 5.65714])
    keys.append([0.3056, 0.9616, 0.9592, 0.9616, 0.9616])

    names.append("LHipPitch")
    times.append([0.714286, 1.65714, 5, 5.65714])
    keys.append([0.136568, -0.144154, -0.268407, -0.268407])

    names.append("LHipRoll")
    times.append([0.714286, 1.65714, 5, 5.65714])
    keys.append([0.115092, 0.233211, 0.173384, 0.173384])

    names.append("LHipYawPitch")
    times.append([0.714286, 1.65714, 5, 5.65714])
    keys.append([-0.1733, -0.288349, -0.28068, -0.28068])

    names.append("LKneePitch")
    times.append([0.714286, 1.65714, 5, 5.65714])
    keys.append([-0.090548, 0.539926, 0.820649, 0.820649])

    names.append("LShoulderPitch")
    times.append([0.714286, 1.71429, 1.77143, 2.14286, 5, 5.65714])
    keys.append([1.53089, -0.420357, -0.560251, -0.417134, -0.0966839, -0.0966839])

    names.append("LShoulderRoll")
    times.append(
        [0.714286, 1.71429, 2.14286, 2.45714, 2.71429, 3, 3.28571, 3.54286, 3.85714, 4.14286, 4.4, 4.71429, 5, 5.65714])
    keys.append([0.13495, 0.819114, 0.461692, 0.610865, 0.223402, 0.460767, 0.0436332, 0.312414, -0.0610865, 0.207694,
                 -0.195477, 0.0593412, -0.159578, -0.159578])

    names.append("LWristYaw")
    times.append([0.714286, 1.71429, 2.14286, 2.45714, 2.71429, 5, 5.65714])
    keys.append([0.121144, 0.312894, 0.131882, 0.0663225, 0.0663225, -0.29457, -0.29457])

    names.append("RAnklePitch")
    times.append([0.714286, 1.65714, 5, 5.65714])
    keys.append([0.10282, -0.0199001, -0.263807, -0.263807])

    names.append("RAnkleRoll")
    times.append([0.714286, 1.65714, 5, 5.65714])
    keys.append([0.07214, 0.116626, 0.0828778, 0.0828778])

    names.append("RElbowRoll")
    times.append(
        [0.714286, 1.74286, 2.11429, 2.42857, 2.71429, 3.02857, 3.28571, 3.57143, 3.91429, 4.14286, 4.42857, 4.68571, 5,
         5.65714])
    keys.append(
        [0.385075, 1.54462, 1.53864, 1.54462, 1.53864, 1.54462, 1.53864, 1.54462, 1.53864, 1.54462, 1.53864, 1.54462,
         1.53558, 1.53558])

    names.append("RElbowYaw")
    times.append(
        [0.714286, 1.74286, 2.11429, 2.42857, 2.71429, 3.02857, 3.28571, 3.57143, 3.91429, 4.14286, 4.42857, 4.68571, 5,
         5.65714])
    keys.append([1.18421, 0.966378, 1.38823, 0.966378, 1.38823, 0.966378, 1.38823, 0.966378, 1.38823, 0.966378, 1.38823,
                 0.966378, 1.36982, 1.36982])

    names.append("RHand")
    times.append(
        [0.714286, 1.74286, 2.11429, 2.42857, 2.71429, 3.02857, 3.28571, 3.57143, 3.91429, 4.14286, 4.42857, 4.68571, 5,
         5.65714])
    keys.append([0.3068, 0.7708, 0.7696, 0.7708, 0.7696, 0.7708, 0.7696, 0.7708, 0.7696, 0.7708, 0.7696, 0.7708, 0.7692,
                 0.7692])

    names.append("RHipPitch")
    times.append([0.714286, 1.65714, 5, 5.65714])
    keys.append([0.130348, 0.138018, -0.251617, -0.251617])

    names.append("RHipRoll")
    times.append([0.714286, 1.65714, 5, 5.65714])
    keys.append([-0.06592, -0.0383082, -0.0291041, -0.0291041])

    names.append("RHipYawPitch")
    times.append([0.714286, 1.65714, 5, 5.65714])
    keys.append([-0.1733, -0.288349, -0.28068, -0.28068])

    names.append("RKneePitch")
    times.append([0.714286, 1.65714, 5, 5.65714])
    keys.append([-0.0904641, 0.0798099, 0.676537, 0.676537])

    names.append("RShoulderPitch")
    times.append(
        [0.714286, 1.74286, 2.11429, 2.42857, 2.71429, 3.02857, 3.28571, 3.57143, 3.91429, 4.14286, 4.42857, 4.68571, 5,
         5.65714])
    keys.append(
        [1.51103, -0.742414, -0.566003, -0.742414, -0.566003, -0.742414, -0.566003, -0.742414, -0.566003, -0.742414,
         -0.566003, -0.742414, -0.544529, -0.544529])

    names.append("RShoulderRoll")
    times.append(
        [0.714286, 1.74286, 2.11429, 2.42857, 2.71429, 3.02857, 3.28571, 3.57143, 3.91429, 4.14286, 4.42857, 4.68571, 5,
         5.65714])
    keys.append(
        [-0.113558, -0.43263, -0.0614019, -0.43263, -0.0614019, -0.43263, -0.0614019, -0.43263, -0.0614019, -0.43263,
         -0.0614019, -0.43263, -0.075208, -0.075208])

    names.append("RWristYaw")
    times.append(
        [0.714286, 1.74286, 2.11429, 2.42857, 2.71429, 3.02857, 3.28571, 3.57143, 3.91429, 4.14286, 4.42857, 4.68571, 5,
         5.65714])
    keys.append(
        [0.105804, 1.30539, 0.803775, 1.30539, 0.803775, 1.30539, 0.803775, 1.30539, 0.803775, 1.30539, 0.803775,
         1.30539, 0.820649, 0.820649])

    try:

        motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print
        err


def Sprinkler_right(motionProxy, NAO_IP, PORT):
    # Choregraphe simplified export in Python.
    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1.77143, 5, 5.31429, 6.25714])
    keys.append([-0.233874, -0.173384, -0.173384, -0.173384])

    names.append("HeadYaw")
    times.append([1.77143, 5, 5.31429, 6.25714])
    keys.append([-0.912807, -0.21932, -0.21932, 0.0107799])

    names.append("LAnklePitch")
    times.append([1.65714, 5, 5.31429, 6.25714])
    keys.append([-0.0199001, -0.263807, -0.263807, 0.107422])

    names.append("LAnkleRoll")
    times.append([1.65714, 5, 5.31429, 6.25714])
    keys.append([-0.116626, -0.0828778, -0.0828778, -0.073674])

    names.append("LElbowRoll")
    times.append(
        [1.74286, 2.11429, 2.42857, 2.71429, 3.02857, 3.28571, 3.57143, 3.91429, 4.14286, 4.42857, 4.68571, 5, 5.31429,
         6.25714])
    keys.append(
        [-1.54462, -1.53864, -1.54462, -1.53864, -1.54462, -1.53864, -1.54462, -1.53864, -1.54462, -1.53864, -1.54462,
         -1.53558, -1.53558, -0.412688])

    names.append("LElbowYaw")
    times.append(
        [1.74286, 2.11429, 2.42857, 2.71429, 3.02857, 3.28571, 3.57143, 3.91429, 4.14286, 4.42857, 4.68571, 5, 5.31429,
         6.25714])
    keys.append(
        [-0.966378, -1.38823, -0.966378, -1.38823, -0.966378, -1.38823, -0.966378, -1.38823, -0.966378, -1.38823,
         -0.966378, -1.36982, -1.36982, -1.19494])

    names.append("LHand")
    times.append(
        [1.74286, 2.11429, 2.42857, 2.71429, 3.02857, 3.28571, 3.57143, 3.91429, 4.14286, 4.42857, 4.68571, 5, 5.31429,
         6.25714])
    keys.append([0.7708, 0.7696, 0.7708, 0.7696, 0.7708, 0.7696, 0.7708, 0.7696, 0.7708, 0.7696, 0.7708, 0.7692, 0.7692,
                 0.3068])

    names.append("LHipPitch")
    times.append([1.65714, 5, 5.31429, 6.25714])
    keys.append([0.138018, -0.251617, -0.251617, 0.133416])

    names.append("LHipRoll")
    times.append([1.65714, 5, 5.31429, 6.25714])
    keys.append([0.0383082, 0.0291041, 0.0291041, 0.0643861])

    names.append("LHipYawPitch")
    times.append([1.65714, 5, 5.31429, 6.25714])
    keys.append([-0.288349, -0.28068, -0.28068, -0.168698])

    names.append("LKneePitch")
    times.append([1.65714, 5, 5.31429, 6.25714])
    keys.append([0.0798099, 0.676537, 0.676537, -0.091998])

    names.append("LShoulderPitch")
    times.append(
        [1.74286, 2.11429, 2.42857, 2.71429, 3.02857, 3.28571, 3.57143, 3.91429, 4.14286, 4.42857, 4.68571, 5, 5.31429,
         6.25714])
    keys.append(
        [-0.742414, -0.566003, -0.742414, -0.566003, -0.742414, -0.566003, -0.742414, -0.566003, -0.742414, -0.566003,
         -0.742414, -0.544529, -0.544529, 1.48189])

    names.append("LShoulderRoll")
    times.append(
        [1.74286, 2.11429, 2.42857, 2.71429, 3.02857, 3.28571, 3.57143, 3.91429, 4.14286, 4.42857, 4.68571, 5, 5.31429,
         6.25714])
    keys.append(
        [0.43263, 0.0614019, 0.43263, 0.0614019, 0.43263, 0.0614019, 0.43263, 0.0614019, 0.43263, 0.0614019, 0.43263,
         0.075208, 0.075208, 0.0813439])

    names.append("LWristYaw")
    times.append(
        [1.74286, 2.11429, 2.42857, 2.71429, 3.02857, 3.28571, 3.57143, 3.91429, 4.14286, 4.42857, 4.68571, 5, 5.31429,
         6.25714])
    keys.append(
        [-1.30539, -0.803775, -1.30539, -0.803775, -1.30539, -0.803775, -1.30539, -0.803775, -1.30539, -0.803775,
         -1.30539, -0.820649, -0.820649, -0.167164])

    names.append("RAnklePitch")
    times.append([1.65714, 5, 5.31429, 6.25714])
    keys.append([-0.214803, -0.406552, -0.406552, 0.101202])

    names.append("RAnkleRoll")
    times.append([1.65714, 5, 5.31429, 6.25714])
    keys.append([0.14262, 0.11961, 0.11961, 0.118076])

    names.append("RElbowRoll")
    times.append([1.71429, 2.14286, 5, 5.31429, 6.25714])
    keys.append([0.0349066, 0.0459781, 0.358915, 0.358915, 0.38806])

    names.append("RElbowYaw")
    times.append([1.71429, 2.14286, 5, 5.31429, 6.25714])
    keys.append([1.48956, 1.48035, 1.26099, 1.26099, 1.21497])

    names.append("RHand")
    times.append([1.71429, 2.14286, 5, 5.31429, 6.25714])
    keys.append([0.9616, 0.9592, 0.9616, 0.9616, 0.3052])

    names.append("RHipPitch")
    times.append([1.65714, 5, 5.31429, 6.25714])
    keys.append([-0.144154, -0.268407, -0.268407, 0.142704])

    names.append("RHipRoll")
    times.append([1.65714, 5, 5.31429, 6.25714])
    keys.append([-0.233211, -0.173384, -0.173384, -0.115092])

    names.append("RHipYawPitch")
    times.append([1.65714, 5, 5.31429, 6.25714])
    keys.append([-0.288349, -0.28068, -0.28068, -0.168698])

    names.append("RKneePitch")
    times.append([1.65714, 5, 5.31429, 6.25714])
    keys.append([0.539926, 0.820649, 0.820649, -0.0923279])

    names.append("RShoulderPitch")
    times.append([1.71429, 1.77143, 2.14286, 5, 5.31429, 6.25714])
    keys.append([-0.420357, -0.560251, -0.417134, -0.0966839, -0.0966839, 1.48794])

    names.append("RShoulderRoll")
    times.append(
        [1.71429, 2.14286, 2.45714, 2.71429, 3, 3.28571, 3.54286, 3.85714, 4.14286, 4.4, 4.71429, 5, 5.31429, 6.25714])
    keys.append(
        [-0.819114, -0.461692, -0.610865, -0.223402, -0.460767, -0.0436332, -0.312414, 0.0610865, -0.207694, 0.195477,
         -0.0593412, 0.159578, 0.159578, -0.0889301])

    names.append("RWristYaw")
    times.append([1.71429, 2.14286, 2.45714, 2.71429, 5, 5.31429, 6.25714])
    keys.append([-0.312894, -0.131882, -0.0663225, -0.0663225, 0.29457, 0.29457, -0.161028])

    try:
        # uncomment the following line and modify the IP if you use this script outside Choregraphe.
        # motion = ALProxy("ALMotion", IP, 9559)
        motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print
        err


def Hello(motionProxy, NAO_IP, PORT):

    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([0.8, 1.56, 2.24, 2.8, 3.48, 4.6])
    keys.append([0.29602, -0.170316, -0.340591, -0.0598679, -0.193327, -0.01078])

    names.append("HeadYaw")
    times.append([0.8, 1.56, 2.24, 2.8, 3.48, 4.6])
    keys.append([-0.135034, -0.351328, -0.415757, -0.418823, -0.520068, -0.375872])

    names.append("LElbowRoll")
    times.append([0.72, 1.48, 2.16, 2.72, 3.4, 4.52])
    keys.append([-1.37902, -1.29005, -1.18267, -1.24863, -1.3192, -1.18421])

    names.append("LElbowYaw")
    times.append([0.72, 1.48, 2.16, 2.72, 3.4, 4.52])
    keys.append([-0.803859, -0.691876, -0.679603, -0.610574, -0.753235, -0.6704])

    names.append("LHand")
    times.append([1.48, 4.52])
    keys.append([0.238207, 0.240025])

    names.append("LShoulderPitch")
    times.append([0.72, 1.48, 2.16, 2.72, 3.4, 4.52])
    keys.append([1.11824, 0.928028, 0.9403, 0.862065, 0.897349, 0.842125])

    names.append("LShoulderRoll")
    times.append([0.72, 1.48, 2.16, 2.72, 3.4, 4.52])
    keys.append([0.363515, 0.226991, 0.20398, 0.217786, 0.248467, 0.226991])

    names.append("LWristYaw")
    times.append([1.48, 4.52])
    keys.append([0.147222, 0.11961])

    names.append("RElbowRoll")
    times.append([0.64, 1.4, 1.68, 2.08, 2.4, 2.64, 3.04, 3.32, 3.72, 4.44])
    keys.append([1.38524, 0.242414, 0.349066, 0.934249, 0.680678, 0.191986, 0.261799, 0.707216, 1.01927, 1.26559])

    names.append("RElbowYaw")
    times.append([0.64, 1.4, 2.08, 2.64, 3.32, 3.72, 4.44])
    keys.append([-0.312978, 0.564471, 0.391128, 0.348176, 0.381923, 0.977384, 0.826783])

    names.append("RHand")
    times.append([1.4, 3.32, 4.44])
    keys.append([0.853478, 0.854933, 0.425116])

    names.append("RShoulderPitch")
    times.append([0.64, 1.4, 2.08, 2.64, 3.32, 4.44])
    keys.append([0.247016, -1.17193, -1.0891, -1.26091, -1.14892, 1.02015])

    names.append("RShoulderRoll")
    times.append([0.64, 1.4, 2.08, 2.64, 3.32, 4.44])
    keys.append([-0.242414, -0.954191, -0.460242, -0.960325, -0.328317, -0.250085])

    names.append("RWristYaw")
    times.append([1.4, 3.32, 4.44])
    keys.append([-0.312978, -0.303775, 0.182504])

    try:
        motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print
        err

def Workout(motionProxy, NAO_IP, PORT):

    names = list()
    times = list()
    keys = list()

    names.append("HeadPitch")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append(
        [-0.15651, -0.136568, -0.136568, -0.136568, -0.136568, -0.136568, -0.136568, -0.136568, -0.136568, -0.136568])

    names.append("HeadYaw")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append([-0.019984, -0.00617791, -0.00464392, -0.00617791, -0.00464392, -0.00464392, -0.00617791, -0.00617791,
                 -0.00464392, -0.00617791])

    names.append("LAnklePitch")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append(
        [-1.18944, -1.18889, 0.095066, 0.095066, 0.0966001, 0.095066, 0.0966001, 0.0966001, 0.0966001, 0.0966001])

    names.append("LAnkleRoll")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append(
        [-0.05058, -0.049046, -0.115008, -0.115008, -0.116542, -0.116542, -0.116542, -0.116542, -0.116542, -0.115008])

    names.append("LElbowRoll")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append(
        [-0.397265, -0.398797, -0.384992, -1.52936, -0.397265, -1.52936, -0.237728, -1.39283, -0.37272, -0.929562])

    names.append("LElbowYaw")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append([-1.34996, -1.37144, -1.72272, -1.52177, -1.46348, -1.45581, -1.42666, -1.47115, -0.124296, -0.128898])

    names.append("LHand")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append([0.9576, 0.0352, 0.016, 0.0268, 0.0268, 0.0268, 0.0268, 0.0268, 0.0268, 0.0268])

    names.append("LHipPitch")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append([-0.559868, -0.559868, 0.135034, 0.135034, 0.135034, 0.135034, 0.135034, 0.135034, 0.135034, 0.135034])

    names.append("LHipRoll")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append([0.16418, 0.16418, 0.115092, 0.115092, 0.115092, 0.115092, 0.115092, 0.115092, 0.115092, 0.115092])

    names.append("LHipYawPitch")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append([-0.504645, -0.504645, -0.1733, -0.1733, -0.1733, -0.174835, -0.1733, -0.1733, -0.1733, -0.1733])

    names.append("LKneePitch")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append(
        [2.11255, 2.11255, -0.090548, -0.090548, -0.090548, -0.092082, -0.090548, -0.090548, -0.090548, -0.090548])

    names.append("LShoulderPitch")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append([1.70116, 1.86684, 1.71957, 1.00933, 1.49407, 1.09063, 1.36368, 1.04308, -1.55245, -1.54631])

    names.append("LShoulderRoll")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append(
        [0.395731, 0.292952, 0.228525, -0.00924586, 0.00916195, -0.00771189, 0.00762796, -0.038392, 0.34971, 1.04154])

    names.append("LWristYaw")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append([-0.352862, -0.40962, 0.0843279, -1.62915, -1.63835, -1.61228, -1.61688, -1.70278, -0.47865, -0.47865])

    names.append("RAnklePitch")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append([-1.18421, -1.18574, 0.101286, 0.099752, 0.101286, 0.099752, 0.101286, 0.101286, 0.10282, 0.099752])

    names.append("RAnkleRoll")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append([0.0429941, 0.0429941, 0.073674, 0.073674, 0.073674, 0.073674, 0.073674, 0.073674, 0.073674, 0.073674])

    names.append("RElbowRoll")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append([0.346725, 0.441834, 0.441834, 1.5233, 1.52484, 0.159578, 1.50029, 1.50029, 0.309909, 1.07691])

    names.append("RElbowYaw")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append([1.52169, 1.5447, 1.26704, 1.30539, 1.30693, 1.61679, 1.57691, 1.57691, 0.754686, 0.282215])

    names.append("RHand")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append([0.9432, 0.0176001, 0.0172, 0.1056, 0.1056, 0.1056, 0.1056, 0.1056, 0.1056, 0.1056])

    names.append("RHipPitch")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append([-0.564555, -0.575959, 0.131882, 0.131882, 0.131882, 0.131882, 0.130348, 0.131882, 0.131882, 0.131882])

    names.append("RHipRoll")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append(
        [-0.115008, -0.116542, -0.0643861, -0.0643861, -0.0643861, -0.0643861, -0.0643861, -0.0643861, -0.0643861,
         -0.0643861])

    names.append("RHipYawPitch")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append([-0.504645, -0.504645, -0.1733, -0.1733, -0.1733, -0.174835, -0.1733, -0.1733, -0.1733, -0.1733])

    names.append("RKneePitch")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append(
        [2.11255, 2.11255, -0.091998, -0.091998, -0.0923279, -0.0923279, -0.0923279, -0.091998, -0.091998, -0.0904641])

    names.append("RShoulderPitch")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append([1.67824, 1.69818, 1.55859, 1.08611, 1.08765, 1.26252, 1.11526, 1.11679, -1.37135, -1.35908])

    names.append("RShoulderRoll")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append([-0.262356, -0.506262, -0.219404, 0.174835, 0.168698, 0.06592, 0.15029, 0.15029, -0.236277, -1.09839])

    names.append("RWristYaw")
    times.append([1, 1.76, 2.92, 3.84, 4.56, 5.12, 5.72, 6.32, 7.48, 8.52])
    keys.append([0.0168321, 0.151824, 0.239262, 1.58458, 1.58458, 1.6306, 1.53396, 1.53396, 0.154892, 0.154892])

    try:
        motionProxy.angleInterpolation(names, keys, times, True)
    except BaseException, err:
        print
        err
