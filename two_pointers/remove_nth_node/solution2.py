class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_nth_last_node(head, n):
    prev = head
    last = head
    
    count = 0
    while count < n:
        if last == None:
            return head
        last = last.next
        count += 1
        
    if last == None:
        return head.next
    
    while last.next != None:
        prev = prev.next
        last = last.next

    prev.next = prev.next.next
    return head
