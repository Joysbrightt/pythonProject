def bracket_pair_checkers(brackets: str) -> bool:
    stack: list[str] = []

    for bracket in brackets:
        if bracket in '{[(':
            stack.append(bracket)

        if bracket in ')]}':

            if bracket == '}' and stack[-1] == '{':
                stack.pop()

            if bracket == ']' and stack[-1] == '[':
                stack.pop()

            if bracket == ')' and stack[-1] == '(':
                stack.pop()

    return len(stack) == 0


print(bracket_pair_checkers('{[()]}'))
print(bracket_pair_checkers('{[(]})'))
