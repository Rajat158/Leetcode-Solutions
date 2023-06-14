'''
Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).

 

Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105
'''
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        # Store the first row of the grid
        column_starts_with = grid[0]

        # Initialize a list to store the columns of the grid
        columns = [[] for _ in column_starts_with]
        
        # Iterate through each row of the grid
        for row in grid:
            # Iterate through each element in the row and append it to the corresponding column
            for j, element in enumerate(row):
                columns[j].append(element)
        
        # Initialize a variable to count the equal pairs
        equal_pairs = 0

        # Iterate through each row of the grid
        for row in grid:
            # Iterate through each element in the first row
            for j, element in enumerate(column_starts_with):
                # Check if the first element of the row is equal to the element in the corresponding column
                if row[0] == element:
                    # Check if the entire row is equal to the column
                    if row == columns[j]:
                        equal_pairs += 1
    
        return equal_pairs
