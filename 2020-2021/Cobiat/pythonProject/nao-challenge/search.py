class IterativeDeepening:

    def __init__(self, pool_times, max_error, max_depth):
        self.pool_states = list(range(0, len(pool_times)))
        self.pool_times = pool_times
        self.max_error = max_error
        self.max_depth = max_depth

    def find_solution(self, init_state, goal_state, goal_time, bar_time):
        for depth in range(1, self.max_depth+1):
            solution = self._find_solution(goal_state, goal_time, [init_state], 0, depth, bar_time)
            if solution is not None:
                return solution

        return None

    def find_complete_path(self, mandatory_positions, mandatory_times, bar_time):
        solution = [mandatory_positions[0]]
        for current_goal, goal_time in zip(mandatory_positions[1:], mandatory_times[1:]):
            found = False
            for depth in range(1, self.max_depth+1):
                partial_path = self._find_solution(current_goal, goal_time, solution, 0, depth, bar_time)
                if partial_path is not None:
                    solution = partial_path
                    found = True
                    break

            if not found:
                return None

        return solution

    def _find_solution(self, goal_state, goal_time, solution, current_time, current_depth, bar_time):
        if abs(goal_time - current_time) < self.max_error and solution[-1] == goal_state:
            return solution

        if current_time > goal_time or current_depth <= 0:
            return None

        for next_state in self.ordered_state(solution[-1], current_time, bar_time):
            if next_state != solution[-1]:
                temporary_solution = solution[:]
                temporary_solution.append(next_state)
                possible_solution = self._find_solution(goal_state, goal_time, temporary_solution,
                                                        current_time + self.pool_times[solution[-1], next_state],
                                                        current_depth - 1, bar_time)

                if possible_solution is not None and possible_solution[-1] == goal_state:
                    return possible_solution

        return None

    def ordered_state(self, current_state, current_time, bar_time):
        states_copy = self.pool_states[:]
        states_copy.sort(key=lambda s: self.heuristic(current_time, current_state, s, bar_time))
        return states_copy

    def heuristic(self, current_time, current_state, next_state, bar_time):
        mod = (current_time + self.pool_times[current_state, next_state]) % bar_time
        return min(mod, bar_time-mod)
