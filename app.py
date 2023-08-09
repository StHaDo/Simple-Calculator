# Math operation with two numbers
def calc(num1: float, num2: float, operator: str):
    match operator:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            return num1 / num2


# Get first number
while True:
    try:
        num1 = float(input("Erste Zahl: "))
        break
    except ValueError:
        print("Das war keine Zahl! Bitte nochmal versuchen")
# Get the operator
while True:
    operator = input("Operator: ")
    if operator == "+" or operator == "-" or operator == "*" or operator == "/":
        break
    print("Kein gültiger Operator! Nur + , - , * , / verwenden")
# Get the second number
while True:
    try:
        num2 = float(input("Zweite Zahl: "))
        break
    except ValueError:
        print("Das war keine Zahl! Bitte nochmal versuchen")

# Calculate the result
result = calc(num1, num2, operator)
# Print the result
print(str(result))
