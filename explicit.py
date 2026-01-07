
lst=[x for x in range(11)]
maplst = []
for item in lst:
    item **= 2
    maplst.append(item) 
print(maplst)

filterlst = []
for num in lst:
    if not(num%2):
        filterlst.append(num)
print(filterlst)



def custom_map(func, lst):
    result_lst = [func(x) for x in lst]
    return result_lst

userLst= []
n=int(input("Enter the number of elements:\t"))
for i in range(n):
    item=int(input(f"Enter input number {i+1}:\t"))
    userLst.append(item)
print(userLst)
operation = input("Enter lamdba operation to carry out:\t")
print(operation)
operation = lambda x: x*2
result = list(custom_map(operation, userLst))
print(result)

def custom_filter(func, lst):
    result_lst = [x for x in lst if func(x)]
    return result_lst

operation = lambda x: x%2==0
result= list(custom_filter(operation, [x for x in range(11)]))
print(result)