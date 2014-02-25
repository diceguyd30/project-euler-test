from piece import Piece

class Bishop(Piece):

    def isLegalMove(self, x1, x2, y1, y2, isEnemy):
        return x1-x2 == y1 - y2
    
    def pointValue(self):
        return 3
    
    def canMoveThroughPieces(self):
        return False
        
test = Bishop()
print test.pointValue()
print test.isLegalMove(1,1,2,3,True)
print test.isLegalMove(1,1,2,2,False)
print test.canMoveThroughPieces()