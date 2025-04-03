def total(a, b):
  return a+b

def sub(a,b):
  return a-b

def mult(a,b):
  return a*b

def division(a,b):
  return a/b

print('''
1. Add
2. Subtract
3. Multiply
4. Divide
''')

choice = int(input("CHOOSE OPTIONS: "))

switch(choice):
  case 1:
     num1 = int(input("Enter the first number: "))
     num2 = int(input("Enter the second number: "))
     print(total(num1, num2))
  case 2:
     num1 = int(input("Enter the first number: "))
     num2 = int(input("Enter the second number: "))
     print(sub(num1, num2))
  case 3:
       num1 = int(input("Enter the first number: "))
       num2 = int(input("Enter the second number: "))
       print(mult(num1, num2))
  case 4:
       num1 = int(input("Enter the first number: "))
       num2 = int(input("Enter the second number: "))
       print(division(num1, num2))
