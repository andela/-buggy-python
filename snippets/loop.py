"""
Simple array of lambda functions that is used to calculate the addition
of a number on the fly.
"""


def lambda_array():
    # initialize an empty array
    lambda_methods = []
    # implement a for loop to count from 0 to 9
    for i in range(10):
        # append the lambda function to the array defined above
        lambda_methods.append(lambda x: x + i)

    return lambda_methods
