one = int(input())
two = int(input())
three = int(input())
 
if one > two and two > three:
    print(one)
    print(two)
    print(three)
elif one > three and three > two:
    print(one)
    print(three)
    print(two)    
elif two > one and one > three:
    print(two)
    print(one)
    print(three)
elif two > three and three > one:
    print(two)
    print(three)
    print(one)
elif three > two and two > one:
    print(three)
    print(two)
    print(one)
elif three > one and one > two:
    print(three)
    print(one)
    print(two)

