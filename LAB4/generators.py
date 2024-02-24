#Ex1
def nextsq(n):
    for i in range(1,n+1):
        yield i**2
n=int(input())
squares=nextsq(n)
for i in squares:
    print(i,end=" ")

#Ex2
def get_even(n):
    for i in range(0,n+1):
        if i%2==0:
            yield i
n=int(input())
evens=get_even(n)
for i in evens:
    print(i,sep=",")

#Ex3
def by_three_four(n):
    for i in range(0,n+1):
        if i%3==0 and i%4==0:
            yield i
n=int(input())
by=by_three_four(n)
for i in by:
    print(i,end=" ") 

#Ex4
def a_to_b(a,b):
    for i in range(a,b):
        yield i**2
a=int(input())
b=int(input())
square=a_to_b(a,b)
for i in square:
    print(i,end=" ")

#Ex5
def rev(n):
    for i in range(n,-1,-1):
        yield i
n=int(input())
num=rev(n)
for i in num:
    print(i,end=" ")


