"""
Solutions to module 4
Review date:
"""

student = "Cecilia"
reviewer = ""

import concurrent.futures as future
from time import perf_counter as pc
from time import sleep as pause

import math as m
import random as r

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

def hypersphere_exact(n,d):
    d_fac = m.gamma(d/2+1)
    V_d = m.pi**(d/2) / d_fac
    return V_d


# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
     with future.ProcessPoolExecutor() as ex:
         results = ex.map(sphere_volume, [n]*np, [d]*np)
     result = sum(list(results))/np
     return result

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n,d,np):
     with future.ProcessPoolExecutor() as ex:
         results = ex.map(sphere_volume, [n//np]*np, [d]*np)
     result = sum(list(results))/np
     return result

def main():
# part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11
    np = 10
    start = pc()
    for y in range (np):
        sphere_volume(n,d)

    end = pc()
    print(f"Iteration process took {round(end-start, 2)} seconds")

# part 2 -- parallelization of a for loop among 10 processes
    start = pc()
    sphere_volume_parallel1(n,d,np)
    end = pc()
    print(f"Parallelization process 1 took {round(end-start, 2)} seconds")

# part 3 -- parallelization of a for loop among 10 processes
    start = pc()
    sphere_volume_parallel2(n,d,np)
    end = pc()
    print(f"parallelization process 2 took {round(end-start, 2)} seconds")

if __name__ == '__main__':
    main()
    

