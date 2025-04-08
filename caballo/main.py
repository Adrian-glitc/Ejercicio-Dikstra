import pygame
import sys


class Caballo:
    def __init__(self, origen, destino):
        """
        Clase que representa un nodo para el movimiento del caballo en un tablero de ajedrez.
        
        :param origen: Tupla (x, y) que indica la posición inicial del caballo.
        :param destino: Tupla (x, y) que indica la posición final del caballo.
        """
        self.origen = origen
        self.destino = destino

    def __repr__(self):
        return f"Caballo(origen={self.origen}, destino={self.destino})"

    MOVES = {
        0: [4, 6],
        1: [6, 8],
        2: [7, 9],
        3: [4, 8],
        4: [0, 3, 9],
        5: [],        # No se puede mover desde el 5
        6: [0, 1, 7],
        7: [2, 6],
        8: [1, 3],
        9: [2, 4],
    }

    def knight_moves(self, max_moves):
        dp = [[0] * 10 for _ in range(max_moves + 1)]

        # Caso base: 1 movimiento desde cualquier número = 1 camino
        for i in range(10):
            dp[0][i] = 1

        for move in range(1, max_moves + 1):
            for digit in range(10):
                dp[move][digit] = sum(dp[move - 1][prev] for prev in self.MOVES[digit])

        # Suma total de caminos posibles desde cualquier número inicial
        return sum(dp[max_moves][i] for i in range(10))

def draw_board(screen, font, possibilities):
    screen.fill((255, 255, 255))
    for i in range(10):
        x = (i % 3) * 100 + 50
        y = (i // 3) * 100 + 50
        if i == 9:  # Ajustar posición del 0
            x = 150
            y = 350
        pygame.draw.circle(screen, (0, 0, 0), (x, y), 40, 2)
        text = font.render(str(i), True, (0, 0, 0))
        screen.blit(text, (x - 10, y - 10))

    # Mostrar posibilidades
    text = font.render(f"Posibilidades: {possibilities}", True, (0, 0, 0))
    screen.blit(text, (50, 400))

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((300, 450))
    pygame.display.set_caption("Movimientos del Caballo")
    font = pygame.font.Font(None, 36)

    caballo = Caballo((0, 0), (0, 0))
    moves = [1, 2, 3, 5, 8, 10, 15, 18, 21, 23, 32]
    move_index = 0

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move_index = (move_index + 1) % len(moves)
                elif event.key == pygame.K_LEFT:
                    move_index = (move_index - 1) % len(moves)

        possibilities = caballo.knight_moves(moves[move_index])
        draw_board(screen, font, possibilities)

        pygame.display.flip()
        clock.tick(30)