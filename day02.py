INPUT = "data/day02_data.txt"

'''
ROCK = A, X = 1
PAPER = B, Y = 2
SCISSORS = C, Z = 3
'''

SCORES = {'X': 1, 'Y': 2, 'Z': 3}
WINNINGDICT = {'A': ['X', 'Y', 'Z'],
               'B': ['Y', 'Z', 'X'],
               'C': ['Z', 'X', 'Y']}
RESULTTOSCORE = {0: 3, 1: 6, 2: 0}


def round(line):
    score = SCORES[line[1]]
    score_key = WINNINGDICT[line[0]]
    result = score_key.index(line[1])
    score += RESULTTOSCORE[result]
    return score


if __name__ == "__main__":

    total = 0
    with open(INPUT) as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            line = line.split(" ")
            total += round(line)

    print(total)
