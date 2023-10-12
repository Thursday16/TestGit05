import random
import math

# Number of random points to generate
num_points = 1000000


def pi(circle):

    # Initialize counters for points inside the square and the circle
    inside_square = 0
    inside_circle = 0
    for i in range(num_points):
        x = random.random()
        y = random.random()

        # Calculate the Euclidean distance from the origin
        distance = x ** 2 + y ** 2


        # Check if the point is inside the square
        if 0 <= x < 1 and 0 <= y < 1:
            inside_square += 1

        # Check if the point is inside the circle (inside the square and within the circle)
        if distance <= 1:
            inside_circle += 1

    ratio = inside_circle / inside_square

    estimated_pi_over_2 = ratio * 4

    print("Estimated Pi:", estimated_pi_over_2)

