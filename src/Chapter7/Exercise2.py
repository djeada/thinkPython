'''
Exercise 2  
Encapsulate this loop in a function called square_root that
takes a as a parameter, chooses a reasonable value of x,
and returns an estimate of the square root of a.
'''

import math
def square_root(a):
  x = 10
  while True:
    # print x
    y = (x + a/x) / 2
    if abs(y- x )< 0.000001:
      break
    x = y
  return x

print square_root(4)
