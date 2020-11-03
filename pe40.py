def digit(n):
    digits = 1
    while 10**digits < n:
        digits +=1
    
    base = 10**(digits-1)
    offset = n -base
    number = offset // digits
    numberoffset = offset % digits

    print(digits,offset,number,numberoffset)


digit(37)

