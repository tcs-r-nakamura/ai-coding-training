def calc(a, b, op):
    """2つの数値と演算子を受け取り、計算結果を返す関数"""

    if op == "+":
        return a + b

    if op == "-":
        return a - b

    if op == "*":
        return a * b

    if op == "/":
        return a / c

    return "対応していない演算子です"


print(calc(6, 2, "/"))