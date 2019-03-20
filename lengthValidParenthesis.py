# Length of valid parenthesis


def validParenthesis(s):
    n = len(s)
    stack = []
    length = 0
    stack.append(-1)
    for i in range(n):
        if s[i] == '(':
            stack.append(1)
        if s[i] == ')':
            popVal = stack.pop()
            if popVal == 1:
                length += 2
            elif popVal == -1:
                stack.append(-1)
    return length

s = "()(()))))"
print(validParenthesis(s))
