import os


def main():
    print(os.getcwd())
    day = "06"
    inputFile = f'input/input{day}.txt'
    with open(inputFile) as f:
         lines = f.read().splitlines()
    
    # convert to ints
    banks = [int(c) for c in lines[0].split('\t')]
    # banks = [0,2,7,0]
    seen = set()
    seenPos = dict()
    n = len(banks)
    steps = 1
    part2 = 0
    while True:
    
        # find bank with most blocks
        pos = banks.index(max(banks))
        blocks = banks[pos]
        banks[pos] = 0
        for i in range(1,blocks+1):
            banks[(pos+i)%n] += 1
        
        
        bankHash = tuple(banks)
        
        if bankHash in seen:
            part2 = steps - seenPos[bankHash]
            break
            
        seen.add(bankHash)
        seenPos[bankHash] = steps
        steps += 1
        
    
    print(steps)
    print(part2)
    #print(seenPos)
    # part1 = sum(d for i,d in enumerate(numbers) if d == numbers[(i+1) % n])
    
    # part2 = sum(d for i,d in enumerate(numbers[:n//2]) if d == numbers[(i+n//2) % n]) << 1
    # print(part1)
    # print(part2)
if __name__ == "__main__":
    main()