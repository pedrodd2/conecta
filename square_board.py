from unittest import result
from list_utils import displace_matrix, reverse_matrix, transpose
from linear_board import LinearBoard
from settings import BOARD_LENGTH, VICTORY_STRIKE

class  SquareBoard():
    """
    representa un tablero cuadrado
    """
    @classmethod
    def fromList(cls, list_of_list):
        """
        transforma una lista de lista en una list de LinearBoard
        """
        board = cls()
        board._columns = list(map(lambda element: LinearBoard.fromList(element), list_of_list))
        return board
        
    def __init__(self):
        self._columns = [LinearBoard() for i in range(BOARD_LENGTH)]
    
        #dunders mnnetodos magicos

    def __repr__(self):
        return f'{self.__class__}:{self._columns}'

    
    def is_full(self):
        """
        True si todos los LinearBoards estan llenos
        """
        result = True
        for lb in self._columns:
            result = result and lb.is_full()
        return result
    
    def as_matrix(self):
        """
        Devuelve una representación en fromato de matriz, es decir,
        lista de listas.
        """
        return list(map(lambda x: x._column, self._columns))
    
    #Detecta victorias
    def is_victory(self, char):
        return self._any_vertical_victory(char) or self._any_horizontal_victory(char) or self._any_rising_victory(char) or  self._any_sinking_victory(char)

    def _any_vertical_victory(self, char):
        result = False
        for lb in self._columns:
            result = result or lb.is_victory(char)
        return result  
    
    def _any_horizontal_victory(self, char):
        # Transponemos _columns
        transp = transpose(self.as_matrix())
        # Creamos un tablero temporal con esa matriz transpuesta
        tmp = SquareBoard.fromList(transp)

        # comprobamos si tiene una victoria temporal
        return tmp._any_vertical_victory(char)


    def _any_rising_victory(self, char):
        # obtener las columnas
        m = self.as_matrix()
        # las invertimos
        rm = reverse_matrix(m)
        # creamos tablero temporal con esa matriz
        tmp = SquareBoard.fromList(rm)
        # devolvemos si tiene una victoria descendente
        return tmp._any_sinking_victory(char)

    def _any_sinking_victory(self, char):
        # Obtenemos las columnas como una matriz
        m = self.as_matrix()
        # la desplazamos
        d = displace_matrix(m)
        # creamos un tablero temporal con esa matriz
        tmp = SquareBoard.fromList(d)
        # averiguamos si tiene una vitroia horizontal
        return tmp._any_horizontal_victory(char) 




        