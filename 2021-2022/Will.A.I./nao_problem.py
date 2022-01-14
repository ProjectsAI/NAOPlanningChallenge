#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from aima.search import Problem
from utils import from_state_to_dict, entropy_calc


class NaoProblem(Problem):

    def __init__(self, init, goal, moves, avg_time, previous_moves):
        super().__init__(init, goal)
        # We save the moves set
        self.available_moves = moves
        # List representing the past steps
        self.previous_moves = previous_moves
        # Average time for our move set
        self.avg_time = avg_time

    # Function that evaluates if a move is usable after a certain state
    def move_usable(self, state, move_name, move):
        # We used a util function to convert the state in a dictionary
        state_dict = from_state_to_dict(state)

        # Check if there is enough time in the current step to chose this move
        if state_dict['remaining_time'] < move.duration:
            return False

        # Check if the preconditions are satisfied (standing/sitting)
        if 'standing' in move.preconditions:
            if state_dict['standing'] != move.preconditions['standing']:
                return False

        # Check if the move is different from the last two in the choreography
        size = len(state_dict['choreography'])
        if size > 1:
            if move_name == state_dict['choreography'][-1] or move_name == state_dict['choreography'][-2]:
                return False
        if len(self.previous_moves) > 5:
            if move_name == self.previous_moves[-1] or move_name == self.previous_moves[-2] or move_name == self.previous_moves[-3] or \
                    move_name == self.previous_moves[-4] or move_name == self.previous_moves[-5]:
                return False
        return True

    # Std function used in AIMA Lib to evaluate usable action
    def actions(self, state):
        usable_actions = []
        # We cycle trough the moves set and check each for usability from current state
        for move_name, move in self.available_moves.items():
            if self.move_usable(state, move_name, move):
                # The moves that satisfy our condition are added to the result
                usable_actions.append(move_name)
        # We shuffle the result list to increase diversity in the final solution
        random.shuffle(usable_actions)
        return usable_actions

    # Std function used in AIMA Lib to evaluate the resulting state of an action
    def result(self, state, action):
        # We already checked the action in the actions function so they are valid
        nao_move = self.available_moves[action]
        # We used a util function to convert the state in a dictionary
        state_dict = from_state_to_dict(state)

        # We create a temp choreography, including past steps, to later calculate its entropy
        temp_choreography = [*self.previous_moves, *state_dict['choreography'], action]
        # Now we calculate the entropy of the temp choreography using a util function
        temp_entropy = entropy_calc(temp_choreography)

        # We set the postcondition of this action
        if 'standing' in nao_move.postconditions:
            temp_standing = nao_move.postconditions['standing']
        else:
            # If the action don't modify the standing state we keep the last one
            temp_standing = state_dict['standing']

        return (('choreography', (*state_dict['choreography'], action)),
                ('standing', temp_standing),
                ('remaining_time', state_dict['remaining_time'] - nao_move.duration),
                ('moves_done', state_dict['moves_done'] + 1),
                ('entropy', temp_entropy))

    # Std function used in AIMA Lib to check if the goal state is reached
    def goal_test(self, state):
        # Given a state, return True if state is a goal state or False, otherwise
        # We used a util function to convert the state in a dictionary
        state_dict = from_state_to_dict(state)
        goal_dict = from_state_to_dict(self.goal)

        # We create an interval to check if we filled the time slot for this step
        goal_remaining_time = goal_dict['remaining_time']
        a = goal_remaining_time
        b = goal_remaining_time + 1

        # We check if all our condition are met
        # Check if we filled the time slot for this step
        time_constraint = (a <= state_dict['remaining_time'] <= b)
        # Check if we chose enough moves for this step
        moves_done_constraint = (state_dict['moves_done'] >= goal_dict['moves_done'])
        # Check if we chose moves that are diverse enough
        entropy_constraint = (state_dict['entropy'] >= goal_dict['entropy'])
        # Check if we reached our goal standing state
        standing_constraint = (state_dict['standing'] == goal_dict['standing'])
        return time_constraint and moves_done_constraint and entropy_constraint and standing_constraint

    # Heuristic function used in A* search
    def h(self, node):
        # We implemented a simple heuristic that estimates the cost to reach the goal
        # by multiplying the number of remaining moves to the avg_time of our moves set
        state_dict = from_state_to_dict(node.state)
        goal_dict = from_state_to_dict(self.goal)
        return (goal_dict['moves_done'] - state_dict['moves_done']) * self.avg_time
