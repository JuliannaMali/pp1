import stack
exp = str(input("Enter expression: "))
exp = list(exp)
operators = ['+', '–', '/', '*']
for x in exp:
    if x == ' ':
        pass
    if x not in operators and x !=" " and x != "=":
        stack.push(float(x))
    if x in operators:
        y = stack.pop()
        z = stack.pop()
        if x == "+":
            v = y+z
            stack.push(v)
        if x == "–":
            v = y-z
            stack.push(v)
        if x == "/":
            v = y/z
            stack.push(v)
        if x == "*":
            v = y*z
            stack.push(v)
    if x == "=":
        y = stack.pop()
        print(y)