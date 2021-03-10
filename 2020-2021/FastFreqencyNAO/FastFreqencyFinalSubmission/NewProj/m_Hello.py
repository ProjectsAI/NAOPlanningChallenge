from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([0.4, 0.78, 1.12, 1.4, 1.74, 2.3])
keys.append([0.29602, -0.170316, -0.340591, -0.0598679, -0.193327, -0.01078])

names.append("HeadYaw")
times.append([0.4, 0.78, 1.12, 1.4, 1.74, 2.3])
keys.append([-0.135034, -0.351328, -0.415757, -0.418823, -0.520068, -0.375872])

names.append("LElbowRoll")
times.append([0.36, 0.74, 1.08, 1.36, 1.7, 2.26])
keys.append([-1.37902, -1.29005, -1.18267, -1.24863, -1.3192, -1.18421])

names.append("LElbowYaw")
times.append([0.36, 0.74, 1.08, 1.36, 1.7, 2.26])
keys.append([-0.803859, -0.691876, -0.679603, -0.610574, -0.753235, -0.6704])

names.append("LHand")
times.append([0.74, 2.26])
keys.append([0.238207, 0.240025])

names.append("LShoulderPitch")
times.append([0.36, 0.74, 1.08, 1.36, 1.7, 2.26])
keys.append([1.11824, 0.928028, 0.9403, 0.862065, 0.897349, 0.842125])

names.append("LShoulderRoll")
times.append([0.36, 0.74, 1.08, 1.36, 1.7, 2.26])
keys.append([0.363515, 0.226991, 0.20398, 0.217786, 0.248467, 0.226991])

names.append("LWristYaw")
times.append([0.74, 2.26])
keys.append([0.147222, 0.11961])

names.append("RElbowRoll")
times.append([0.32, 0.7, 0.84, 1.04, 1.2, 1.32, 1.52, 1.66, 1.86, 2.22])
keys.append([1.38524, 0.242414, 0.349066, 0.934249, 0.680678, 0.191986, 0.261799, 0.707216, 1.01927, 1.26559])

names.append("RElbowYaw")
times.append([0.32, 0.7, 1.04, 1.32, 1.66, 1.86, 2.22])
keys.append([-0.312978, 0.564471, 0.391128, 0.348176, 0.381923, 0.977384, 0.826783])

names.append("RHand")
times.append([0.7, 1.66, 2.22])
keys.append([0.853478, 0.854933, 0.425116])

names.append("RShoulderPitch")
times.append([0.32, 0.7, 1.04, 1.32, 1.66, 2.22])
keys.append([0.247016, -1.17193, -1.0891, -1.26091, -1.14892, 1.02015])

names.append("RShoulderRoll")
times.append([0.32, 0.7, 1.04, 1.32, 1.66, 2.22])
keys.append([-0.242414, -0.954191, -0.460242, -0.960325, -0.328317, -0.250085])

names.append("RWristYaw")
times.append([0.7, 1.66, 2.22])
keys.append([-0.312978, -0.303775, 0.182504])

import numpy as np
# randomness for the movements
data = list()
data.append(np.std(keys[5]))
data.append(np.std(keys[6]))
data.append(np.std(keys[8]))
data.append(np.std(keys[10]))
data.append(np.std(keys[11]))
data.append(np.std(keys[12]))
data.append(np.std(keys[13]))
print("KeyValue ", data)
keysValue = list()

# ending positions for the moves
tempPositionValue = list()
tempPositionValue.append(keys[5][-1])
tempPositionValue.append(keys[6][-1])
tempPositionValue.append(keys[8][-1])
tempPositionValue.append(keys[10][-1])
tempPositionValue.append(keys[11][-1])
tempPositionValue.append(keys[12][-1])
tempPositionValue.append(keys[13][-1])
print("tempPosition ", tempPositionValue)
finalPositionValue = list()

x = np.hstack(times)
print("time taken", np.sum(times[0]))

# copy paste the printed value and uncomment
keysValue = [0.09031111977199827, 0.05334998207122472, 0.4158334424121754, 0.2022756022960313, 0.8794257010385937, 0.308673913935978, 0.23143378543668933]
finalPositionValue = [0.842125, 0.226991, 1.26559, 0.425116, 1.02015, -0.250085, 0.182504]
