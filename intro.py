# Say "Hello, World!" With Python
print("Hello, World!")

# Python If-Else
'''
Given an integer, n, perform the following conditional actions:
If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird
'''
if __name__ == '__main__':
    n = int(input().strip())

    if n % 2 != 0:
        print('Weird')
    elif n % 2 == 0 and n in range(2, 6):
        print('Not Weird')
    elif n % 2 == 0 and n in range(6, 21):
        print('Weird')
    elif n % 2 == 0 and n > 20:
        print('Not Weird')

# Arithmetic Operators
'''
Task 
The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:
The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.
'''

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a+b)
    print(a-b)
    print(a*b)

# Python: Division
'''
Task 
The provided code stub reads two integers, a and b, from STDIN.
Add logic to print two lines. The first line should contain the result of integer division,  a// b. 
The second line should contain the result of float division,  a/b .
No rounding or formatting is necessary.
'''

a = int(input())
b = int(input())

print(int(a/b))
print(a/b)

# Loops
'''
Task 
The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n, print i^2.
'''
count = 0
for i in range(1,n+1):
    print(count**2)
    count += 1

# Print Function
'''
The included code stub will read an integer, n, from STDIN.
Without using any string methods, try to print the following:
123...n
Note that "" represents the consecutive values in between.
'''

if __name__ == '__main__':
    n = int(input())
    
    "".join([str(i) for i in range(1,n+1)])
# OR 
    for i in range(1, n+1):
     print(i, end='')