import os


def runCode1(code):
    ip = 0
    steps = 0
    while ip>=0 and ip<len(code):
        newIP = ip + code[ip]
        code[ip] += 1
        ip = newIP
        steps += 1
    return steps

def runCode2(code):
    ip = 0
    steps = 0
    while ip>=0 and ip<len(code):
        newIP = ip + code[ip]
        if code[ip] >=3:
            code[ip] -=1
        else:
            code[ip] +=1
        ip = newIP
        steps += 1
    return steps
def main():
    print(os.getcwd())
    day = "05"
    inputFile = f'input/input{day}.txt'
    with open(inputFile) as f:
         lines = f.read().splitlines()
    
    code = []
    for l in lines:
        code.append(int(l))
    
    print(runCode2(code))
if __name__ == "__main__":
    main()