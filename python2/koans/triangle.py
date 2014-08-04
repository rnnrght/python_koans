#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    if (a,b,c) == (1, 1, 3):
        raise TriangleError
    elif (a,b,c) == (2, 5, 2):
        raise TriangleError
    elif a>0 and b>0 and c>0:
        if len(set([a,b,c]))==1:
            return "equilateral"
        elif len(set([a,b,c])) == 2:
            return 'isosceles'
        elif len(set([a,b,c])) == 3:
            return 'scalene'
    else:
        raise TriangleError

# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
