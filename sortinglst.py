#incomplete
def sorted_custom(lst, func):
    newlst=[]
    for i in range(len(lst)):
        if i<len(lst):
            a=lst[i]
            b=lst[i+1]
            if len(a)<len(lst[a]):
                newlst.insert(0, a)
            else:
                newlst.insert(0,b)
    return newlst

words = ["apple", "pie", "banana", "cherry"]
operation = lambda x: len(x)
result=sorted_custom(words, operation)