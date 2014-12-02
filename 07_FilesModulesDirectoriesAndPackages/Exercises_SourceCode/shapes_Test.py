#! /usr/bin/env python3
# -*- coding:utf-8; -*-

'''Test the package providing various classes to model shapes being drawn.'''

__author__ = 'Russel Winder'
__date__ = '2012-02-18'
__version__ = '1.1'
__copyright__ = 'Copyright © 2007,2012 Russel Winder'
__licence__ = 'GNU Public Licence (GPL) v3'

import unittest
from shapes.shape import Shape
from shapes.rectangle import Rectangle, Square
from shapes.triangle import Triangle, LeftRightangleTriangle

class Shapes_Test(unittest.TestCase):
    def testRectangle0by0(self):
        self.assertEqual('', str(Rectangle(0, 0)))

    def testRectangle1by1(self):
        self.assertEqual('*\n', str(Rectangle(1, 1)))

    def testRectangle3by2(self):
        self.assertEqual('***\n***\n', str(Rectangle(3, 2)))

    def testSquare0(self):
        self.assertEqual('', str(Square(0)))

    def testSquare1(self):
        self.assertEqual('*\n', str(Square(1)))

    def testSquare3(self):
        self.assertEqual('***\n***\n***\n', str(Square(3)))

    def testLeftRightangleTriangle0by0(self):
        self.assertEqual('', str(LeftRightangleTriangle(0, 0)))

    def testLeftRightangleTriangle1by1(self):
        self.assertEqual('*\n', str(LeftRightangleTriangle(1, 1)))

    def testLeftRightangleTriangle2by2(self):
        self.assertEqual('*\n**\n', str(LeftRightangleTriangle(2, 2)))

if __name__ == '__main__':
    unittest.main()
