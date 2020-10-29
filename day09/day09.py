import os


def countGroups(s):
    level = 0
    balance = 0
    garbage = False
    skip = False
    score = 0
    garbageCount = 0
    for c in s:
        if skip:
            skip = False
            continue
        if garbage:
            if c == '!':
                skip = True
            elif c=='>':
                garbage = False
            else:
                garbageCount +=1
        else:
            if c == '{':
                level += 1
                balance += 1
            elif c == '}':
                score += level
                level -= 1
                balance -=1
            elif c=='<':
                garbage = True
        
    return score,garbageCount
def main():
    print(os.getcwd())
    day = "09"
    inputFile = f'input/input{day}.txt'
    with open(inputFile) as f:
         lines = f.read().splitlines()
    
    # convert to ints
    #print(countGroups("{{<!!>},{<!!>},{<!!>},{<!!>}}"))
    print(countGroups(lines[0]))
if __name__ == "__main__":
    main()