Don't Use Mutable Types As Default Values!

It is dangerous to use a mutable type (eg a list, dictionary) as a default value, because on repeated calls to the function, a new default value will not be allocated!

Check out the following sample code:
def f(x, myList = []):
    myList.append(x)
    return myList
>>> f(6)
[6]
>>> f(10)
[6, 10]


The correct, "Pythonic" way to write this code would be:
def f(x, myList = None):
    if myList == None:
        # This WILL allocate a new list on every call to the function.
        myList = []
    myList.append(x)
    return myList
>>> f(6)
[6]
>>> f(10)
[10]

=================================================================================================================================

You can't pass positional arguments after keyword arguments.

def lotsOfParameters1(a,b,c,d,e):
    print a
    print b
    print c
    print d
    print e

>>> lotsOfParameters1(a=5,b=1,c=4,d=2,3)
  File "<stdin>", line 1
SyntaxError: positional argument follows keyword argument

def lotsOfParameters2(a=1,b=2,c=3,d=4,e=5):
    print a
    print b
    print c
    print d
    print e

>>> lotsOfParameters2(1, e=20, b=3, a=10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: lotsOfParameters2() got multiple values for argument 'a'

=================================================================================================================================

random.randint(start, end) returns a distribution that is inclusive of both the given start and end points.

=================================================================================================================================


