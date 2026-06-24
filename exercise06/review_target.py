def calc(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        return a / b
    else:
        return None


def process(data):
    result = []

    for d in data:
        if d > 10:
            result.append(d)

    return result


print(calc(10, 0, "/"))