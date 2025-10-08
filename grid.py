# grid.py
import random

class Grid:
    """Grid representation with variable movement costs and obstacles."""

    def __init__(self, width, height, cells=None):
        self.width = width
        self.height = height
        if cells:
            self.cells = cells
        else:
            self.cells = [[1.0 for _ in range(width)] for _ in range(height)]

    def in_bounds(self, x, y):
        return 0 <= x < self.width and 0 <= y < self.height

    def passable(self, x, y):
        return self.cells[y][x] is not None

    def cost(self, x, y):
        return self.cells[y][x]

    def neighbors(self, x, y, diagonals=False):
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        if diagonals:
            directions += [(1,1),(1,-1),(-1,1),(-1,-1)]
        result = []
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if self.in_bounds(nx, ny) and self.passable(nx, ny):
                result.append((nx, ny))
        return result

    @staticmethod
    def random(width, height, obstacle_prob=0.2, cost_range=(1,5), seed=None):
        """Generate random grid with obstacles and varying costs."""
        rnd = random.Random(seed)
        cells = []
        for _ in range(height):
            row = []
            for _ in range(width):
                if rnd.random() < obstacle_prob:
                    row.append(None)  # obstacle
                else:
                    row.append(rnd.uniform(cost_range[0], cost_range[1]))
            cells.append(row)
        return Grid(width, height, cells)
