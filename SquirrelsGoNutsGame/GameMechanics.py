# Implementing SquirrelsGoNuts
import np
import pygame

class SquirrelPieces():
    def __init__(self, color, shape, size, flower):
        self.color = color
        self.shape = shape
        self.size = size
        self.flower = flower

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
    redSquirrel = SquirrelPieces("red", "L", 2, False)  # size 2; hole at the very end

    flowerPiece = FlowerPieces("yellow")  # size 1; flower on top

    acornPieces = ["a", "a", "a", "a" "a"]  # 5 pieces total --> placed in board's "o"

    def __init__(self):
        # game begins by placing pieces of board based on challenge packet

        """ squirrel pieces have the ability to slide across the puzzle (what are all the possible ways a piece can slide
       this game is a dead end game, you do have the ability to reach a point where there is no possible solution (how do you
       determine when there are no other possible moves?) """

    # how do you determine whether a move is valid?
    def is_Valid(self):
        return

    # how can you generate all possible moves?
    def generateAllMoves(self):
        return

    # what constitutes a solution?
    def is_Solution(self):
        return
