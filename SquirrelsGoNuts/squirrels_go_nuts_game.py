from copy import deepcopy
from puzzlesolver.util import *
from puzzlesolver.puzzles import Puzzle
from puzzlesolver.solvers import GeneralSolver
from puzzlesolver.players import TUI

class Squirrels:
    id = "squirrels"
    variants = ['basic','medium', 'hard']
    # "True" would mean that the game would start at a random solvable board,
    # by looking at all solvable hashes -- hence False to ensure we fix a start position
    startRandomized = False

    @classmethod
    def generateStartPosition(cls, variantid, **kwargs):
        """
        Return an instance of the Puzzle Class corresponding to the initial position.
        """
        if not isinstance(variantid, str) or variantid not in Squirrels.variants:
            raise TypeError("Invalid variantid")
        return Squirrels(variant_id=variantid)

    def __init__(self, variant_id, puzzle_id=None, pos=None, squirrels_list={}, nuts_list={}, hole_list={}, actual_hole_list={}, hole_matching={}):
        """
        Your constructor can have any signature you'd like,
        because it is only called by the other methods of this class.
        If your puzzle supports multiple variants, it should
        receive some information on the variant as input.

        An instance of the puzzle class represents a position
        in the puzzle, so the constructor should take in information
        that sufficienctly defines a position as input.
        """
        super().__init__()
        self.variant_id = variant_id
        self.squirrels_list = squirrels_list
        self.nuts_list = nuts_list
        self.hole_list = hole_list
        self.actual_hole_list = actual_hole_list
        self.pos = pos
        self.hole_coords = [2, 4, 9, 15] # the coordinates in holes
        self.hole_matching = hole_matching # the coordinate to hole piece string matching
        if self.pos is None:
            #/Users/User/Desktop/SquirrelsGoNuts/assets/squirrelsgonuts/starter
            #assets/squirrelsgonuts/starter
            variant_file = f"/Users/User/Desktop/SquirrelsGoNuts/assets/squirrelsgonuts/{variant_id}.txt"
            if puzzle_id is None:
                # Search the database for a random puzzle with the given difficulty level.
                #variant_ranges = {"basic": 4943, "medium": 5000, "hard": 4043}
                #puzzle_id = random.randrange(variant_ranges[variant_id])
                puzzle_id = 0
                with open(variant_file, 'r') as variants:
                    for i, variant in enumerate(variants):
                        if i == puzzle_id:
                            self.pos = variant[:].rstrip().split(",")  # remove trailing newline
                            break
        else:
            self.pos = pos
        if self.squirrels_list == {} and self.nuts_list == {} and self.hole_list == {} and self.actual_hole_list == {}:
            for i, piece in enumerate(self.pos):
                if len(piece) == 5: #means we have a nut or hole
                    type, type_index, relation = piece.split("_")
                    if type == "H":
                        self.hole_list[type_index] = relation
                        #print(i, piece)
                        self.hole_matching[i] = piece
                        #print(self.hole_matching)
                if len(piece) >= 7:
                    type, type_index, relation, orientation = piece.split("_")
                    if type == "N":
                        if relation == "O":
                            self.nuts_list[type_index] = piece
                        if type_index not in self.squirrels_list:
                            self.squirrels_list[type_index] = []
                        self.squirrels_list[type_index].append(piece)
    def __hash__(self):
        """ Return a hash value of your position
        SQUIRRELS GO NUTS:

        - We could hash the position of the squirrels b/c not just a red piece
        - a bit more interesting b/c some squirrels are L shaped
        -
        """
        squirrel_positions = tuple(sorted(self.squirrels_list.items()))
        nut_positions = tuple(sorted(self.nuts_list.items()))
        hole_states = tuple(sorted(self.actual_hole_list.items()))
        return hash((squirrel_positions, nut_positions, hole_states))

    def primitive(self, **kwargs):
        """
        Return PuzzleValue.SOLVABLE if the current position is primitive;
        otherwise return PuzzleValue.UNDECIDED.
        """
        if self.nuts_list.count() == 0 and self.nuts_list == self.actual_hole_list:
            return PuzzleValue.SOLVABLE
        return PuzzleValue.UNDECIDED

    def generateMoves(self, movetype="all"):
        if movetype == 'for' or movetype == 'back':
            return []  # All moves are bidirectional
        moves = []
        checked_squirrel = []
        for i, piece in enumerate(self.pos):
            # Check for leftward moves
            if piece in self.nuts_list.values(): # checks if its a squirrel + nut -> can enumerate from there with squirrel index
                type, type_index, relation, orientation = piece.split("_")
                if type_index not in checked_squirrel:
                    num_blocks = len(self.squirrels_list[type_index])
                    # will need to check if the move is also a hole -> can move into holes as well as a move
                    j = 0
                    blocked = False
                    while (i - j) % 4 > 0 and not blocked: # checks if leftward move possible
                        count = []
                        for squirrel_block in self.squirrels_list[type_index]:
                            Stype, Stype_index, Srelation, Sorientation = squirrel_block.split("_")
                            Sorientation = int(Sorientation)
                            if (i - j + Sorientation) % 4 > 0:
                                left_block = self.pos[i - j + Sorientation - 1]
                                # if hole or empty or part of this squirrel, we can move
                                #print(left_block)
                                if len(left_block) == 5 or left_block == '-' or left_block in self.squirrels_list[type_index]:
                                    count.append(f"M_{i + Sorientation}_{i - j + Sorientation - 1}_{squirrel_block}") # Move, curr, next, nut index
                                else : blocked = True # can't execute any move past this

                        if len(count) == num_blocks: # if all blocks can move for the squirrel
                            moves.append(count)
                        j += 1
                    j = 0
                    blocked = False
                    while (i + j) % 4 < 3 and not blocked:
                        count = []
                        for squirrel_block in self.squirrels_list[type_index]:
                            # Check for rightward moves
                            Stype, Stype_index, Srelation, Sorientation = squirrel_block.split("_")
                            Sorientation = int(Sorientation)
                            if (i + Sorientation + j) % 4 < 3:
                                right_block = self.pos[i + j + 1 + Sorientation]
                                #print(i + j + 1 + Sorientation)
                                if len(right_block) == 5 or right_block == "-" or right_block in self.squirrels_list[type_index]:
                                    #print(i + j + 1 + Sorientation)
                                    count.append(f"M_{i + Sorientation}_{i + j + 1 + Sorientation}_{squirrel_block}") # CHECK HERE COULD BE SUS
                                else : blocked = True # can't execute any move past this
                        if len(count) == num_blocks:
                            moves.append(count)
                        j += 1
                    j = 1
                    blocked = False
                    while i - 4 * j >= 0 and not blocked:
                        count = []
                        for squirrel_block in self.squirrels_list[type_index]:
                            # Check for upward moves
                            Stype, Stype_index, Srelation, Sorientation = squirrel_block.split("_")
                            Sorientation = int(Sorientation)
                            if (i+Sorientation) - 4 * j >= 0:
                                up_block = self.pos[(i + Sorientation) - 4 * j]
                                if len(up_block) == 5  or up_block == "-" or up_block in self.squirrels_list[type_index]:
                                    count.append(f"M_{i + Sorientation}_{(i + Sorientation) - 4 * j}_{squirrel_block}")
                                else : blocked = True # can't execute any move past this
                        if len(count) == num_blocks:
                            moves.append(count)
                        j += 1
                    j = 1
                    blocked = False
                    while i + 4 * j < 16 and not blocked:
                        count = []
                        for squirrel_block in self.squirrels_list[type_index]:
                            # Check for downward moves
                            Stype, Stype_index, Srelation, Sorientation = squirrel_block.split("_")
                            Sorientation = int(Sorientation)
                            if (i + Sorientation) + 4 * j < 16:
                                down_block = self.pos[(i + Sorientation) + 4 * j]
                                if len(down_block) == 5 or down_block == "-" or down_block in self.squirrels_list[type_index]:
                                    count.append(f"M_{i + Sorientation}_{(i + Sorientation) + 4 * j}_{squirrel_block}")
                                else : blocked = True # can't execute any move past this
                        if len(count) == num_blocks:
                            #print(count)
                            moves.append(count)
                        j += 1

                    checked_squirrel.append(type_index)
        return moves

    def doMove(self, move, **kwargs):
        if move not in self.generateMoves():
            raise ValueError
        #print(self.hole_matching)
        new_pos = list(self.pos)
        for piece in move:
            _, start, end, type, type_index, relation, orientation = piece.split("_")
            start = int(start)
            end = int(end)
            # Make sure to adjust when a nut is in a hole
            # First check the move's orientation to know which way to move
            # check if new piece has hole -> means it needs to be updated into the hole placements
            piece_string = type+"_"+type_index+"_"+relation+"_"+orientation
            new_pos[end] = piece_string
            #print(new_pos[end])
            if end in self.hole_coords and end in self.nuts_list: # CHECK THIS IT IS SUS AND NOT DELETING HMMMM
                self.actual_hole_list[end] = type + "_" + type_index # hole location : nut index
                print(self.nuts_list)
                self.nuts_list.pop(type_index) # takes the nuts on the board off -> no more nut to consider
                #self.nuts_list
            if start not in self.hole_coords and not (len(new_pos[start]) == 7 and new_pos[start] != piece_string): # needs to check that it is not a nut
                new_pos[start] = "-"
            if start in self.hole_coords: # if there was a hole here
                print(self.hole_matching)
                new_pos[start] = self.hole_matching[start] # initialize back to the previous hole
                # check if the old piece has a hole inside, t
        return Squirrels(variant_id=self.variant_id, pos=new_pos, squirrels_list=self.squirrels_list, nuts_list=self.nuts_list, hole_list=self.hole_list, actual_hole_list=self.actual_hole_list, hole_matching=self.hole_matching)

    def printPuzzle(self):
        print(self.pos)
        print(self.squirrels_list)
        print(self.nuts_list)
        print(self.hole_list)

#setter = Squirrels("starter")
#setter.printPuzzle()
#print(setter.generateMoves("bi"))
#print(setter.doMove(['M_5_4_N_1_O_0', 'M_6_5_N_1_X_1']).pos)

setter = Squirrels("starter")
#setter.printPuzzle()
setter_move = setter.generateMoves("bi")
print(setter_move)
print(setter.nuts_list)
setter_move_do = setter.doMove(['M_5_4_N_1_O_0', 'M_6_5_N_1_X_1'])
print(setter_move_do.nuts_list)
print(setter_move_do.pos)
print(setter_move_do.generateMoves())
setter_move_do_do = setter_move_do.doMove(['M_4_5_N_1_O_0', 'M_5_6_N_1_X_1'])
#print(setter_move_do_do.pos)
print(setter_move_do_do.nuts_list)
print(setter_move_do_do.actual_hole_list)