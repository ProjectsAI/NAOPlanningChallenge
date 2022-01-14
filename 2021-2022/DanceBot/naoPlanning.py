import random
from search import Problem


class NaoProblem(Problem):

    def __init__(self, initial, goal, intermediatePos, solution):
        super().__init__(initial, goal)
        self.intermediatePos = intermediatePos
        self.solution = solution

    def checkMove(self, state, next_move_name,
                  next_move):  # next_move is the list which contains preconditions, postconditions, duration
        # Here we select possible intermediate positions
        state_dict = dict()
        for a in state:
            len_a = len(a)
            if len_a < 2:
                continue
            key = a[0]
            if len_a > 2:
                value = a[1:]
            else:
                value = a[1]
            if key not in state_dict:
                state_dict[key] = value

        # Check if there is enough time to complete the next_move
        if state_dict['intermediate_time'] < next_move[2]:  # move[2] is the duration of the next_move
            return False

        # Check if the preconditions of the next_move are respected in the current state
        if 'isStanding' in next_move[0]:
            if state_dict['isStanding'] != next_move[0]['isStanding'] and state_dict['isStanding'] is not None and \
                    next_move[0]['isStanding'] is not None:
                return False

        # Check if the move is different from the previous one
        prev_move = state_dict['namePos'][-1]
        if next_move_name == prev_move:
            return False

        # We can accept the move if all the constraints are satisfied
        return True

    def actions(self, state):
        # Return the actions accepted in the given state
        accepted_actions = []
        for intermediate_pos_name, intermediate_pos in self.intermediatePos.items():
            if self.checkMove(state, intermediate_pos_name, intermediate_pos):
                accepted_actions.append(intermediate_pos_name)
        random.shuffle(accepted_actions)
        return accepted_actions

    def result(self, state, action):
        # This function returns a new state, which is the result of the action
        move = self.intermediatePos[action]

        state_dict = dict()
        for a in state:
            len_a = len(a)
            if len_a < 2:
                continue
            key = a[0]
            if len_a > 2:
                value = a[1:]
            else:
                value = a[1]
            if key not in state_dict:
                state_dict[key] = value

        # Here we get the postconditions of the move and compute the new 'isStanding' value
        if 'isStanding' in move[1]:  # move[1] are the postconditions of move[1]
            # Get the postconditions of this move
            new_isStanding = move[1]['isStanding']
        else:
            new_isStanding = state_dict['isStanding']

        return (('namePos', (state_dict['namePos'], action)),
                ('isStanding', new_isStanding),
                ('intermediate_time', state_dict['intermediate_time'] - move[2]),
                ('moves_done', state_dict['moves_done'] + 1),
                )

    def goal_test(self, state):
        # Given a state, return True if state is a goal state or False, otherwise
        state_dict = dict()
        for a in state:
            len_a = len(a)
            if len_a < 2:
                continue
            key = a[0]
            if len_a > 2:
                value = a[1:]
            else:
                value = a[1]
            if key not in state_dict:
                state_dict[key] = value

        goal_dict = dict()  # (self.goal)
        for a in self.goal:
            len_a = len(a)
            if len_a < 2:
                continue
            key = a[0]
            if len_a > 2:
                value = a[1:]
            else:
                value = a[1]
            if key not in goal_dict:
                goal_dict[key] = value

        goal_available_time = goal_dict['intermediate_time']
        x = goal_available_time
        y = goal_available_time + 1  # 1 is a threshold

        # Checking the constraints
        time_constraint = (x <= state_dict['intermediate_time'] <= y)
        moves_done_constraint = (state_dict['moves_done'] >= goal_dict['moves_done'])
        isStanding_constraint = (state_dict['isStanding'] == goal_dict['isStanding'])

        if goal_dict['isStanding'] is None:
            # If the preconditions are 'None', we can accept all the postconditions of the moves
            return time_constraint and moves_done_constraint
        else:
            # On the contrary, we have to consider the isStanding_constraint
            return time_constraint and moves_done_constraint and isStanding_constraint
