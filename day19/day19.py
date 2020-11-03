import os
from collections import namedtuple
from dataclasses import dataclass

@dataclass
class pos2d:
    x: int
    y:int

def main():
    print(os.getcwd())
    day = "19_d"
    inputFile = f'input/input{day}.txt'
    with open(inputFile) as f:
        lines = f.read().splitlines()

    # convert to ints
    #pos2d = namedtuple("pos2d", ['x', 'y'])
    #pos2d = recordtype("pos2d", ['x', 'y'])
   
    dirs = {0: pos2d(1, 0), 1: pos2d(0, -1), 2: pos2d(-1, 0),
            3: pos2d(0, 1)}  # R D L D
    # search startpos
    xs = lines[0].index('|')
    minX, minY, maxX, maxY = 0, 0, len(lines[0])-1, len(lines)-1

    currPos = pos2d(xs, 0)
    direction = 3
    print(currPos)
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    way = "-|"
    path = []
    print(lines)

    def validPos(pos):
        if pos.x < minX or pos.x > maxX or pos.y < minY or pos.y > maxY:
            return False
        return True
    # find starting pos
    runs = 0
    steps = 0
    while True:
        runs += 1
        currPos.x += dirs[direction].x
        currPos.y += dirs[direction].y
        
        if not validPos(currPos):
            print("OutOfBounds")
            print(steps)
            break
        steps += 1
        currToken = lines[currPos.y][currPos.x]
        
        #print(currToken,currPos,direction)
        if currToken in letters or currToken in way:
            if currToken in letters:
                path += currToken
            
        
        elif currToken == '+':
            # look for possivle pos
            foundNextPos = False
            possibleNextDirs = [(direction+1) % 4, (direction-1) % 4]
            for d in possibleNextDirs:
                possibleNextPos = pos2d(
                    currPos.x + dirs[d].x, currPos.y + dirs[d].y)
                nextToken = lines[possibleNextPos.y][possibleNextPos.x]
                if nextToken in letters or nextToken == '+':
                    direction = d
                    foundNextPos = True
                    break
                elif nextToken in way:
                    if (((direction % 2) == 0 and nextToken == '|') or ((direction % 2) == 1 and nextToken == '-')):
                        direction = d
                        foundNextPos = True
                        break
            if not foundNextPos:
                print("NO WAY OUT")
                break
        else:
            print("ERROR")
            break

    print(''.join(path))
    print(steps)


if __name__ == "__main__":
    main()
