# visualize.py
def print_grid_ascii(grid, start, goal, path=None):
    """Prints the grid with the path in ASCII format."""
    path_set = set(path) if path else set()
    for y in range(grid.height):
        line = ""
        for x in range(grid.width):
            if (x, y) == start:
                line += "S "
            elif (x, y) == goal:
                line += "G "
            elif (x, y) in path_set:
                line += "* "
            elif not grid.passable(x, y):
                line += "# "
            else:
                line += str(int(round(grid.cost(x, y)))) + " "
        print(line)
    print()
