# tests.py
from grid import Grid
from astar import AStarSolver
from visualize import print_grid_ascii

def run_test(width, height, obstacle_prob, cost_range, seed):
    grid = Grid.random(width, height, obstacle_prob, cost_range, seed)
    start, goal = (0, 0), (width - 1, height - 1)
    solver = AStarSolver(grid, diagonals=True)
    path, cost, expanded = solver.solve(start, goal)

    print(f"\n=== Test Grid {width}x{height} (seed={seed}) ===")
    print(f"Start: {start}, Goal: {goal}")
    print(f"Expanded Nodes: {expanded}")
    if path:
        print(f"Path found with total cost = {round(cost, 3)}")
        print_grid_ascii(grid, start, goal, path)
        print("Path:", path)
    else:
        print("No path found.")

if __name__ == "__main__":
    # Run multiple diverse test cases
    test_configs = [
        (8, 8, 0.1, (1, 4), 42),
        (10, 10, 0.2, (1, 5), 7),
        (12, 12, 0.3, (1, 8), 21),
        (15, 15, 0.25, (1, 10), 100),
    ]
    for cfg in test_configs:
        run_test(*cfg)
