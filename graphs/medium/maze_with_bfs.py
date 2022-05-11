"""
@TODO: 
Find a way out of a maze with the help of Breadth First Search
In an N X N array, 0 denotes walls or obstacles & 1 denotes valid path
"""

from collections import deque


class MazeSolverBFS:
    def __init__(self, matrix):
        self.matrix = matrix
        # D(0, 1), U(0, 1), L(1, 0), R(-1, 0)
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
        self.visited[i][j] = True
        # Queue is implemented using a doubly linked list : O(1) runtime for first and last element operations
        queue = deque()
        queue.append((i, j, 0))

        while queue:
            # Check the first item inserted
            (i, j, dist) = queue.popleft()
            # If destination is reached
            if i == destination_x and j == destination_y:
                self.min_distance = dist
                break

            # Move L, U, D, R
            for move in range(len(self.move_x)):
                # Calculate position after move
                next_x = i + self.move_x[move]
                next_y = j + self.move_y[move]

                # Check move possibility for next_x & next_y
                if self.is_valid_move(next_x, next_y):
                    self.visited[next_x][next_y] = True
                    queue.append((next_x, next_y, dist + 1))

    def show_maze(self):
        if self.min_distance != float("inf"):
            print("Shortest path from source to destination is : ", self.min_distance)
        else:
            print("No feasible solution to reach destination...")
        pass


if __name__ == "__main__":
    maze = [[1, 1, 1, 1, 1],
            [0, 1, 1, 1, 1],
            [0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1],
            [0, 0, 0, 1, 1]]
    maze_route = MazeSolverBFS(maze)
    maze_route.search_maze(0, 0, 4, 4)
    maze_route.show_maze()

