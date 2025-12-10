class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self, iterable=None):
        self.head = None
        if iterable:
            for item in iterable:
                self.append(item)

    def append(self, value):
        node = ListNode(value)
        if self.head is None:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

    def reverse(self):
        """Реверсування списку з перестановкою посилань між вузлами."""
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    def sort(self):
        """Сортування однозв'язного списку методом злиття."""
        self.head = merge_sort_list(self.head)


def merge_sorted_lists(a: ListNode, b: ListNode) -> ListNode:
    dummy = ListNode(0)
    tail = dummy

    while a and b:
        if a.value <= b.value:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next

    tail.next = a or b
    return dummy.next


def merge_sort_list(head: ListNode) -> ListNode:
    if head is None or head.next is None:
        return head

    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = merge_sort_list(head)
    right = merge_sort_list(mid)
    return merge_sorted_lists(left, right)


def merge_two_sorted_lists(list1: SinglyLinkedList,
                           list2: SinglyLinkedList) -> SinglyLinkedList:
    merged_head = merge_sorted_lists(list1.head, list2.head)
    result = SinglyLinkedList()
    result.head = merged_head
    return result


if __name__ == "__main__":
    lst = SinglyLinkedList([3, 1, 4, 1, 5, 9])
    print("Початковий список:", lst.to_list())

    lst.reverse()
    print("Після реверсу:", lst.to_list())

    lst.sort()
    print("Після сортування:", lst.to_list())

    a = SinglyLinkedList([1, 3, 5])
    b = SinglyLinkedList([2, 4, 6, 7])
    c = merge_two_sorted_lists(a, b)
    print("Об'єднаний відсортований список:", c.to_list())