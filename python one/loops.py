a=0
while a<10:
    print(a)
    a+=1

timer=30
while timer>=0:
    print(timer) if timer!=0 else print("Finish")    
    timer -= 1


names=['John', 'Jane', 'Alex', 'Michael']
i=0
while i<4:
    # names[i]=names[i] + str(i)
    names[i]=f"{names[i]}, {i+1}"
    i += 1

print(names)