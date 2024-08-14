op = input("Enter The Operation + - / * ")
num1 = float(input("First Number "))
num2 = float(input("second number "))

if op == "+":
    result = num1 + num2
    print(round(result , 3))
elif op == "-":
    result = num1 - num2
    print(round(result , 3))
elif op == "/":
    result = num1 / num2
    print(round(result , 3))
elif op =="*":
    result = num1/num2
    print(round(result , 3))    
else:
    print( f"{op} is not valid operator")
input()
