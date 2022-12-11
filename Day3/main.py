LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def part1():
    with open("input.txt") as file:
        lines = file.readlines()
        result = 0

        for line in lines:
            halfway = int(len(line) / 2)
            a = line[0:halfway].strip()
            b = line[halfway:].strip()

            intersection = list(set(a).intersection(set(b)))[0]
            priority = LETTERS.index(intersection) + 1
            print("P", priority)
            result += priority

        print(result)


def part2():
    with open("input.txt") as file:
        lines = file.readlines()
        result = 0
        i = 0
        while(i < len(lines)):
            a = set(lines[i].strip())
            b = set(lines[i + 1].strip())
            c = set(lines[i + 2].strip())

            intersection = list(a.intersection(b).intersection(c))[0]
            priority = LETTERS.index(intersection) + 1
            result += priority
            i += 3

        print(result)


if(__name__ == "__main__"):
    part2()
