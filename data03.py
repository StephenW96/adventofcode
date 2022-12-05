import string

INPUT = "data/day03_data.txt"

def find_common(line):
    left_compartment = line[0:len(line)//2]
    right_compartment = line[len(line)//2:]
    common_letter = set(left_compartment).intersection(set(right_compartment))
    return(common_letter)

def find_item_priority(item):
    item = item.pop()
    if item in string.ascii_lowercase:
        return string.ascii_lowercase.index(item) + 1
    return string.ascii_uppercase.index(item) + 27


if __name__ == "__main__":

    total = 0

    with open(INPUT) as f:
        lines = f.readlines()
        for line in lines:
            line = line.replace("\n", "")
            common_element = find_common(line)
            total += find_item_priority(common_element)

    print(f"Total: {total}")

