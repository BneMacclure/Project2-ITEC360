#!/usr/bin/python
# Project 2 
# ITEC360
# Spring 2021
# Ben McClure

from closest import Point, Result, calcDistance, bruteForce, sortByX, dacHelper
import sys, math

def main():
    # ********************************TESTS********************************* #
    # Test sets of List<Point>
    pts1 = [Point(3,4), Point(-12, 5), Point(0,0), Point(200, -300)]
    pts2 = []
    pts3 = [Point(3,4), 
            Point(-12, 5), 
            Point(0,0), 
            Point(200, -300), 
            Point(-122222222222, 222222222234),
            Point(-3333333333333, -222222222222),
            Point(1,0),
            Point(47, 2.6087635650665566e+19),
            Point(1,1)]
    pts4 = [Point(3,4), Point(-12, 5), Point(0,0)]
    pts5 = [Point(3,4), Point(0,0), Point(1,0), Point(500, -300)]

    # Test sets of Points
    pt1 = Point(0,0)
    pt2 = Point(sys.maxsize, sys.maxsize)
    pt3 = Point(-sys.maxsize-1, -sys.maxsize-1)
    pt4 = Point(47, -3450000)


    # tests for calcDistance
    # Function Usage: calcDistance(Point, Point) -> int
    assert (math.isclose(calcDistance(pt1, pt4), 3450000.00032)),  "\nExpected: {}\nActual: {}".format(3450000.00032, calcDistance(pt1, pt4))
    assert (math.isclose(calcDistance(pt2, pt2), 0)), "\nExpected: {}\nActual: {}".format(0, calcDistance(pt2, pt2))
    assert (math.isclose(calcDistance(pt3, pt3), 0)), "\nExpected: {}\nActual: {}".format(0, calcDistance(pt3, pt3))
    assert (math.isclose(calcDistance(pt3, pt2), 2.6087635650665566e+19)), "\nExpected: {}\nActual: {}".format(2.6087635650665566e+19, calcDistance(pt3, pt2))

    # tests for sortByX
    assert(sortByX([]) == []), "\nExpected: {}\nActual: {}".format([], sortByX([]))
    assert(sortByX(pts1) == [Point(-12, 5), Point(0,0), Point(3,4), Point(200, -300)]), "\nExpected: {}\nActual: {}".format([Point(-12, 5), Point(0,0), Point(3,4), Point(200, -300)], sortByX(pts1))
    assert(sortByX([pt1]) == [pt1]), "\nExpected: {}\nActual: {}".format([pt1], sortByX([pt1]))

    # tests for bruteForce
    # Function Usage: bruteForce( List<Point> ) -> Result
    # Focus on the distance, as the timing will vary
    assert (math.isclose(bruteForce(pts1).distance, 5)), "\nExpected: {}\nActual: {}".format(5,  bruteForce(pts1).distance)
    assert (math.isclose(bruteForce(pts2).distance, 0)), "\nExpected: {}\nActual: {}".format(0,  bruteForce(pts2).distance)
    assert (math.isclose(bruteForce(pts3).distance, 1)), "\nExpected: {}\nActual: {}".format(1,  bruteForce(pts3).distance)
    
    # tests for dacHelper
    expected = Result(Point(3,4), Point(0,0), 5, 0, 0, 'divide')
    assert (dacHelper(pts4) == expected), "\nExpected: {}\nActual: {}".format(expected, dacHelper(pts4))
    assert (dacHelper(pts5) == 1), "\nExpected: {}\nActual: {}".format(1, dacHelper(pts5))

    # tests for divideAndConquer

    print('ALL TESTS PASSED')

if __name__ == "__main__":
    main()