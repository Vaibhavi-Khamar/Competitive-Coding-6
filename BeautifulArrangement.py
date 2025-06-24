# for loop based recursion
# Time Complexity : Exponential O(n!)
# Space Complexity : O(n) - n used for visited array
class Solution:
    def countArrangement(self, n: int) -> int:
        # Initialize a visited list to track which numbers are used
        visited = [False] * (n + 1) # Index 0 is unused to allow 1-based indexing        
        # Start recursion from index 1 (first position)
        return self.helper(n, 1, visited)
    def helper(self, n: int, index: int, visited: list[bool]) -> int:
        # Base case: if we've placed numbers in all positions
        if index > n:
            return 1  # Found a valid arrangement
        count = 0  # Count of valid arrangements from this point
        for num in range(1, n + 1):
            # If num is not used and it satisfies the Beautiful Arrangement condition
            if not visited[num] and (num % index == 0 or index % num == 0):
                # Choose this number for current position
                visited[num] = True
                # Recurse to the next position
                count += self.helper(n, index + 1, visited)
                # Backtrack: unmark this number
                visited[num] = False
        return count