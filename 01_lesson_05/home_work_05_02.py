flag = 'y'
while flag == 'y':
    a = int(input("input the first number: "))
    b = int(input("input the second number: "))
    action = input("input the sign for calculation action: ")

    if action == "+":
        print("a + b =", a + b)
    elif action == "-":
        print("a - b =", a - b)
    elif action == "*":
        print("a * b =", a * b)
    elif action == "/":
        if b == 0:
            print("The denominator can't be 0. Calculation can't be done")
        else:
            print("a / b =", a / b)
    else:
        print("Please choose one of the following simbols for calculation: +, -, *, /")

    flag = input("Input 'y' if you would like to do next calculation, otherwise press 'Enter': ").lower()
