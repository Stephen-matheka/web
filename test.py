def total(a, b):
    return a + b

def sub(a, b):
    return a - b

def mult(a, b):
    return a * b

def division(a, b):
    return a / b

print('''
1. Add
2. Subtract
3. Multiply
4. Divide
''')

choice = int(input("CHOOSE OPTIONS: "))

if choice == 1:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(total(num1, num2))

elif choice == 2:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(sub(num1, num2))

elif choice == 3:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    print(mult(num1, num2))

elif choice == 4:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if num2 == 0:
        print("Error! Division by zero.")
    else:
        print(division(num1, num2))

else:
    print("Invalid choice! Please select a valid option.")
