import sys
import subprocess
import random
import re

from numpy.core.numeric import full
from aima.utils import *
from aima.search import *
from aima.planning import *

# Global variables

# Dictionary that contains all the preconditions for every move of the choreography
# value: moves that can be executed BEFORE the key-move
preconditions = {
    "RotationFeet": ["Hello", "Stand", "StandZero", "WipeForehead", "BlowKisses", "DanceMove", "Disco", "VOnEyes"],
    "ArmDanceDX": ["RotationFeet", "ArmDanceSX", "BirthdayDance", "Sprinkler1", "Sprinkler2", "Hello", "Stand", "StandZero", "WipeForehead", "DanceMove", "Disco", "ThrillerClap", "ThrillerArmSideways", "ThrillerSnapSnap", "VOnEyes"],
    "ArmDanceSX": ["RotationFeet", "ArmDanceDX", "BirthdayDance", "Sprinkler1", "Sprinkler2", "Hello", "Stand", "StandZero", "WipeForehead", "DanceMove", "Disco", "ThrillerClap", "ThrillerArmSideways", "ThrillerSnapSnap", "VOnEyes"],
    "BirthdayDance": ["RotationFeet", "ArmDanceDX", "ArmDanceSX", "Sprinkler1", "Sprinkler2", "Hello", "Stand", "StandZero", "WipeForehead", "DanceMove", "Disco", "ThrillerClap", "ThrillerArmSideways", "ThrillerSnapSnap", "VOnEyes"],
    "Sprinkler1": ["Hello", "Stand", "StandZero", "WipeForehead", "BlowKisses", "VOnEyes"],
    "Sprinkler2": ["Hello", "Stand", "StandZero", "WipeForehead", "BlowKisses", "VOnEyes"],
    # Sit and SitRelax can be a preconditions only of Stand and StandZero
    "Stand": ["RotationFeet", "BirthdayDance", "Hello", "StandZero", "WipeForehead", "DanceMove", "Disco", "VOnEyes", "Sit", "SitRelax"],
    "StandZero": ["RotationFeet", "ArmDanceDX", "ArmDanceSX", "BirthdayDance", "Hello", "Stand", "WipeForehead", "DanceMove", "Disco", "VOnEyes", "Sit", "SitRelax"],
    "WipeForehead": ["RotationFeet", "ArmDanceDX", "ArmDanceSX", "BirthdayDance", "Sprinkler1", "Sprinkler2", "Hello", "Stand", "StandZero", "DanceMove", "Disco", "ThrillerClap", "ThrillerArmSideways", "ThrillerSnapSnap", "VOnEyes"],
    "DanceMove": ["RotationFeet", "ArmDanceDX", "ArmDanceSX", "BirthdayDance", "Sprinkler1", "Sprinkler2", "Hello", "Stand", "StandZero", "WipeForehead", "Disco", "ThrillerClap", "ThrillerArmSideways", "ThrillerSnapSnap", "VOnEyes"],
    "Disco": ["RotationFeet", "ArmDanceDX", "ArmDanceSX", "BirthdayDance", "Sprinkler1", "Sprinkler2", "Hello", "Stand", "StandZero", "WipeForehead", "DanceMove", "ThrillerClap", "ThrillerArmSideways", "ThrillerSnapSnap", "VOnEyes"],
    "ThrillerClap": ["Hello", "WipeForehead", "BlowKisses", "DanceMove", "VOnEyes"],
    "ThrillerArmSideways": ["Hello", "WipeForehead", "BlowKisses", "DanceMove", "VOnEyes"],
    "ThrillerSnapSnap": ["Hello", "WipeForehead", "BlowKisses", "DanceMove", "VOnEyes"],
    "VOnEyes": ["RotationFeet", "ArmDanceDX", "ArmDanceSX", "BirthdayDance", "Sprinkler1", "Sprinkler2", "Hello", "Stand", "StandZero", "WipeForehead", "DanceMove", "Disco", "ThrillerClap", "ThrillerArmSideways", "ThrillerSnapSnap"],
    "Sit": ["Hello", "Stand", "StandZero", "WipeForehead", "DanceMove", "VOnEyes"],
    "SitRelax": ["Hello", "Stand", "StandZero", "WipeForehead", "DanceMove", "VOnEyes"],
    "BlowKisses": ["RotationFeet", "ArmDanceDX", "ArmDanceSX", "BirthdayDance", "Sprinkler1", "Sprinkler2",  "Stand", "StandZero", "WipeForehead", "DanceMove", "Disco", "ThrillerClap", "ThrillerArmSideways", "ThrillerSnapSnap", "VOnEyes", "Hello"],
    "Hello": ["StandInit", "RotationFeet", "ArmDanceDX", "ArmDanceSX", "BirthdayDance", "Sprinkler1", "Sprinkler2", "Stand", "StandZero", "WipeForehead", "DanceMove", "Disco", "ThrillerClap", "ThrillerArmSideways", "ThrillerSnapSnap", "VOnEyes"],
    "Crouch": ["RotationFeet", "BirthdayDance", "Stand", "StandZero", "WipeForehead", "DanceMove", "Disco", "VOnEyes"]
}

