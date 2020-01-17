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
    
    def sum_list(self, l1, l2):
        l1  = l1.head
        l2 = l2.head
        # l1 = self.head
        # l2 = self.head
        value = 0
        while l1 is not None and l2 is not None:
            value += l1.data
            value += l2.data
            l1.data = value%10
            value = int(value/10)
            l1 = l1.next
            l2 = l2.next

        if l1 is None and l2 is None:
            return
        
        if l1 is  None:
            l1.next = l2.next
        
        while l1 is not  None:
            value += l1.data
            l1.data = value%10
            value = int(value/10)
            l1 = l1.next

        if value == 1:
            l1.next = Node(value)
       

    def display(self):
        start = self.head
        while start:
            print(start.data, end=" ")
            start = start.next

if __name__ == "__main__":
  
    obj = LinkedList()

    first = LinkedList()
    first.push(2)
    first.push(0)
    first.push(0)
    first.push(0)

    second = LinkedList()
    second.push(2)
    second.push(0)
    second.push(0)
    second.push(0)
    
    first.display()
    print()
    second.display()
    print()
    first.sum_list(first, second)
    first.display()
    print()