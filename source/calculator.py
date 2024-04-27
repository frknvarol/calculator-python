from _pydecimal import Decimal


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
        case '(':
            return -1
        case ')':
            return -1
        case _:
            return 0


def infix_split(infix):
    infix = infix.replace(' ', '')
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    result = []
    start_index = 0

    for i in range(len(infix)):
        if infix[i] not in numbers:
            result.append(infix[start_index: i])
            if isinstance(infix[i], str):
                result.append(infix[i])
            i += 1
            start_index = i

    if len(infix[start_index:]) != 0:
        result.append((infix[start_index:]))
    while '' in result:
        result.remove('')
    return result


def infix_to_postfix(infix):

    operator_stack = []
    output_stack = []
    infix = infix_split(infix)

    for x in infix:
        # if it's a number put it in output_stack
        if precedence(x) == 0:
            output_stack.append(x)
        # if it's an operator check the operator_stack, put the operators with higher precedence into the output_stack
        # when there is no operators with higher precedence on top of the stack put the current operator on top of
        # the operator_stack
        elif precedence(x) > 0:
            while len(operator_stack) > 0 and precedence(operator_stack[-1]) >= precedence(x):
                output_stack.append((operator_stack.pop()))
            operator_stack.append(x)
        # if it's a left bracket put it on top of operator_stack
        elif x == '(':
            operator_stack.append(x)
        # until you reach the left bracket pop the operators from the operator_stack and put them on top of output_stack
        elif x == ')':
            while operator_stack[-1] != '(':
                output_stack.append(operator_stack.pop())
            # pop the left bracket
            operator_stack.pop()
    # pop the remaining operators from the operator_stack and put them on top of the output_stack
    while len(operator_stack) > 0:
        output_stack.append(operator_stack.pop())

    return output_stack


def calculate(infix):
    postfix = infix_to_postfix(infix)
    operand_stack = []

    for x in postfix:
        if precedence(x) == 0:
            operand_stack.append(Decimal(x))
        else:
            last = operand_stack.pop()
            penultimate = operand_stack.pop()

            if x == '^':
                operand_stack.append(penultimate ** last)
            elif x == '*':
                operand_stack.append(penultimate * last)
            elif x == '/':
                operand_stack.append(penultimate / last)
            elif x == '+':
                operand_stack.append(penultimate + last)
            elif x == '-':
                operand_stack.append(penultimate - last)

    return operand_stack[0]
