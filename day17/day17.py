import os


def main():
    print(os.getcwd())
    day = "17"
    # inputFile = f'input/input{day}.txt'
    # with open(inputFile) as f:
    #      lines = f.read().splitlines()
    
    # convert to ints
    inp = 345
   # inp = 3
    
    # buffer = [0]
    # pos = 0
    # bufferLength = 1
    # numInsertions = 50000001
    # for i in range(1,numInsertions):
    #     pos += inp
    #     pos %= bufferLength
    #     buffer.insert(pos+1,i)
    #     bufferLength += 1
    #     pos += 1
    #     #print(i,pos,buffer)
    # # print(buffer[pos-5:pos+5])
    # # print(buffer[pos+1])
    # zeroLoc = buffer.index(0)
    # print(buffer[zeroLoc],buffer[zeroLoc+1],zeroLoc)
    # print(buffer[zeroLoc:zeroLoc+3])
    #part 2
    buffer = [0]
    pos = 0
    part2 = 0
    bufferLength = 1
    numInsertions = 50000001
    for i in range(1,numInsertions):
        pos += inp
        pos %= bufferLength
        if pos == 0:
            part2 = i
        #buffer.insert(pos+1,i)
        bufferLength += 1
        pos += 1
        #print(i,pos,buffer)
    print(part2)
    # print(buffer[pos-5:pos+5])
    # print(buffer[pos+1])
    # zeroLoc = buffer.index(0)
    # print(buffer[zeroLoc],buffer[zeroLoc+1],zeroLoc)
    # print(buffer[zeroLoc:zeroLoc+3])
if __name__ == "__main__":
    main()