# list of mandatory moves
goals = ["StandInit", "Sit", "WipeForehead", "Hello", "SitRelax", "Stand", "StandZero", "Crouch"]

# number of moves executed between each subgoal
n_of_moves = 3


# This function cycle on the goals list and return the full planning
def find_full_planning(goals, preconditions):
    full_planning = []

	# cycle that find partial planning between sub_goals
    for i in range(len(goals) - 1):
        print("Finding subplan from " + goals[i] + " to " + goals[i + 1])
        # call to the function that finds the subplan
        subplan = find_partial_planning(preconditions, goals[i], goals[i + 1])
        #print(subplan)
        full_planning.extend(subplan)
        
    #print("THE FINAL PLANNING IS =>", full_planning)
    return full_planning


# preconditions: complete dictionary
# initial_state - final_state: mandatory sub_goals 
# Function that finds the sub-sub-goal -> the 5 moves between the initial_state and the final_state (sub_goals)
def find_partial_planning(preconditions, initial_state, final_state):
    partial_planning = []
    
	# copy of the precondition dictionary -> use the copy method to copy a dictionary and only edit the copy
    update_preconditions = preconditions.copy()
	
	# all the mandator moves (the sub-goals) are removed so we can pick random moves as sub-sub-goals
    for key in update_preconditions.copy(): # we use the copy to avoid errors like "changed dimension of the dictionary during iteration"
        if key in goals:
            update_preconditions.pop(key, 0)

    # search of the planning -> we try to find a planning with 6 move between the initial and final state
    partial_planning.extend(find_and_solve_subproblem(preconditions, initial_state, final_state))
    
    last_element = ""
    new_initial_state = ""

    # if partial_planning is empty (there are non intermidiate moves) the final_state is updated with a move randomly chosen from the update_preconditions
    if len(partial_planning) == 0:
        # final_position randomly taken from the update_preconditions
        new_final_state = random.choice(list(update_preconditions))
        partial_planning = find_and_solve_subproblem(update_preconditions, initial_state, new_final_state)
    # if partial_planning is not full, we take the last element and we set it as the new initial element
    elif len(partial_planning) != n_of_moves:
        last_element = str(partial_planning[-1])
        delimiters = "Move(", ",", " ", ")"	# Move(Hello, Sit), we take the move in the Hello position
        state = split(delimiters, last_element)[1]
        if state != "Sit" and state != "SitRelax":
			# we take the last move and we set it as the new initial state
            partial_planning.pop()
            new_initial_state = state
        else:
			# if the state is Sit or SitRelax -> the new initial state is the one that follow Sit/SitRelax
            new_initial_state = split(delimiters, last_element)[3]

	# cycle that finds sub-sub goal
    while len(partial_planning) < n_of_moves:
        
        # if len == n_of_moves - 1 we need the final sub_goal -> final_state
        if len(partial_planning) == (n_of_moves - 1):
            #partial_planning.extend(find_and_solve_subproblem(preconditions, new_initial_state, final_state))
            solution = find_and_solve_subproblem(preconditions, new_initial_state, final_state)
            partial_planning.extend(solution)
        # else we put in the new_final_state a random sub_sub_goal until we reach the limit of 5 moves
        else:
            new_final_state = random.choice(list(update_preconditions))
            partial_planning.extend(find_and_solve_subproblem(update_preconditions, new_initial_state, new_final_state))
            new_initial_state = new_final_state
    
    return partial_planning



