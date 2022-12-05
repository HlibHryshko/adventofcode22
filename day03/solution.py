def task1(fileName):
    priority = 0
    with open(fileName, 'r') as inputFile:
        for line in inputFile:
            line = line.strip()
            length = len(line)//2
            rucksack = []
            rucksack.append(line[0:length])
            rucksack.append(line[length:])
            for sym in rucksack[0]:
                if sym in rucksack[1]:
                    symbolPriority = ord(sym) - 96
                    if symbolPriority < 1:
                        symbolPriority += 32 + 26
                    priority += symbolPriority
                    break
            
    return priority

def task2(fileName):
    lines = []
    priority = 0
    with open(fileName, 'r') as inputFile:
        for line in inputFile:
            line = line.strip()
            lines.append(line)
            if len(lines) == 3:
                for sym in lines[0]:
                    if sym in lines[1] and sym in lines[2]:
                        symbolPriority = ord(sym) - 96
                        if symbolPriority < 1:
                            symbolPriority += 32 + 26
                        priority += symbolPriority
                        break
                lines = []
            
    return priority


if __name__ == '__main__':
    print(task1('test1.txt'))
    print(task1('task1.txt'))
    print(task2('test1.txt'))
    print(task2('task1.txt'))
    