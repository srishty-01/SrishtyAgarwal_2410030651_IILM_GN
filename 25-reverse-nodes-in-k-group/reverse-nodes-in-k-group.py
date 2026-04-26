class Solution:
    def reverseKGroup(self, head, k):
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1
        
        if count == k:
            prev = None
            curr = head
            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            

            if curr:
                head.next = self.reverseKGroup(curr, k)
            
            return prev
        
        return head