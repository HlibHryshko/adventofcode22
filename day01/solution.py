def task1(fileName):
    maxCalories = 0
    currentCalories = 0
    with open(fileName, 'r') as inputFile:
        for line in inputFile:
            line = line.strip();
            if line == '':
                if maxCalories < currentCalories:
                    maxCalories = currentCalories
                currentCalories = 0
            else:
                currentCalories += int(line)
    if maxCalories < currentCalories:
        maxCalories = currentCalories
    return maxCalories

def task2(fileName):
    maxCalories = [0, 0, 0]
    currentCalories = 0
    with open(fileName, 'r') as inputFile:
        for line in inputFile:
            line = line.strip();
            if line == '':
                if maxCalories[2] < currentCalories:
                    if maxCalories[0] < currentCalories:
                        maxCalories[2] = maxCalories[1]
                        maxCalories[1] = maxCalories[0]
                        maxCalories[0] = currentCalories
                    elif maxCalories[1] < currentCalories:
                        maxCalories[2] = maxCalories[1]
                        maxCalories[1] = currentCalories
                    else:
                        maxCalories[2] = currentCalories
                currentCalories = 0
            else:
                currentCalories += int(line)
    if maxCalories[2] < currentCalories:
                    if maxCalories[0] < currentCalories:
                        maxCalories[2] = maxCalories[1]
                        maxCalories[1] = maxCalories[0]
                        maxCalories[0] = currentCalories
                    elif maxCalories[1] < currentCalories:
                        maxCalories[2] = maxCalories[1]
                        maxCalories[1] = currentCalories
                    else:
                        maxCalories[2] = currentCalories
    return maxCalories[0] + maxCalories[1] + maxCalories[2] 

if __name__ == '__main__':
    print(task1('test1.txt'))
    print(task1('task1.txt'))
    print(task2('test1.txt'))
    print(task2('task1.txt'))
    