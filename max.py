def total(*args):
    sum = 0
    for num in args:
        sum += num
    return sum
print(total(5,4,3,2,1))



def max_of_all(*args):
    if len(args) == 0:
        return None
    num1 = args[0]
    for num in args:
        if num>num1:
            num1=num
    return num1



def max_of_all(*args):
    if len(args) == 1:
        return args[0]
    else:
        max = args[0] if args[0]>args[1] else args[1]
        return max_of_all(max, *args[2:])

print(max_of_all(10, 50, 22, 11, 77, 22, 33))   



def maxxx(*args):
    if len(args) == 1:
        return args[0]
    else:
        return args[0] if args[0] > maxxx(*args[1:]) else maxxx(*args[1:])
    
print(maxxx(10, 50, 22, 11, 77, 22, 33)) 

thislst = [1,2,2,2,2]
newlst = [x for x in thislst if x%2==0]
print(newlst)

