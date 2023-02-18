import sys


def goofy(num):
    the_args = []
    try:
        result = 1 / num
    except TypeError as t:
        for a in t.args:
            the_args.append(a)  # sys.exc_info()
        return the_args
    except ZeroDivisionError as d:
        return 'divided by zero!'
    else:
        return result


class EmTee:
    result = None
