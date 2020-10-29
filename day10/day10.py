import os

def reverseCyclic(s,start,length):
    n = len(s)
    temp = []
    for i in range(length):
        temp.append(s[(start+i)%n])
    temp.reverse()
    for i in range(length):
        s[(start+i)%n] = temp[i]
    
    return s
def part1(lens):
    knot = [i for i in range(256)]
    #knot = [0,1,2,3,4]
    skip = 0
    pos = 0
    for l in lens:
        knot = reverseCyclic(knot,pos,l)
        pos += (l+skip)
        skip += 1
        #print(knot)
    print(knot)
    print(knot[0] * knot[1])

def part2(lens,runs):
    knot = [i for i in range(256)]
    skip = 0
    pos = 0
    for i in range(runs):
        for l in lens:
            knot = reverseCyclic(knot,pos,l)
            pos += (l+skip)
            skip += 1
    #sparse hash
    print(knot)
    dknot = [0] * 16
    # densify
    for i in range(16):
        dknot[i] = knot[16*i]
        for j in range(1,16):
            dknot[i] ^= knot[16*i+j]
    print(dknot)
    # convert to string
    hashString = ''
    for i in dknot:
        tmpHex = hex(i)
        if len(tmpHex[2:]) == 2:
            hashString += tmpHex[2:]
        else:
            hashString += ('0' + tmpHex[2:])
    print(hashString)
def main():
    print(os.getcwd())
    day = "10"
    inputFile = f'input/input{day}.txt'
    with open(inputFile) as f:
         lines = f.read().splitlines()
    
    # convert to ints
    lens = [int(c) for c in lines[0].split(',')]
    lens2 = [ord(c) for c in lines[0]]
    lens2 += [17,31,73,47,23]
    
    part2(lens2,64)
    # print(hex(208))
    # print(lens)
    #part1(lens)
    #print(code)
    
    # print(a)
    # aa = reverseCyclic(a,7,5)
    # print(aa)
if __name__ == "__main__":
    main()