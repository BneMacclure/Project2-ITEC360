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
    def __str__(self):
        s = "{} {}".format(self.x,self.y)
        return s


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
    def __str__(self):
     return "foo"

# Function to process the file and make a list of points
# Usage: getPoints() -> List<Point>
def getPoints():
    points = []
    lineNum = 1
    for line in sys.stdin:
        # make the points
        if (lineNum > 1):
            strip = line.rstrip('\n')
            l = strip.split(' ') 
            pt = Point(int(l[0]), int(l[1])) # make the point here, assuming it's [x,y]
            print(pt)
            # append to list
            points.append(pt)
        lineNum = lineNum + 1

    return points

# Function to print out a result
# Usage: stringifyResult( Result ) -> String
def stringifyResult(res):
    return 'stringify'

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
    if (len(argv) == 0): # default is divide and conquer if not input
        result = divideAndConquer(points) 
    if (len(argv) > 0):
        if (argv[0] == 'brute'):
            print('Brute Method')
            result = bruteForce(points)
        elif (argv[0] == 'divide'):
            print('Divide and Conquer Method')
            result = divideAndConquer(points)
        elif (argv[0] == 'both'):
            print('Both Methods')
            result = divideAndConquer(points)
            auxResult = bruteForce(points)
            auxResultUsed = True
    
    print(stringifyResult(result))
    if (auxResultUsed):
        print(stringifyResult(auxResult))

if __name__ == "__main__":
   main(sys.argv[1:])