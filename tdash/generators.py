import functools


def count(gen):
    return functools.reduce(lambda x,y: x + 1, gen, 0)
