

lst = [1,2,3,4,5,2,3,1,6,7,8,9,10,5,4,1]  #3 one, 2 two, 2 three, 2 five, 2 four
temp = {}  
for i in range(len(lst)):
    count = 0
    for j in range(len(lst)):
        if lst[i]==lst[j]:
            count += 1
            temp.update({lst[i]: count})
for k,v in temp.items():
    print(f"Count for {k}:\t{v}")