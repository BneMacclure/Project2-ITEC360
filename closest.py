#!/usr/bin/python
# Project 2 
# ITEC360
# Spring 2021
# Ben McClure

import sys, math, time, gc

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
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


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
        if self.distance is not None:
            return "{:g} {} ({},{}) ({},{}) n={} {} {:9.3f}".format(self.distance, 
                                                    self.distance**2, 
                                                    self.point1.x,
                                                    self.point1.y,
                                                    self.point2.x,
                                                    self.point2.y,
                                                    self.n,
                                                    self.method,
                                                    self.time)
        else:
            return "{:g} {} ({},{}) ({},{}) n={} {} {:9.3f}".format(self.distance, 
                                                    self.distance, 
                                                    self.point1.x,
                                                    self.point1.y,
                                                    self.point2.x,
                                                    self.point2.y,
                                                    self.n,
                                                    self.method,
                                                    self.time)
    def __eq__(self, other):
        return self.point1 == other.point1 and self.point2 == other.point2 and self.distance == other.distance and self.n == other.n and self.method == other.method

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

# Function to quick sort the points by X coordinate
# Usage: sortByX(List<Point>) -> List<Point>
def sortByX(points):
    if points == []:
        return []
    else:
        pivot = points[0]
        equalX = [ point for point in points if point.x == pivot.x ]     
        smallX =  [ point for point in points if point.x < pivot.x ]  
        bigX =    [ point for point in points if point.x > pivot.x ]  
        return  sortByX(smallX) + equalX + sortByX(bigX)

# Function to quick sort the points by Y coordinate
# Usage: sortByY(List<Point>) -> List<Point>
def sortByY(points):
    if points == []:
        return []
    else:
        pivot = points[0]
        equalY = [ point for point in points if point.y == pivot.y ]     
        smallY =  [ point for point in points if point.y < pivot.y ]  
        bigY =    [ point for point in points if point.y > pivot.y ]  
        return  sortByY(smallY) + equalY + sortByY(bigY)

# Brute force algorithm for finding the smallest distance between two points
# Usage: bruteForce( List<Point> ) -> Result
def bruteForce(points):
    # stub some points out and distance
    pt1 = Point(None, None)
    pt2 = Point(None, None)
    d = sys.maxsize
    

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
    d = 0 if math.isclose(d, sys.maxsize) else d
    return Result(pt1, pt2, d, len(points), totalTime, "brute")

# Divide and Conquer Helper function. does the divide
# Contract: points cannot be empty or of size 1
# Usage: divideHelper( List<Point> ) -> Result
def divideHelper(points):
    # if it's a list of two points, return the distance
    if (len(points) == 2):
        res = Result(points[0], points[1], calcDistance(points[0], points[1]), 0, 0, 'divide')
        # print('Res of 2: {}'.format(res))
        return res
    # if it's a list of 3 points, calc the three distances and return the least one
    elif (len(points) == 3):
        res = Result(points[0], points[1], sys.maxsize, None, None, None)
        d1 = calcDistance(points[0], points[1])
        d2 = calcDistance(points[0], points[2])
        d3 = calcDistance(points[1], points[2])
        # print('dists: {} {} {}'.format(d1,d2,d3))
        res =  Result(points[0], points[1], d1, 0, 0, 'divide') if d1 < res.distance else res
        res =  Result(points[0], points[2], d2, 0, 0, 'divide') if d2 < res.distance else res
        res =  Result(points[1], points[2], d3, 0, 0, 'divide') if d3 < res.distance else res
        # print('Res of 3: {}'.format(res))
        return res
    else:
        length = len(points)
        divide = round(length/2)
        leftSide = points[0:divide]
        rightSide = points[divide:len(points)]
        # print('Divide: {}'.format(divide))
        # print('Left: {}'.format(leftSide))
        # print('Right: {}'.format(rightSide))
        leftRes = divideHelper(leftSide)
        rightRes = divideHelper(rightSide)
        # print("Left dist: {}".format(leftRes.distance))
        # print("Right dist: {}".format(rightRes.distance))
        return leftRes if leftRes.distance < rightRes.distance else rightRes

# Divide and Conquer Helper function. does the conquer
# Usage: conquerHelper( Result, List<Point> ) 
# Res is the result from the initial analysis from dividing
# strip is the section surrounding the divide point, with width size res.distance*2
#       strip contains the points inside this 'strip', sorted by y coordinate
# divide is the dividing line
def conquerHelper(res, strip, divide):
    shortestDist = res.distance
    pt1 = res.point1
    pt2 = res.point2
    # Finding the shortest distance
    for i in range(len(strip)):
        if (i + 7 < len(strip)):
            for j in range(i+1, i + 7): # only need to check 7 after the point
                d = calcDistance(strip[i], strip[j])
                if d < shortestDist:
                    shortestDist =  d 
                    pt1 = strip[i]
                    pt2 = strip[j]
                
        else:
            for j in range(i+1, len(strip)): # only need to check 7 after the point
                d = calcDistance(strip[i], strip[j])
                if d < shortestDist:
                    shortestDist =  d 
                    pt1 = strip[i]
                    pt2 = strip[j]
                
    r =  res
    r.distance = shortestDist
    r.point1 = pt1
    r.point2 = pt2
    
    return r
 

# Divide-And-Conquer algorithm for finding the smallest distance between two points
# Thoughts:
# 1) Sort points by X coordinate
# 2) Recur on the left and right halves
# Ex:
# divideAndConquer([(3,4), (1,5), (0, -200), (100, 200), (235, -98)])
# left side:
# [(3,4), (1,5), (0, -200)]
# [(3,4), (1,5)], [(0, -200)]
# Usage: divideAndConquer( List<Point> ) -> Result
def divideAndConquer(points):
    res = Result(None, None, None, None, None, None)
    

    start = time.time()
    if len(points) > 0:
        # 1) sort the points by X coordinate
        sortedPoints = sortByX(points) 

        # 2 ) Divde
        res = divideHelper(sortedPoints)

        # 3) Conquer
        d = res.distance
        divide = round(len(sortedPoints)/2)
        dividePt = sortedPoints[divide]
        lower = dividePt.x - d
        upper = dividePt.x + d
        strip = sortedPoints
        # print('x: {}, y: {}'.format(dividePt.x, dividePt.y))
        # print('lower/upper/divide/d: {} {} {} {}'.format(lower, upper, divide, d))
        filter(lambda pt: pt.x <= upper and pt.x >= lower, strip)
        strip = sortByY(strip)
        res = conquerHelper(res, strip, divide)
    else:
        res = Result(None, None, None, 0, 0, 'divide')
        
    # 3) Set the result
    end = time.time()
    totalTime = (end-start) * 1000
    
    res.time = totalTime
    res.n = len(points)

    return res

# Main Driver of file
def main(argv):
    gc.enable()
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
