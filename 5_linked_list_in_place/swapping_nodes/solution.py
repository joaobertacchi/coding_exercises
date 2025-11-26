class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap_nodes(head, k):
    if not head or not head.next:
        return head
    
    curr = head
    count = 1
    
    k_node = None
    k_from_end_node = None
    while curr.next:
        curr = curr.next
        count += 1
        
    size = count
    k_from_end = size - k + 1
    print(k, k_from_end, size)
    
    curr = head
    count = 1
    while count <= max(k, k_from_end):
        if count == k:
            k_node = curr
        if count == k_from_end:
            k_from_end_node = curr
        curr = curr.next
        count += 1

    k_node.val, k_from_end_node.val = k_from_end_node.val, k_node.val
    
    return head
