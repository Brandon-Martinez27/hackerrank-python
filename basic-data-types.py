# List Comprehensions
'''
Let's learn about list comprehensions! 
You are given three integers x, y, z and representing the dimensions of a cuboid along with an integer n. 
Print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k
is not equal to n. Here, 0 <= i <= x; 0 <= j<= y; 0 <= k <= z; Please use list comprehensions rather than 
multiple loops, as a learning exercise.
'''

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    print ([[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n ])

# Find the Runner-up Score!
'''
Given the participants' score sheet for your University Sports Day, 
you are required to find the runner-up score. You are given scores. 
Store them in a list and find the score of the runner-up.
'''

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    a = list(set(arr))
    a.sort(reverse=True)
    print(a[1])

# Nested Lists
'''
Given the names and grades for each student in a class of N students, 
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, 
order their names alphabetically and print each name on a new line.
'''

main_list = []
second_lowest_names = []
scores = set()
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        main_list.append([name, score])
        scores.add(score)
        
second_lowest = sorted(scores)[1]

for name, score in main_list:
    if score == second_lowest:
        second_lowest_names.append(name)

for name in sorted(second_lowest_names):
    print(name, end='\n')

# Finding the percentage
'''
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. 
Print the average of the marks array for the student name provided, showing 2 places after the decimal.
'''

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    average = sum(student_marks[query_name])/len(student_marks[query_name])
    print(round(average, 2))

# Lists
'''
Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of 
commands where each command will be of the 7 types listed above. 
Iterate through each command in order and perform the corresponding operation 
on your list.
'''

# Tuples
'''

'''