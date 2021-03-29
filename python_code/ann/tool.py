import numpy as np


def binary_to_decimal(binary_number):
    """TODO: Docstring for binary_to_decimal.
    :returns: decimal value
    """
    decimal = 0
    for i in range(len(binary_number)):
        decimal = decimal + binary_number[i]*np.power(2,len(binary_number)-i-1)
    return int(decimal)


if __name__ == '__main__':
    print(binary_to_decimal([1,1,1])) #7
    print(binary_to_decimal([0,1,1])) #3

