import re
import os
import vlc
import sys
import time
import subprocess
from mutagen.mp3 import MP3

from constants import *
from movements import *

"""
This function is used to convert the minimum time of a movement into
the number of bars that it exploits. In short, the minimum time of a movement is stretched
to the next bar, in order to allow the robot to dance following the beat
"""
def from_time_to_bars(time, bar_time): 
    num_bars = time/bar_time 
    epsilon = 0.05 
    num_bars_stretched = int(num_bars) 
    if num_bars - int(num_bars) > epsilon: 
        num_bars_stretched += 1 
    return num_bars_stretched

def filter_by_pre_post_conditions(nn_mandatory_movements_sorted,condition):
    result = [ mov for mov in nn_mandatory_movements_sorted if (    len(NON_MANDATORY_MOVEMENTS[mov][PRECONDITIONS]) == 2 and
                                                                    condition in NON_MANDATORY_MOVEMENTS[mov][POSTCONDITIONS]) or
                                                                    (NON_MANDATORY_MOVEMENTS[mov][PRECONDITIONS][0] == condition and
                                                                    NON_MANDATORY_MOVEMENTS[mov][POSTCONDITIONS][0] == condition)]
    return result

def move_to_file(move):
    switcher = {
        'rotation-handgun-object': '1-Rotation_handgun_object',
        'right-arm' : '2-Right_arm',
        'double-movement': '3-Double_movement',
        'arms-opening': '4-Arms_opening',
        'union-arms': '5-Union_arms',
        'Crouch': '6-Crouch',
        'move-forward' : '7-Move_forward',
        'move-backward' : '8-Move-backward',
        'diagonal-left' : '9-Diagonal_left',
        'diagonal-right' : '10-Diagonal_right',
        'Stand': '11-Stand',
        'rotation-foot-r': '12-Rotation_foot_RLeg',
        'rotation-foot-l': '13-Rotation_foot_LLeg',
        'StandInit': '14-StandInit',
        'StandZero': '15-StandZero',
        'Sit': '16-Sit',
        'SitRelax': '17-SitRelax',
        'arms-dance': 'Arms_dance',
        'birthday-dance-no-sound' : 'Birthday_dance_no_sound',
        'clip-clap' : 'Clip_Clap',
        'dance-move' : 'Dance_move',
        'disco' : 'Disco',
        'fever' : 'Fever',
        'fly' : 'Fly',
        'Hello' : 'Hello',
        'macarena' : 'Macarena',
        'plie' : 'Plie',
        'pray' : 'Pray',
        'rush' : 'Rush',
        'single-snap' : 'Single_Snap',
        'sing-with-me' : 'Sing_with_me',
        'snaps' : 'Snaps',
        'sprinkler' : 'Sprinkler',
        'swing' : 'Swing',
        'tai-chi-chuan' : 'Tai_Chi_Chuan',
        'the-robot' : 'The_robot',
        'vanity' : 'Vanity',
        'Wipe-forehead' : 'Wipe_Forehead',
        'workout' : 'Workout',
    }
    file_name = switcher.get(move, lambda: 'Invalid move')
    return file_name

