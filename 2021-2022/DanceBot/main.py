#!/usr/bin/python
# -*- coding: utf-8 -*-
import subprocess
from naoPlanning import NaoProblem
from search import *
import time
import setting as set

def add_list(input):
    new_item = list()
    new_item.append(input[0][0][0])
    new_item.append(input[0][0][1])
    new_item.append(input[0][1])
    new_item.append(input[1])
    return new_item


def nao_dance(moves, robotIP, port):
    # To execute moves on Choreographe we need a Python2 environment
    for move in moves:
        python2_command = f"python2 ./NEW_MOVES/{move}.py  {robotIP} {port}"
        moveToPrint = 'Move: ' + move
        print(moveToPrint, end='', flush=True)
        start_move = time.time()
        process = subprocess.run(python2_command.split(), stdout=subprocess.PIPE)
        end_move = time.time()
        toPrint = ' (' + str(round(end_move - start_move, 2)) + ' seconds)'
        print(toPrint, flush=True)


def sum_time_mandatory():
    sum = 0.0
    sum += initialPos[1][2]
    sum += goalPos[1][2]
    for i in mandatoryPos:
        sum += i[1][2]
    return sum


# Structure of a single move: ('name_of_the_MOVE', [precondition, postcondition, ESTIMATED duration of the move])
# True if Nao standing; False otherwise:

intermediatePos = {'i_start': [{'isStanding': True}, {'isStanding': True}, 4.53],
                   'i_up_down_hands': [{'isStanding': True}, {'isStanding': True}, 4.23],
                   'i_head_flex': [{'isStanding': True}, {'isStanding': True}, 5.67],
                   'i_front_arms': [{'isStanding': True}, {'isStanding': True}, 0.05],
                   'i_alternate': [{'isStanding': True}, {'isStanding': True}, 3.79],
                   'i_sit_hands': [{'isStanding': False}, {'isStanding': False}, 3.59],
                   'i_ext_clap': [{'isStanding': True}, {'isStanding': True}, 5.63],
                   'i_arm_dance': [{'isStanding': True}, {'isStanding': True}, 12.28],
                   'i_sit_dance': [{'isStanding': False}, {'isStanding': False}, 8.03],
                   'i_one_foot_hand_up': [{'isStanding': True}, {'isStanding': True}, 9.23],
                   'i_shuffle': [{'isStanding': True}, {'isStanding': True}, 6.79],
                   'i_random_robot': [{'isStanding': True}, {'isStanding': True}, 6.43],
                   'i_dance_move': [{'isStanding': True}, {'isStanding': True}, 6.02],
                   'i_finger_face': [{'isStanding': True}, {'isStanding': True}, 5.63],
                   'i_waving_pos': [{'isStanding': False}, {'isStanding': False}, 4.75],
                   'i_arms_rotate': [{'isStanding': None}, {'isStanding': None}, 4.35],
                   'i_Move_forward': [{'isStanding': True}, {'isStanding': True}, 2.70],
                   'i_Move_backward': [{'isStanding': True}, {'isStanding': True}, 2.70]
                   }

initialPos = ('m_StandInit', [None, True, 0.05])
mandatoryPos = [
    ('m_Sit', [True, False, 9.04]),
    ('m_Stand', [False, True, 11.32]),
    ('m_SitRelax', [True, False, 11.48]),
    ('m_StandZero', [False, True, 8.28]),
    ('m_Wipe_Forehead', [None, None, 5.13]),
    ('m_Hello', [False, False, 4.66])
]
goalPos = ('m_Crouch', [True, None, 1.63])

totalMandatory = [('m_StandInit', [True, True, 0.05]),
                  ('m_Sit', [True, False, 9.1]),
                  ('m_Stand', [False, True, 11.32]),
                  ('m_SitRelax', [True, False, 11.48]),
                  ('m_StandZero', [False, True, 8.28]),
                  ('m_Wipe_Forehead', [None, None, 5.13]),
                  ('m_Hello', [None, None, 4.66]),
                  ('m_Crouch', [True, True, 3.05])
                  ]

remaining_time = 180.0 - sum_time_mandatory()  # remaining time to execute intermediate positions
print("Remaining time for the execution of intermediate positions:", remaining_time)
intermediate_time = remaining_time / 7


# START PLANNING
def main(robot_ip, port):
    solution = list()
    final_list = list()
    for i in range(1, len(totalMandatory)):

        # We consider the current mandatory position and the next mandatory position
        startPos = totalMandatory[i - 1]
        endPos = totalMandatory[i]

        moveName = (startPos[0])  # extract the name of the current move

        # Extract the preconditions of the current mandatory position and the postconditions of the next one
        # (they can be True, False or None)
        postcond_initial = startPos[1][1]
        prec_end = endPos[1][0]

        # State of the current mandatory position
        current_state = (('namePos', moveName),
                         ('isStanding', postcond_initial),
                         ('intermediate_time', intermediate_time),
                         ('moves_done', 0),
                         )

        # State of the next mandatory position
        goal_state = (('isStanding', prec_end),
                      ('moves_done', 3),
                      ('intermediate_time', 0),
                      )

        moveProblem = NaoProblem(current_state, goal_state, intermediatePos, solution)

        partial_solution = iterative_deepening_search(moveProblem)

        if partial_solution is None:
            raise RuntimeError(f'No solution was found (step {i})!')

        partial_solution_dict = dict()

        for a in partial_solution.state:
            len_a = len(a)
            if len_a < 2:
                continue
            key = a[0]
            if len_a > 2:
                value = a[1:]
            else:
                value = a[1]
            if key not in partial_solution_dict:
                partial_solution_dict[key] = value

        partial_choreography = partial_solution_dict['namePos']

        for a in add_list(partial_choreography):
            final_list.append(a)

    final_list.append(goalPos[0])

    print('Solution', final_list, '\n')

    nao_dance(final_list, robotIP, port)


# END PLANNING
if __name__ == "__main__":

    robotIP = set.ip
    port = set.port  # Insert NAO port
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
        robotIP = sys.argv[1]
    elif len(sys.argv) == 2:
        robotIP = sys.argv[1]

    main(robotIP, port)
