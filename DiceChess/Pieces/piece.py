from abc import ABCMeta, abstractmethod, abstractproperty

class Piece():
    __metaclass__ = ABCMeta
    
    @abstractmethod
    def isLegalMove(self, x1, x2, y1, y2, isEnemy):
        pass
    
    @abstractproperty
    def pointValue(self):
        pass
    
    @abstractproperty
    def canMoveThroughPieces(self):
        pass
