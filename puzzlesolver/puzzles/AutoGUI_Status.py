def get_gui_status(puzzle_id, variant_id=None):
    if puzzle_id in ('npuzzle', 'hanoi', 'lights', 'nqueens'):
        return 'v1'
    else:
        return 'v0'