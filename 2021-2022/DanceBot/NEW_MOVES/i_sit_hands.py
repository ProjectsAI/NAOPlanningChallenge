# Choregraphe bezier export in Python.

import sys
import time

from naoqi import ALProxy


def main(robotIP, port):
  names = list()
  times = list()
  keys = list()

  names.append("HeadPitch")
  times.append([0.6, 0.64, 1.28, 1.84, 1.88, 2.32, 2.88, 2.92])
  keys.append([[-0.286234, [3, -0.2, 0], [3, 0.0133333, 0]], [-0.286234, [3, -0.0133333, 0], [3, 0.213333, 0]], [0.225147, [3, -0.213333, 0], [3, 0.186667, 0]], [-0.286234, [3, -0.186667, 0], [3, 0.0133333, 0]], [-0.286234, [3, -0.0133333, 0], [3, 0.146667, 0]], [0.225147, [3, -0.146667, 0], [3, 0.186667, 0]], [-0.286234, [3, -0.186667, 0], [3, 0.0133333, 0]], [-0.286234, [3, -0.0133333, 0], [3, 0, 0]]])

  names.append("HeadYaw")
  times.append([0.64, 1.88, 2.92])
  keys.append([[-0.0335083, [3, -0.213333, 0], [3, 0.413333, 0]], [-0.0335082, [3, -0.413333, 0], [3, 0.346667, 0]], [-0.0335082, [3, -0.346667, 0], [3, 0, 0]]])

  names.append("LAnklePitch")
  times.append([0.68, 1.92, 2.96])
  keys.append([[0.834819, [3, -0.226667, 0], [3, 0.413333, 0]], [0.834819, [3, -0.413333, 0], [3, 0.346667, 0]], [0.834819, [3, -0.346667, 0], [3, 0, 0]]])

  names.append("LAnkleRoll")
  times.append([0.68, 1.92, 2.96])
  keys.append([[-0.00817124, [3, -0.226667, 0], [3, 0.413333, 0]], [-0.00817125, [3, -0.413333, 0], [3, 0.346667, 0]], [-0.00817125, [3, -0.346667, 0], [3, 0, 0]]])

  names.append("LElbowRoll")
  times.append([0.04, 0.12, 0.6, 1.2, 1.84, 2.24, 2.88, 3.56])
  keys.append([[-0.226893, [3, -0.0133333, 0], [3, 0.0266667, 0]], [-0.1756, [3, -0.0266667, 0], [3, 0.16, 0]], [-0.497899, [3, -0.16, 0], [3, 0.2, 0]], [-0.175599, [3, -0.2, 0], [3, 0.213333, 0]], [-0.497899, [3, -0.213333, 0], [3, 0.133333, 0]], [-0.175599, [3, -0.133333, 0], [3, 0.213333, 0]], [-0.497899, [3, -0.213333, 0.207998], [3, 0.226667, -0.220998]], [-1.46259, [3, -0.226667, 0], [3, 0, 0]]])

  names.append("LElbowYaw")
  times.append([0.04, 0.12, 0.6, 1.2, 1.84, 2.24, 2.88, 3.56])
  keys.append([[-0.195201, [3, -0.0133333, 0], [3, 0.0266667, 0]], [-0.19386, [3, -0.0266667, -0.000185514], [3, 0.16, 0.00111308]], [-0.191305, [3, -0.16, 0], [3, 0.2, 0]], [-0.193861, [3, -0.2, 0], [3, 0.213333, 0]], [-0.191306, [3, -0.213333, 0], [3, 0.133333, 0]], [-0.193861, [3, -0.133333, 0], [3, 0.213333, 0]], [-0.191306, [3, -0.213333, 0], [3, 0.226667, 0]], [-2.08567, [3, -0.226667, 0], [3, 0, 0]]])

  names.append("LHand")
  times.append([0.04, 0.12, 0.6, 1.2, 1.84, 2.24, 2.88, 3.56])
  keys.append([[0.74, [3, -0.0133333, 0], [3, 0.0266667, 0]], [0.74, [3, -0.0266667, 0], [3, 0.16, 0]], [0, [3, -0.16, 0], [3, 0.2, 0]], [0.74, [3, -0.2, 0], [3, 0.213333, 0]], [0, [3, -0.213333, 0], [3, 0.133333, 0]], [0.74, [3, -0.133333, 0], [3, 0.213333, 0]], [0, [3, -0.213333, 0], [3, 0.226667, 0]], [1, [3, -0.226667, 0], [3, 0, 0]]])

  names.append("LHipPitch")
  times.append([0.68, 1.92, 2.96])
  keys.append([[-1.52647, [3, -0.226667, 0], [3, 0.413333, 0]], [-1.52647, [3, -0.413333, 0], [3, 0.346667, 0]], [-1.52647, [3, -0.346667, 0], [3, 0, 0]]])

  names.append("LHipRoll")
  times.append([0.68, 1.92, 2.96])
  keys.append([[0.27501, [3, -0.226667, 0], [3, 0.413333, 0]], [0.27501, [3, -0.413333, 0], [3, 0.346667, 0]], [0.27501, [3, -0.346667, 0], [3, 0, 0]]])

  names.append("LHipYawPitch")
  times.append([0.68, 1.92, 2.96])
  keys.append([[-0.617592, [3, -0.226667, 0], [3, 0.413333, 0]], [-0.617592, [3, -0.413333, 0], [3, 0.346667, 0]], [-0.617592, [3, -0.346667, 0], [3, 0, 0]]])

  names.append("LKneePitch")
  times.append([0.68, 1.92, 2.96])
  keys.append([[1.3959, [3, -0.226667, 0], [3, 0.413333, 0]], [1.3959, [3, -0.413333, 0], [3, 0.346667, 0]], [1.3959, [3, -0.346667, 0], [3, 0, 0]]])

  names.append("LShoulderPitch")
  times.append([0.04, 0.12, 0.6, 1.2, 1.84, 2.24, 2.88, 3.56])
  keys.append([[-0.937242, [3, -0.0133333, 0], [3, 0.0266667, 0]], [-0.905536, [3, -0.0266667, -0.000467007], [3, 0.16, 0.00280204]], [-0.902734, [3, -0.16, 0], [3, 0.2, 0]], [-0.905536, [3, -0.2, 0], [3, 0.213333, 0]], [-0.902733, [3, -0.213333, 0], [3, 0.133333, 0]], [-0.905536, [3, -0.133333, 0], [3, 0.213333, 0]], [-0.902733, [3, -0.213333, -0.00280298], [3, 0.226667, 0.00297816]], [1.14843, [3, -0.226667, 0], [3, 0, 0]]])

  names.append("LShoulderRoll")
  times.append([0.04, 0.12, 0.6, 1.2, 1.84, 2.24, 2.88, 3.56])
  keys.append([[-0.314159, [3, -0.0133333, 0], [3, 0.0266667, 0]], [-0.170725, [3, -0.0266667, -0.0642077], [3, 0.16, 0.385246]], [1.0342, [3, -0.16, 0], [3, 0.2, 0]], [-0.170725, [3, -0.2, 0], [3, 0.213333, 0]], [1.0342, [3, -0.213333, 0], [3, 0.133333, 0]], [-0.170725, [3, -0.133333, 0], [3, 0.213333, 0]], [1.0342, [3, -0.213333, 0], [3, 0.226667, 0]], [-0.143117, [3, -0.226667, 0], [3, 0, 0]]])

  names.append("LWristYaw")
  times.append([0.04, 0.12, 0.6, 1.2, 1.84, 2.24, 2.88])
  keys.append([[-1.12122, [3, -0.0133333, 0], [3, 0.0266667, 0]], [-1.12122, [3, -0.0266667, 0], [3, 0.16, 0]], [-1.12122, [3, -0.16, 0], [3, 0.2, 0]], [-1.12122, [3, -0.2, 0], [3, 0.213333, 0]], [-1.12122, [3, -0.213333, 0], [3, 0.133333, 0]], [-1.12122, [3, -0.133333, 0], [3, 0.213333, 0]], [-1.12122, [3, -0.213333, 0], [3, 0, 0]]])

  names.append("RAnklePitch")
  times.append([0.68, 1.92, 2.96])
  keys.append([[0.293215, [3, -0.226667, 0], [3, 0.413333, 0]], [0.293215, [3, -0.413333, 0], [3, 0.346667, 0]], [0.293215, [3, -0.346667, 0], [3, 0, 0]]])

  names.append("RAnkleRoll")
  times.append([0.68, 1.92, 2.96])
  keys.append([[0.0186613, [3, -0.226667, 0], [3, 0.413333, 0]], [0.0186612, [3, -0.413333, 0], [3, 0.346667, 0]], [0.0186612, [3, -0.346667, 0], [3, 0, 0]]])

  names.append("RElbowRoll")
  times.append([0.04, 0.12, 0.6, 1.2, 1.84, 2.24, 2.88, 3.56])
  keys.append([[0.226893, [3, -0.0133333, 0], [3, 0.0266667, 0]], [0.175767, [3, -0.0266667, 0], [3, 0.16, 0]], [0.497899, [3, -0.16, 0], [3, 0.2, 0]], [0.175767, [3, -0.2, 0], [3, 0.213333, 0]], [0.497899, [3, -0.213333, 0], [3, 0.133333, 0]], [0.175767, [3, -0.133333, 0], [3, 0.213333, 0]], [0.497899, [3, -0.213333, -0.207971], [3, 0.226667, 0.220969]], [1.46259, [3, -0.226667, 0], [3, 0, 0]]])

  names.append("RElbowYaw")
  times.append([0.04, 0.12, 0.6, 1.2, 1.84, 2.24, 2.88, 3.56])
  keys.append([[0.195212, [3, -0.0133333, 0], [3, 0.0266667, 0]], [0.193879, [3, -0.0266667, 0.000184873], [3, 0.16, -0.00110924]], [0.19133, [3, -0.16, 0], [3, 0.2, 0]], [0.19388, [3, -0.2, 0], [3, 0.213333, 0]], [0.19133, [3, -0.213333, 0], [3, 0.133333, 0]], [0.19388, [3, -0.133333, 0], [3, 0.213333, 0]], [0.19133, [3, -0.213333, 0], [3, 0.226667, 0]], [2.08567, [3, -0.226667, 0], [3, 0, 0]]])

  names.append("RHand")
  times.append([0.04, 0.12, 0.6, 1.2, 1.84, 2.24, 2.88, 3.56])
  keys.append([[0.74, [3, -0.0133333, 0], [3, 0.0266667, 0]], [0.74, [3, -0.0266667, 0], [3, 0.16, 0]], [0, [3, -0.16, 0], [3, 0.2, 0]], [0.74, [3, -0.2, 0], [3, 0.213333, 0]], [0, [3, -0.213333, 0], [3, 0.133333, 0]], [0.74, [3, -0.133333, 0], [3, 0.213333, 0]], [0, [3, -0.213333, 0], [3, 0.226667, 0]], [1, [3, -0.226667, 0], [3, 0, 0]]])

  names.append("RHipPitch")
  times.append([0.68, 1.92, 2.96])
  keys.append([[-1.53392, [3, -0.226667, 0], [3, 0.413333, 0]], [-1.53392, [3, -0.413333, 0], [3, 0.346667, 0]], [-1.53392, [3, -0.346667, 0], [3, 0, 0]]])

  names.append("RHipRoll")
  times.append([0.68, 1.92, 2.96])
  keys.append([[-0.266008, [3, -0.226667, 0], [3, 0.413333, 0]], [-0.266007, [3, -0.413333, 0], [3, 0.346667, 0]], [-0.266007, [3, -0.346667, 0], [3, 0, 0]]])

  names.append("RHipYawPitch")
  times.append([0.68, 1.92, 2.96])
  keys.append([[-0.617592, [3, -0.226667, 0], [3, 0.413333, 0]], [-0.617592, [3, -0.413333, 0], [3, 0.346667, 0]], [-0.617592, [3, -0.346667, 0], [3, 0, 0]]])

  names.append("RKneePitch")
  times.append([0.68, 1.92, 2.96])
  keys.append([[1.40519, [3, -0.226667, 0], [3, 0.413333, 0]], [1.40519, [3, -0.413333, 0], [3, 0.346667, 0]], [1.40519, [3, -0.346667, 0], [3, 0, 0]]])

  names.append("RShoulderPitch")
  times.append([0.04, 0.12, 0.6, 1.2, 1.84, 2.24, 2.88, 3.56])
  keys.append([[-0.937242, [3, -0.0133333, 0], [3, 0.0266667, 0]], [-0.904551, [3, -0.0266667, -0.000496424], [3, 0.16, 0.00297855]], [-0.901573, [3, -0.16, 0], [3, 0.2, 0]], [-0.904552, [3, -0.2, 0], [3, 0.213333, 0]], [-0.901573, [3, -0.213333, 0], [3, 0.133333, 0]], [-0.904552, [3, -0.133333, 0], [3, 0.213333, 0]], [-0.901573, [3, -0.213333, -0.00297928], [3, 0.226667, 0.00316548]], [1.14843, [3, -0.226667, 0], [3, 0, 0]]])

  names.append("RShoulderRoll")
  times.append([0.04, 0.12, 0.6, 1.2, 1.84, 2.24, 2.88, 3.56])
  keys.append([[0.314159, [3, -0.0133333, 0], [3, 0.0266667, 0]], [0.16989, [3, -0.0266667, 0.0642077], [3, 0.16, -0.385246]], [-1.0342, [3, -0.16, 0], [3, 0.2, 0]], [0.16989, [3, -0.2, 0], [3, 0.213333, 0]], [-1.0342, [3, -0.213333, 0], [3, 0.133333, 0]], [0.16989, [3, -0.133333, 0], [3, 0.213333, 0]], [-1.0342, [3, -0.213333, 0], [3, 0.226667, 0]], [0.143117, [3, -0.226667, 0], [3, 0, 0]]])

  names.append("RWristYaw")
  times.append([0.04, 0.12, 0.6, 1.2, 1.84, 2.24, 2.88])
  keys.append([[1.12122, [3, -0.0133333, 0], [3, 0.0266667, 0]], [1.12122, [3, -0.0266667, 0], [3, 0.16, 0]], [1.12122, [3, -0.16, 0], [3, 0.2, 0]], [1.12122, [3, -0.2, 0], [3, 0.213333, 0]], [1.12122, [3, -0.213333, 0], [3, 0.133333, 0]], [1.12122, [3, -0.133333, 0], [3, 0.213333, 0]], [1.12122, [3, -0.213333, 0], [3, 0, 0]]])

  try:
    # uncomment the following line and modify the IP if you use this script outside Choregraphe.
    motion = ALProxy("ALMotion", robotIP, port)
    #  motion = ALProxy("ALMotion")
    motion.angleInterpolationBezier(names, times, keys)
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

  start = time.time()
  main(robotIP, port)
  end = time.time()
  duration = end - start
  print ("%.2f seconds elapsed" % duration)