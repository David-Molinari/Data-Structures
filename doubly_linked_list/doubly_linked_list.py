import gc

"""
Each ListNode holds a reference to its prev node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's prev pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        new_node.next = self.head
        new_node.prev = None
        if self.head is not None:
            self.head.prev = new_node
        if self.tail is None:
            self.tail = new_node
        self.head = new_node
        self.length = self.length + 1
  
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if self.length != 0:
            old_head = self.head
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            self.length -= 1
            return old_head.value
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        new_node.prev = self.tail
        new_node.next = None
        if self.tail is not None:
            self.tail.next = new_node
        if self.head is None:
            self.head = new_node
        self.tail = new_node
        self.length = self.length + 1

    """
    Removes the List's current tail node, making the 
    current tail's prev node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length != 0:
            old_tail = self.tail
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.tail = self.tail.prev
            self.length -= 1
            return old_tail.value
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        if self.head != node:
            old_head = self.head
            if self.tail is node:
                self.tail = self.tail.prev
                self.tail.next = None
                self.head = node
            else:
                node.next.prev = node.prev
                node.prev.next = node.next
            self.head = node
            self.head.next = old_head
            self.head.next.prev = self.head
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.tail != node:
            old_tail = self.tail
            if self.head is node:
                self.head = self.head.next
                self.head.prev = None
                self.tail = node
            else:
                node.prev.next = node.next
                node.next.prev = node.prev
            self.tail = node
            self.tail.prev = old_tail
            self.tail.prev.next = self.tail

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        if self.head is None and self.tail is None:
            return
        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = node.next
            node.delete()
        elif node is self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
        self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        if self.head is None and self.tail is None:
            return
        max_value = self.head.value
        current = self.head.next
        while current is not None:
            if current.value > max_value:
                max_value = current.value
            current = current.next
        return max_value 