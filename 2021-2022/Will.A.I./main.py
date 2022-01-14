#!/usr/bin/python
# -*- coding: utf-8 -*-

from aima.search import *
from nao_problem import NaoProblem
from utils import *

# Function to determine the initial standing state and prerequisites
def precondition_stand(pos):
    if pos == 'M_SitRelax':
        # Is the only position that requires the sitting prerequisite
        return False
    return True

# Function to determine the final standing state and postconditions
def postcondition_stand(pos):
    if pos in ('M_Sit', 'M_SitRelax'):
        # In the moves we chosen, these are the only ones
        # that result in a not standing state.
        return False
    return True

class NaoMove:

    def __init__(self, duration=None, preconditions=None, postconditions=None):
        self.duration = duration
        self.preconditions = preconditions if preconditions is not None else {}
        self.postconditions = postconditions if preconditions is not None else {}

def main(ip, port):
    # These moves are available to robot.
    # We averaged the exec time of each move and we defined preconditions and postconditions.

    moves = {'StandUp': NaoMove(9.0, {'standing': False}, {'standing': True}),
                  'DiagonalLeft': NaoMove(4.0, None, {'standing': True}),
                  'DoubleMovement': NaoMove(3.70, None, None),
                  'MoveBackward': NaoMove(4.0, None, {'standing': True}),
                  'MoveForward': NaoMove(4.0, None, {'standing': True}),
                  'RotationFootLLeg': NaoMove(6.10, {'standing': True}, {'standing': True}),
                  'RotationFootRLeg': NaoMove(6.10, {'standing': True}, {'standing': True}),
                  'RotationHandgun': NaoMove(6.0, None, None),
                  'Union_arms': NaoMove(9.10, None, None),
                  'ArmsOpening': NaoMove(4.30, None, None),
                  'ArmDance': NaoMove(10.42, {'standing': True}, {'standing': True}),
                  'BlowKisses': NaoMove(4.75, {'standing': True}, {'standing': True}),
                  'Bow': NaoMove(4.30, {'standing': True}, {'standing': True}),
                  'DiagonalRight': NaoMove(2.95, {'standing': True}, {'standing': True}),
                  'DanceMove': NaoMove(6.50, {'standing': True}, {'standing': True}),
                  'SprinklerL': NaoMove(4.35, {'standing': True}, {'standing': True}),
                  'SprinklerR': NaoMove(4.45, {'standing': True}, {'standing': True}),
                  'TheRobot': NaoMove(6.10, {'standing': True}, {'standing': True}),
                  'ComeOn': NaoMove(4.00, {'standing': True}, {'standing': True}),
                  'StayingAlive': NaoMove(5.90, {'standing': True}, {'standing': True}),
                  'Rhythm': NaoMove(3.20, {'standing': True}, {'standing': True}),
                  'PulpFiction': NaoMove(5.9, {'standing': True}, {'standing': True}),
                  'RightArm': NaoMove(9.19, None, None),
                  'Wave': NaoMove(3.72, None, None),
                  'Glory': NaoMove(3.45, None, None),
                  'Clap': NaoMove(4.30, None, None),
                  'Joy': NaoMove(5.00, None, None)}

    # Fixed order of mandatory positions:
    start_pos = ('M_StandInit', NaoMove(1.80))
    mandatory_pos = [('M_WipeForehead', NaoMove(4.80)),
                     ('M_Stand', NaoMove(2.7)),
                     ('M_Hello', NaoMove(4.6)),
                     ('M_Sit', NaoMove(10.2)),
                     ('M_SitRelax', NaoMove(4.15)),
                     ('M_StandZero', NaoMove(1.6))]
    end_pos = ('M_Crouch', NaoMove(1.55))
    pos_list = [start_pos, *mandatory_pos, end_pos]
    # We account time lost for the execution of mandatory moves
    total_time = 0.0
    for pos in pos_list:
        total_time += pos[1].duration
    # We calculate the average time of the moves set using a simple mean
    avg_time = 0.0
    for pos in moves:
        avg_time += moves[pos].duration
    avg_time = avg_time/len(moves)

    # Now we can start planning the solution
    solution = tuple()
    print("SOLUTION:")
    start_planning = time.time()
    # We initialize the var to the time available to complete each step
    remaining_time = (180 - total_time) / (len(pos_list) - 1)
    # Var used to keep track of the remaining time at the end of a step
    change = 0.0
    for index in range(1, len(pos_list)):
        # Dividing the problem in 7 steps, each one is solved using A* search
        # then choosing a solution based on constraints
        s_pos = pos_list[index - 1]
        e_pos = pos_list[index]

        choreography = (s_pos[0],)  # Initial state
        initial_standing = postcondition_stand(s_pos[0])
        goal_standing = precondition_stand(e_pos[0])
        # We defined entropy targets that allow us to get a diverse choreography
        # If we chose a value too high we couldn't find a solution in every step
        entropy = [1, 2.5, 3.4, 3.9, 4, 4, 2.8, 4.4]
        cur_state = (('choreography', choreography),
                     ('standing', initial_standing),
                     # At each iteration we add the residual time from the previous iteration
                     ('remaining_time', remaining_time+change),
                     ('moves_done', 0),
                     ('entropy', 0.0))
        cur_goal_state = (('standing', goal_standing),
                          ('remaining_time', 0),
                          # Minimum number of moves in each step
                          ('moves_done', 5),
                          # Entropy target to achieve in this step
                          ('entropy', entropy[index]))

        # We defined the initial state and goal state for this step and now we pass it to A* search
        # with also the choreography planned so far to calculate its entropy
        cur_problem = NaoProblem(cur_state, cur_goal_state, moves, avg_time,solution)
        cur_solution = astar_search(cur_problem)
        if cur_solution is None:
            raise RuntimeError(f'In step {index} i could not find a solution!')

        cur_solution_dict = from_state_to_dict(cur_solution.state)
        cur_choreography = cur_solution_dict['choreography']
        print(f"Step {index}:")
        for m in cur_choreography:
            print("\t"+m)
        # Here we save the remaining time
        change = cur_solution_dict['remaining_time']
        solution += cur_choreography

    end_planning = time.time()
    solution += (end_pos[0],)
    # We used a utility function to help us printing the solution in neater way
    state_dict = from_state_to_dict(cur_solution.state)

    # Now we start executing the dance
    print("\nLET'S DANCE:")
    print("\n┗(＾0＾)┓  ┏(＾0＾)┛")
    # Starting the soundtrack
    play_song("the-black-eyed-peas-boom-boom-pow-edit2.mp4")
    start_dance = time.time()
    do_moves(solution, ip, port)
    end_dance = time.time()
    print("\nDATA COLLECTED:")
    print(f"Planning Time: %.2f s." % (end_planning - start_planning))
    print(f"Entropy: {state_dict['entropy']}")
    print(f"Estimated duration: {180.0 - state_dict['remaining_time']}")
    print("Real duration: %.2f seconds." % (end_dance - start_dance))


if __name__ == "__main__":

    robot_ip = "127.0.0.1"
    port = 9559  # Standard NAO port
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
        robot_ip = sys.argv[1]
    elif len(sys.argv) == 2:
        robot_ip = sys.argv[1]

    main(robot_ip, port)
