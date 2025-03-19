"""
## Problem 2

Employee Impotance(https://leetcode.com/problems/employee-importance/)
"""

from collections import deque, defaultdict
from typing import List

# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    """
    Solution class implementing BFS and DFS approaches to compute total employee importance.
    """

    # ========================= 1. BFS (Iterative) Approach =========================
    # TC: O(N) - We visit each employee once.
    # SC: O(N) - Space for the queue and employee_map.
    def getImportanceBFS(self, employees: List['Employee'], id: int) -> int:
        """
        Uses Breadth-First Search (BFS) to compute the total importance of an employee and their subordinates.
        """
        employee_map = {emp.id: emp for emp in employees}  # Employee lookup dictionary
        queue = deque([id])  # Initialize queue with given employee ID
        total_importance = 0

        while queue:
            emp_id = queue.popleft()
            employee = employee_map[emp_id]
            total_importance += employee.importance  # Add importance

            # Enqueue all subordinates
            for sub_id in employee.subordinates:
                queue.append(sub_id)

        return total_importance

    # ========================= 2. DFS (Recursive) Approach (Global Variables) =========================
    # TC: O(N) - We visit each employee once.
    # SC: O(N) - Space for the recursion stack.
    def getImportanceDFSGlobal(self, employees: List['Employee'], id: int) -> int:
        """
        Uses Depth-First Search (DFS) to compute the total importance using global variables.
        """
        self.employee_map = {emp.id: emp for emp in employees}  # Employee lookup dictionary
        self.total_importance = 0  # Track importance globally

        def dfs_helper(emp_id):
            """
            Helper function for recursive DFS traversal.
            """
            employee = self.employee_map[emp_id]
            self.total_importance += employee.importance  # Add importance
            for sub_id in employee.subordinates:
                dfs_helper(sub_id)

        dfs_helper(id)
        return self.total_importance

    # ========================= 3. DFS (Recursive) Approach (Return-Based) =========================
    # TC: O(N) - We visit each employee once.
    # SC: O(N) - Space for the recursion stack.
    def getImportanceDFSReturn(self, employees: List['Employee'], id: int) -> int:
        """
        Uses Depth-First Search (DFS) to compute total importance using return-based recursion.
        """
        employee_map = {emp.id: emp for emp in employees}  # Employee lookup dictionary

        def dfs(emp_id):
            employee = employee_map[emp_id]
            return employee.importance + sum(dfs(sub_id) for sub_id in employee.subordinates)

        return dfs(id)
