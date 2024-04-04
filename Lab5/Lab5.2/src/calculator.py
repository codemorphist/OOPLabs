from rational import Rational


operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b
}


def precedence(operation) -> int:
    """
    Return precedence of operation in infix notation
    """
    precedence_map = {'+': 1, '-': 1, '*': 2, '/': 2}
    return precedence_map.get(operation, 0)


def infix_to_postfix(expr: str, delim: str="  ") -> list[any]:
    """
    Function convert infix notation to postfix
    by Dijkstra's algorithm and RPN notation
    """
    tokens = expr.split(delim)
    stack = []
    postfix = []
    

    for token in tokens:
        if token in operations:
            if token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop() 
            else:
                while (stack and precedence(stack[-1]) <= precedence(token)):
                    postfix.append(stack.pop())
                stack.append(token)
        else:
            stack.append(Rational(token))

    while stack:
        postfix.append(stack.pop())

    return postfix


def calculate(expr: str) -> Rational:
    """
    Calculate value of expression
    """
    pass
    

def calculate_hack(expr: str) -> Rational:
    new_expr = ""
    tokens = expr.split()
    for token in tokens:
        if token in operations:
            new_expr += token
        else:
            new_expr += repr(Rational(token))
    return eval(new_expr)


if __name__ == "__main__":
    expr = input()
    print(calculate_hack(expr)())
    print(eval(expr))

