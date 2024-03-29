from shunting_yard import infix_to_postfix
from shunting_yard import precedence


def calculate(infix):
    postfix = infix_to_postfix(infix)
    operand_stack = []

    for x in postfix:
        if precedence(x) == 0:
            operand_stack.append(x)
        else:
            last = operand_stack.pop()
            penultimate = operand_stack.pop()

            if x == '^':
                operand_stack.append(int(penultimate) ** int(last))
            elif x == '*':
                operand_stack.append(int(penultimate) * int(last))
            elif x == '/':
                operand_stack.append(int(penultimate) / int(last))
            elif x == '+':
                operand_stack.append(int(penultimate) + int(last))
            elif x == '-':
                operand_stack.append(int(penultimate) - int(last))

    return operand_stack[0]


