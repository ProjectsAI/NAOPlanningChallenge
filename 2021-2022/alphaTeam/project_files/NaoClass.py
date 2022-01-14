from reporting import *


class NaoClass(Problem):
    def __init__(self, initial, goal, mandatoryMoves, availableMoves, timeLimit, allStatesTimes):
        super().__init__(initial, goal)
        self.availableMoves = availableMoves
        self.mandatoryMoves = mandatoryMoves
        self.allStatesTimes = allStatesTimes

    def isValid(self, state, move):
        # Check if time is greater than remaining time
        duration = self.calculateDuration(move)
        stateDict = self.convert_tuple(state)
        if stateDict["remainingTime"] < duration:
            return False

        # Already done move
        if move in stateDict["movesList"]:
            return False

        # Check for repeated move
        lastMove = stateDict['movesList'][-1]
        if move == lastMove:
            return False

        return True

    def actions(self, state):
        result = []
        stateDict = self.convert_tuple(state)
        if len(stateDict["movesList"]) == 0:
            result.append("StandInit")
        elif len(stateDict["movesList"]) == 1:
            result.append("Crouch")
        else:
            lastMove = stateDict["movesList"][-2]
            if lastMove in self.mandatoryMoves:
                for move in self.availableMoves:
                    if self.isValid(state, move):
                        result.append(move)
            else:
                for move in self.mandatoryMoves:
                    if self.isValid(state, move):
                        result.append(move)
                if len(result) == 0:
                    for move in self.availableMoves:
                        if self.isValid(state, move):
                            result.append(move)
        return result

    def result(self, state, action):
        duration = self.calculateDuration(action)
        stateDict = self.convert_tuple(state)
        tupleLen = len(stateDict['movesList'])

        # Insert new items between StandInit and Crouch
        if tupleLen >= 2:
            moves = stateDict['movesList'][:tupleLen - 1] + (action,) + (stateDict['movesList'][-1],)
        else:
            moves = stateDict['movesList'] + (action,)
        newState = (('movesList', moves),
                    ('remainingTime', stateDict["remainingTime"] - duration),
                    ('movesDone', stateDict["movesDone"] + 1))
        return newState

    def goal_test(self, state):
        stateDict = self.convert_tuple(state)
        goalDict = self.convert_tuple(self.goal)

        # Check if last element is Crouch
        lastElementCheck = False
        if len(stateDict["movesList"]) > 0:
            lastElement = stateDict["movesList"][-1]
            lastElementCheck = lastElement == "Crouch"

        # Check if all mandatory moves have been added to state
        goalTest = set(self.mandatoryMoves).issubset(stateDict["movesList"])

        # Check if move count is satisfied
        moves = (stateDict["movesDone"] >= goalDict["movesDone"])

        # Remaining time between 0 and min time from the possible available moves
        min_move_time = min(self.allStatesTimes.items(), key=lambda x: x[1])[1]
        timeCheck = (goalDict["remainingTime"] <= stateDict["remainingTime"] <= min_move_time)

        if timeCheck and moves and goalTest and lastElementCheck:
            return True;
        else:
            return False;

    def path_cost(self, c, statel, action, state2):
        # The duration of each possible action is defined as the cost path #
        duration = self.calculateDuration(action)
        return c + duration

    def h(self, node):
        # Remaining time to reach the goal is defined as heuristic here #
        state = node.state
        stateDict = self.convert_tuple(state)
        result = stateDict["remainingTime"]
        return result

    def calculateDuration(self, move):
        duration = self.allStatesTimes[move]
        return duration

    def convert_tuple(self, tupleVar):
        dictVar = {}
        for i in tupleVar:
            key = i[0]
            value = i[1]
            dictVar[key] = value
        return dictVar
