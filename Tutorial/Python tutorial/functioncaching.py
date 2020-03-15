import time
from functools import lru_cache


"""lru cache will store the 3 latest value of some_
work finction here max size =3 so it will store latest
3 value in cache memory"""
@lru_cache(maxsize=3)
def some_work(n):
    time.sleep(n)
    return n

if __name__ =="__main__":
    print("Now running")
    some_work(3)
    print("done")
    some_work(3)
    print("calling again")
'''Function caching is used to call the method from
memory so it will increase speed of execution of program
It will work like webpage caching'''
