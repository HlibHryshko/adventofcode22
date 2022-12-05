def task1(fileName):
    score = 0
    with open(fileName, 'r') as inputFile:
        for line in inputFile:
            choices = line.strip().split()
            if choices[0] == 'A':
                choices[0] = 1
            elif choices[0] == 'B':
                choices[0] = 2
            else:
                choices[0] = 3
            if choices[1] == 'X':
                choices[1] = 1
            elif choices[1] == 'Y':
                choices[1] = 2
            else:
                choices[1] = 3
            score += choices[1]
            if (choices[1] > choices[0] and not (choices[1] == 3 and choices[0] == 1)) or (choices[1] == 1 and choices[0] == 3):
                score += 6
            elif choices[1] == choices[0]:
                score += 3
    return score

def task2(fileName):
    score = 0
    with open(fileName, 'r') as inputFile:
        for line in inputFile:
            choices = line.strip().split()
            if choices[0] == 'A':
                choices[0] = 1
            elif choices[0] == 'B':
                choices[0] = 2
            else:
                choices[0] = 3
            if choices[1] == 'X':
                if choices[0] != 1:
                    score += choices[0] - 1
                else:
                    score += 3
            elif choices[1] == 'Y':
                score += 3 + choices[0]
            else:
                if choices[0] == 3:
                    score += 7
                else:
                    score += choices[0] + 7
    return score


if __name__ == '__main__':
    print(task1('test1.txt'))
    print(task1('task1.txt'))
    print(task2('test1.txt'))
    print(task2('task1.txt'))
    