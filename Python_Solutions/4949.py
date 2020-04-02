while True:
    bracket = input()
    if bracket == ".":
        break
    bracket_stack = []
    answer = True

    for j in bracket:
        if j == "(" or j == "[":
            bracket_stack.append(j)

        elif j == ")":
            if len(bracket_stack) == 0:
                answer = False
                break
            if bracket_stack[-1] == "(":
                bracket_stack.pop()
            else:
                answer = False
                break

        elif j == "]":
            if len(bracket_stack) == 0:
                answer = False
                break
            if bracket_stack[-1] == "[":
                bracket_stack.pop()
            else:
                answer = False
                break

    if answer and not bracket_stack:
        print("yes")
    else:
        print("no")