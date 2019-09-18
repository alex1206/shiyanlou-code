a = 1
while a <= 100:
    if a%7==0 or a%10==7 or a//10==7:
        pass
    else:
        print(a)
    a+=1
