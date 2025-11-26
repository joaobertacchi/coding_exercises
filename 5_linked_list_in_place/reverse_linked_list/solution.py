class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_between(head, left, right):
  if left == right:
    return head

  curr = head
  prev = None
  pos = 1
  left_ptr = None
  right_ptr = None
  while pos < right:
    if pos == left:
      left_ptr = curr
    if pos < left:
      prev = curr
    curr = curr.next
    pos += 1
  right_ptr = curr
  
  tail = right_ptr.next
  last = prev
  
  # Invert
  curr = left_ptr
  next = left_ptr.next
  while curr != right_ptr:
    curr.next = prev
    prev = curr
    curr = next
    next = curr.next
  curr.next = prev
  
  left_ptr.next = tail
  if left == 1:
    return right_ptr
  
  last.next = right_ptr
  return head
