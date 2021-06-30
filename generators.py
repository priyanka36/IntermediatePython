#Generators are functions that return an object that can be iterated over.And the special thing is that they generate the items inside the object lazily.It means they generate the objects only one at a time and only when we ask for it.And because  of this they are much more memory efficient  when we have to deal with large datasets.They are powerful advanced Python Technique 

# def mygenerator():
#     yield 1
#     yield 2
#     yield 3

# g = mygenerator()

# # for i in g:
# #     print(i)

# # value = next(g)
# # print(value)

# # value = next(g)
# # print(value)

# # value = next(g)
# # print(value)

# # value = next(g)
# # print(value)


# def countdown(num):
#     print("Starting")
#     while num >= 0:
#         yield num
        
#         num-= 1

# cd = countdown(5)
# value = next(cd)
# print(value)
# value = next(cd)
# print(value)
# value = next(cd)
# print(value)
# value = next(cd)
# print(value)
# value = next(cd)
# print(value)
# value = next(cd)
# print(value)

import sys

def first(n):
    nums=[]
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums
def first_using_generator(n):
    num=0
    while num <n:
        yield num
        num += 1

print(sum(first(10)))
print(sum(first_using_generator(10)))
print(sys.getsizeof(first(10)))
print(sys.getsizeof(first_using_generator(10)))

def fibonnaci(num):
    a,b = 0,1
    while a < num:
        yield a 
        a,b = b, a+b 

fib = fibonnaci(130)
for i in fib:
    print(i)

mygenerator = {i for i in range(10) if i%2 == 0}
for i in mygenerator:
    print(i)
mylist1 = [i for i in range(10) if i%2 == 0] 
print(mylist1)  

mylist = list(mygenerator)
print(mylist)
print(sys.getsizeof(mylist))
print(sys.getsizeof(mylist1))
print(sys.getsizeof(mygenerator))