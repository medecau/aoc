import itertools
from functools import reduce

import utils

dimensions_list = utils.get_input(__file__).split("\n")

total_area = 0
total_ribon = 0
for dims in dimensions_list:
    dims = sorted(map(int, dims.split("x")))

    smallest_perimeter = (dims[0] + dims[1]) * 2
    volume = reduce(lambda x, y: x * y, dims)
    total_ribon += volume + smallest_perimeter

    sides = list(itertools.combinations(dims, 2))

    areas = utils.lmap(lambda side: side[0] * side[1], sides)
    areas += areas
    areas.append(areas[0])

    total_area += sum(areas)

print(total_area, total_ribon)
