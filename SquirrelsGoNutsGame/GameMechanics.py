# Implementing SquirrelsGoNuts
import pygame

""" Game Rules: Place puzzle pieces on board as indicated via booklet 
Nuts get placed in front of squirrels when game starts; once flower pieces have been set
they can't be moved (yay!) 
squirrels can move horizontally or vertically; also have one hole per acorn"""

class SquirrelPieces():
    def __init__(self, color, shape, size, flower):
        self.color = color
        self.shape = shape
        self.size = size
        self.flower = flower

        self.shape = self.shapeCoordinates(shape)

    def has_Flower(self):
        return not self.flower == None

    """ need to set up coordinates squirrel will be placed based on 
    squirrel's shape instance attribute"""

    def shapeCoordinates(self, shape):
        if shape == "L":
            self.shape = ([(0, 0), (0, 1), (1, 0)],
                           [(0, 0), (1, 0), (1, -1)],
                           [(0, 0), (0, -1), (-1, 0)],
                           [(0, 0), (-1, 0), (-1, 1)])

        elif shape == "rectangle":
            self.shape = [
                [(0, 0), (1, 0), (2, 0)],  # Vertical
                [(0, 0), (0, 1), (0, 2)]   # Horizontal
            ]

        else:
            # you're not funny don't break my game mf
            raise TypeError

        return self.shape


class FlowerPieces():
    def __init__(self, color):
        self.color = color


class SquirrelsGoNuts():
    # board is 4 x 4
    board = [
        ["x", "x", "o", "x"],  # o represents hole in board, holes should never change
        ["o", "x", "x", "x"],
        ["x", "o", "x", "x"],
        ["x", "x", "x", "o"]
    ]

    # squirrel game pieces --> pieces can move horizontally or vertically
    whiteSquirrel = SquirrelPieces("white", "rectangle", 2, False)  # size 2; hole at the very end
    blondSquirrel = SquirrelPieces("blond", "L", 4, True)  # size 4 in an L shape; flower at the end
    graySquirrel = SquirrelPieces("gray", "rectangle", 2, False)  # size 2; hole at the very end
    orangeSquirrel = SquirrelPieces("red", "L", 2, False)  # size 2; hole at the very end

    flowerPiece = FlowerPieces("yellow")  # size 1; flower on top

    acornPieces = ["a", "a", "a", "a" "a"]  # 5 pieces total --> placed in board's "o"

    # maps integer (difficulty level) to squirrel coordinates
    challengePositions = {}
    for i in range(61):
        challengePositions[i] = None


    """ when I place pieces on the board, move them around, would it be better to make a copy of the
    board each time, rather than mutating the board itself here? How would I implement something
    like that for this game"""
    # setting pieces on the board (testing with white squirrel)
    for coords in whiteSquirrel.shape:
        for xy in coords:
            xcoord = xy[0]
            ycoord = xy[1]
            if board[xcoord][ycoord] != "o":
                board[xcoord][ycoord] = "W"
    print(board)




    def __init__(self, difficultyLevel):
        """ if the challenge position determines how many squirrels you'll have, how can I represent
        that diagram in code? """
        SquirrelsGoNuts.whiteSquirrel.acorn = SquirrelsGoNuts.acornPieces[0]

        # placement of game pieces dependent on boardSetUp tuple
        boardSetUp = SquirrelsGoNuts.challengePositions.get(difficultyLevel)

    # how can you generate all possible moves?
    def generateAllMoves(self):
        return

    def doMove(self):
        return
