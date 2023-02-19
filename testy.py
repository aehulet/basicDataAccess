import sys
import datetime


def goofy(num):
    try:
        result = 1 / num
    except:
        cls, funct, tb = sys.exc_info()
        dt = datetime.datetime.now()
        err_info = [cls, funct, 'testy.goofy', dt.isoformat()]  # exclude traceback address from exc_info
        return err_info
    else:
        return result


class EmTee:
    result = None
