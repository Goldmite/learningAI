# 2025-02-23
# Šarūnas Lingė ir Aurijus Šustikas, ISf-22/2

from search import *

class MazeProblem(Problem):
    """ Represents an 8x8 maze-solving problem
    # are walls,
    . is empty space,
    S is starting position,
    G is goal position
    """
    map_moves = {(0, 1): 'Right', (1, 0): 'Down', (0, -1): 'Left', (-1, 0): 'Up'} # for output readability

    def __init__(self, initial, goal, maze):
        self.maze = maze  # Store the maze grid
        super().__init__(initial, goal)  # Initialize the class

    def actions(self, state):
        # Returns valid actions (moves) from the current state
        x, y = state
        possible_moves = [(0, 1), (1, 0), (0, -1), (-1, 0)] # right, down, left, up
        valid_moves = []
        for px, py in possible_moves: #go through every move
            new_x = x + px
            new_y = y + py
            if 0 <= new_x < 8 and 0 <= new_y < 8 and self.maze[new_x][new_y] != '#':
                valid_moves.append((px, py))  # if valid, add move

        return valid_moves

    def result(self, state, action):
        # Returns the new state after taking an action
        x, y = state
        ax, ay = action #action is new coordinates of position
        new_x = x + ax
        new_y = y + ay
        return new_x, new_y #new state X, Y pair

    def goal_test(self, state):
        # Check if the current state is the goal
        return state == self.goal # state == 'G'

    def path_cost(self, cost, state1, action, state2):
        # Defines the cost of moving from one square to the adjacent one (changing states
        return cost + 1  # each step costs 1, this helps find shortest path for solution

    def h(self, node):
        """
        Heuristic function for A* search (Manhattan Distance)
        it's an approximate distance of the current position x and y difference to the goal positions x and y. (goes through walls)
        """
        x1, y1 = node.state
        x2, y2 = self.goal
        manhattan_dist = abs(x1 - x2) + abs(y1 - y2)
        return manhattan_dist # Manhattan distance

#(8x8) change configuration as you want
maze = [
    ['S', '.', '.', '#', '.', '.', '.', '.'],
    ['.', '#', '.', '#', '.', '#', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '#', '#', '.', '#', '#'],
    ['.', '.', '.', '.', '#', '.', '#', 'G'],
    ['.', '#', '#', '.', '#', '.', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '#', '#', '.'],
]

#find 'S' start, 'G' - goal
start = None
goal = None
for i in range(8):
    for j in range(8):
        if maze[i][j] == 'S':
            start = (i, j)
        elif maze[i][j] == 'G':
            goal = (i, j)

maze_problem = MazeProblem(start, goal, maze)
solution = astar_search(maze_problem).solution()
#solution = breadth_first_graph_search(maze_problem).solution()
#solution = best_first_graph_search(maze_problem, lambda n: maze_problem.h(n) ).solution()
print([maze_problem.map_moves[move] for move in solution])