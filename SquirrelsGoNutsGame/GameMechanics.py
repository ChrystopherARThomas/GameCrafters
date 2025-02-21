# Implementing SquirrelsGoNuts
import copy
""" Game Rules: Place puzzle pieces on board as indicated via booklet 
Nuts get placed in front of squirrels when game starts; once flower pieces have been set
they can't be moved (yay!) 
squirrels can move horizontally or vertically; also have one hole per acorn"""


class SquirrelPieces:
    def __init__(self, color, shape, size, flower):
        self.color = color
        self.shape = shape
        self.size = size
        self.flower = flower
        self.shape = self.shapeCoordinates(shape)
        self.origin = (0, 0)  # where squirrel piece starts on the board, changes once squirrel starts moving
        self.orientation = 0  # rotate piece around the board
        self.tiles = self.calculateTiles()

    """returns a list containing all coordinates a squirrel pieces takes up"""
    def calculateTiles(self):
        x_origin, y_origin = self.origin
        curr_shape = self.shape[self.orientation]
        return [(x + x_origin, y + y_origin) for x, y in curr_shape]


    def has_Flower(self):
        return not self.flower == None

    """ need to set up coordinates squirrel will be placed based on 
    squirrel's shape instance attribute, shapes attributes should be immutable"""
    def shapeCoordinates(self, shape):
        if shape == "L":
            # different ways you can make an L shape on the board
            self.shape = ([(0, 0), (0, 1), (1, 0)],  # orientation @ 0
                          [(0, 0), (1, 0), (1, -1)],  # orientation @ 1
                          [(0, 0), (0, -1), (-1, 0)],  # orientation @ 2
                          [(0, 0), (-1, 0), (-1, 1)])  # orientation @ 3

        elif shape == "rectangle":
            self.shape = (
                [(0, 0), (1, 0), (2, 0)],
                [(0, 0), (0, 1), (0, 2)]
            )

        else:
            # you're not funny don't break my game mf
            raise TypeError

        return self.shape

    """" move function for each squirrel piece; every time a squirrel pieces moves,that
     squirrel's origin will change """

    def move(self, direction):
        return None


class FlowerPieces:  # flower pieces, once set, can't ever move
    def __init__(self, color):
        self.color = color


class SquirrelsGoNuts:
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

    acornPieces = ["a", "a", "a", "a", "a"]  # 5 acorn pieces total --> placed in board's "o"

    # maps integer (difficulty level) to squirrel coordinates
    challengePositions = {}

    """ when I place pieces on the board, move them around, would it be better to make a copy of the
    board each time, rather than mutating the board itself here? How would I implement something
    like that for this game; difficulty position will determine how many squirrels we set on board 
    picking random colored squirrels easier"""
    boardCopy = copy.deepcopy(board)  # making a copy so no mutation problems later

    def __init__(self, difficultyLevel):
        """ if the challenge position determines how many squirrels you'll have, how can I represent
        that diagram in code? """
        SquirrelsGoNuts.whiteSquirrel.acorn = SquirrelsGoNuts.acornPieces[0]

        # placement of game pieces dependent on boardSetUp tuple
        boardSetUp = SquirrelsGoNuts.challengePositions.get(difficultyLevel)

    def generateAllMoves(self):
        return

    def doMove(self):
        return
