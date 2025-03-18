# 在Python中，使用list来模拟栈
stack = []
stack.append(1)  # 入栈
stack.append(2)
stack.append(3)
stack.pop()
stack.pop()
print(stack)

# 或者使用collections的deque
from collections import deque
stack1 = deque()
# deque的append和pop方法
stack1.append(1)
stack1.append(2)
stack1.append(3)
stack1.pop()
print(stack1)


