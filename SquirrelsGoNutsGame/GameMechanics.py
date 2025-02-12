# Implementing SquirrelsGoNuts
import np
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
        self.acorn

    def has_Flower(self):
        return not self.flower == None


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

    # adding all of the starting positions to challengePositions map
    for i in range(61):
        challengePositions(i)

    def challengePositionsAdd(self, key):
        SquirrelsGoNuts.challengePositions.get(key)


    def __init__(self, difficultyLevel):
        """ if the challenge position determines how many squirrels you'll have, how can I represent
        that diagram in code? """
        SquirrelsGoNuts.whiteSquirrel.acorn = SquirrelsGoNuts.acornPieces[0]

        # placement of game pieces dependent on boardSetUp
        boardSetUp = SquirrelsGoNuts.challengePositions.get(difficultyLevel)



    # how do you determine whether a move is valid?
    def is_Valid(self):
        return

    # how can you generate all possible moves?
    def generateAllMoves(self):
        return

    # what constitutes a solution?
    def is_Solution(self):
        return
