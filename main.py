class NQueensSolver:
    def __init__(self, n):
        self.n = n
        self.board = [-1] * n
        self.solutions = []

    def is_safe(self, row, col):
        for i in range(row):
            if self.board[i] == col or \
               self.board[i] - i == col - row or \
               self.board[i] + i == col + row:
                return False
        return True

    def solve(self, row=0):
        if row == self.n:
            self.solutions.append(self.board[:])
            return True
        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row] = col
                self.solve(row + 1)
                self.board[row] = -1
        return False

    def get_solutions(self):
        self.solve()
        return self.solutions


def fill_table(max_n):
    print(f"{'n-reinas':<10}{'Soluciones distintas':<20}{'  Todas las soluciones':<20}{'  Una solución':<15}")
    print("-" * 65)
    for n in range(1, max_n + 1):
        solver = NQueensSolver(n)
        solutions = solver.get_solutions()
        distinct_solutions = len(solutions)
        all_solutions = len(solutions) * (1 if n < 4 else 2)  # Consider symmetry for n >= 4
        one_solution = solutions[0] if solutions else "-"
        print(f"{n:<10}{distinct_solutions:<20}{all_solutions:<20}{one_solution}")


# Example usage
fill_table(10)  # Change 10 to a higher value to compute more rows