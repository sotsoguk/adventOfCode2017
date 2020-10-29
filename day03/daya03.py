import os
import math

def spiralToXY(s):
    if s == 1:
        return (0,0)
    spirNum = lambda x: math.ceil((math.sqrt(x)+1) / 2)
    i = spirNum(s)
    # compute sidelength 
    spiralLength = (i-1)*8
    sideLength = spiralLength // 4
    posInSpiral = ((s - (2*i-3)**2)) % spiralLength
    posInSide = posInSpiral % sideLength
    side = (posInSpiral) //sideLength
    cornerCoords = {0:[1,-1], 1:[1,1],2:[-1,1],3:[-1,-1]}
    sideWalk={0:[0,1],1:[-1,0],2:[0,-1],3:[1,0]}
    #corner = cornerCoords[side] * (i-1)
    
    cx = cornerCoords[side][0]*(i-1) + posInSide*sideWalk[side][0]
    cy = cornerCoords[side][1]*(i-1) + posInSide*sideWalk[side][1]
    return cx,cy
    #print(s,i, side,posInSpiral,posInSide, cx,cy)
    #print(f'{s}: spiral {i}, side {side}, sidelength {sideLength} posSpirtal {posInSpiral}, posSide {posInSide} : ({cx},{cy}')


def XYtoSpiral(x,y):
    if x==0 and y == 0:
        return 1
    # corner element
    i = max(abs(x),abs(y))+1
    sqr = (2*i-1)**2
    # corners
    if (abs(x) == abs(y)):
       
        if x>0 and y>0: # right upper
            return sqr-6*(i-1)
        elif x<0 and y>0: # left upper
            return sqr-4*(i-1)
        elif x<0 and y<0: # left lower
            return sqr - 2*(i-1)
        else:
            return sqr
    # check right side
    if x==(i-1):
        return sqr-6*(i-1) -(i-1)+y
    elif x==-(i-1):
        return sqr-4*(i-1) +(i-1)-y
    elif y == (i-1):
        return sqr-6*(i-1) + (i-1)-x
    else:
        return sqr - 2*(i-1) + x-(1-i)
def part2(m):
    diags = {0:[1,0],1:[1,1],2:[0,1],3:[-1,1],4:[-1,0],5:[-1,-1],6:[0,-1],7:[1,-1]}
    series = [1]
    i = 2
    while series[-1] < m:
        x,y = spiralToXY(i)
        currSum = 0
        for direction in diags.values():
            
            currX = x + direction[0]
            currY = y + direction[1]
            currN = XYtoSpiral(currX,currY)
            if currN < i:
                currSum += series[currN-1]
        series.append(currSum)
        i += 1
    print(series[-1])
def main():
    print(os.getcwd())
    day = "03"
    #inputFile = f'input/input{day}.txt'

    input03 = 368078;
    # with open(inputFile) as f:
    #      lines = f.read().splitlines()
    
    # convert to ints
  #  numbers = [int(c) for c in lines[0]]
    
    # part1
    # x,y = spiralToXY(input03)
    # print(abs(x)+abs(y))

    # print(XYtoSpiral(3,3))
    # print(XYtoSpiral(2,3))
    # print(XYtoSpiral(0,3))
    # print(XYtoSpiral(-3,3))
    # print(XYtoSpiral(-3,0))
    # print(XYtoSpiral(-3,-3))
    # print(XYtoSpiral(3,-3))

    part2(368078)
    

if __name__ == "__main__":
    main()