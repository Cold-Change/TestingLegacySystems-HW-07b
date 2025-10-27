# TestTriangle.py
# -*- coding: utf-8 -*-
"""
Updated Oct 27, 2025
The primary goal of this file is to demonstrate testing of a legacy system

@author: Jared Simonetti
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    # --- Right Triangles ---
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(6,8,10), 'Right', '6,8,10 is a Right triangle')

    def testRightTriangleD(self):
        self.assertEqual(classifyTriangle(8,6,10), 'Right', '8,6,10 is a Right triangle')

    # --- Equilateral Triangles ---
    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testEquilateralTriangleB(self):
        self.assertEqual(classifyTriangle(10,10,10), 'Equilateral', '10,10,10 should be Equilateral')

    # --- Isoceles Triangles ---
    def testIsocelesTriangleA(self):
        self.assertEqual(classifyTriangle(5,5,8), 'Isoceles', '5,5,8 is an Isoceles triangle')

    def testIsocelesTriangleB(self):
        self.assertEqual(classifyTriangle(8,5,5), 'Isoceles', '8,5,5 is an Isoceles triangle')

    def testIsocelesTriangleC(self):
        self.assertEqual(classifyTriangle(7,10,7), 'Isoceles', '7,10,7 is an Isoceles triangle')

    # --- Scalene Triangles ---
    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(4,5,6), 'Scalene', '4,5,6 is a Scalene triangle')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(10,15,12), 'Scalene', '10,15,12 is a Scalene triangle')

    # --- Invalid Inputs ---
    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(0,4,5), 'InvalidInput', '0,4,5 is InvalidInput because of zero')

    def testInvalidInputB(self):
        self.assertEqual(classifyTriangle(201,10,10), 'InvalidInput', '201,10,10 is InvalidInput because a side > 200')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle(3.5,4,5), 'InvalidInput', '3.5,4,5 is InvalidInput because sides must be integers')

    # --- Not a Triangle ---
    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(1,10,12), 'NotATriangle', '1,10,12 cannot form a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

