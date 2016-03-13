import random
from itertools import cycle


def genEven():
    """
    :return:  Returns a random number x, where 0 <= x < 100
    """
    return random.randrange(0, 100, 2)


def deterministicNumber():
    """
    :return: Deterministically generates and returns a generator which in turn returns a even number between 9 and 21
    """
    for num in cycle(range(10, 21, 2)):
        yield num

# OR for goodness sake use random.seed()

def deterministricNumber2():
    """
    :return: Deterministically generates and returns a generator which in turn returns a even number between 9 and 21
    """
    random.seed(0)
    return random.randrange(10, 21, 2)

def stochasticNumber():
    """
    :return: Stochastically generates and returns a uniformly distributed even number between 9 and 21
    """
    return random.randrange(10, 21, 2)



