import random as r
import graphics as g
import time as t

def sim(similar: float, ratio: float, empty: float, size: int, delay: float):
    """Schelling's Model of Segregation
    sim(similar goal (float <= 1), ratio of red dots (float <= 1), ratio of empty spaces (float <= 1), length of square grid (int), delay of steps in preview in  (float))"""
    

def createGrid(size: int) -> list:
    """returns a 2d square array of len size"""
    

def fillGrid(grid: list, seed : list) -> list:
    """fills grid with given parameters (initialization)"""


def getCounts(grid: list, ratio : float, empty : float) -> tuple:
    """returns a tuple with the amount of each type of dot there will be in the grid"""
    

def getSeed(counts : tuple) -> list:
    """creates a list with the corresponding amount of dots in the grid for each color/empty"""
    

def getUpdateList(grid: list, similar: float) -> list:
    """returns a list of all coordinates that need to be updated in tuples"""
           

def getEmptyList(grid : list) -> list:
    """returns a list of the coordinates of all empty spaces in tuples"""
    

def updateGrid(grid : list, updateList : list, emptyList : list) -> list:
    """returns a grid that's updated from the one passed to it based on contents of the updatedList and the emptyList"""
    

def getPerSatisfied(grid: list, similar: float) -> float:
    """returns a float value reflecting the current percentage of satisfied colored dots against the total number of colored dots rounded to 4 digits"""
    

def drawSim(win : g.GraphWin, grid : list, similar : float, iteration : int):
    """function that draws the simulation after the initialization process is complete"""
    

def clear(win):
    """function that clears the window so the next frame can be displayed"""
    

def runSim(win : g.GraphWin, grid: list, similar: float, delay: float, iteration: int):
    """function that runs the simulation in a while loop and creates the first frame"""
    