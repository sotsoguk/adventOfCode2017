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
    # p, v a
    timeStep = 1000000000
    minDist, minArg = 1e100,0

    # for i,p in enumerate(particles):
    #     finalpos = [0,0,0]
    #     for c in range(2):
    #         finalpos[c] = p[c] + p[c+3] * timeStep + p[c+6] * timeStep**2 //2
    #     tmpDist = abs(finalpos[0])+ abs(finalpos[1]) + abs(finalpos[2])
    #     print(tmpDist)
    #     if tmpDist < minDist:
    #         minDist = tmpDist
    #         minArg = i

    # find stars with minimal acceleration
    
    minAccel = min(particles,key = lambda p:sum(abs(x) for x in p[6:]))
    print(minAccel)
    minA = sum([abs(c) for c in minAccel[6:]])
    print(minA)
    allMinAccel = [x for x in particles if sum([abs(c) for c in x[6:]])==minA]
    
    minVel = min(allMinAccel, key = lambda p:sum(abs(x) for x in p[3:6]))
    minV = sum([abs(c) for c in minVel[3:6]])
    allMinVel = [x for x in allMinAccel if sum([abs(c) for c in x[3:6]])==minV]
    print(minV)
    print(minVel)
    test = [-1,-2,-3,4]
    #print(sum([abs(t) for t in test]))
   # print(allMinAccel)
   # find particle
    for i,p in enumerate(particles):
        if p == minVel[0]:
            print(i,p)
    
if __name__ == "__main__":
    main()


12499999531999996713
124999953199996713