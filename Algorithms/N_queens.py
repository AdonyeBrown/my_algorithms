class NQueens:
    def solveNQueens(self, n) -> list[list[str]]:
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions

    def is_valid_state(self, state, n):
        return len(state) == n

    def get_candidates(self, state, n):
        if not state:
            return range(n)

        position = len(state)
        candidate = set(range(n))

        for row, column in enumerate(state):
            candidate.discard(column)
            dist = position - row
            candidate.discard(column + dist)
            candidate.discard(column - dist)
        return candidate

    def search(self, state, solutions, n):
        if self.is_valid_state(state, n):
            state_string = self.state_to_string(state)
            solutions.append(state_string)
            return

        for candidate in self.get_candidates(state, n):
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()

    def state_to_string(self, state, n):
        ret = ["."*i + "Q" + "."*(n-i + 1) for i in state]
