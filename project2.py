#!/usr/bin/python
# Project 2 
# ITEC360
# Spring 2021
# Ben McClure

import sys

# Class representing a Point
# 'x' is the x coordinate of the point
# 'y' is the y coordinate of the point
# Ex: 
# Point(1,2)
# Point(0,0)
# Point(-100, 100)
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Class representing a Result, the smallest distanc between two points
# point1 is one of the points
# point2 is the other point
# distance is the distance between point1 and point2
# Ex:
# Result( Point(1,2), Point(3,4), 2)
# Result( Point(1,1), Point(3,4), 3)
class Result:
    def __init__(self, point1, point2, distance):
        self.point1 = point1
        self.point2 = point2
        self.distance = distance

# Function to process the file and make a list of points
# Usage: getPoints() -> List<Point>
def getPoints():
    points = []
    for line in sys.stdin:
        # make the points
        print('TODO')
        # append to list
    return points

# Function to print out a result
# Usage: stringifyResult( Result ) -> String
def stringifyResult(res):
    print('got it')

# Brute force algorithm for finding the smallest distance between two points
# Usage: bruteForce( List<Point> ) -> Result
def bruteForce(points):
    return Result(None, None, None)

# Divide-And-Conquer algorithm for finding the smallest distance between two points
# Usage: divideAndConquer( List<Point> ) -> Result
def divideAndConquer(points):
    return Result(None, None, None)

# Main Driver of file
def main(argv):
    points = getPoints() # get list of points
    result = Result(None, None, None) # primary result
    auxResult = Result(None, None, None) # used if there is both in use
    auxResultUsed = False
    if (len(argv) > 0):
        if (argv[0] == 'brute'):
            result = bruteForce(points)
        elif (argv[0] == 'divide'):
            result = divideAndConquer(points)
        elif (argv[0] == 'both'):
            result = divideAndConquer(points)
            auxResult = bruteForce(points)
            auxResultUsed = True
    
    print(stringifyResult(result))
    if (auxResultUsed):
        print(stringifyResult(auxResult))

if __name__ == "__main__":
   main(sys.argv[1:])