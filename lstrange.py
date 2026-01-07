lst=[x for x in range(11)]
newLst=[x for x in range(12, 21)]
newLst += lst[2:5]
newLst[:4]=[2222, 3333]
newLst.sort(reverse=False)
print(newLst)

divided =  list(map(lambda x: x/2, newLst))
print(divided)
evens = list(filter(lambda x: x%2==0, newLst))
print(evens)

sortLst=["one", "two", "three", "four", "five"]
newSort = list(sorted(sortLst, key= lambda x: x.upper()))
print(newSort)