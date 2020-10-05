def compose(*functions):
    def composed(*args):
        val = functions[-1](*args)
        for func in functions[:-1][::-1]:
            val = func(val)
        return val
    return composed

lmap = compose(list,map)

def get_input(fn):
    return open(fn).read()


