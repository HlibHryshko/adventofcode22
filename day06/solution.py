def solution(fileName):
    charSequence = ''
    with open(fileName, 'r') as inputFile:
        charSequence = inputFile.readline().strip()
    
    for index in range(4, len(charSequence)):
        if len(set(charSequence[index - 4:index])) == 4:
            print(index)
            break

    for index in range(14, len(charSequence)):
        if len(set(charSequence[index - 14:index])) == 14:
            print(index)
            break    

if __name__ == '__main__':
    solution('test.txt')
    solution('task.txt')
    