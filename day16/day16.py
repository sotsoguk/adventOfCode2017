import os


def main():
    print(os.getcwd())
    day = "16"
    inputFile = f'input/input{day}.txt'
    with open(inputFile) as f:
         lines = f.read().splitlines()
    
    # convert to ints
    pos = [chr(i+97) for i in range(16)]
    print(pos)
    print(pos.index('o'))
    seen= []

    for i in range(1000000000):
        h = tuple(pos)
        if h in seen:
            print("Part 2:",i, ''.join(seen[1000000000%len(seen)]))
            break
        seen += [h]
        for inst in lines[0].split(','):
            if inst[0] == 'x':
                a,b = [int(c) for c in inst[1:].split('/')]
                #print("x",a,b)
                pos[a], pos[b] = pos[b], pos[a]
            elif inst[0] =='s':
                cycle = (int(inst[1:]))
                pos = pos[-cycle:] + pos[:-cycle]
            else:
                aname, bname = inst[1:].split('/')
                a,b = pos.index(aname), pos.index(bname)
                pos[a],pos[b] = bname,aname

    str = ""
    print(str.join(pos))

    #part 2
    

#     test = ['a','b','c','d','e']
#     test = test[2:]+test[0:2]
#    # test[3],test[4] = test[4],test[3]
#     print(test)
if __name__ == "__main__":
    main()