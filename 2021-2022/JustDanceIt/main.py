import numpy as np
import random

# from search import *
# from collections import defaultdict, deque, Counter
# from reporting import *

from constants import *
from movements import *
from nao_problem import *
from func import *

random.seed(17)
np.random.seed(17)


def main(ROBOT_IP, PORT, SONG):

    # =============================================================================
    #               The algorithm is based on bars, aka "measures"
    # A bar is a segment of time corresponding to a specific number of beats.
    # =============================================================================

    print("\n############\nJustDanceIt\n############")

    total_time = get_duration_from_song(SONG) #seconds
    print("\nSong duration: {} seconds".format(total_time))

    """This is the number of intervals between mandatory positions"""
    INTERVALS_BETWEEN_MANDATORY_POSITIONS = 7
    MIN_MOVEMENTS_PER_INTERVAL = 5

    """
    First of all, we need to know the bpm and time signature of the selected song, because, 
    the algorithm will choose the sequence of movements, according to these parameters.
    """
    bpm = get_bpm_from_song(SONG)
    print("BPM: {}".format(bpm))
    """In this case we work under the assumption that the song has as time signuture 4/4"""
    num_beats_per_bar = 4
    """This is the number of bars per minute"""
    num_bars = bpm/num_beats_per_bar
    """This is the time in seconds of a bar"""
    bar_time = 60/num_bars #seconds
    """
    For sake of semplicity, at the beginning we split the total amount of time 
    into 7 intervals with the same duration (in seconds).
    Then, we will work on these intervals in order to avoid wasting time and 
    to allow the algorithm to reach the goal in every interval. 
    """
    interval_time = total_time/INTERVALS_BETWEEN_MANDATORY_POSITIONS

    """These are the times of the mandatory movements according to the sequence of mandatory positions"""
    times_mandatory_movements = [MANDATORY_MOVEMENTS[mandatory_pos][MIN_TIME] for mandatory_pos in mandatory_positions ][1:]
    """These are times available for non mandatory movements in each interval"""
    available_times = np.ones((7,)) * interval_time - times_mandatory_movements

    """
    In order to allow an easier computation of the sequence of movements and to allow
    the robot to dance following the beat, 
    we transformed the available times into available bars.
    """
    available_bars = available_times/bar_time

    """We order the non-mandatory movements by increasing min-time"""
    nn_mandatory_movements_sorted = sorted(NON_MANDATORY_MOVEMENTS, key = lambda mov: NON_MANDATORY_MOVEMENTS[mov][MIN_TIME])

    """
    First of all, we want to ensure that the algorithm will not fail during the execution.
    For this reason, we start looking for all the intervals in which it is not possible to
    reach the gaol, so all the intervals in which the number of available bars is less than 
    the minimum number of bars necessary to reach the minimum goal of 5 movements per interval
    We talk about the minimum number because we have sorted the list of non-mandatory
    movements by increasing time.
    Furthermore, we filter the non-mandatory movements by post and pre conditions of the
    previous and next mandatory movements, respectively, as a prevision of what 
    will happen in the phase of the search execution.
    """
    isUnderThr = []
    num_min_bars = []
    for i in range(len(mandatory_positions) - 1):
        nn_mandatory_movements_sorted_filtered = filter_by_pre_post_conditions(nn_mandatory_movements_sorted, MANDATORY_MOVEMENTS[mandatory_positions[i]][POSTCONDITIONS][0])
        bars_nn_mandatory_movements_sorted_filtered = [from_time_to_bars(NON_MANDATORY_MOVEMENTS[mov][MIN_TIME], bar_time) for mov in nn_mandatory_movements_sorted_filtered]
        num_min_bars.append(np.sum(bars_nn_mandatory_movements_sorted_filtered[:MIN_MOVEMENTS_PER_INTERVAL]))
        isUnderThr.append(available_bars[i] < num_min_bars[i])

    """
    After finding the intervals in which we do not have enough available bars,
    bars are redistributed, in particular from the over threshold intervals to
    the under threshold intervals, randomly.
    """
    under_thr = np.where(isUnderThr == True)[0]
    over_thr = np.where(isUnderThr == False)[0]
    random.shuffle(over_thr)

    for j in range(len(under_thr)):
        k = 0
        while available_bars[under_thr[j]] < num_min_bars[under_thr[j]]:
            
            if available_bars[over_thr[k]] - 1 >= num_min_bars[over_thr[k]]:
                available_bars[under_thr[j]] += 1
                available_bars[over_thr[k]] -= 1
            
            k = (k+1)%len(over_thr)

    """
    At the end, it is preferable to have an integer number of available bars per interval, 
    and for this purpose, a cast to integer is applied, but being careful to not waste bars.
    So, a further redistribution is applied randomly.
    """
    excess = 0
    for j in range(len(available_bars)):
        excess += available_bars[j] - int(available_bars[j])
        available_bars[j]= int(available_bars[j])
    excess = int(excess)

    rnd_idx = np.asarray((np.random.random(size = (excess,))*1000)%len(available_bars), 
                        dtype = int)
    for i in rnd_idx:
        available_bars[i] += 1

    """
    For a matter of style, the movements are split into two classes, according to their 
    min-time duration. 
    For this purpose, we take into account how many times, the non-mandatory movements 
    are used in the choreography.
    """
    mean_time = np.mean([NON_MANDATORY_MOVEMENTS[mov][MIN_TIME] for mov in NON_MANDATORY_MOVEMENTS])
    shorter = [mov for mov in NON_MANDATORY_MOVEMENTS if NON_MANDATORY_MOVEMENTS[mov][MIN_TIME] < mean_time]
    longer = [mov for mov in NON_MANDATORY_MOVEMENTS if NON_MANDATORY_MOVEMENTS[mov][MIN_TIME] >= mean_time]

    """Classes creation"""
    movements_classes = {}
    for mov in shorter:
        movements_classes[mov] = 1
        
    for mov in longer:
        movements_classes[mov] = 0

    movements_count = {}

    """Count reset"""
    for mov in NON_MANDATORY_MOVEMENTS:
        movements_count[mov] = 0

    """STATE (movements_done_list, num_bars_exploited, (position, legs))"""
    """PATTERN ((),0,('standing', True))"""
    f = open(OUTPUT_FILE, "w")

    excess = 0
    for i in range(len(mandatory_positions) - 1):
        initial_position = MANDATORY_MOVEMENTS[mandatory_positions[i]][POSTCONDITIONS][0]
        """
        In order to control some movements, it is important to keep track of the position
        of the legs.
        Initial legs configuration depends on the phase in which the algorithm is.
        """
        if i == 0:
            initial_legs = MANDATORY_MOVEMENTS[mandatory_positions[i]][LEGS]
        else:
            initial_legs = states[len(states)-1][BODY][LEGS_POSITION]

        initial = ((),0,(initial_position, initial_legs))
        
        """
        In the search strategy, a limited depth alogorithm is used with a limit of the depth
        that is grater than or equal to 5.
        This fragment of code is used in order to compute the maximum depth limit that it is
        possible to achieve in each interval.
        Then, in order to avoid wasting bars, it is necessary to compute the maximum number of 
        bars that will be used withouth problems, because we want to use all the available bars, 
        resulting in a maximized solution
        """
        bars_needed = 0
        num_max_movements = 0
        
        nn_mandatory_movements_sorted_filtered = filter_by_pre_post_conditions(nn_mandatory_movements_sorted, MANDATORY_MOVEMENTS[mandatory_positions[i]][POSTCONDITIONS][0])
        available_bars[i] += excess
        excess = 0
        for j in range(len(nn_mandatory_movements_sorted_filtered)):
            if (bars_needed + from_time_to_bars(NON_MANDATORY_MOVEMENTS[nn_mandatory_movements_sorted_filtered[j]][MIN_TIME], bar_time)) <= available_bars[i]:
                bars_needed += from_time_to_bars(NON_MANDATORY_MOVEMENTS[nn_mandatory_movements_sorted_filtered[j]][MIN_TIME], bar_time)
            else:
                num_max_movements = j
                break
        
        if num_max_movements == 0:
            num_max_movements = len(nn_mandatory_movements_sorted_filtered)
        
        """
        The prevision of the possible excess of bars is done here.
        In the case in which, it is not possible to reach a maximum solution with 
        the initial available bars, it is computed the number of exceeding measures.
        This excess will be used in the next interations, so in the next intervals.
        """
        excess = available_bars[i] - bars_needed
        
        """
        Here, a nao problem is initialized with the initial state and with 
        the goal state.
        The purpose is to reach at least 5 movements per interval, using all the given
        bars and with the guaranty that post-conditions and preconditions are satisfied.
        """
        goal_position = MANDATORY_MOVEMENTS[mandatory_positions[i+1]][PRECONDITIONS]
        goal = (MIN_MOVEMENTS_PER_INTERVAL, bars_needed,goal_position)
        nao = NAO(initial, goal, bar_time, movements_count, movements_classes)
        
        print("\n-----------------------------------\n")
        print("Initial:{}".format(initial))
        print("Goal:\t{}\n".format(goal))
        
        """
        The depth limit search will find the path to the solution, and each level of the 
        tree corresponds to a movement. So, this uninformed search strategy is expected to 
        find a solution with a number of levels(movements) >=5 and <= limit(num_max_movements).
        """
        soln = depth_limited_search(nao, limit = num_max_movements)
        actions = path_actions(soln)
        
        """
        In this snippet of code, the number of times in which the movements are used, is updated
        """
        for action in actions:
            movements_count[action] += 1*(movements_classes[action] + 1)
        
        print("ACTIONS:", actions)
        states = path_states(soln)
        bars_exploited = states[len(states) - 1][1]
        print("STATES:\t",states)
        
        generate_choreography(actions, states, bar_time, i, f)

    f.close()

    do_choreography(ROBOT_IP, PORT, SONG)


if __name__ == "__main__":
    ROBOT_IP = "127.0.0.1"
    PORT = 9559
    SONG = None

    if len(sys.argv) == 3:
        ROBOT_IP = sys.argv[1]
        SONG = sys.argv[2]
    else:
        ROBOT_IP = sys.argv[1]
        PORT = int(sys.argv[2])
        SONG = sys.argv[3]

    print("robotIP: {}\nport: {}".format(ROBOT_IP, PORT))

    main(ROBOT_IP, PORT, SONG)