#!/usr/bin/python
# -*- coding: utf-8 -*-

from aima.search import *
from nao_problem import NaoProblem
from utils import *


def precondition_standing(position):
    if position == 'M_SitRelax':
        # Unlike what was done for "M_Sit", we measured the duration of
        # "M_SitRelax" as the time required to reach this position
        # from a position in which the robot is sit down. Hence,
        # "M_SitRelax" has the precondition 'standing' == False.
        return False
    return True


def postcondition_standing(position):
    if position in ('M_Sit', 'M_SitRelax'):
        # In our case, this two moves are the only ones
        # that finish in a 'standing' == False state.
        return False
    return True


class NaoMove:
    """
    This class defines the information related
    to a particular move.
    """
    def __init__(self, duration=None, preconditions=None, postconditions=None):
        self.duration = duration
        self.preconditions = preconditions if preconditions is not None else {}
        self.postconditions = postconditions if preconditions is not None else {}


def main(robot_ip, port):
    # TODO: win the challenge :-)
    # The following ones are the moves made available to the robot:
    moves = {'StandUp':       NaoMove(8.35,  {'standing': False}, {'standing': True}),
             'AirGuitar':     NaoMove(4.10,   {'standing': True},  {'standing': True}),
             'ArmDance':      NaoMove(10.42, {'standing': True},  {'standing': True}),
             'BlowKisses':    NaoMove(4.58,  {'standing': True},  {'standing': True}),
             'Bow':           NaoMove(3.86,   {'standing': True},  {'standing': True}),
             'DiagonalRight': NaoMove(2.56,  {'standing': True},  {'standing': True}),
             'DanceMove':     NaoMove(6.13,  {'standing': True},  {'standing': True}),
             'SprinklerL':    NaoMove(4.14,   {'standing': True},  {'standing': True}),
             'SprinklerR':    NaoMove(4.36,  {'standing': True},  {'standing': True}),
             'RightArm':      NaoMove(9.19,  None, None),
             'TheRobot':      NaoMove(6.10,   {'standing': True},  {'standing': True}),
             'ComeOn':        NaoMove(3.62,   {'standing': True},  {'standing': True}),
             'StayingAlive':  NaoMove(5.90,   {'standing': True},  {'standing': True}),
             'Rhythm':        NaoMove(2.95,  {'standing': True},  {'standing': True}),
             'PulpFiction':   NaoMove(5.8,   {'standing': True},  {'standing': True}),
             'Wave':          NaoMove(3.72,  None, None),
             'Glory':         NaoMove(3.28,  None, None),
             'Clap':          NaoMove(4.10,  None, None),
             'Joy':           NaoMove(4.50,  None, None)}

    # The following is the order we chose for the mandatory positions:
    initial_pos = ('M_StandInit',       NaoMove(1.60))
    mandatory_pos = [('M_WipeForehead', NaoMove(4.48)),
                     ('M_Stand',        NaoMove(2.32)),
                     ('M_Hello',        NaoMove(4.34)),
                     ('M_Sit',          NaoMove(9.84)),
                     ('M_SitRelax',     NaoMove(3.92)),
                     ('M_StandZero',    NaoMove(1.4))]
    final_goal_pos = ('M_Crouch',       NaoMove(1.32))
    pos_list = [initial_pos, *mandatory_pos, final_goal_pos]
    number_of_steps = len(pos_list) - 1

    # Here we compute the total time lost during the
    # entire choreography for the execution of mandatory moves
    total_time = 0.0
    for pos in pos_list:
        total_time += pos[1].duration
    # We consider 'total_time' as being
    # evenly spread over each planning step:
    mean_time_lost_because_of_mandatory_positions = total_time / number_of_steps

    # Planning phase of the algorithm
    solution = tuple()
    print("PLANNED CHOREOGRAPHY:")
    start_planning = time.time()
    for index in range(1, len(pos_list)):
        # The planning is done in several distinct steps: each
        # one of them consists in solving a tree search in the space
        # of possible choreographies between a mandatory position
        # and the next one.
        starting_pos = pos_list[index - 1]
        ending_pos = pos_list[index]

        choreography = (starting_pos[0],)  # Initial choreography
        initial_standing = postcondition_standing(starting_pos[0])
        goal_standing = precondition_standing(ending_pos[0])
        remaining_time = 180.0/number_of_steps - mean_time_lost_because_of_mandatory_positions
        cur_state = (('choreography', choreography),
                     ('standing', initial_standing),
                     ('remaining_time', remaining_time),
                     ('moves_done', 0),
                     ('entropy', 0.0))
        cur_goal_state = (('standing', goal_standing),
                          ('remaining_time', 0),  # About this amount of time left
                          ('moves_done', 5),  # At least this number of moves done
                          ('entropy', 2.5 + 0.3*(index-1)))  # At least this entropy value

        # The partial solution is found with an Iterative Deepening Search algorithm.
        # We pass the full choreography built so far ('solution') to the class that
        # describes the problem ('NaoProblem'): this is because we chose to compute the
        # entropy of each possible partial choreography taking into account the entire sequence
        # of moves from the initial position of the dance to the current one. This helps
        # the algorithm to choose a partial solution which differs enough from the previous
        # ones (as it keeps the entropy of the full choreography above a given threshold).
        cur_problem = NaoProblem(cur_state, cur_goal_state, moves, 1, solution)
        cur_solution = iterative_deepening_search(cur_problem)
        if cur_solution is None:
            raise RuntimeError(f'Step {index} - no solution was found!')

        cur_solution_dict = from_state_to_dict(cur_solution.state)
        cur_choreography = cur_solution_dict['choreography']
        print(f"Step {index}: \t" + ", ".join(cur_choreography))
        solution += cur_choreography

    end_planning = time.time()
    solution += (final_goal_pos[0],)
    state_dict = from_state_to_dict(cur_solution.state)
    print("\nSTATISTICS:")
    print(f"Time required by the planning phase: %.2f seconds." % (end_planning-start_planning))
    print(f"Entropy of the solution found: {state_dict['entropy']}")
    print(f"Estimated choreography duration: {180.0 - state_dict['remaining_time']}")
    print("-------------------------------------------------------")
    
    # Dance execution
    print("\nDANCE EXECUTION:")
    play_song("Don't stop me now - Queen.mp3")
    start_dance = time.time()
    do_moves(solution, robot_ip, port)
    end_dance = time.time()
    print("Length of the entire choreography: %.2f seconds." % (end_dance-start_dance))


if __name__ == "__main__":

    robot_ip = "127.0.0.1"
    port = 9559  # Insert NAO port
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
        robot_ip = sys.argv[1]
    elif len(sys.argv) == 2:
        robot_ip = sys.argv[1]
    
    main(robot_ip, port)
