# Reverse Stack using Recursion


def createStack():
    stack = []
    return stack

def push(stack, item):
    stack.append(item)
    
def pop(stack):
    if len(stack) == 0:
        return False
    else:
        return stack.pop()
    
def reverseStack(stack):
    if len(stack) >= 1:
        temp = pop(stack)
        reverseStack(stack)
        pushlast(stack, temp)
        
def pushlast(stack, item):
    if len(stack) == 0:
        push(stack, item)
    else:
        temp = pop(stack)
        pushlast(stack, item)
        push(stack, temp)
    
    
stack = createStack()
push(stack, 1)
push(stack, 2)
push(stack, 3)
push(stack, 4)




