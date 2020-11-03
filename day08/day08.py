import os
from collections import defaultdict, namedtuple

def main():
    print(os.getcwd())
    day = "08"
    inputFile = f'input/input{day}.txt'
    with open(inputFile) as f:
         lines = f.read().splitlines()
    
    # convert to ints
    print(lines[0].split(' '))

    # instructions
    inStruct = namedtuple("inStruct","reg op opVal condReg condCond condValue")
    instructions =[]
    # < = 0, <= 1, > 2 >= 3, == 4, != 5
    condDict = {'<':0, '<=':1, '>':2, '>=': 3, '==': 4, '!=':5}
    opDict = {'inc':1,'dec':-1}
    for l in lines:
        c = l.split(' ')
        currInst = inStruct(c[0],opDict[c[1]],int(c[2]),c[4],condDict[c[5]],int(c[6]))
        instructions.append(currInst)

    # registers 
    regs = defaultdict(int)
    print(regs["oa"])
    print(instructions[:3])
    def applyInst(reg,op,value):
        regs[reg] += (op*value)
    # work 
    maxMemory = 0
    minMemory = 0
    for i in instructions:
        if ((i.condCond == 0 and regs[i.condReg] < i.condValue) or (i.condCond==1 and regs[i.condReg]<= i.condValue)
            or (i.condCond == 2 and regs[i.condReg] > i.condValue) or (i.condCond == 3 and regs[i.condReg]>= i.condValue)
            or (i.condCond == 4 and regs[i.condReg] == i.condValue) or (i.condCond == 5 and regs[i.condReg] != i.condValue)):
                applyInst(i.reg,i.op,i.opVal)
        maxMemory = max(max(regs.values()),maxMemory)
        #minMemory = min(regs.values())
    print(max(regs.values()))
    print(maxMemory,minMemory)
if __name__ == "__main__":
    main()