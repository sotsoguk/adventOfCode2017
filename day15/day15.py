import os


def main():
    print(os.getcwd())
    # day = "01"
    # inputFile = f'input/input{day}.txt'
    # with open(inputFile) as f:
    #      lines = f.read().splitlines()
    
    valueA ,valueB= 289,629
    #valueA, valueB = 65, 8921
    facA, facB = 16807, 48271
    divisor = 2147483647
    modulus = 1<<16
    runs = 5000000
    matches = 0
    for i in range(runs):
        while True:
            valueA = (valueA * facA) % divisor
            if not(valueA&3):
                break
        while True:
            valueB = (valueB * facB) % divisor
            if not(valueB&7):
                break
        #print(valueA, valueB)
        if ((valueA & 0xffff) ^ (valueB &0xffff)) == 0:
            matches += 1
        
    #print(not(15&3))
    print(matches)
if __name__ == "__main__":
    main()