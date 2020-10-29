import os
#from sets import Set

def computeHash(word):
    charHash = list(0 for i in range(26))
    for c in word:
        charHash[ord(c)-97] +=1
    
    #print(tuple(charHash))
    return tuple(charHash)

def isValidPassphrase2(line):
    seen = set()
    for word in line.split():
        h = computeHash(word)
        if h in seen:
            return False
        seen.add(h)
    return True

def isValidPassphrase(line):
    seen = set()
    for word in line.split():
        if word  in seen:
            return False
        seen.add(word)
    return True

def main():
    print(os.getcwd())
    day = "04"
    inputFile = f'input/input{day}.txt'
    with open(inputFile) as f:
         lines = f.read().splitlines()
    
    # convert to ints
    
    part1, part2 = 0,0
    for line in lines:
        if isValidPassphrase(line):
            part1 += 1
        if isValidPassphrase2(line):
            part2 += 1
    print(part1,part2)
   # print(isValidPassphrase2("abcde xyz ecdab"))
if __name__ == "__main__":
    main()