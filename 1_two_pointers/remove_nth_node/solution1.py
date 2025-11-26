class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def list_size(head):
    node = head
    count = 0
    while node != None:
        count += 1
        node = node.next
    return count
    
def get_nth_node(head, n):
    node = head
    count = 1
    while count != n:
        count += 1
        node = node.next
    return node

def remove_nth_last_node(head, n):
    if n < 1:
        return head
    size = list_size(head)
    if n > size:
        return head
    if n == size:
        return head.next
    prev_index = size - n
    prev = get_nth_node(head, prev_index)
    prev.next = prev.next.next
    
    return head
