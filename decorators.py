#DECORATORS

# @mydecorator
# def dosomething():
#     pass
import functools


def print_name():
    print('Alex')

def start_end_decorator(func):

    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print("Start")
        result=func(*args,**kwargs)
        print("End")
        return result
    return wrapper

@start_end_decorator
def add5(x):
    return x+5

@start_end_decorator
def subtract(x):
    return x-5

result = add5(10)
print(result)
print(help(add5))
print(add5.__name__)

result1= subtract(10)
print(result1)
print(help(subtract))
print(subtract.__name__)



def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                result = func(*args,**kwargs)
            return result
        return wrapper
    return decorator_repeat



@repeat(num_times=4)
def greet(name):
    print(f"Hello {name}")

greet("Alex")


#Nested decorators 

def nested_decorators():
    def nest_decorators(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
          a = func.__name__
        return wrapper
    return nest_decorators




#Class Decorators 

class CountCalls:

    def __init__(self,func):
        self.func = func
        self.num_calls = 0
    
    def __call__(self,*args,**kwargs):
        self.num_calls += 1
        print(f"This is excuted {self.num_calls} times")
        return self.func(*args,**kwargs)


@CountCalls
def say_hi():
    print("HI")

say_hi()