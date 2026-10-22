operations = ["*", "%", "+", "-"]


def calculate(tokens):
    if not tokens:
        return ""

    result = int(tokens[0])
    for index in range(1, len(tokens), 2):
        operator = tokens[index]
        number = int(tokens[index + 1])

        if operator == "+":
            result += number
        elif operator == "-":
            result -= number
        elif operator == "*":
            result *= number
        elif operator == "%":
            if number == 0:
                return "ERROR"
            result %= number

    return str(result)