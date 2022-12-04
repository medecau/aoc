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


def get_input_basename(filename):
    dirname, basename = os.path.split(filename)
    name, _ = os.path.splitext(basename)
    inputbasename = name + ".txt"
    return os.path.join(dirname, inputbasename)
