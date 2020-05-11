class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        stack = []
        node = head
        while node.next:
            stack.append(node.val)
            node = node.next
        stack.append(node.val)
        node = head
        while node.next:
            node.val = stack.pop()
            node = node.next
        node.val = stack.pop()
        return head
