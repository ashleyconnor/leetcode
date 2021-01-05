class Solution:
    def number_of_islands(self, grid):
        number_of_islands = 0
        visited_islands = set()

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and not (row, col) in visited_islands:
                    number_of_islands += 1
                    self.dfs(row, col, grid, visited_islands)
        return number_of_islands

    def dfs(self, row, col, grid, visited_islands):
        if (
            row < 0
            or row >= len(grid)
            or col < 0
            or col >= len(grid[0])
            or grid[row][col] == "0"
            or (row, col) in visited_islands
        ):
            return
        visited_islands.add((row, col))
        ## loop up
        self.dfs(row - 1, col, grid, visited_islands)
        ## loop down
        self.dfs(row + 1, col, grid, visited_islands)
        ## loop left
        self.dfs(row, col - 1, grid, visited_islands)
        ## loop right
        self.dfs(row, col + 1, grid, visited_islands)
