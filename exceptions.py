# exception handling is very essential.
# syntax and runtime errors can be mitigated through these.

def simpleAddition():
    try:
        result = 10 + '20'
        print(result)
    except TypeError:
        print('Try again')

simpleAddition()

