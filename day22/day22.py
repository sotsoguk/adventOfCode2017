import os
from dataclasses import dataclass
from collections import defaultdict
@dataclass
class p2d:
    x: int
    y: int

def main():
    print(os.getcwd())
    day = "22"
    inputFile = f'input/input{day}.txt'
    with open(inputFile) as f:
         lines = f.read().splitlines()
    
    # convert to ints
    gridSize = len(lines[0])
    print(gridSize)
    startX = gridSize //2
    startPos = p2d(startX,startX)
    print(startPos)
    infected = defaultdict(int)
    #print(infected[tuple([2,2])])
    # for x in range(gridSize):
    #     for y in range(gridSize):
    #         if lines[y][x] == '#':
    #             infected[tuple([x,y])] = 1
    
    # print(infected)

    # # U L D R
    # dirs = {0: p2d(0,-1), 1: p2d(-1,0),2:p2d(0,1),3:p2d(1,0)}
    # d = 0
    # b = 0
    # runs = 10000
    # currPos = startPos
    # for i in range(runs):
    #     currTuple = tuple([currPos.x,currPos.y])
    #     if infected[currTuple] == 1:
    #         d = (d-1) %4
    #         del infected[currTuple]
    #     else:
    #         d = (d+1) %4
    #         infected[currTuple] =1
    #         b +=1

    #     currPos.x += dirs[d].x
    #     currPos.y += dirs[d].y
    #     #print(i,infected)
    
    # print(b)
    
    # part 2
    for x in range(gridSize):
        for y in range(gridSize):
            if lines[y][x] == '#':
                infected[tuple([x,y])] = 2
    
    print(infected)

    # U L D R
    dirs = {0: p2d(0,-1), 1: p2d(-1,0),2:p2d(0,1),3:p2d(1,0)}
    d = 0
    b = 0
    runs = 10000000
    currPos = startPos
    for i in range(runs):
        currTuple = tuple([currPos.x,currPos.y])
        if infected[currTuple] == 0:
            d = (d+1)%4
            #del infected[currTuple]
        elif infected[currTuple] == 1:
             b +=1
        elif infected[currTuple] == 2:
            d = (d-1) %4
            #infected[currTuple] =1
           
        else:
            d = (d+2) %4
        
        infected[currTuple] = (infected[currTuple]+1)%4

        currPos.x += dirs[d].x
        currPos.y += dirs[d].y
        #print(i,infected)
    
    print(b)
if __name__ == "__main__":
    main()