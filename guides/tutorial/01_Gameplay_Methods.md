# Gameplay Methods
<p align="center">
<img src='assets/Tower_of_hanoi.jpeg'>
</p>

Hanoi is a commonly known and simple puzzle. It consists of three rods and a stack of differently sized rings on one rod. The goal is to take a stack of rings and move them one by one to form another stack of rings on the rightmost rod. The only restriction is that a bigger ring cannot be on top of a smaller ring.

This guide will implement a simple implementation of Hanoi to familiarize the developer about how the Puzzle framework works. Please note that this is an earlier implementation of Hanoi and will not be the same implementation as the official GamesmanPuzzles Hanoi.

Create a new puzzle of Hanoi following the Puzzle interface:
```python
class Hanoi(Puzzle):
```

The rest of guide will implement the instance methods of this class.

## Gameplay functions
#### `__init__(self, **kwargs)`
We want to initialize our puzzle with its starting position. For Hanoi, our starting position is a stack of discs on the leftmost rod. For this example, we will represent the rods with a list of lists containing integers, which represent the size of the disc. Also, the order of the integers from left to right, represents the order of the discs from bottom to top.
```python
def __init__(self, **kwargs):
    self.stacks = [[3, 2, 1], [], []]
```
#### `toString(self, **kwargs)`
The string representation of the puzzle will help visualize the state of our stacks on our PuzzlePlayer interface. For a quick visual, we'll be using the string representation of the lists we used.
```python
def toString(self, **kwargs):
    return str(self.stacks)
```
#### `primitive(self, **kwargs)`
The primitive of the puzzle describes if the puzzle has reached the solution or not. If it has reached the endstate, we will return an arbitrary value that we define as SOLVABLE. Otherwise, it's considered to be UNDECIDED. For our version of Hanoi, a SOLVABLE primitive would be when all the rings are stacked on the rightmost rod.
```python
def primitive(self, **kwargs):
    if self.stacks[2] == [3, 2, 1]:
        return PuzzleValue.SOLVABLE 
    return PuzzleValue.UNDECIDED
```
[Next step: Implementing the Move functions](02_Moves.md)
