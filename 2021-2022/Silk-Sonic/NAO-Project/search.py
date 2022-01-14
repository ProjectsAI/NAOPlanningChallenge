from moves import *
import random

# mandatory moves, the main function will iterate trough these, in this order
mandatory = [standinit, hello, stand, sit, sit_relax, wipe_forehead, standzero, crouch]
# possible intermediate moves, which will be taken into account when creating the subsequence
possible_moves = [sitting_wavess, sprinkler, guitar, rotation_foot_rleg, finger_snap, sitting_handkiss, union_arms,
                  arms_opening, sitting_mood, proud, disco, dab, rotation_handgun, high_clap, arm_drag, whip]


# algorithm that finds the subsequence of moves, choosing the ones that respect the constraints
def generate_transition(past_moves):
    # total elapsed time since the main function has started
    tot_time = total_time(past_moves)

    # in case the total time exceeds 170, no new subsequence will be generated -> the next moves will only be
    # mandatory ones
    if tot_time >= 170:        
        return []
    # if the last move performed is crouch, no further subsequences will be generated
    if past_moves[-1] == crouch:
        return []

    else:
        # shuffle the list of possible moves
        random.shuffle(possible_moves)
        sequence = []
        count = 0
        sequence_time = 0

        # if the post condition of the previous move is True (it means NAO is standing)
        if past_moves[-1].post:
            for i in possible_moves:

                # set of constraints (technical and style) that a move has to comply with:
                # 1) technical: pre condition of the move must be True (standing)
                # 2) technical: the sequence is composed of maximum 4 elements
                # 3) style: the move should not be in the last 4 -> prevent a repetitive movement
                # 4) style: the move can be used maximum 3 times in the entire choreography
                # 5) technical: constraint: the maximum time spent for a sequence cannot exceed 30 seconds
                if i.pre and count <= 4 and i not in past_moves[:-5:-1] and past_moves.count(
                        i) <= 3 and (sequence_time + i.t) <= 30:

                    # towards the end of the iteration through mandatory moves, it can happen that the time left
                    # is not enough, and the sequence could be too long and exeed max time ,
                    # this check prevents this and exits the sequence generation early
                    if end_sequence(tot_time, sequence_time):
                        return sequence

                    # style additional constraint: if the last move performed is one pf the static mandatory
                    # submoves, such as rotation_handgun of opening_arms (which are poor style wise), then the next
                    # move cannot be another static mandatory moves, in order to give more fluidity to the movements
                    if len(sequence) != 0:
                        if not (sequence[-1].mandatory_submove == i.mandatory_submove):
                            sequence, sequence_time, count = add_move_to_sequence(sequence, sequence_time, count, i)

                    else:
                        sequence, sequence_time, count = add_move_to_sequence(sequence, sequence_time, count, i)

        # if post condition is False (NAO is sitting)
        else:
            for i in possible_moves:

                # similar constraints to the standing case
                if not i.pre and count <= 2 and i not in past_moves[:-5:-1] and past_moves.count(
                        i) <= 2 and sequence_time + i.t < 30:

                    if end_sequence(tot_time, sequence_time):
                        return sequence

                    sequence, sequence_time, count = add_move_to_sequence(sequence, sequence_time, count, i)

        return sequence


def total_time(past_moves):
    tot_time = 0
    for i in past_moves:
        tot_time += i.t
    return tot_time


def end_sequence(tot_time, sequence_time):
    if (tot_time + sequence_time) >= 170:
        return True


def add_move_to_sequence(sequence, sequence_time, count, i):
    sequence.append(i)
    sequence_time += i.t
    count += 1
    return sequence, sequence_time, count