def convert_mp3_to_flac(mp3_song):
    mp3_path = os.path.abspath(mp3_song)
    flac_path = re.sub(".mp3", ".flac", mp3_path)
    if not os.path.exists(flac_path):
        command = f"ffmpeg -i {mp3_path} {flac_path}"
        subprocess.run(command.split(), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return flac_path

def get_bpm_from_song(mp3_song):
    mp3_path = os.path.abspath(mp3_song)
    flac_path = convert_mp3_to_flac(mp3_path)
    bpm_str = subprocess.check_output(f"sox {flac_path} -t raw -r 44100 -e float -c 1 - | bpm", shell=True).decode('utf-8')
    bpm = int(float(bpm_str))
    return bpm

def get_duration_from_song(mp3_song):
    mp3_path = os.path.abspath(mp3_song)
    audio = MP3(mp3_path)
    duration = int(audio.info.length)
    return duration  

"""In this part, the choreography.txt file is generated"""
def generate_choreography(actions, states, bar_time, i, f):
    sep = ','
    bars_used = 0
    for j in range(len(actions)):
        move = actions[j]
        line = move #ove_to_file(move)
        state_now = states[j+1][1]
        bars_current = state_now - bars_used
        for control in NON_MANDATORY_MOVEMENTS[move][TYPE_CONTROL]:
            if control == TIME:
                line += sep + "{:.2f}".format(bars_current*bar_time)
            if control == LEGS_CONTROL:
                line += sep + str(int(states[j][BODY][LEGS_POSITION]))
            if control == BODY_CONTROL:
                line += sep + str(int(states[j][BODY][BODY_POSITION] == STANDING))
        bars_used = state_now
        print(line, file = f)
    
    move = mandatory_positions[i+1]
    line = move #move_to_file(move)
    for control in MANDATORY_MOVEMENTS[move][TYPE_CONTROL]:
        if control == TIME:
            line += sep + str(MANDATORY_MOVEMENTS[move][MIN_TIME])
        if control == SPEED:
            line += sep + "1.33"
    print(line, file = f)

finish = 0
def do_choreography(robotIP, port, song):
    global finish

    def SongFinished(event):
        global finish
        finish = 1

    f = open(OUTPUT_FILE, "r")

    python2_command = f"python2 ./RobotPositions/14-StandInit.py {robotIP} {port} 1.33"
    subprocess.run(python2_command.split(), stdout=subprocess.PIPE)

    time.sleep(0.5)

    instance = vlc.Instance()
    player = instance.media_player_new()
    media = instance.media_new_path(song)
    player.set_media(media)
    events = player.event_manager()
    events.event_attach(vlc.EventType.MediaPlayerEndReached, SongFinished)

    player.play()

    start_t = time.time()
    now = f.readline()
    now = now.rstrip('\n')
    delay = 0

    print("\n-----------------------------------\n-----------------------------------\n")
    print("START CHOREOGRAPHY\nPlaying \"{}\"".format(song))
    print("\n-----------------------------------\n-----------------------------------\n")

    while (now):
        now = now.split(",")
        move = now[0]
        print(f"Executing \"{move}\"")
        tempoOrLegs = now[1]

        if move in mandatory_positions:
            controls = MANDATORY_MOVEMENTS[move][TYPE_CONTROL]
        else:
            controls = NON_MANDATORY_MOVEMENTS[move][TYPE_CONTROL]

        if TIME not in controls:
            correct = tempoOrLegs
        else:
            correct = float(tempoOrLegs) - delay

        if len(now) == 3:
            legsOrBody = now[2]
            python2_command = f"python2 ./RobotPositions/{move_to_file(move)}.py {robotIP} {port} {correct} {legsOrBody}"
        else:
            python2_command = f"python2 ./RobotPositions/{move_to_file(move)}.py {robotIP} {port} {correct}"

        start_move = time.time()
        process = subprocess.run(python2_command.split(), stdout=subprocess.PIPE)
        end_move = time.time()
        total = end_move-start_move
        print("\tdone in %.2f seconds" % total, flush=True)

        #delay = 0
        if SPEED not in controls:
            if LEGS_CONTROL in controls and len(controls) == 1:
                battute_to_time = time_battuta*2 #3.90
            else:
                battute_to_time = tempoOrLegs 
            delay = total - float(battute_to_time)
        
        if move in mandatory_positions:
            print('\tMANDATORY_MOVE')

        print("-----------------------------------")

        now = f.readline()
        now = now.rstrip('\n')

    while finish == 0:
        time.sleep(0.1)

    end_t = time.time()
    print("\nTOTAL TIME: {:.2f} seconds".format(end_t - start_t))

    f.close()
