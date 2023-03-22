class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
        
class DLinkedList:
    def __init__(self):
        self.head = None
    
    # insert data into empty list
    def insert_emptylist(self,data):
        new_node = Node(data)
        if(self.head is None):
            self.head = new_node
        else:
            return("List is not empty")
    
    # insert data at the end of list
    def insert_rear(self,data):
        new_node = Node(data)
        if(self.head is None):
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
            new_node.prev = current
    
    # insert value at front of list
    def insert_front(self,data):
        if(self.head is None):
            return("List is empty")
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    # insert data after item
    # data will be inserted after item
    def insert_aftervalue(self,item,data):
        new_node = Node(data)
        current = self.head
        while current is not None:
            if(current.data == item):
                break
            current = current.next
        if(current is None):
            print(f"value {item} not found")
            return
        new_node.next = current.next
        current.next = new_node
        return
    
    # display list in reverse order
    def display_reverse(self):
        current = self.head
        while current is not None:
            copy = current
            current = current.next     
        while copy is not None:
            print(copy.data)
            copy = copy.prev
    
    # display list    
    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
    
    # delete front node 
    def delete_atfront(self):
        if(self.head is None):
            return("List is empty")
        else:
            self.head = self.head.next
            self.head.prev = None
            
    # delete last node
    def delete_atend(self):
        if(self.head is None):
            return("List is empty")
        else:
            node = self.head
            while node is not None:
                copy = node
                node = node.next
            copy.prev.next = None
