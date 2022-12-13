def main():
    rawCrates, rawCommands = getRawInput("input.txt")
    print(rawCrates)
    crates = processCrates(rawCrates)
    # print(crates[0])

    return


def getRawInput(fileName):
    rawCrates = []
    rawCommands = []
    inputState = 0
    with open(fileName) as file:
        lines = file.readlines()
        for line in lines:
            if(line == "\n"):
                inputState = 1
                rawCrates.pop()

            elif(inputState == 0):
                rawCrates.append(line.strip())

            elif(inputState == 1):
                rawCommands.append(line.strip())

    return rawCrates, rawCommands


def processCrates(rawCrates):
    crates = [[[]] * len(rawCrates)][0]
    for i in range(len(rawCrates) - 1, -1, -1):
        splitLine = rawCrates[i].split(" ")
        # print(splitLine)
        return []
        for j in range(len(splitLine)):
            crates[i].append(splitLine[j].replace("[", "").replace("]", ""))

    return crates


if(__name__ == '__main__'):
    main()
