from functools import wraps

def smart_div(f):
    """This div function checks whether we are dividing
        by zero if yes then print the message on screen"""
    @wraps(f)
    def wrapper(a,b):
        if b==0:
            print("You can not divide by Zero")
        else:
            f(a,b)
    return wrapper

@smart_div
def div(a,b):
    """This function is used to divide"""
    return print(a/b)
div(10,2)
div(10,0)
div(10,5)

