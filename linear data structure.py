#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def delete_zero_sum_nodes(head):
    current = head
    while current:
        sum_values = current.data
        temp = current.next
    while temp:
        sum_values += temp.data
        if sum_values ==0:
            current.next =temp.next
            break
        temp = temp.next
        current = current.next
def print_list(head):
    current = head
    while current:
        print(current.data, end="")
        current = current.next
    print()
if __name__ == "__main__":
    head= Node(1)
    head.next =Node(-2)
    head.next.next =Node(3)
    head.next.next.next =Node(4)
    head.next.next.next.next =Node(-4)
    head.next.next.next.next.next =Node(2)  
    head.next.next.next.next.next.next =Node(-1)
print("Original Linked List:")
print_list(head)

delete_zero_sum_nodes(head)
print("\nLinked List after deleting zero-sum nodes:")
print_list(head)

