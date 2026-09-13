# Reorder List
# Problem: https://leetcode.com/problems/reorder-list/
# Difficulty: Medium
# Language: python3

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return None

        #find middle
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        #sort the 2nd half
        second = slow.next
        slow.next = None

        prev = None

        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node

        # prev is the head of reversed second half
        second = prev

        # 3. Merge the two halves
        first = head

        while second:
            next_first = first.next
            next_second = second.next

            first.next = second
            second.next = next_first

            first = next_first
            second = next_second