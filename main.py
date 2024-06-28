import random


def main():
    """
    ########################################
    Code Your Program here
    ########################################
    """
    total = 0
    numbers = [0] * 5
    for i in range(5):
        numbers.append(random.randint(0, 100))
        total += numbers[i]

    print(f'The random values are {numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
