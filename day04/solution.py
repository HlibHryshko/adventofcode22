def task1(fileName):
    overlapCount = 0
    with open(fileName, 'r') as inputFile:
        for line in inputFile:
            line = line.strip()
            line = line.split(',') 
            elf1 = line[0].split('-')
            elf2 = line[1].split('-')
            if (int(elf1[0]) >= int(elf2[0]) and int(elf1[1]) <= int(elf2[1])) or ((int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]))):
                overlapCount += 1
    return overlapCount                                    

def task2(fileName):
    overlapCount = 0
    with open(fileName, 'r') as inputFile:
        for line in inputFile:
            line = line.strip()
            line = line.split(',') 
            elf1 = line[0].split('-')
            elf2 = line[1].split('-')
            if (int(elf1[0]) >= int(elf2[0]) and int(elf1[0]) <= int(elf2[1])) or ((int(elf1[1]) <= int(elf2[1]) and int(elf1[1]) >= int(elf2[0]))) or (int(elf2[0]) >= int(elf1[0]) and int(elf2[0]) <= int(elf1[1])) or ((int(elf2[1]) <= int(elf1[1]) and int(elf2[1]) >= int(elf1[0]))):
                overlapCount += 1
                print(elf1, elf2)
    return overlapCount                                    


if __name__ == '__main__':
    print(task1('test.txt'))
    print(task1('task.txt'))
    print(task2('test.txt'))
    print(task2('task.txt'))
    