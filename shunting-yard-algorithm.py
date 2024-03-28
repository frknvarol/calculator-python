def precedence(char):
    match char:
        case '^':
            return 3
        case '*':
            return 2
        case '/':
            return 2
        case '+':
            return 1
        case '-':
            return 1
        case _:
            return 0


def infix_to_postfix(infix):
    result = []