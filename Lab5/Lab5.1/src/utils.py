def prior(op):
    precedence_map = {'+': 1, '-': 1, '*': 2, '/': 2}
    return precedence_map.get(op, 0)


def infix_to_postfix(expression: str) -> list[int | str]:
    expr = expression.split()[::-1]
    print(expr)

    res = []
    stack = []
    ops = set(["(", ")", "+", "-", "*", "/"])

    while expr:
        token = expr.pop()
        print(token, res, stack)
        # input()

        if token in ops:
            if token == ")":
                while stack and stack[-1] != "(":
                    res.append(stack.pop())
                stack.pop()
            elif token in "+-":
                while stack and prior(stack[-1]) >= prior(token):
                    res.append(stack.pop())
                stack.append(token)
            else:
                stack.append(token)
        else:
            res.append(token)

    while stack:
        res.append(stack.pop())
    return res        


if __name__ == "__main__":
    print(infix_to_postfix("( 2 * 3 + 7 ) * ( 4 - 1 ) / 5"))
