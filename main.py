#1st TASK
from collections import deque
input1 = input("Enter any string: ")
stack1 = deque()
reverse_input1 = ""
i = 0
while i < len(input1):
    stack1.append(input1[i])
    i = i + 1
while len(stack1) != 0:
    reverse_input1 = reverse_input1 + stack1.pop().upper()
if input1.upper() == reverse_input1:
    print(input1, "is Palindrome.")
else:
    print(input1, "is not Palindrome.")
#2nd TASK
from collections import deque
eq = input("Please Enter equation: ")
stack = deque()
result = "Equation is balanced"
counter = 0
for i in eq:
    if (i == '(' or i == '[' or i == '{'):
        stack.append(i)
        counter = counter + 1
    elif (i == ')' or i == ']' or i == '}'):
        if (len(stack) != 0):
            if (i == ')'):
                if(stack[-1] == '('):
                    counter = counter - 1
            if (i == ']'):
                if (stack[-1] == '['):
                    counter = counter - 1
            if (i == '}'):
                if (stack[-1] == '{'):
                    counter = counter - 1
            stack.pop()
        else:
            result = "Equation is unbalanced!"
            break
if (counter != 0):
    result = "Equation is unbalanced"
print (result)


