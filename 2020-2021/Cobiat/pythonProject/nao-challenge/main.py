from naoqi import ALProxy
from configuration import nao_ip, nao_port, music_path, modules_list
from search import IterativeDeepening
import numpy as np
import time
from performer import Performer

mpm = 60/(136/4)

mandatory_position = [14, 17, 15, 18, 11, 13, 12, 1]
mandatory_times = [0, 14.12, 14.12, 28.24, 28.24, 28.24, 26.47, 15.88]

pool_times = np.loadtxt('times.txt')
search_alg = IterativeDeepening(pool_times, max_error=0.01, max_depth=5)

solution = search_alg.find_complete_path(mandatory_position, mandatory_times, mpm)
print(solution)

positions = [modules_list[i] for i in solution]

performer = Performer(nao_ip, nao_port, positions[0])

t1 = time.time()
performer.perform(positions[1:], music_path)
print("Tempo effettivo: ", time.time() - t1)





