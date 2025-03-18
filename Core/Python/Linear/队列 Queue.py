from collections import deque
queue = deque()

# basic operation
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
queue.pop()

# print(queue)

# 优先队列
import heapq
pq = []
heapq.heappush(pq, 1)
heapq.heappush(pq, 2)
heapq.heappush(pq, 2077)
heapq.heappush(pq, 3)

# 堆的内部结构是二叉树数组表示，列表顺序不等于弹出顺序
print(pq)  # 输出：[1, 2, 2077, 3]

# 正确使用方式：按升序弹出元素
while pq:
    print(heapq.heappop(pq), end=' ')  # 输出：1 2 3 2077
# 所以这也是一种堆排序算法
# 真正有序的输出需要通过 heappop() 方法依次取出元素
# 插入和弹出操作的时间复杂度均为O(log n)