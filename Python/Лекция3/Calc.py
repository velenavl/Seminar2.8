# def sum(x, y):
#     return x+y



def mylt(x, y):
    return x*y

def calc(op, a, b):
    print(op(a, b))
    # return op(a, b)

calc(lambda x, y: x+y , 4, 5)
