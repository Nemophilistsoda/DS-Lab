class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

# 创建链表
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)

another = ListNode(2077)
another.next = ListNode(2088)
another.next.next = ListNode(2099)

# 遍历链表
# while head:
#     print(head.val)
#     head = head.next
def traverse(head):
    while head:
        print(head.val)
        head = head.next

# traverse(head)
# traverse(another)

# 同行箭头指向打印链表
def traverse2(head):
    while head:
        print(head.val, end = '->')
        head = head.next
    # print(None)

traverse2(another)