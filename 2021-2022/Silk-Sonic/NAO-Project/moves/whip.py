# Choregraphe simplified export in Python.
t = 4.8
pre = True
post = True
mandatory_submove = False


names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.12])
keys.append([-0.178373])

names.append("HeadYaw")
times.append([0.12])
keys.append([-0.00598348])

names.append("LAnklePitch")
times.append([0.12])
keys.append([0.0867684])

names.append("LAnkleRoll")
times.append([0.12])
keys.append([-0.129721])

names.append("LElbowRoll")
times.append([0.12, 2.24])
keys.append([-0.402849, -1.54462])

names.append("LElbowYaw")
times.append([0.12])
keys.append([-1.19017])

names.append("LHand")
times.append([0.12])
keys.append([0.3])

names.append("LHipPitch")
times.append([0.12])
keys.append([0.129705])

names.append("LHipRoll")
times.append([0.12, 1.28, 1.76])
keys.append([0.0967259, 0.378736, 0])

names.append("LHipYawPitch")
times.append([0.12, 1.28])
keys.append([-0.16437, -0.118682])

names.append("LKneePitch")
times.append([0.12])
keys.append([-0.0866527])

names.append("LShoulderPitch")
times.append([0.12, 0.72, 2.24])
keys.append([1.47022, 2.08567, -0.0610865])

names.append("LShoulderRoll")
times.append([0.12])
keys.append([0.186405])

names.append("LWristYaw")
times.append([0.12, 0.72])
keys.append([0.0942099, -1.82387])

names.append("RAnklePitch")
times.append([0.12, 1.76])
keys.append([0.0867282, -0.345575])

names.append("RAnkleRoll")
times.append([0.12])
keys.append([0.129713])

names.append("RElbowRoll")
times.append([0.12, 0.72, 1.28, 1.76])
keys.append([0.410111, 1.54462, 1.54462, 0.0349066])

names.append("RElbowYaw")
times.append([0.12])
keys.append([1.1917])

names.append("RHand")
times.append([0.12])
keys.append([0.3])

names.append("RHipPitch")
times.append([0.12, 1.28, 1.76])
keys.append([0.129705, -1.53589, -0.469494])

names.append("RHipRoll")
times.append([0.12, 1.76])
keys.append([-0.0965754, -0.368264])

names.append("RHipYawPitch")
times.append([0.12])
keys.append([-0.16437])

names.append("RKneePitch")
times.append([0.12, 1.28, 1.76])
keys.append([-0.0865824, 2.11185, 1.0088])

names.append("RShoulderPitch")
times.append([0.12, 0.72, 1.76])
keys.append([1.46504, 0.453786, 0.151844])

names.append("RShoulderRoll")
times.append([0.12])
keys.append([-0.181877])

names.append("RWristYaw")
times.append([0.12, 1.76])
keys.append([0.099568, -1.30725])

'''try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolation(names, keys, times, True)
except BaseException, err:
  print err
'''