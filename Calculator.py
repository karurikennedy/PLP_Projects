first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
operator = input("Enter operator: ")

if operator == "+":
    print(first_number + second_number)
elif operator == "-":
    print(first_number - second_number)
elif operator == "*":
    print(first_number * second_number)
elif operator == "/":
    print(first_number / second_number)
else:
    print("Invalid operator")