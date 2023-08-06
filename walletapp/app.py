def odd():
    maximum = int(input(" Please Enter the Maximum Value : "))
    Oddtotal = 0

    for number in range(1, maximum + 1):
        if (number % 2 != 0):
            print("{0}".format(number))
            Oddtotal = Oddtotal + number

    print("The Sum of Odd Numbers from 1 to {0} = {1}".format(number, Oddtotal))

def oddnum():
    odd_sum = 0

    # Loop through the range from 1 to 10
    for num in range(1, 11):
        if num % 2 != 0 and prime(num) == False: # Check if the number is odd
            odd_sum += num

    # Print the sum of odd numbers
    print("Sum of odd numbers:", odd_sum)


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

non_prime_sum = 0

# Loop through the range from 1 to 10
for num in range(1, 11):
    if not is_prime(num):
        non_prime_sum += num

# Print the sum of non-prime numbers
print("Sum of non-prime numbers:", non_prime_sum)


def prime(x):
    for i in range(2,10):
        if x != i:
             if x%i == 0:
                 return False
    return True

def run():
    #odd()
    oddnum()
    #is_prime(10)

#https://docs.google.com/document/d/1Z_g7OgKw1AB9SdS-BVgGF3F2f5KewFE3rWhLV243AIg/edit?usp=sharing

#https://docs.google.com/document/d/1f2hUV9LVJPAspA0FbAy7YzjP61EePZLLibRUF8fswio/edit?usp=sharing

