def mixture(name, **details):
    print(f"User {name.upper()}, Welcome!")
    for k, v in details.items():
        print(k + ':', v)
    
mixture("Bob", status= "Married", age= 44, address= "Nevada")

def Book(Bookname, *args, **kwargs):
    print(f"The Book's name is {Bookname}.")
    print("Details:")
    for arg in args:
        print(arg)
    for k,v in kwargs.items():
        print(k+':', v)

Book("Moby", "Herman Hessee", 1885, "US publishing studio", pages=397, cost="58$")