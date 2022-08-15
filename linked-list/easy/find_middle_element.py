
"""
@TODO:
Given a singly linked list of N nodes, the task is to find the middle of the linked list.
For example, if the linked list is 1->2->3->4->5, then the middle node of the list is 3.
If there are two middle nodes(in case, when N is even), print the second middle element.
For example, if the linked list given is 1->2->3->4->5->6, then the middle node of the list is 4.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.no_of_nodes = 0

    def insert_element(self, node):
        current_node = Node(node)
        self.no_of_nodes += 1
        if self.head is None:
            current_node = Node(node)
            self.head = current_node
            current_node.next_node = None
        else:
            actual_node = self.head
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node

            actual_node.next_node = current_node
            current_node.next_node = None

    def print_elements(self):
        if self.head is None:
            print("No of elements in Linked List : ", self.no_of_nodes)
            return

        actual_node = self.head
        while actual_node is not None:
            print("Node Value", actual_node.data, sep=" -> ")
            actual_node = actual_node.next_node

    def get_size_of_ll(self):
        print("Size of Linked List ->", self.no_of_nodes)
        return self.no_of_nodes


if __name__ == "__main__":
    ll = LinkedList()
    ll.get_size_of_ll()
    ll.print_elements()
    ll.insert_element(1)
    ll.get_size_of_ll()
    ll.print_elements()
    ll.insert_element(2)
    ll.get_size_of_ll()
    ll.print_elements()
    ll.insert_element(3)
    ll.get_size_of_ll()
    ll.print_elements()
    ll.insert_element(4)
    ll.get_size_of_ll()
    ll.print_elements()
    ll.insert_element(5)
    ll.get_size_of_ll()
    ll.print_elements()

