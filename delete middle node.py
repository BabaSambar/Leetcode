
class Solution: 
    def deleteMiddle(self, head):
        if not head.next:
            return None
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = head.next
            fast = head.next.next

        slow.next = slow.next.next
        return head