# Definition of the knowledge base in PDDL = Planning Domain Definition Language, as follow:
# 	In(initial_state)	=> the initial state
# 	IsPrecondition('nameOfPosition1', 'nameOfPosition2')	=> the domain of preconditions: states that the position1 is a precondition of position2
# 	Action('Move(x, y)', precond = In(x), IsPrecondition(x, y), effect = In(y), ~In(x))		=> set of viable actions that can be executed in the search space of the problem
# 	In(final_state)		=> the final state
def find_and_solve_subproblem(preconditions, initial_state, final_state):
    knowledge_base = []
    positions = []

    # initial state = we add to the knowledge base (KB) the initial state
    knowledge_base.extend([expr('In(' + initial_state + ')')])

    # preconditions = we add the preconditions to the KB
    for key, content in preconditions.items():
        positions.append(key)
        for c in content:
            knowledge_base.append(expr('IsPrecondition(' + str(c) + ',' + str(key) + ')'))

    # move = we define the action that we can make in the KB
    move = Action('Move(x,y)',
                  precond = 'In(x) & IsPrecondition(x,y)',
                  effect = 'In(y) & ~In(x)')

    # we define the final state
    subgoal = 'In(' + final_state + ')'

	#We have defined the KB, know we define the Planning Problem

    # PlanningProblem - attributes essential to the definition of the problem:
	# an initial state
	# a set of goals -> (defined like a list [move] - usually more moves)
	# a set of viable actions that can be executed in the search space of the problem
    partial_problem = PlanningProblem(knowledge_base, subgoal, [move])

    # We search the partial_solution with GraphPlan
    partial_solution = []

    try:
        partial_solution.extend(GraphPlan(partial_problem).execute()) # not linearized, we need a list of strings
        partial_solution_lin = linearize(partial_solution) # return a linearized list -> [move(standinit, hello), move(hello, sit)]
    except:
        partial_solution_lin = []
    
    return partial_solution_lin


# takes the list moves of moves as input and NAO executes every move
def do_moves(moves, robot_ip, port):
    # Here we execute all the given moves
    # in a Python2 environment.
    for move in moves:
        print(f"Executing: {move}... ", end="", flush=True)
        python2_command = f"python2 ./moves/{move}.py  {robot_ip} {port}"
        process = subprocess.run(python2_command.split(), stdout=subprocess.PIPE)
        #print(process.stdout) # receive output from the python2 script


# split string given multiple separators
def split(delimiters, string, maxsplit=0):
    import re
    regexPattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexPattern, string, maxsplit)

def execute_in_python2(nameoffile):
    #print(f"Executing: {nameoffile}", end="", flush=True)
    python2_command = f"python2 ./{nameoffile}.py  {robot_ip} {port}"
    process = subprocess.run(python2_command.split(), stdout=subprocess.PIPE)
    #print(process.stdout) # receive output from the python2 script


def main(robot_ip, port):

	# return the full plan as a list
    full_planning = find_full_planning(goals, preconditions)

	# list that cointains the choreography's moves 
    choreography = []
    delimiters = "Move(", ",", " ", ")"

	# fill the list of moves from the full_planning list
    for move in full_planning:
        #print(str(move))
        splitted_move = split(delimiters, str(move))[1]
        choreography.append(splitted_move)

    # add the final state (Crouch) at the end of the choreography 
    choreography.append(goals[-1])
    print("I've choosen this choreography: ", choreography)

    # play music
    execute_in_python2("play_music")

    # execute of the choreography
    do_moves(choreography, robot_ip, port)

if __name__ == "__main__":
    robot_ip = "127.0.0.1"
    port = 9559  # Insert NAO port
    if len(sys.argv) > 2:
        port = int(sys.argv[2])
        robot_ip = sys.argv[1]
    elif len(sys.argv) == 2:
        robot_ip = sys.argv[1]
    main(robot_ip, port)

# . venv/bin/activate
# python3.7 planning_choreography.py localhost 35435