# functions
def greet():  # this is just printing, it doesn't return anything
    print("Hello everybody")

# we need to call the function:
p = greet() # its not returning anything that's why p is empty


def getsum(a, b):  # this function returns something(c)
    c = a + b
    return c

add = getsum(2, 5)
print(add)


def getSum(a, b=1):  # this function returns c,
    c = a + b
    return c


z = getSum(4) # b is already mention it will take this as default value if not mentioned
print(z)


num = 4
def getSums(a, b):
    global num
    num = a + b
    return num


p = getSums(1, 5)
print(p)
print(num) # it will print 4 , if we mention global num in the function then it wil change the value to 6
# the value be change if we mention global num in the function

# sum of 3 variables
def getSum3(a, b, c):
    num = a + b + c
    return num


k = getSum3(1, 2, 3)
print(k)


def getSumM(*args):  # for many inputs and type of args is tuple
    print(args)
    num = 0
    for a in range:
        num = num + a
        return num


l = getSumM(1, 2, 3, 4, 5)
print(l)


def getSumd(**kwargs):  # for many inputs and type of args is dict
    print(kwargs, type(kwargs))


l = getSumd(a=1, b=2, c=3, d=4, e=5)



def getdict1(**kwargs):  # for many inputs and type of args is dict
    print(kwargs, type(kwargs))


pp = getdict1(id=13, name='Sheenu', age=28)


from mypackage import calc as c
from mypackage import calc1 as c1
# create files in another package and import their function in current file
print(c.mgetsum(2, 4))
print(c1.mgetsub(1, 2))
