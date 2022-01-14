#!/usr/bin/python
# -*- coding: utf-8 -*-

from aima.search import *
from nao_problem import NaoProblem
import vlc
import subprocess
import time

def play_song(song_name):
    p = vlc.MediaPlayer(song_name)
    p.play()

def precondition_standing(position):
    if position == 'SitRelax':
        #SitRelax can be used only if Lucy is already sitting down
       return False
    return True

def postcondition_standing(position):
    if position in ('Sit', 'SitRelax'):
        #Sit and SitRelax don't finish in a standing position
        return False
    return True

def do_moves(moves, robot_ip, robot_port):
    for move in moves:
        print(f"Executing: "+(move)+ "... ")
        python2_command = f"python2 ./NaoMoves/{move}.py  {robot_ip} {robot_port}"
        start = time.time()
        process = subprocess.run(python2_command.split(), stdout=subprocess.PIPE)
        stop = time.time()
        print("done in %.2f seconds." % (stop-start), flush=True)

def from_state_to_dict(state):
    """
    Converts a state into a dictionary for easier access to the key-value pairs.
    Please note: in case of repeated properties, only the last value is kept!

    :param state: a problem state in the form of tuple of tuples
    :return: a dictionary representation of the given state
    """
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
        if key not in params_dict:
            params_dict[key] = value
    return params_dict

class Move:
    def __init__(self, duration=None, preconditions=None, postconditions=None):
        self.duration = duration
        self.preconditions = preconditions if preconditions is not None else {}
        self.postconditions = postconditions if preconditions is not None else {}


def main(robot_ip, port):
    # Mandatory moves in an order choosen by us:
    mandatory_moves = [('StandInit', Move(1.5)),('WipeForehead', Move(4.5)),('Stand', Move(1.5)),('Hello', Move(4.5)),('Sit', Move(17.0)),('SitRelax', Move(7.0)),('StandZero', Move(1.5))]
    final_move = ('Crouch', Move(2.5))
    # Moves used between mandatory ones:
    moves = {
             'FootSteps':               Move(8.0,  {'standing': True},  {'standing': True}),
             'HulaHoop':                Move(4.5,  {'standing': True},  {'standing': True}),
             'HeadMove':                Move(6.0,  {'standing': True},  {'standing': True}),
             'Kick':                    Move(7.5,  {'standing': True},  {'standing': True}),
             'AirGuitar':               Move(4.5,  {'standing': True},  {'standing': True}),
             'SprinklerL':              Move(4.5,  {'standing': True},  {'standing': True}),
             'SprinklerR':              Move(4.5,  {'standing': True},  {'standing': True}),
             'StandUp':                 Move(11.0,  {'standing': False},  {'standing': True}),
             'StandZero':               Move(2.0,  {'standing': True},  {'standing': True}),
             'Hello':                   Move(4.5,  None,None),
             'WipeForehead':            Move(4.5,  None,None),
             'Rotation_handgun_object': Move(3.5,  None,None),
             'Double_movement':         Move(5.0,  None,None),
  	     'Right_arm':               Move(6.5,  None,None),
             'Arms_opening':            Move(4.5,  None,None),
             'Union_arms':              Move(8.0,  None,None),
             'Move_forward':            Move(3.5,   {'standing': True},  {'standing': True}),
             'Move_backward':           Move(3.5,   {'standing': True},  {'standing': True}),
             'Diagonal_left':           Move(2.5,   {'standing': True},  {'standing': True}),
             'Diagonal_right':          Move(2.5,   {'standing': True},  {'standing': True}),
            }
    
    moves_list = [*mandatory_moves, final_move]
    number_of_moves = len(moves_list) - 1

    # Total time lost during the for the execution of mandatory moves
    total_time = 0.0
    for move in moves_list:
        total_time += move[1].duration

    # Planning 
    solution = tuple()
    total_remaining_time = 0
    print("LUCY'S CHOREOGRAPHY:")
    for index in range(1, len(moves_list)):
        starting_move = moves_list[index - 1]
        ending_move = moves_list[index]

        choreography = (starting_move[0],) 
        remaining_time = (180.0 - total_time)/number_of_moves 
        current_state = (('choreography', choreography),
                     ('standing', postcondition_standing(starting_move[0])),
                     ('remaining_time', remaining_time),
                     ('moves_done', 0))
        current_goal = (('standing', precondition_standing(ending_move[0])), 
                          ('moves_done', 5)) 
           
        # The partial solution is found with an Iterative Deepening Search algorithm
        current_problem = NaoProblem(current_state, current_goal, moves)
        current_solution = iterative_deepening_search(current_problem)
        if current_solution is None:
            raise RuntimeError('No solution found for step ' + str(index) +'!')

        current_solution_dict = from_state_to_dict(current_solution.state)
        
        total_remaining_time += current_solution_dict['remaining_time']
                   
        current_choreography = current_solution_dict['choreography']
        print("Step " + str(index) + ": \t" + ", ".join(current_choreography))
        solution += current_choreography
    
    #extra moves to fill the remaining time before last mandatory move
    extra_moves = [('HulaHoop', Move(4.5)),('Hello', Move(4.5)),('SprinklerL', Move(4.5)),('Bow', Move(4.0)),('Move_forward', Move(3.5)),('Move_backward', Move(3.5)),('Rotation_handgun_object', Move(3.5)),('Diagonal_left', Move(2.5)),('Diagonal_right', Move(2.5)),('StandZero', Move(2.0))]
    i = 0
    final_moves = []
    while total_remaining_time >= 3:
       if extra_moves[i][1].duration <= total_remaining_time:
           solution += (extra_moves[i][0],)
           total_remaining_time -= extra_moves[i][1].duration
           final_moves.append(extra_moves[i][0])
           del extra_moves[i]
       else:
           i += 1

    solution += (final_move[0],) 
    print('Final Step: \t' + ', '.join(final_moves) + ', Crouch') 
    state_dict = from_state_to_dict(current_solution.state)
    print("-------------------------------------------------------")
    
    print("\nLUCY WILL START DANCING NOW:")
    play_song("Singin in the rain.mp3")
    start = time.time()
    do_moves(solution, robot_ip, port)
    stop = time.time()
    print("Lucy danced for: %.2f seconds." % (stop-start))


if __name__ == "__main__":

    robot_ip = "127.0.0.1"
    port = 9559  
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
        robot_ip = sys.argv[1]
    elif len(sys.argv) == 2:
        robot_ip = sys.argv[1]
    
    main(robot_ip, port)
