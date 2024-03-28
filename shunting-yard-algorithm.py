def precedence(char):
    match char:
        case '(':
            return 4
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


def infix_split(infix):
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
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


# 1.  While there are tokens to be read:
# 2.        Read a token
# 3.        If it's a number add it to queue
# 4.        If it's an operator
# 5.               While there's an operator on the top of the stack with greater precedence:
# 6.                       Pop operators from the stack onto the output queue
# 7.               Push the current operator onto the stack
# 8.        If it's a left bracket push it onto the stack
# 9.        If it's a right bracket
# 10.            While there's not a left bracket at the top of the stack:
# 11.                     Pop operators from the stack onto the output queue.
# 12.             Pop the left bracket from the stack and discard it
# 13. While there are operators on the stack, pop them to the queue

def infix_to_postfix(infix):
    operator_stack = []
    output_stack = []
    infix = infix_split(infix)
    for i in range(len(infix)):
        if precedence(infix[i]) == 0:
            output_stack.append(infix[i])
        else:
            while len(operator_stack) != 0 and precedence(operator_stack[len(operator_stack) - 1]) > precedence(infix[i]):
                output_stack.append(operator_stack.pop())
            operator_stack.append(infix[i])
        if infix[i] == '(':
            operator_stack.append(infix[i])
        if infix[i] == ')':
            while len(operator_stack) != 0 and operator_stack[len(operator_stack) - 1] != '(':
                output_stack.append(operator_stack.pop())
            #operator_stack.pop()
    while len(operator_stack) != 0:
        output_stack.append(operator_stack.pop())

    return output_stack




print(infix_to_postfix('4+18/(9-3)'))