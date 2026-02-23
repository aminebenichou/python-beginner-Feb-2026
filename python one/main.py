numbers=[1,2,3,4,5,6,7,8,9,10]

# method 1
if 8 in numbers:
    position = numbers.index(8)
    print(position)


# method 2

a=6
part_one = list(range(1, 6))
part_two = list(range(6, 11))
if a in part_one:
    if a==part_one[0]:
        print(0)
    elif a==part_one[1]:
        print(1)
    elif a==part_one[2]:
        print(2)
    elif a==part_one[3]:
        print(3)
    elif a==part_one[4]:
        print(4)
elif a in part_two:
    if a==part_two[0]:
        print(5)
    elif a==part_two[1]:
        print(6)
    elif a==part_two[2]:
        print(7)
    elif a==part_two[3]:
        print(8)
    elif a==part_two[4]:
        print(9)

# method 3
if numbers[0]==a or numbers[-1]==a:
    if numbers[0]==a:
        print(0)
    else:
        print(9)
elif numbers[1]==a or numbers[-2]==a:
    if numbers[1]==a:
        print(1)
    else:
        print(8)

elif numbers[2]==a or numbers[-3]==a:
    if numbers[2]==a:
        print(2)
    else:
        print(7)

elif numbers[3]==a or numbers[-4]==a:
    if numbers[3]==a:
        print(3)
    else:
        print(6)

elif numbers[4]==a or numbers[-5]==a:
    if numbers[4]==a:
        print(4)
    else:
        print(5)