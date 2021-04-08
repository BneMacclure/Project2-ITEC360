#!/usr/bin/python
# Project 2 
# ITEC360
# Spring 2021
# Ben McClure

from project2 import Point, Result, calcDistance, bruteForce
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
            Point(47, 3000000000000),
            Point(1,1)]

    # Test sets of Points
    pt1 = Point(0,0)
    pt2 = Point(sys.maxsize, sys.maxsize)
    pt3 = Point(-sys.maxsize-1, -sys.maxsize-1)
    pt4 = Point(47, -3450000)


    # tests for calcDistance
    # Usage: calcDistance(Point, Point) -> int
    assert (math.isclose(calcDistance(pt1, pt4), 3450000.00032)),  "\nExpected: {}\nActual: {}".format(3450000.00032, calcDistance(pt1, pt4))
    assert (math.isclose(calcDistance(pt2, pt2), 0)), "\nExpected: {}\nActual: {}".format(0, calcDistance(pt2, pt2))
    assert (math.isclose(calcDistance(pt3, pt3), 0)), "\nExpected: {}\nActual: {}".format(0, calcDistance(pt3, pt3))
    assert (math.isclose(calcDistance(pt3, pt2), 2.6087635650665566e+19)), "\nExpected: {}\nActual: {}".format(2.6087635650665566e+19, calcDistance(pt3, pt2))



    # tests for bruteForce
    # Usage: bruteForce( List<Point> ) -> Result
    # Focus on the distance, as the timing will vary
    assert (math.isclose(bruteForce(pts1).distance, 5)), "\nExpected: {}\nActual: {}".format(5,  bruteForce(pts1).distance)
    assert (math.isclose(bruteForce(pts2).distance, 0)), "\nExpected: {}\nActual: {}".format(0,  bruteForce(pts2).distance)
    assert (math.isclose(bruteForce(pts3).distance, 1)), "\nExpected: {}\nActual: {}".format(1,  bruteForce(pts3).distance)

    # tests for divideAndConquer

    print('ALL TESTS PASSED')

if __name__ == "__main__":
    main()