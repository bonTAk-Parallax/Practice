#Complete--Bubble sort on lists

# words = ["apple", "pie", "banana", "cherry", "ea"]

# def sorted_custom(lst, func):
#     temp = []
#     for k in range(len(lst)):
#         min = lst[k]
#         i=0
#         while i < len(words)-1:
#             if len(lst[i+1])<len(min):
#                 temp.insert(0, min)
#                 min=lst[i+1]
#             i+=1
#         print(temp)       
        # temp.insert(0, min)
        # return lst if len(lst)==len(words) else sorted_custom(lst[i:])




words = ['one', 'five', 'three', 'ten', 'eight', 'fifteen', 'nine', 'six']
words = ["apple", "pie", "banana", "cherry", "ea"]

def sorted_custom(lst, func):
    for j in range(func(lst)-1):
        print(f"Iteration number: {j+1}.")
        i=0
        while i < func(words)-1:
            if func(lst[i])>func(lst[i+1]):
                # right = lst[i+1]
                # lst[i+1] = lst[i]
                # lst[i] = right
                lst[i], lst[i+1] = lst[i+1], lst[i]
                print(lst)
            i+=1
        print("\n")
    return lst

operation = lambda x: len(x)
result=sorted_custom(words, operation)
print(result)




        
