data={1:1, 2:8, 4:5, 3:3}

def sorted_custom(data, op):
    lst = list(data.items())
    print(lst)
    n = len(lst)-1
    for i in range(n): #0,1,2,3
        k = 0
        while k < n:  #0,1,2,3
            if lst[k+1][1]<lst[k][1]:
                lst[k+1], lst[k] = lst[k], lst[k+1]
                print(lst)
            k += 1
    flst = dict(lst)
    return(flst)


operation = lambda x: len(x)
result=sorted_custom(data, operation)
print("result:\t")
print(result)