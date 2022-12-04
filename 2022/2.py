import utils

rows = utils.get_lines(__file__)

choice_points = {
    "X": 1,  # paper
    "Y": 2,  # rock
    "Z": 3,  # scissors
}
play_points = {
    "A": {  # rock
        "X": 3,  # rock
        "Y": 6,  # paper
        "Z": 0,  # scissors
    },
    "B": {  # paper
        "X": 0,  # rock
        "Y": 3,  # paper
        "Z": 6,  # scissors
    },
    "C": {  # scissors
        "X": 6,  # rock
        "Y": 0,  # paper
        "Z": 3,  # scissors
    },
}

score = 0
for row in rows:
    them, me = row.split(" ")
    score += choice_points[me] + play_points[them][me]

print(score)
