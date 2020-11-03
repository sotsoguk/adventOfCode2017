import os
import re
from collections import defaultdict
def main():
    print(os.getcwd())
    day = "25"
    inputFile = f'input/input{day}.txt'
    with open(inputFile) as f:
         lines = f.read().splitlines()
    
    # find startValues
    startState = lines[0][-2]
    print(startState)
    diag = int(re.findall(r'\d+',lines[1])[0])
    print(diag)
    i = 3
    commands = {}
    while i < len(lines):
        # new state
        activeState = lines[i][-2]
        i+=2
        activeValue = 0
        writeValue = int(lines[i][-2])
        i += 1
        moveDir = -1
        if "right" in lines[i]:
            moveDir = 1
        i += 1
        nextState = lines[i][-2]
        commands[(activeState,activeValue)] = (writeValue,moveDir,nextState)
        i+=2
        
        
        activeValue = 1
        writeValue = int(lines[i][-2])
        i += 1
        moveDir = -1
        if "right" in lines[i]:
            moveDir = 1
        i += 1
        nextState = lines[i][-2]
        commands[(activeState,activeValue)] = (writeValue,moveDir,nextState)
        i+=2

    print(commands)
    tape = defaultdict(int)
    currState = (startState,0)
    step = 0
    while step < diag:
        curr = (currState[0],tape[currState[1]])
        cmd = commands[curr]
        tape[currState[1]] = cmd[0]
        currState = (cmd[2],currState[1]+cmd[1])
        step += 1
    print(tape)
    print(sum(tape.values()))
if __name__ == "__main__":
    main()