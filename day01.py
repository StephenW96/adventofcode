INPUT = "data/day01_data.txt"


def process_lines(lines, elf, elves_and_calories):
    for line in lines:
        line = line.replace("\n", "")
        if line:
            elves_and_calories[elf].append(int(line))
        else:
            elf += 1
            elves_and_calories[elf] = []
    return elves_and_calories


if __name__ == "__main__":
    elves_and_calories = {}
    elf = 1
    elves_and_calories[elf] = []

    with open(INPUT) as f:
        lines = f.readlines()
        process_lines(lines, elf, elves_and_calories)

    total_cals = {k: sum(v) for k, v in elves_and_calories.items()}
    most_cals = max(total_cals.items(), key=lambda k: k[1])

    # For extra star
    # all_cals = [i[1] for i in total_cals.items()]
    # top3 = sum(sorted(all_cals, reverse=True)[:3])
    # print(top3)

    print(f'Elf number {most_cals[0]} has the most calories ({most_cals[1]} total calories)')
