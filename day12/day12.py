import os
import re
from collections import deque

def main():
    print(os.getcwd())
    day = "12"
    inputFile = f'input/input{day}.txt'
    with open(inputFile) as f:
         lines = f.read().splitlines()
    
    # convert to ints
    
    numNodes = len(lines)
    connections = [[] for i in range(numNodes)]
    # parse connections
    for i,l in enumerate(lines):
        #print([int(s) for s in re.findall("\d+",lines[i])])
        _, *connectedTo = [int(s) for s in re.findall("\d+",l)]
        #print(node, connectedTo)
        connections[i] = connectedTo

    # for c in connections:
    #     print(c)

    # part 1
    # visited = set()
    # queue = deque([0])
    # clique = []
    # while queue:
    #     currNode = queue.popleft()
    #     # mark visited
    #     visited.add(currNode)
    #     for n in connections[currNode]:
    #         if not n in visited:
    #             queue.append(n)
        
    #     # print(queue)
    #     # queue.popleft()
    #     # print(queue)
    # print(len(visited))
    # print()
    # part 2
    visited = set()
    remaining = set(i for i in range(numNodes))
    # for i in range(numNodes):
    #     remaining.add(i)
    numCliques = 0
    cliques = []
    while ( len(remaining) > 0):
        numCliques += 1
        cliqueSize = 0
        currClique = []
        # select an unvisited node
        queue = deque([remaining.pop()])
        while queue:
            cliqueSize += 1
            currNode = queue.popleft()
            visited.add(currNode)
            currClique.append(currNode)
            
            if currNode in remaining:
                remaining.remove(currNode)
            for n in connections[currNode]:
                if not n in visited and not n in queue:
                    queue.append(n)
            # print(visited)
            # print(remaining)
            # print(queue)
            # print(currNode,cliqueSize)
        cliques.append(currClique)
    
    print(cliques)
    print(len(cliques))
    print(len(cliques[0]))
if __name__ == "__main__":
    main()