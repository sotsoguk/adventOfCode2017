import os
from collections import defaultdict, deque

def main():
    print(os.getcwd())
    day = "18"
    inputFile = f'input/input{day}.txt'
    with open(inputFile) as f:
         lines = f.read().splitlines()
    regs = [defaultdict(int),defaultdict(int)]
    for i in range(2):
        regs[i]['p'] = i
    # convert to ints
    lastFreq = 0
    recovered = 0
    # store commands
    insts = []
    for cmds in lines:
        cmd, *args = cmds.split(' ')
        insts.append([cmd,args])
    # ip = 0
    # runs = 0
    # notPlayed = True
    def getValue(regorval,currProgram):
        if regorval.isalpha():
           return int(regs[currProgram][regorval])
        else:
            return int(regorval)

    # while notPlayed:
    #     cmd, args = insts[ip]
    #     runs += 1
    #     print(regs,ip,cmd,args)
    #     if cmd == "snd":
    #         lastFreq = getValue(args[0])
    #     elif cmd =="set":
    #         regs[args[0]] = getValue(args[1])
    #     elif cmd == "add":
    #         regs[args[0]] += getValue(args[1])
    #     elif cmd =="mul":
    #         regs[args[0]] *= getValue(args[1])
    #     elif cmd =="mod":
    #         regs[args[0]] %= getValue(args[1])
    #     elif cmd == "rcv":
    #         if regs[args[0]] != 0:
    #             print(ip,lastFreq)
    #             recovered +=1 
    #             notPlayed = False
    #             break
    #     elif cmd =="jgz":
    #         if regs[args[0]] >0:
    #             ip += getValue(args[1])
    #         else:
    #             ip += 1
        
    #     if cmd != "jgz":
    #         ip +=1
    #     print(ip)
    #     if ip<0 or ip>=len(insts):
    #         print("OOB")
    #         break

    # part 2
    currProgram = 0
    ip = [0,0]
    status = [1,1]
    qus = [deque([]),deque([])]
    runs = 0
    send1 = 0
    while True:#(status[0] >0 or status[1] > 0):
        runs += 1
        if ip[currProgram]<0 or ip[currProgram]>=len(insts):
            print("OOB")
            status[currProgram] = 0
            currProgram = (currProgram+1) %2 
            continue
        cmd, args = insts[ip[currProgram]]
        runs += 1
        #print(regs,ip,cmd,args)
        if cmd == "snd":
            value = getValue(args[0],currProgram)
            # print("Send",currProgram)
            if currProgram == 1:
                send1 += 1
            qus[(currProgram+1)%2].append(value)
            ip[currProgram] +=1
        elif cmd =="set":
            regs[currProgram][args[0]] = getValue(args[1],currProgram)
            ip[currProgram] +=1
        elif cmd == "add":
            regs[currProgram][args[0]] += getValue(args[1],currProgram)
            ip[currProgram] +=1
        elif cmd =="mul":
            regs[currProgram][args[0]] *= getValue(args[1],currProgram)
            ip[currProgram] +=1
        elif cmd =="mod":
            regs[currProgram][args[0]] %= getValue(args[1],currProgram)
            ip[currProgram] +=1
        elif cmd == "rcv":
            # if regs[args[0]] != 0:
            #     print(ip,lastFreq)
            #     recovered +=1 
            #     notPlayed = False
            #     break
            if qus[currProgram]: # not empty
                status[currProgram] = 1
                c = qus[currProgram].popleft()
                regs[currProgram][args[0]] = int(c)
                ip[currProgram] +=1
            else:
                status[currProgram] = 0
                #ip[currProgram] +=1
                currProgram = (currProgram +1)%2
                # if qus[currProgram]:
                #      status[currProgram] = 1
        elif cmd =="jgz":
            #if regs[currProgram][args[0]] >0:
            if getValue(args[0],currProgram) >0:
                ip[currProgram] += getValue(args[1],currProgram)
            else:
                ip[currProgram] += 1
        #print(runs,currProgram,status,regs,qus)
        if ((status[0] == 0 and not qus[0]) and (status[1]==0 and not qus[1])):
            print("EOL")
            break
        # if cmd != "jgz":
        #     ip[currProgram] +=1
        #print(currProgram, ip)
        # if ip[currProgram]<0 or ip[currProgram]>=len(insts):
        #     print("OOB")
        #     status[currProgram] = 0
        #     currProgram = (currProgram+1) %2 

    print(send1)
if __name__ == "__main__":
    main()