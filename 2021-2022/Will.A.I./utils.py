#!/usr/bin/python
# -*- coding: utf-8 -*-
import math
import subprocess
import time

import vlc


def play_song(song_name):
    p = vlc.MediaPlayer(song_name)
    p.play()

# We execute a choreography
def do_moves(moves, ip, port):
    for move in moves:
        print(f"Move: {move}... ", end="", flush=True)
        # We create a command to execute each move one by one
        command = f"python2 ./Animations/{move}.py  {ip} {port}"
        start_move = time.time()
        process = subprocess.run(command.split(), stdout=subprocess.PIPE)
        end_move = time.time()
        # We used this print in testing to adjust the execution time of our moves set
        print("\nExecution time: %.2f seconds." % (end_move-start_move), flush=True)

# We created this function to convert a state to a handy dictionary
def from_state_to_dict(state):
    params_dict = dict()
    for t in state:
        len_t = len(t)
        if len_t < 2:
            continue
        key = t[0]
        if len_t > 2:
            value = t[1:]
        else:
            value = t[1]
        # We save only the fist key in case of doubles
        if key not in params_dict:
            params_dict[key] = value
    return params_dict

# We define the Entropy of a choreography based on Claude Shannon definition
def entropy_calc(choreography):
    # We keep track of the moves used in the choreography
    frequency_dict = {}
    for move in choreography:
        if move not in frequency_dict:
            # If absent initialize it to 1
            frequency_dict[move] = 1
        else:
            # If present update the value
            frequency_dict[move] += 1
    result = 0.0
    # Entropy as defined by Shannon
    for unique_move, frequency in frequency_dict.items():
        probability = frequency / len(choreography)
        # The log is negative so we used -=
        result -= probability * math.log(probability, 2)
    return result
