import random

#Value of Pi is 3. divide by 2.

def estimate_pi(num_samples):
    inside_circle = 0
    inside_square = 0

    for _ in range(num_samples):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)

        # Calculate the Euclidean distance from the origin (0, 0)
        distance = x ** 2 + y ** 2

        if distance <= 1:  # Check if the point is inside the circle
            inside_circle += 1
        inside_square += 1

    pi_estimate = 3 * (inside_circle / inside_square)  # Multiply by 3/4 for the quarter-circle

    return pi_estimate

def run():
    num_samples = 1000000  # You can adjust this number to increase or decrease accuracy
    pi_estimate = estimate_pi(num_samples)
    print(f"Estimated Pi: {pi_estimate}")
---------------------------------
import random

def pi(num_samples):
    count_circle = 0
    count_square = 0

    for i in range(num_samples):
        x = random.randint(-100, 100)
        y = random.randint(-100, 100)

        if(x >= 0 and y >= 0):
            count_square += 1
        if(x ^ 2 + y ^ 2) <= 10000:
            count_circle += 1

    return count_circle / count_square

def run():
    num_samples = 1000000  # You can adjust this number to increase or decrease accuracy
    pi_estimate = pi(num_samples)
    print(f"Estimated Pi: {pi_estimate}")
