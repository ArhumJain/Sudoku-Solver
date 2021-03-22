import numpy as np

def findNextEmpty(grid):
    indexes = np.where(grid == 0)
    if len(indexes[0]) != 0:
        rowIndex = indexes[0][0] 
        columnIndex = indexes[1][0]
    else:
        rowIndex = -1
        columnIndex = -1
    return rowIndex, columnIndex
def getBlock(rowIndex, columnIndex, grid):
    blockRows = []
    blockColumns = []
    block = []
    # Ugly if statements but I'm too lazy to do anything about it B)
    if rowIndex in range(0,3):
        blockRows = [0,1,2]
    if columnIndex in range(0,3):
        blockColumns = [0,1,2]
    if rowIndex in range(3,6):
        blockRows = [3,4,5]
    if columnIndex in range(3,6):
        blockColumns = [3,4,5]
    if rowIndex in range(6,9):
        blockRows = [6,7,8]
    if columnIndex in range(6,9):
        blockColumns = [6,7,8]
    for row in blockRows:
        for col in blockColumns:
            value = grid[row][col]
            if value != 0:
                block.append(value)
    return np.array(block)
    
def solve(grid):
    rowIndex, columnIndex = findNextEmpty(grid)
    row = grid[rowIndex]
    column = np.array([row[columnIndex] for row in grid])
    block = getBlock(rowIndex, columnIndex, grid)
    gridSolved = False
    if rowIndex == -1:
        return grid.tolist()
    for i in range(1,10):
        if i not in row and i not in column and i not in block:
            grid[rowIndex][columnIndex] = i
            solvedGrid = solve(grid)
            if solvedGrid == False:
                grid[rowIndex][columnIndex] = 0
                continue
            else:
                return solvedGrid
            gridSolved = True
        if i == 9 and gridSolved == False:
            return False
    return False

# Demo Sudoku Puzzles
grid0 = np.array([[0,0,0,0,0,9,4,0,0],
                [0,0,0,0,0,0,7,2,0],
                [1,0,0,5,2,0,0,0,0],
                [0,0,0,7,0,0,5,3,0],
                [0,1,4,8,0,0,2,6,0],
                [0,0,0,0,0,3,0,0,0],
                [7,4,5,1,0,0,0,0,0],
                [0,0,0,0,6,0,0,0,0],
                [2,8,0,0,0,0,0,0,0]])
grid2 = np.array([
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
])
grid3 = np.array([
    [0,0,0,0,0,1,9,0,8],
    [0,0,0,8,5,0,2,0,0],
    [0,0,0,9,0,0,0,3,5],
    [8,0,0,0,3,0,0,0,0],
    [4,6,0,0,0,0,0,1,2],
    [0,0,0,0,4,0,0,0,6],
    [6,3,0,0,0,2,0,0,0],
    [0,0,9,0,7,3,0,0,0],
    [7,0,1,6,0,0,0,0,0]
])

print("Solving...")
solved = solve(grid3)
if solved == False:
    print("The puzzle is not solvable")
else:
    print(np.array(solved))
                