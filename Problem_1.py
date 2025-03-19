"""
## Problem 1

Rotting Oranges(https://leetcode.com/problems/rotting-oranges)
"""

from collections import deque
from typing import List

class Solution:
    """
    Solution class implementing two approaches to solve the Rotting Oranges problem.
    """

    # ========================= 1. DFS (Recursive) Approach =========================
    # TC: O(N*M) - We visit each cell once.
    # SC: O(N*M) - Recursive stack space in the worst case.
    def orangesRottingDFS(self, grid: List[List[int]]) -> int:
        """
        Uses Depth-First Search (DFS) to propagate rotting oranges.
        """
        self.m = len(grid)
        self.n = len(grid[0])
        self.directions = [(1,0), (0,1), (-1, 0), (0, -1)]

        # Spread rot using DFS for every rotten orange
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 2:
                    self._dfs(grid, i, j, 2)

        # Determine the max time and check if any fresh oranges remain
        max_time = 2
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    return -1  # If there's still a fresh orange, return -1
                max_time = max(grid[i][j], max_time)

        return max_time - 2  # Adjust time by subtracting initial infection value

    def _dfs(self, grid: List[List[int]], row: int, col: int, time: int):
        """
        Helper function for recursive DFS traversal.
        """
        # Base case: Out of bounds or already visited with a shorter time
        if row < 0 or col < 0 or row >= self.m or col >= self.n or (grid[row][col] != 1 and grid[row][col] < time):
            return 

        # Mark the grid with the current time
        grid[row][col] = time

        # Explore all four directions
        for dr, dc in self.directions:
            self._dfs(grid, row + dr, col + dc, time + 1)

    # ========================= 2. BFS (Iterative) Approach =========================
    # TC: O(N*M) - We visit each cell once.
    # SC: O(N*M) - Space for the queue in the worst case.
    def orangesRottingBFS(self, grid: List[List[int]]) -> int:
        """
        Uses Breadth-First Search (BFS) to propagate rotting oranges level by level.
        """
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh_oranges = 0
        time = 0

        # Find all initially rotten oranges and count fresh ones
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))  # Store (row, col, time)
                elif grid[i][j] == 1:
                    fresh_oranges += 1

        # Early exit if no fresh oranges are present
        if fresh_oranges == 0:
            return 0

        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        # Process rotting using BFS
        while queue:
            r, c, time = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 2  # Mark orange as rotten
                    fresh_oranges -= 1  # Reduce fresh orange count
                    queue.append((nr, nc, time + 1))  # Enqueue with updated time

        # If fresh oranges remain, return -1; otherwise, return total time taken
        return -1 if fresh_oranges > 0 else time
