# How do you remove a loop in a linked list?
# Detecting and removing a loop in a linked list is a complex algorithmic task and typically involves Floyd’s Tortoise and Hare algorithm.

class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def detect_and_remove_loop(head):
    slow = head
    fast = head

    # Step 1: Detecting the loop
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        # Loop detected
        if slow == fast:
            break

    # No loop found
    if not fast or not fast.next:
        return None

    # Step 2: Finding the start of the loop
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    # Now, slow (or fast) is at the start of the loop
    loop_start = slow

    # Step 3: Remove the loop
    current = loop_start
    while current.next != loop_start:
        current = current.next
    current.next = None  # Remove the loop

    return head

# Example Usage
if __name__ == "__main__":
    # Creating a linked list with a loop: 1 -> 2 -> 3 -> 4 -> 5 -> 3
    head = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    fourth = ListNode(4)
    fifth = ListNode(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    fifth.next = third  # Creating a loop

    # Detect and remove the loop
    detect_and_remove_loop(head)

    # Printing the list to confirm the loop has been removed
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
