messages = [
    "Enter an equation", "Do you even know what numbers are? Stay focused!",
    "Yes ... an interesting math operation. You've slept through all classes, haven't you?",
    "Yeah... division by zero. Smart move...",
    "Do you want to store the result? (y / n):",
    "Do you want to continue calculations? (y / n):",
    " ... lazy",
    " ... very lazy",
    " ... very, very lazy",
    "You are",
    "Are you sure? It is only one digit! (y / n)",
    "Don't be silly! It's just one number! Add to the memory? (y / n)",
    "Last chance! Do you really want to embarrass yourself? (y / n)"
]

valid_operators = ["+", "-", "*", "/"]

memory = 0
result = 0

def is_number(string):
    return type(string) == float or type(string) == int


def validate_number(number):
    if number.count(".") == 1:
        return float(number)

    elif number.isnumeric():
        return int(number)

    elif number.lower() == "m":
        return "M"

    else:
        return False


def is_one_digit(v):
    return v > -10 and v < 10 and float(v).is_integer()


def check(x, y, oper):
    msg = ""

    if is_one_digit(x) and is_one_digit(y):
        msg = msg + messages[6]

    if (x == 1 or y == 1) and oper == "*":
        msg = msg + messages[7]

    if (x == 0 or y == 0) and (oper == "*" or oper == "+" or oper == "-"):
        msg = msg + messages[8]

    if msg != "":
        msg = messages[9] + msg
        print(msg)


while True:
    print(messages[0])

    x, oper, y = input().split()

    x = validate_number(x)
    y = validate_number(y)

    x = memory if x == "M" else x
    y = memory if y == "M" else y

    if not is_number(x) or not is_number(y):
        print(messages[1])
        continue

    if oper not in valid_operators:
        print(messages[2])
        continue

    check(x, y, oper)

    if oper == valid_operators[0]:
        result = float(x + y)
        print(result)

    elif oper == valid_operators[1]:
        result = float(x - y)
        print(result)

    elif oper == valid_operators[2]:
        result = float(x * y)
        print(result)

    elif oper == valid_operators[3] and y != 0:
        result = float(x / y)
        print(result)

    else:
        print(messages[3])
        continue


    print(messages[4])

    memory_answer = input().strip().lower()

    if memory_answer == "y":
        if is_one_digit(result):
            msg_index = 10

            while True:
                print(messages[msg_index])
                one_digit_question = input().strip().lower()

                if one_digit_question == "y":
                    if msg_index < 12:
                        msg_index = msg_index + 1

                    else:
                        memory = result
                        break
                else:
                    break

        else:
            memory = result

    print(messages[5])

    continue_answer = input().strip()

    if continue_answer.lower() == "y":
        continue

    break
