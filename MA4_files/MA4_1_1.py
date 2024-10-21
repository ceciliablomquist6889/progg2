"""
Solutions to module 4
Review date:
"""

student = "Cecilia"
reviewer = ""


import random as r
import math
import matplotlib.pyplot as plt 

def approximate_pi(n):
    xy_coord = [(r.uniform(-1,1), r.uniform(-1,1)) for i in range(n)]
    x_square = [x for x, y in xy_coord if x**2 + y**2 > 1]
    y_square = [y for x, y in xy_coord if x**2 + y**2 > 1]

    x_circle = [x for x, y in xy_coord if x**2 + y**2 <= 1]
    y_circle = [y for x, y in xy_coord if x**2 + y**2 <= 1]

    n_c = len(x_circle)
    pi_approx = 4*n_c/n
    #square_x, square_y = zip(*xy_square)
    #circle_x, circle_y = zip(*xy_circle)
    plt.plot(x_square, y_square, 'o', color='blue', markersize=1)
    plt.plot(x_circle, y_circle, 'o', color='red', markersize=1)
    plt.title(f'Approximation of {r'$\pi$'} using Monte Carlo for n={n}')
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')

    plt.savefig(f'Approximation of pi using Monte Carlo for n={n}')

    print(f'The number of points in the circle are {n_c}')
    print(f'The approximation of pi is {pi_approx}')
    print(f'The real value of pi is {math.pi}')
    return pi_approx
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

if __name__ == '__main__':
	main()
