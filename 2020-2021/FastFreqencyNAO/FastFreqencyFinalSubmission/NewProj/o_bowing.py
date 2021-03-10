# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("LAnklePitch")
times.append([0.133333, 0.933333, 1.86667])
keys.append([-0.121359, -0.409751, 0.09])

names.append("LAnkleRoll")
times.append([0.133333, 0.933333, 1.86667])
keys.append([0.0153604, -0.116564, -0.127952])

names.append("LElbowRoll")
times.append([0.133333, 0.933333, 1.66667, 1.86667])
keys.append([-0.306757, -1.30539, -0.306757, -0.404206])

names.append("LElbowYaw")
times.append([0.133333, 0.933333, 1.66667, 1.86667])
keys.append([-0.12583, 0.469363, -0.12583, -1.18752])

names.append("LHand")
times.append([0.133333, 0.933333, 1.66667, 1.86667])
keys.append([0.924024, 0.924024, 0.924024, 0.300872])

names.append("LHipPitch")
times.append([0.133333, 0.933333, 1.86667])
keys.append([0.0749446, -0.761086, 0.128755])

names.append("LHipRoll")
times.append([0.133333, 0.933333, 1.86667])
keys.append([-0.0477461, 0.028954, 0.0950101])

names.append("LHipYawPitch")
times.append([0.133333, 0.933333, 1.86667])
keys.append([0.0291025, -0.319116, -0.172992])

names.append("LKneePitch")
times.append([0.133333, 0.933333, 1.86667])
keys.append([0.0855841, 1.0474, -0.0884112])

names.append("LShoulderPitch")
times.append([0.133333, 0.933333, 1.66667, 1.86667])
keys.append([2.0417, 2.06319, 2.0417, 1.47844])

names.append("LShoulderRoll")
times.append([0.133333, 0.933333, 1.66667, 1.86667])
keys.append([0.417205, 0.246933, 0.417205, 0.189801])

names.append("LWristYaw")
times.append([0.133333, 0.933333, 1.66667, 1.86667])
keys.append([-0.998676, -1.01708, -0.998676, 0.0965961])

names.append("RAnklePitch")
times.append([0.133333, 0.933333, 1.86667])
keys.append([-0.102805, -0.543063, 0.0891156])

names.append("RAnkleRoll")
times.append([0.133333, 0.933333, 1.86667])
keys.append([-0.00456227, 0.135032, 0.128071])

names.append("RElbowRoll")
times.append([0.133333, 0.933333, 1.66667, 1.86667])
keys.append([0.435699, 1.27786, 0.435699, 0.411376])

names.append("RElbowYaw")
times.append([0.133333, 0.933333, 1.66667, 1.86667])
keys.append([0.222388, 0.374254, 0.222388, 1.191])

names.append("RHand")
times.append([0.133333, 0.933333, 1.66667, 1.86667])
keys.append([0.917842, 0.469091, 0.917842, 0.300862])

names.append("RHipPitch")
times.append([0.133333, 0.933333, 1.86667])
keys.append([0.041361, -0.65354, 0.128909])

names.append("RHipRoll")
times.append([0.133333, 0.933333, 1.86667])
keys.append([0.0168944, -0.0444656, -0.0921797])

names.append("RKneePitch")
times.append([0.133333, 0.933333, 1.86667])
keys.append([0.103898, 1.03657, -0.0884264])

names.append("RShoulderPitch")
times.append([0.133333, 0.933333, 1.66667, 1.86667])
keys.append([1.06617, 0.943452, 1.06617, 1.46651])

names.append("RShoulderRoll")
times.append([0.133333, 0.933333, 1.66667, 1.86667])
keys.append([-0.398883, -0.0429939, -0.398883, -0.186879])

names.append("RWristYaw")
times.append([0.133333, 0.933333, 1.66667, 1.86667])
keys.append([0.949504, 0.964844, 0.949504, 0.102622])

# copy paste the printed value and uncomment
keysValue = [0.4073845751410276, 0.05833394887833328, 0.4994921055944217, 0.101450213104754, 0.4769822989522272, 0.2646403021222748, 0.064227546918684]
finalPositionValue = [0.128755, 0.0950101, -0.0884112, 0.189801, 0.0965961, 0.0891156, 0.128071]
# times = []