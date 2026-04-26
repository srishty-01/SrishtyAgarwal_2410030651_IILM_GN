import heapq

class Solution:
    def mergeKLists(self, lists):
        min_heap = []
        dummy = ListNode(0)
        current = dummy
        
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i, lists[i]))
        
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            
            current.next = node
            current = current.next
            
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
                
        return dummy.next