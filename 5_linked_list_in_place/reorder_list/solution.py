class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_list(head):
    while head != None:
        print(head)
        head = head.next
            
def reorder_list(head):
    if head.next == None:
        return head

    # Split list
    slow = fast = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    aux = slow.next
    slow.next = None
    print("Head:")
    print_list(head)
    print("Aux:")
    print_list(aux)
    
    # Reverse aux
    prev = None
    curr = aux
    next = aux.next
    
    while next != None:
        curr.next = prev
        prev = curr
        curr = next
        next = next.next
    curr.next = prev
    aux = curr
    print("Aux:")
    print_list(aux)
    
    # Merge lists
    left = head
    left_next = left.next
    right = aux
    right_next = right.next
    
    while left != None or right != None:
        if left != None:
            left.next = right
        if right != None:
            right.next = left_next
        left = left_next
        if left != None:
            left_next = left.next
        right = right_next
        if right != None:
            right_next = right.next
            
    return head
