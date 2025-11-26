class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def count_cycle_length(head):
   slow = fast = head
   
   slow = slow.next
   fast = slow.next.next
   if slow == None or fast == None:
      return 0
   while slow != fast:
      slow = slow.next
      fast = fast.next
      if slow == None or fast == None or fast.next == None:
         return 0
      fast = fast.next
      
   found = slow
   count = 1
   slow = slow.next
   while slow != found:
      count += 1
      slow = slow.next

   return count