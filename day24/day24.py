import os


def main():
    print(os.getcwd())
    day = "24"
    inputFile = f'input/input{day}.txt'
    with open(inputFile) as f:
         lines = f.read().splitlines()
    
    components = []
    for l in lines:
        a,b = l.split('/')
        components.append((int(a), int(b)))
    
    #print(components)
    # convert to ints
    
    bridge = ([],0)

    def build(b, c):
        possible = [p for p in c if b[1] in p]
        #print(possible)
        if len(possible) == 0:
            yield b
        else:
            for p in possible:
                c_ = c.copy()
                c_.remove(p)
                for q in build((b[0] + [p],p[0] if b[1]==p[1] else p[1]),c_):
                    yield q
       
    build(bridge,components)

    # for b in build(bridge,components):
    #     print(b)

    #part1
    print(max( map(lambda bridge: sum([a+b for a,b in bridge[0]]), build(bridge,components) )))

    maxLen = max(map(lambda bridge:len(bridge[0]), build(bridge,components)))
    print(maxLen)
    longBridges = filter(lambda bridge: len(bridge[0]) == maxLen, build(bridge,components))
    #print(list(longBridges))
    print(max( map(lambda bridge: sum([a+b for a,b in bridge[0]]), longBridges )))

if __name__ == "__main__":
    main()