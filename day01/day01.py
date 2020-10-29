import os


def main():
    print(os.getcwd())
    day = "01"
    inputFile = f'input/input{day}.txt'
    with open(inputFile) as f:
         lines = f.read().splitlines()
    
    # convert to ints
    numbers = [int(c) for c in lines[0]]
    
    n = len(numbers)
    
    part1 = sum(d for i,d in enumerate(numbers) if d == numbers[(i+1) % n])
    
    part2 = sum(d for i,d in enumerate(numbers[:n//2]) if d == numbers[(i+n//2) % n]) << 1
    print(part1)
    print(part2)
if __name__ == "__main__":
    main()