import os
import re

def main():
    print(os.getcwd())
    day = "20"
    inputFile = f'input/input{day}.txt'
    with open(inputFile) as f:
         lines = f.read().splitlines()
    
    # convert to ints
    numParticles = len(lines)
    particles = []
    for l in lines:
        particles.append([int(c) for c in re.findall('-?\d+',l)])
    
    timeStep = 1000000000
    minDist, minArg = 1e100,0

    for i,p in enumerate(particles):
        finalpos = [0,0,0]
        for c in range(2):
            finalpos[c] = p[c] + p[c+3] * timeStep + p[c+6] * timeStep**2 //2
        tmpDist = abs(finalpos[0])+ abs(finalpos[1]) + abs(finalpos[2])
        print(tmpDist)
        if tmpDist < minDist:
            minDist = tmpDist
            minArg = i

    print(minDist,minArg)

    
    
if __name__ == "__main__":
    main()