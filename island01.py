#!/usr/bin/python3
# This is a programme that counts the number of islands
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically
# We start by defining the grid to be tested, create a variable that will iterate through each cell in the grid, such that if the Value is 1 then we are on island so we have to explore it by using a depth first search approach
# The explored cell is set to 0 and we explore the 4 surrounding values recursively.
# NumberOfIslands - number of lands surrounded by water
# search - A variable used to serach through the 4 surrounding values "0"of each "1" encountered

grid = [
["1","1","1","1","0"],
["1","1","0","1","0"],
["1","1","0","0","0"],
["0","0","0","0","0"]
]
# define a function called NumberOfIslands
def NumberOfIslands(grid):
# check if the input is always a grid in rows and columns    
    if not grid:
        return 0
# define a count variable
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "1":
                count += 1
                search(grid, i, j)
    return count
def search(grid, i, j):
    if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == "0":
        return
    grid[i][j] = "0"
    search(grid, i+1, j)
    search(grid, i-1, j)
    search(grid, i, j+1)
    search(grid, i, j-1)
print(NumberOfIslands(grid))
