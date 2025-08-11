# Two variables to collect and store user input
num1=int(input("Enter any one number:"))
num2=int(input("Enter any second number:"))
operation=input("Enter operation (+, -, *, /): ")

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by zero."
else:
    result = "Error! Invalid operation." 

#print the result
print(f"{num1}{operation}{num2}={result}")
