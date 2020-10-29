import os
import re

def main():
    print(os.getcwd())
    day = "12"
    inputFile = f'input/input{day}.txt'
    with open(inputFile) as f:
         lines = f.read().splitlines()
    
    # convert to ints
    for i in range(10):
        print([int(s) for s in re.findall("\d+",lines[i])])
if __name__ == "__main__":
    main()