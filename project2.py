#!/usr/bin/python
# Project 2 
# ITEC360
# Spring 2021
# Ben McClure

import sys, math

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
    def __init__(self, point1, point2, distance, n, time, method):
        self.point1 = point1
        self.point2 = point2
        self.distance = distance
        self.n = n
        self.method = method
        self.time = time
    def __str__(self):
        # 5 25 (0,0) (3,4) n=4 brute      0.001s
        return "{:g} {} ({},{}) ({},{}) n={} {} {:9.3f}".format(self.distance, 
                                                    self.distance**2, 
                                                    self.point1.x,
                                                    self.point1.y,
                                                    self.point2.x,
                                                    self.point2.y,
                                                    self.n,
                                                    self.method,
                                                    self.time)

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
            # append to list
            points.append(pt)
        lineNum = lineNum + 1

    return points

# Function to calculate the distance
# Usage: calcDistance(Point, Point) -> int
def calcDistance(pt1, pt2):
    #(x1-x2)^2 + (y1-y2)^2 
    leftSide = (pt2.x - pt1.x)**2
    rightSide = (pt2.y - pt1.y)**2
    distance = math.sqrt(leftSide +  rightSide)
    return distance

# Brute force algorithm for finding the smallest distance between two points
# Usage: bruteForce( List<Point> ) -> Result
def bruteForce(points):
    # stub some points out and distance
    pt1 = Point(None, None)
    pt2 = Point(None, None)
    d = sys.maxsize
    import time

    start = time.time()

    #time to compare them
    for i in range(len(points)):
        for j in range(i+1, len(points)): # don't want to compare a point to itself
            calc = calcDistance(points[i], points[j])
            if (d > calc):
                d = calc
                pt1 = points[i]
                pt2 = points[j]
    end = time.time()
    totalTime = (end-start) * 1000
    return Result(pt1, pt2, d, len(points), totalTime, "brute")

# Divide-And-Conquer algorithm for finding the smallest distance between two points
# Usage: divideAndConquer( List<Point> ) -> Result
def divideAndConquer(points):
    return Result(None, None, None, len(points), "divide")

# Main Driver of file
def main(argv):
    points = getPoints() # get list of points
    result = Result(None, None, None, None, None, None) # primary result
    auxResult = Result(None, None, None, None, None, None) # used if there is both in use
    auxResultUsed = False
    if (len(argv) == 0): # default is divide and conquer if not input
        result = divideAndConquer(points) 
    if (len(argv) > 0):
        if (argv[0] == 'brute'):
            result = bruteForce(points)
        elif (argv[0] == 'divide'):
            result = divideAndConquer(points)
        elif (argv[0] == 'both'):
            result = divideAndConquer(points)
            auxResult = bruteForce(points)
            auxResultUsed = True
    
    print(result)
    if (auxResultUsed):
        print(auxResult)

if __name__ == "__main__":
   main(sys.argv[1:])