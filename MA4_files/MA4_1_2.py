
"""
Solutions to module 4
Review date:
"""

student = "Cecilia"
reviewer = ""

import math as m
import random as r
import matplotlib.pyplot as plt

def sphere_volume(n, d):
# use list comprehensions to create n coordinates in d-dimension 
    coords = [[r.uniform(-1,1) for i in range(d)] for j in range(n)]
# Create a Lambda-function to see if the values are < 1
    f = lambda x : x*x
# Find all the points inside the sphere using filter and lambda
    V_coords = list(filter(lambda x : (sum(f(i) for i in x) <= 1), coords))
    n_d = len(V_coords)
# d is the number of dimensions of the sphere 
    V_d = (n_d/n)*2**d
    return V_d

def hypersphere_exact(n, d):
    d_fac = m.gamma(d/2+1)
    V_d = m.pi**(d/2) / d_fac
    return V_d

     
def main():
    n = 100000
    d = 2
    sphere_volume(n,d)


if __name__ == '__main__':
	main()
