import os


def compose(*functions):
    def composed(*args):
        first, *rest = functions
        val = first(*args)
        for func in rest:
            val = func(val)
        return val

    return composed


lmap = compose(map, list)


def get_input(script_file):
    dirname, basename = os.path.split(script_file)
    name, _ = os.path.splitext(basename)
    inputbasename = f"{name}.txt"
    input_path = os.path.join(dirname, inputbasename)

    return open(input_path).read()


def get_lines(script_file):
    return get_input(script_file).split("\n")
