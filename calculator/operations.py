from __future__ import division


def add(*args):
    '''
    Perform add operation on any number of elements.
    '''
    sum = 0
    for value in args:
        sum += value
    return sum


def subtract(*args):
    '''
    Perform subtract operation on any number of elements.
    '''
    if len(args) == 1:
        return args[0]
    difference = args[0]
    for value in args[1:]:
        difference -= value
    return difference


def multiply(*args):
    '''
    Perform multiply operation on any number of elements.
    '''
    product = 1
    for value in args:
        product *= value
    return product


def divide(*args):
    '''
    Perform divide(quotient) operation on any number of elements.
    '''
    if len(args) == 1:
        return args[0]
    quo = args[0]
    for value in args[1:]:
        quo /= value
    return quo


def plot(*args):
    # OPTIONAL EXTRA CREDIT FUNCTION!
    # See README for info.
    pass

# add your custom operations here


def div_modulo(*args):
    '''
    Perform divide(remainder) operation on any number of elements.
    '''
    if len(args) == 1:
        return args[0]
    remainder = args[0]
    for value in args[1:]:
        remainder %= value
    return remainder


def exponent(*args):
    '''
    Raise value to power of  for any number of elements.
    '''
    if len(args) == 1:
        return args[0]
    expo = args[0]
    for value in args[1:]:
        expo **= value
    return expo
