import numpy as np
import random

from search import *
from collections import defaultdict, deque, Counter
from reporting import *

from constants import *
from movements import *
from func import *

random.seed(17)


"""
NAO_STATE = [MOVEMENTS_DONE, BARS_EXPLOITED, [BODY_POSITION, LEGS_POSITION]]
"""

class NAO(Problem):
    def __init__(self, initial, goal, bar_time, movements_classes, movements_count):
        """Constructor"""
        self.initial = initial
        self.goal = goal
        self.bar_time = bar_time
        self.movements_classes = movements_classes
        self.movements_count = movements_count
        Problem.__init__(self, initial, goal)
    
    """
    This function checks whether it is possible to reach at least 5 movements per interval. 
    When the agent reaches 5 movements this function returns always True.
    This algorithm is a sort of heuristic that helps the agent to find the correct sequences 
    of actions.
    It guarantees that if a specific movement was chosen after the states expansion, 
    there would not be problems, in the pursuit of reaching the goal
    In short, it guarantees that if we chose a specific movement, then we would have 
    enough bars in order to reach the minimum of 5
    """
    def isValid(self, state, movement, available_movements):
        """
        The algorithm deletes the movement that maybe will be chosen by the agent 
        from the list of the available movements. 
        This is done for a matter of style
        """
        available_movements = [mov for mov in available_movements if mov != movement]
        """The movements must be sorted by increasing time"""
        available_movements = sorted(available_movements, key = lambda mov : NON_MANDATORY_MOVEMENTS[mov][MIN_TIME])
        
        #These store the variables
        movements_done, bars_exploited, body = state
        movements_done = list(movements_done)
        position, legs = body
        
        """
        This is the number of the necessary movements needed to reach the 
        minimum of 5 movements.
        In the case in which the number of movements done is greater than or equal to 5, 
        the num_movements_tobe_performed variable will be negative.
        It does not matter because it means that we have reached the minimum goal of 
        5 movements.
        """
        num_movements_tobe_performed = self.goal[MIN_MOVEMENTS] - (len(movements_done) + 1)
        """This is the number of remaining bars"""
        remaining_bars = self.goal[BARS_TO_BE_EXPLOITED] - (bars_exploited + from_time_to_bars(NON_MANDATORY_MOVEMENTS[movement][MIN_TIME], self.bar_time))
        
        """
        In this way we count the number of bars needed in order to have at least
        5 movements between mandatory positions.
        This is done, for semplicity, under the assumption that there are no non mandatory
        movements that could change the body position.
        If the precondition of the movements is eligible with respect to post-condition
        of the previous mandatory position, as consequence it will have the post-condition
        compatible with reference to the preconditions of the next mandatory position.
        This because we have only movements that can be performed in any position or 
        that have pre-conditions equal to the post-conditions
        In the case in which the num_movements_tobe_performed is less than 0, 
        the range will return an empty list of values, so 
        the function will return always True
        """
        min_bars_needed = 0
        for i in range(num_movements_tobe_performed):
            min_bars_needed += from_time_to_bars(NON_MANDATORY_MOVEMENTS[available_movements[i]][MIN_TIME], self.bar_time)
            
        """
        If the minimum number of bars needed to reach 5 is less than the number of measures
        still available, the function will return True. Otherwise, False is returned
        """
        return min_bars_needed <= remaining_bars
    
    
    """
    This function is useful if the search strategy expands the state in a 
    left-most way.
    Among the all possible movements, we give more weight to the ones which are longer
    with respect to the mean time, in fact we apply a small shift on the basis of the 
    class to which the movement belongs to.
    This is done in order to avoid giving more weight to the movements used more 
    frequently in the choreogrpahy, even if they belong to the most 
    preferable class of movements.
    """
    def compareTo(self, mov):
        result = self.movements_count[mov] + self.movements_classes[mov]
        return result
     
    """
    Through this function, the agent performs the state expansion.
    All the possible compatible movements will be selected.
    """
    def actions(self, state):
        """The actions executable in this state."""
        result = []
        
        #Variables assignment
        movements_done, bars_exploited, body = state
        movements_done = list(movements_done)
        position, legs = body
        
        """
        All movements are sorted in order to give more weight to the less used movements
        in the complete sequence of actions of the choreography.
        This is done under the assumption that the search strategy chooses to expand
        the left most state of the tree.
        """
        available_movements = sorted(self.movements_count.keys(), key = self.compareTo)
        """Preconditions filter"""
        pre_filtered = [movement for movement in available_movements if position in NON_MANDATORY_MOVEMENTS[movement][PRECONDITIONS]]
        """
        As a first attempt, we try to delete from the available movements, the ones
        we have selected so far in order to avoid having repeated movements in the 
        same interval between two mandatory positions.
        """
        available_movements = [movement for movement in pre_filtered if movement not in movements_done]
        """
        Then we check that if we chose the specific movement taken in exam, then 
        we would be able to reach the minimum goal of 5 movements.
        """
        valids = [movement for movement in available_movements if self.isValid(state, movement, available_movements)]
        
        """
        If this attempt fails, we try to remove one of the previous constraints.
        In particular, we only filter by pre-conditions and, obviously, then we apply 
        the isValid method
        """
        if len(valids) == 0:
            available_movements = pre_filtered
            valids = [movement for movement in available_movements if self.isValid(state, movement, available_movements)]
            
            """If it is the case of another fail, we are forced to return an empty list"""
            if len(valids) == 0:
                result = []
        else:
            result = valids
    
        return result

    def result(self, state, movement):
        """The state that results from executing this action in this state."""
        movements_done, bars_exploited, body = state
        movements_done = list(movements_done)
        position, legs = body
        
        """
        Through these commands we apply the action, so the movement, selected by
        the search algorithm, resulting in another new state.
        """
        bars_exploited += from_time_to_bars(NON_MANDATORY_MOVEMENTS[movement][MIN_TIME], self.bar_time)
        movements_done.append(movement)
        
        """
        We apply the post-conditions of the selected movement on the state, in order
        to reach a new body configuration.
        """
        if position not in NON_MANDATORY_MOVEMENTS[movement][POSTCONDITIONS]:
            position = NON_MANDATORY_MOVEMENTS[movement][POSTCONDITIONS][0]
            
        legs_postconditions = NON_MANDATORY_MOVEMENTS[movement][LEGS]
        if not legs_postconditions == None:
            legs = legs_postconditions
            
        result = (tuple(movements_done), bars_exploited, (position, legs))
        return result
        
    """
    The goal test checks whether the choreography between two mandatory positions has 
    at least 5 movements and at the same time exploits all the bars available.
    In addition, it checks whether the last position of the choreography is eligible with 
    respect to the precondition of the next mandatory position
    """
    def goal_test(self, state):
        return len(state[MOVEMENTS_DONE]) >= self.goal[MIN_MOVEMENTS] and int(state[BARS_EXPLOITED]) == int(self.goal[BARS_EXPLOITED]) and state[BODY][BODY_POSITION] == self.goal[BODY][BODY_POSITION]
    