import pygame
import sys

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


def draw_board(screen, board, n, cell_size):
    colors = [(255, 255, 255), (0, 0, 0)]  # White and Black
    queen_color = (255, 0, 0)  # Red for queens

    for row in range(n):
        for col in range(n):
            color = colors[(row + col) % 2]
            pygame.draw.rect(screen, color, (col * cell_size, row * cell_size, cell_size, cell_size))

            if board[row] == col:
                pygame.draw.circle(screen, queen_color, 
                                   (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2), 
                                   cell_size // 3)


def visualize_solution(n, solutions):
    pygame.init()
    cell_size = 50
    screen_size = n * cell_size
    screen = pygame.display.set_mode((screen_size, screen_size))
    pygame.display.set_caption(f"{n}-Queens Visualization")

    clock = pygame.time.Clock()
    solution_index = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    solution_index = (solution_index + 1) % len(solutions)
                elif event.key == pygame.K_LEFT:
                    solution_index = (solution_index - 1) % len(solutions)

        screen.fill((0, 0, 0))
        draw_board(screen, solutions[solution_index], n, cell_size)
        pygame.display.flip()
        clock.tick(30)


# Example usage
n = 8  # Change this to visualize a different board size
solver = NQueensSolver(n)
solutions = solver.get_solutions()

if solutions:
    visualize_solution(n, solutions)
else:
    print(f"No solutions found for {n}-Queens.")