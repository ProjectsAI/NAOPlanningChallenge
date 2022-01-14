#AUTHOR: Stefano Ciapponi ID:0001030211
#TNMSA - Totally Non-Deterministic Move-Selection Algorithm
#GENERAL STATS:
#About 30% of moves are "almost" on time
#Time-Constraint tolerance = 0.1 seconds
import numpy as np
from treelib import Node, Tree
import time 

#Global Variables and CONSTANTS
BRANCHING_FACTOR = 4
count = 0
tree = Tree()

#Move Wrapper Class
class NaoMove:
    def __init__(self, name, duration=None, preconditions=None, postconditions=None):
        self.name = name
        self.duration = duration
        self.preconditions = preconditions if preconditions is not None else {}
        self.postconditions = postconditions if preconditions is not None else {}

#reset global variables
def setup(start):
    global tree 
    global count
    count = 0
    tree = Tree()
    tree.create_node(None, count, data=start)
    count += 1

#bpm = 121-> 2 beats/s -> 4/4 beat = 4 beats-> 2 seconds
#if moves before a move end in a multiple of 2 seconds -> match
#Function that computes time matching based on "DaftPunk - Around the World" bpm
def compute_matches(node):
    accumulator = 0
    counter = 0
    for move in node.data:
        accumulator += move.duration
        if accumulator%2 < 0.2:
            counter+=1
    return counter/len(node.data)

#Function that returns the total time-span of a solution by summating it's move durations.
def compute_time(node):
    return sum([move.duration for move in node.data])

#Re-implementation of the .index method starting from the last position in a list
def get_index(array, m):
    index = 0
    for x in array[::-1]:
        if x == m:
            return len(array)-index-1
        index += 1

#Search algorithm:
#It expands nodes based on an Heuristic h
#h: linear combination between the normalized duration of a Solution and the normalized number of beat matching position included
def search():
    global tree
    global BRANCHING_FACTOR
    alpha = 0.9
    beta = 1-alpha
    root = tree[0]
    #Heuristic computation for the Root Node
    times = [compute_time(root)]
    matches = [compute_matches(root)]
    h = [(alpha*compute_time(root)/180)+(beta*compute_matches(root))]
    best = root
    found = False
    while not found:
        expand(best.identifier)
        #Heuristic computation for each new expanded node
        for x in reversed(range(1, BRANCHING_FACTOR+1)):
            times = [*times, compute_time(tree[count-x])]
            matches = [*matches, compute_matches(tree[count-x])]
            h=[*h, (alpha*compute_time(tree[count-x])/180)+(beta*compute_matches(tree[count-x]))]
        m=max(h)
        #stop epoch if solutions get too big (time-wise)
        if max(times) > 182: 
        # if len(tree)>90:
            return False
        index=get_index(h, m)
        best = tree[index]
        #Check solution (According to empirically selected parameters)
        if times[index] > 179.9 and times[index] < 180.1 and m > 0.93 and m < 0.95:
            found = True
    return best
        
#Runs the expand_node function on a selected node BRANCHING_FACTOR times
def expand(node):
    global tree
    global count
    parent = tree[node]
    for x in range(BRANCHING_FACTOR):
        child = expand_node(parent.data)
        #tag = "".join(child)
        #print(tag)
        tree.create_node(None, count, data=child, parent=parent)
        count += 1

#Function in charge of expanding selected nodes.
#It creates a new feasible solution adding a random non-mandatory move before a randomly selected mandatory position 
#to the selected node's solution. (It also checks pre/post conditions)
def expand_node(parent):
    new = parent.copy()
    check = True
    while check:
        #select random mandatory position
        mand_pos = mandatory_pos[np.random.choice(range(len(mandatory_pos)))]
        #select random non mandatory position
        pos = moves[np.random.choice(range(len(moves)))]
        #Check if the Selected non mandatory move is compatible with the one 
        #before it (Mandatory Moves do not have pre/post conditions)
        if pos not in new[new.index(mand_pos)-2: new.index(mand_pos)]: #add preconditions/postconditions control
            if 'standing' in pos.preconditions and 'standing' in new[new.index(mand_pos)-1].postconditions:
                if pos.preconditions['standing'] == new[new.index(mand_pos)-1].postconditions['standing']:
                    new = [*new[:new.index(mand_pos)], pos, *new[new.index(mand_pos):]]
                    check = False
            else:
                new = [*new[:new.index(mand_pos)], pos, *new[new.index(mand_pos):]]
                check = False       
    return new

