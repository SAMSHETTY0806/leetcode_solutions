class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev1 = None; curr = head
        if not head:
            return 
        while curr.next != None:
            temp = curr
            curr = curr.next
            temp.next = prev1
            prev1 = temp
        curr.next = prev1
        return curr
