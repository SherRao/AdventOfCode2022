def part1():
    with open("input.txt") as file:
        lines = file.readlines()
        result = 0
        for line in lines:
            a, b = line.split(",")
            a1, a2 = a.split("-")
            b1, b2 = b.split("-")

            # check if the range of a is inside b or vice versa
            if((int(a1) >= int(b1) and int(a2) <= int(b2)) or (int(b1) >= int(a1) and int(b2) <= int(a2))):
                result += 1

        print(result)


def part2():
    with open("input.txt") as file:
        lines = file.readlines()
        result = 0
        for line in lines:
            a, b = line.split(",")
            a1, a2 = a.split("-")
            b1, b2 = b.split("-")

            # check if the range of a is partially inside b or vice versa
            if((int(a1) >= int(b1) and int(a1) <= int(b2)) or (int(b1) >= int(a1) and int(b1) <= int(a2))):
                result += 1

        print(result)


if(__name__ == "__main__"):
    part2()
