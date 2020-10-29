import os


def main():
    print(os.getcwd())
    day = "02"
    inputFile = f'input/input{day}.txt'
    with open(inputFile) as f:
         lines = f.read().splitlines()
    
    # convert to ints
#    data = [int(c) for c in lines[i].split() for i in len(lines)]
    data = [[int(i) for i in line.split()] for line in lines]

    # part1 
    part1 = sum(max(line) - min(line) for line in data)
    print(data)
    print(part1)

    # part2
    #part2 = sum()
    p2sum = 0

    for l in data:
        for i in range(len(l)):
            for j in range(i+1,len(l)):
                a,b = l[i],l[j]
                if (a<b):
                    a,b = b,a
                if (a%b == 0):
                    # print(a,b,a//b)
                    p2sum += a//b
    print(p2sum)

    p22 = sum(b//a for line in data for a in line for b in line if b>a and b%a==0)
    print(p22)
if __name__ == "__main__":
    main()