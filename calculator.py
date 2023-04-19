def addition(x, y):
    addition = x + y
    return addition


def subtratraction(x, y):
    subtraction = x - y
    return subtraction


def division(x, y):
    division = x / y
    return division


def multiplication(x, y):
    multiplication = x * y
    return multiplication


def signs():
    op_sign = int(
        input(
            "What operation sign do you want to use?\n 1.Addition 2.Subtraction 3.Division 4.Multiplication\n "
        )
    )

    if op_sign == 1:
        print("Addition")

    elif op_sign == 2:
        print("Subtraction")

    elif op_sign == 3:
        print("Division")

    elif op_sign == 4:
        print("Multiplication")

    else:
        exit("wrong number entered")
    return op_sign


op_sign = signs()


def variables():
    x = int(input("Enter your first number:"))
    y = int(input("Enter your second number:"))
    return x, y


x, y = variables()

if op_sign == 1:
    print("The  results of ", x, "+", y, "=", addition(x, y))


elif op_sign == 2:
    print("The  results of ", x, "-", y, "=", subtratraction(x, y))

elif op_sign == 3:
    print("The  results of ", x, "/", y, "=", division(x, y))

elif op_sign == 4:
    print("The results of ", x, "x", y, "=", multiplication(x, y))
