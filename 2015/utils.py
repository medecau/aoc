import os


def compose(*functions):
    def composed(*args):
        first, *rest = functions
        val = first(*args)
        for func in rest:
            val = func(val)
        return val

    return composed


lmap = compose(list, map)


def get_input(fn):
    return open(fn).read()


