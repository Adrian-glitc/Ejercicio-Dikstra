
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
if __name__ == "__main__":
    caballo = Caballo((0, 0), (0, 0))
    for m in [1, 2, 3, 5, 8, 10, 15, 18, 21, 23, 32]:
        print(f"Movimientos: {m}, Posibilidades válidas: {caballo.knight_moves(m)}")