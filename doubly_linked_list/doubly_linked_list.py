"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def next_node(self):
        if not self.next:
            return
        else:
            return self.next

    def prev_node(self):
        if not self.prev:
            return
        else:
            return self.prev

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
        self.value = None
        self.next = None
        self.prev = None
            
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
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            # set the current head's prev node to the new node
            self.head.prev = new_node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if not self.head:
            return "No head in List"
        else:
            self.length -= 1
            # get the current head
            removed_head = self.head
            # set the current head's next as the new head
            removed_head.next = self.head
            # set the new head's prev as None
            self.head.prev = None
            return removed_head
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if not self.tail:
            return "No tail in List"
        else:
            self.length -= 1
            removed_tail = self.tail
            removed_tail.prev = self.tail
            self.tail.next = None
            return removed_tail
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        new_head_node = node
        self.add_to_head(new_head_node)
        node.delete()
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        new_tail_node = node
        self.add_to_tail(new_tail_node)
        node.delete()

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        node.delete()
        self.length -= 1

    def get_node_value(self, node):
        return node.get_value()

    def get_all_nodes(self):
        if not self.head and not self.tail:
            print("No nodes in List")  
        else:
            current_node = self.head
            while current_node is not self.tail:
                print(f"{current_node.get_value().value}")
                current_node = current_node.next_node()
            print(self.tail.get_value().value)

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass

d = DoublyLinkedList()
head = ListNode("head")
new_tail = ListNode("new tail")
new_new_tail = ListNode("new new tail")
tail = ListNode("tagil")
new_head = ListNode("new head")

d.add_to_head(head)
d.add_to_tail(tail)
d.add_to_tail(new_tail)
d.add_to_head(new_head)

d.get_all_nodes()
