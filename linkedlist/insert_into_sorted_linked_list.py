class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insert_into_sorted(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = self.head
            self.head = new_node

        elif new_node.data <= self.head.data:
            new_node.next = self.head
            self.head = new_node
            
        else:
            curr = self.head
            while curr.next != None and curr.next.data < new_node.data:
                curr = curr.next
              
            new_node.next = curr.next
            curr.next = new_node

    def display(self):
        node = self.head
        while node:
            print(node.data," ",end=" ")
            node = node.next

if __name__ == "__main__":
    node = LinkedList()
    node.push(3)
    node.push(2)
    node.push(1)
    node.display()
    print()
    node.insert_into_sorted(4)
    node.insert_into_sorted(0)
    node.display()
    print()