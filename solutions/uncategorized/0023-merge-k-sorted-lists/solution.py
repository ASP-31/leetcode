# 23. Merge k Sorted Lists
# Problem: https://leetcode.com/problems/merge-k-sorted-lists/
# Difficulty: Easy
# Language: python3

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        import heapq

        heap = []

        # Put first node of each list
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))

        dummy = ListNode(0)
        curr = dummy

        while heap:

            # Get smallest node
            val, i, node = heapq.heappop(heap)

            # Add it to answer
            curr.next = node
            curr = curr.next

            # Put next node from same list
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next
