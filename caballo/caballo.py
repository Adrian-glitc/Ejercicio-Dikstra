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
    
    