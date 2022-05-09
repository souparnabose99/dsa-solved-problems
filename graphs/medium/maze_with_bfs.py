
from collections import deque


class MazeSolverBFS:
    def __init__(self, matrix):
        self.matrix = matrix
        self.move_x = [1, 0, 0, -1]
        self.move_y = [0, -1, 1, 0]
        self.visited = [[False for _ in range(len(matrix))] for _ in range(len(matrix))]
        self.min_distance = float("inf")

    def is_valid_move(self, row, col):

        # Horizontally out of maze
        if row < 0 or row >= len(self.matrix):
            return False

        # Vertically out of maze
        if col < 0 or col >= len(self.matrix):
            return False

        # Wall obstacle
        if self.matrix[row][col] == 0:
            return False

        # Cell already visited
        if self.visited[row][col]:
            return False
        # If all validations passed means the cell is valid
        return True

    def search_maze(self, i, j, destination_x, destination_y):


if __name__ == "__main__":
    maze = [[1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1],
            [0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1],
            [0, 0, 0, 1, 1]]
    maze_route = MazeSolverBFS(maze)
    maze_route.search_maze(0, 0, 4, 4)

