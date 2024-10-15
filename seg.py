import random as r
import graphics as g
import time as t

def sim(similar: float, ratio: float, empty: float, size: int, delay: float) -> None:
    """Schelling's Model of Segregation
    sim(similar goal (float <= 1), ratio of red dots (float <= 1), ratio of empty spaces (float <= 1), length of square grid (int), delay of steps in preview in  (float))"""
    grid = []
    grid = createGrid(size)

    counts = getCounts(grid, ratio, empty)

    seed = getSeed(counts)
    r.shuffle(seed) #randomizes the seed

    grid = fillGrid(grid, seed)

    win = makeWin(grid)

    runSim(win, grid, similar, delay, 1)

    win.getMouse()
    win.close()

def createGrid(size: int) -> list:
    """returns a 2d square array of len size"""
    l = []
    for row in range(size):
        temp = []
        for col in range(size):
            temp.append("")
        l.append(temp)
    return l

def fillGrid(grid: list, seed : list) -> list:
    """fills grid with given parameters (initialization)"""

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            grid[row][col] = grid[row][col].join(seed[0])
            seed = seed[1:]
    
    return grid

def getCounts(grid: list, ratio : float, empty : float) -> tuple:
    """returns a tuple with the amount of each type of dot there will be in the grid"""
    emptyCount = int(empty * (len(grid) ** 2))
    fillCount = (len(grid) ** 2) - emptyCount 
    redCount = int(fillCount * ratio)
    blueCount = fillCount - redCount

    return (emptyCount, redCount, blueCount)

def getSeed(counts : tuple) -> list:
    """creates a list with the corresponding amount of dots in the grid for each color/empty"""
    (emptyCount, redCount, blueCount) = counts
    seed = []
    for x in range(redCount):
        seed.append("r")
    for x in range(blueCount):
        seed.append("b")
    for x in range(emptyCount):
        seed.append("e")

    return list(seed)

def getUpdateList(grid: list, similar: float) -> list:
    """returns a list of all coordinates that need to be updated in tuples"""
    updateList = []
    for row in range(0, len(grid), 1): #all this is essentially going through and adding the coords of all the ones that need to be updated
        for col in range(len(grid)):
            simCount = 0
            elseCount = 0
            for rowDiff in range(-1, 2): 
                for colDiff in range(-1, 2):
                    if ((row + rowDiff) >= 0) and ((col + colDiff) >= 0) and (((row + rowDiff) < len(grid)) and ((col + colDiff) < len(grid))): #making sure the spot exists
                        if (grid[row+rowDiff][col+colDiff] == grid[row][col] and abs(rowDiff)+abs(colDiff)!=0): #making sure the spot is similar but also not itself
                            if grid[row+rowDiff][col+colDiff] == grid[row][col] and grid[row+rowDiff][col+colDiff] != "e": #making sure it's similar and not e
                                simCount += 1
                        elif grid[row+rowDiff][col+colDiff] != "e" and abs(rowDiff)+abs(colDiff)!=0 and grid[row][col] != "e": #making sure it's not similar but also not e
                                elseCount += 1
                    else:
                        print(f"{rowDiff+row}, {colDiff+col} difference for {row}, {col} does not exist")
            if simCount > 0 and float(simCount / (simCount + elseCount)) >= similar: #checking if it needs to go on the updatelist
                print("not needed to update") 
            elif grid[row][col] != "e": #checking again to make sure its not e before going on the update list
                updateList.append(tuple([row, col]))

    return updateList            

def getEmptyList(grid : list) -> list:
    """returns a list of the coordinates of all empty spaces in tuples"""
    emptyList = []
    for row in range(len(grid)):
        for col in range(len(grid)):
            if grid[row][col] == "e":
                emptyList.append(tuple([row, col]))
    return emptyList

def updateGrid(grid : list, updateList : list, emptyList : list) -> list:
    """returns a grid that's updated from the one passed to it based on contents of the updatedList and the emptyList"""
    if len(updateList) <= len(emptyList):
        for el in updateList:
            (row, col) = el
            emptySlot = r.randint(0, int(len(emptyList)-1))
            (emptyRow, emptyCol) = emptyList[emptySlot]
            savedValue = str(grid[row][col])
            grid[emptyRow][emptyCol] = savedValue
            grid[row][col] = "e"
            emptyList.pop(emptySlot)
    else:
        for el in emptyList:
            (emptyRow, emptyCol) = el
            updateSlot = r.randint(0, int(len(updateList)-1))
            (row, col) = updateList[updateSlot]
            savedValue = str(grid[row][col])
            grid[emptyRow][emptyCol] = savedValue
            grid[row][col] = "e"
            updateList.pop(updateSlot)
    return grid

def getPerSatisfied(grid: list, similar: float) -> float:
    """returns a float value reflecting the current percentage of satisfied colored dots against the total number of colored dots rounded to 4 digits"""
    updateList = getUpdateList(grid, similar)
    emptyList = getEmptyList(grid)
    return round((((len(grid)**2)-len(emptyList))-len(updateList))/((len(grid)**2)-len(emptyList)), 4)

def drawSim(win : g.GraphWin, grid : list, similar : float, iteration : int) -> None:
    """function that draws the simulation after the initialization process is complete"""
    for row in range(len(grid)):
        for col in range(len(grid)):
            b = g.Rectangle(g.Point(row, col), g.Point(row+1, col+1))
            if grid[row][col] == "r":
                b.setFill("red")
            if grid[row][col] == "b":
                b.setFill("blue")
            b.draw(win)
    
    count = g.Text(g.Point(len(grid)/2, (-1)*len(grid)*(1/12)-(len(grid)*(1/48))), f"Round {iteration}")
    count.draw(win)
    sat = g.Text(g.Point(len(grid)/2, (-1)*len(grid)*(1/24)), f"Satisfied {round(round(getPerSatisfied(grid, similar), 3)*100,1) }%")
    sat.draw(win)
    g.update()

def clear(win):
    """function that clears the window so the next frame can be displayed"""
    for item in win.items[:]:
        item.undraw()

def runSim(win : g.GraphWin, grid: list, similar: float, delay: float, iteration: int) -> None:
    """function that runs the simulation in a while loop and creates the first frame"""
    drawSim(win, updateGrid(grid, getUpdateList(grid, similar), getEmptyList(grid)), similar, iteration)
    while getPerSatisfied(grid, similar) != 1:
        t.sleep(delay)
        iteration+=1
        clear(win)
        drawSim(win, updateGrid(grid, getUpdateList(grid, similar), getEmptyList(grid)), similar, iteration)

def makeWin(grid : list) -> g.GraphWin:
    """function that returns a window for graphics package that is scaled to the size of the grid passed to work with the runSim function"""
    win = g.GraphWin("Segregation Simulation", 400, 400, autoflush=False)
    win.setCoords((-1) * (len(grid)/6), (-1) * (len(grid)/6), len(grid) + (len(grid)/6), len(grid) + (len(grid)/6))
    return win

if __name__ == '__main__':
    sim(0.5, 0.5, 0.1, 25, 0.25)