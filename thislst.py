op_on = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 9, 10]
nums = [ x**2 if x%2==0 else x*2 for x in range(10) ]
print(nums)
numsE = [x**2 for x in range(10) if x%2==0 ]
numsO = [x*2 for x in range(10) if x%2!=0]
nums = numsE + numsO


def square(func):
    def myinner(num):
        result = func(num)
        print(result**2)
    return myinner


@square
def testing(num):
    return num+5

testing(2)

def Capitalize(func):
    def myinner(value):
        return func(value).upper()
    return myinner

@Capitalize
def testfunc(name):
    return "The Name is " + name

print(testfunc("bdog"))