#Moves
moves = [   NaoMove('StandUp', 8.35,  {'standing': False}, {'standing': True}),
            NaoMove('AirGuitar', 4.10,   {'standing': True},  {'standing': True}),
            NaoMove('ArmDance', 10.42, {'standing': True},  {'standing': True}),
            NaoMove('BlowKisses', 4.58,  {'standing': True},  {'standing': True}),
            NaoMove('Bow', 3.86,   {'standing': True},  {'standing': True}),
            NaoMove('DiagonalRight', 2.56,  {'standing': True},  {'standing': True}),
            NaoMove('DanceMove', 6.13,  {'standing': True},  {'standing': True}),
            NaoMove('SprinklerL', 4.14,   {'standing': True},  {'standing': True}),
            NaoMove('SprinklerR', 4.36,  {'standing': True},  {'standing': True}),
            #NaoMove('RightArm', 9.19,  None, None),
            NaoMove('TheRobot', 6.10,   {'standing': True},  {'standing': True}),
            NaoMove('ComeOn', 3.62,   {'standing': True},  {'standing': True}),
            NaoMove('StayingAlive', 5.90,   {'standing': True},  {'standing': True}),
            NaoMove('Rhythm', 2.95,  {'standing': True},  {'standing': True}),
            NaoMove('PulpFiction', 5.8,   {'standing': True},  {'standing': True}),
            NaoMove('Wave', 3.72,  None, None),
            NaoMove('Glory', 3.28,  None, None),
            NaoMove('Clap', 4.10,  None, None),
            NaoMove('Joy', 4.50,  None, None)]

#Compulsory Moves
initial_pos = NaoMove('I_StandInit', 1.60)
mandatory_pos = [NaoMove('M_WipeForehead', 4.48),
                        NaoMove('M_Stand', 2.32),
                        NaoMove('M_Hello', 4.34),
                        NaoMove('M_Sit', 9.84),
                        NaoMove('M_SitRelax', 3.92),
                        NaoMove('M_StandZero',1.4)]
#Mandatory Moves are shuffled since there's no constraint which affects the order
np.random.shuffle(mandatory_pos)
final_goal_pos = NaoMove('F_Crouch', 1.32)

def search_coreography():
    #Initial Solution Composition
    start = [initial_pos, *mandatory_pos, final_goal_pos]
    print("Starting moves:",*[x.name for x in start], sep=' ► ')
    #Search Phase
    setup(start)
    b = False
    iteration_number = 0
    start_time = time.time()
    loading_animation = "⣾⣽⣻⢿⡿⣟⣯⣷ ⠁⠂⠄⡀⢀⠠⠐⠈"
    idx = 0
    # print("\nComputing Sequence:")
    #Search Method Epochs
    while not b:   
        # print("■", sep  = "", end = "", flush=True)
        print("Computing Sequence:",loading_animation[idx % len(loading_animation)], end="\r")
        idx += 1
        b = search()
        if not b:
            setup(start)
        iteration_number+=1


    #Results Printing
    end_time = time.time()
    print("\n\nComputing Time: {} seconds".format(end_time-start_time))
    print("Number of epochs:", iteration_number) 

    print("\n\nSTATS:\n\nBest Move Sequence:")
    print(*[x.name for x in b.data], sep=" ► ")
    print("\nTotal Time: {:}s".format(compute_time(b)))
    print("{}% moves match the Beat:\n{} Matches over {} moves".format(int(compute_matches(b)*100), int(compute_matches(b)*len(b.data)), len(b.data)))
    print("Nodes in the last Tree:", tree.size())
    move_list = [x.name for x in b.data]
    return move_list

if __name__ == "__main__":
	movee_list = search_coreography()

#check preconditions USED FOR DEBUGGING
"""
for i in range(len(b.data)-1):
    if 'standing' in b.data[i+1].preconditions and 'standing' in b.data[i].postconditions:
                if b.data[i].postconditions['standing'] == b.data[i+1].preconditions['standing']:
                    print(b.data[i+1].name,":OK")
"""
