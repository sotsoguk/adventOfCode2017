import os
from collections import defaultdict
import re

def balanceTower(root) 

def main():
    print(os.getcwd())
    day = "07"
    inputFile = f'input/input{day}.txt'
    with open(inputFile) as f:
         lines = f.read().splitlines()
    
    weights = {}
    children = defaultdict(list)
    #name, weight, *children = re.findall(r'\w+',lines[0])
    
    for l in lines:
        name, weight, *kids = re.findall(r'\w+',l)
        weights[name] = int(weight)
        children[name] = kids

    print(set(weights.keys())- set(sum(children.values(),[])))
    # print(weights)
    # print(children)
if __name__ == "__main__":
    main()