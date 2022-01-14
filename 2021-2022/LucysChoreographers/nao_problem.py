#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

from aima.search import Problem


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

class NaoProblem(Problem):

    def __init__(self, initial, goal, moves):
        super().__init__(initial, goal)
        self.available_moves = moves

    def is_move_applicable(self, state, move_name, move):
        # Here we check what moves can be executed
        state_dict = from_state_to_dict(state)
        last_move = state_dict['choreography'][-1]
        move_index = len(state_dict['choreography'])

        # 1: check if we have enough time
        if state_dict['remaining_time'] < move.duration:
            return False

        # 2: check if the preconditions are satified
        if 'standing' in move.preconditions:
            if state_dict['standing'] != move.preconditions['standing']:
                return False

        # 3: avoid repeating moves
        if move_name == last_move:
            return False

        # 4: avoid repeating mandatory moves
        if move_index == 5:
            if move_name in ['StandInit','WipeForehead','Stand','Hello','Sit','SitRelax','StandZero']:
               return False

        # 5: constraint for AirGuitar move
        if last_move == 'AirGuitar':
           if move_name in ['StandInit','Stand','StandZero','Sit','HeadMove','Crouch','HulaHoop','Kick','FootSteps']:
              return False 
        
        if move_index == 5 and move_name == 'AirGuitar':
           return False

        return True

    def actions(self, state):
        actions = []
        time = 0
        state_dict = from_state_to_dict(state)
        for move_name, move in self.available_moves.items():
            if self.is_move_applicable(state, move_name, move):
                actions.append(move_name)
        random.shuffle(actions)
        return actions

    def result(self, state, action):
        move = self.available_moves[action]
        state_dict = from_state_to_dict(state)

        if 'standing' in move.postconditions:
            new_standing = move.postconditions['standing']
        else:
            new_standing = state_dict['standing']

        return (('choreography', (*state_dict['choreography'], action)),
                ('standing', new_standing),
                ('remaining_time', state_dict['remaining_time'] - move.duration),
                ('moves_done', state_dict['moves_done'] + 1))

    def goal_test(self, state):
        #True if state is a goal
        state_dict = from_state_to_dict(state)
        goal_dict = from_state_to_dict(self.goal)

        moves_done_constraint = (state_dict['moves_done'] >= goal_dict['moves_done'])
        standing_constraint = (state_dict['standing'] == goal_dict['standing'])
        

        if goal_dict['standing'] is None:
            # No standing precondition 
            return moves_done_constraint
        else:
            return moves_done_constraint and standing_constraint
