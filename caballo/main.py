from caballo import Caballo


if __name__ == "__main__":
    caballo = Caballo((0, 0), (0, 0))
    for m in [1, 2, 3, 5, 8, 10, 15, 18, 21, 23, 32]:
        print(f"Movimientos: {m}, Posibilidades válidas: {caballo.knight_moves(m)}")