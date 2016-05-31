import functools
import pydash.arrays as arrays

def count(gen):
    return functools.reduce(lambda x,y: x + 1, gen, 0)

def flatten(gen):
    for arr in gen:
        for elem in arrays.flatten(arr, is_deep=True):
            yield elem

def split_list(self, input_data, n):
    """ Yield successive n-sized chunks from input_data """
    for i in xrange(0, len(input_data), n):
        yield input_data[i:i+n]
