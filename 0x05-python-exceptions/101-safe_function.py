#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        out = fct(*args)
    except BaseException as err:
        out = None
        print("Exception: {}".format(err), file=sys.stderr)
    finally:
        return (out)
