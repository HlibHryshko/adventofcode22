def readCrates(line, crates):
    line = line.rstrip()
    for ind in range(len(line)):
        if line[ind] == '[':
            if (ind//4 + 1) in crates.keys():
                crates[ind//4 + 1].insert(0, line[ind + 1])
            else:
                crates[ind//4 + 1] = [line[ind + 1]]
    if line == '':  
        return True
    return False

def readMove(line, moves):
    line = line.split()
    moves.append([int(line[1]), int(line[3]), int(line[5])])


def moveCrate(crates, amount, fromCrate, toCrate, type = 0):
    if type == 0:
        crates[toCrate]+= crates[fromCrate][-amount::][::-1]
        crates[fromCrate] = crates[fromCrate][:-amount]
    else:
        crates[toCrate]+= crates[fromCrate][-amount:]
        crates[fromCrate] = crates[fromCrate][:-amount]
            

def getTopCrates(crates):
    length = len(crates.keys())
    topCrates = ''
    for index in range(length):
        topCrates += crates[index + 1].pop()
    return topCrates
    
    

def solution(fileName):
    cratesData = {}
    movesData = []
    with open(fileName, 'r') as inputFile:
        readingMoves = False
        for line in inputFile:
            if readingMoves:
                readMove(line, movesData)
            else:
                readingMoves = readCrates(line, cratesData)
    moves = movesData.copy()
    crates = cratesData.copy()                
    for move in moves:
         moveCrate(crates, move[0], move[1], move[2])
    print(getTopCrates(crates)) 
         
    moves = movesData.copy()
    crates = cratesData.copy()
    for move in moves:
         moveCrate(crates, move[0], move[1], move[2], 1)
    print(getTopCrates(crates))

if __name__ == '__main__':
    solution('test.txt')
    solution('task.txt')
    