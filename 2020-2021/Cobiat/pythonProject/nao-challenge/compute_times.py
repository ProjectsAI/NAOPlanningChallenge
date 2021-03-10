"""
This file has to be intended as a utility script modified multiple times.
Don't use it as it is.
"""

from configuration import nao_ip, nao_port, modules_list
import numpy as np
import time

n_mod = len(modules_list)
times = np.loadtxt('times.txt')
pad0 = n_mod - times.shape[0]
pad1 = n_mod - times.shape[1]

times = np.pad(times, [(0, pad0), (0, pad1)],  mode='constant')

for pre in range(0, n_mod):
    for post in range(0, n_mod):
        if times[pre, post] == 0:
            modules_list[pre].main(nao_ip, nao_port)
            time1 = time.time()
            modules_list[post].main(nao_ip, nao_port)
            total_time = time.time() - time1
            times[pre, post] = total_time
            np.savetxt('times.txt', times)
