# How do you find the middle element of a linked list?
# To determine a linked list’s midpoint, employ a method with two pointers. One progresses by one step, while the other advances by two steps.
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def find_middle_element(head):
    slow = head
    fast = head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow  # Returns the middle element

# Example Usage
if __name__ == "__main__":
    # Creating a linked list: 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    middle_node = find_middle_element(head)
    
    # Print the middle element's value
    if middle_node:
        print("The middle element is:", middle_node.value)  # Output: The middle element is: 3
    else:
        print("The list is empty.")
