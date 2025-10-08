# astar.py
import heapq
import math

class AStarSolver:
    """Implements A* pathfinding on a weighted grid."""

    def __init__(self, grid, diagonals=False):
        self.grid = grid
        self.diagonals = diagonals
        # Find the smallest terrain cost for heuristic scaling
        costs = [grid.cells[y][x] for y in range(grid.height)
                 for x in range(grid.width) if grid.cells[y][x] is not None]
        self.min_cost = min(costs) if costs else 1.0

    def heuristic(self, a, b):
        (x1, y1), (x2, y2) = a, b
        # Euclidean distance times minimum traversal cost
        return math.hypot(x2 - x1, y2 - y1) * self.min_cost

    def solve(self, start, goal):
        if not self.grid.passable(*start) or not self.grid.passable(*goal):
            return None, float('inf'), 0
        if start == goal:
            return [start], 0.0, 0

        open_heap = []
        g_score = {start: 0.0}
        heapq.heappush(open_heap, (self.heuristic(start, goal), start))
        came_from = {}
        expanded = 0

        while open_heap:
            _, current = heapq.heappop(open_heap)
            expanded += 1

            if current == goal:
                path = [current]
                while current in came_from:
                    current = came_from[current]
                    path.append(current)
                path.reverse()
                return path, g_score[goal], expanded

            for neighbor in self.grid.neighbors(*current, self.diagonals):
                nx, ny = neighbor
                move_cost = self.grid.cost(nx, ny)
                tentative_g = g_score[current] + move_cost
                if tentative_g < g_score.get(neighbor, float('inf')):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + self.heuristic(neighbor, goal)
                    heapq.heappush(open_heap, (f_score, neighbor))

        return None, float('inf'), expanded  # No path found
