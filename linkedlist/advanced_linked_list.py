import traceback

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.size() == 0

    def push_back(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def push_front(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def pop_front(self):
        if self.isEmpty():
            print("Underflow!")
        else:
            self.head = self.head.next

    def pop_back(self):
        if self.isEmpty():
            print("Underflow!")
        if self.head.next == None:
            self.head = None
        else:
            start = self.head
            while start.next.next:
                start = start.next
            self.tail = start
            self.tail.next = None

    def value_at(self, index):
        if index >= self.size():
            return "Out of index"
        begin = 0
        start = self.head
        while begin != index:
            start = start.next
            begin += 1
        return start.data

    def erase(self, index):
        if index >= self.size():
            return "Out of index"
        elif index  == self.size()-1:
            self.pop_back()
        elif index == 0:
            self.pop_front()
        else:
            count = 1
            start = self.head
            while count != index:
                start = start.next
                count += 1
            start.next = start.next.next
        return "Success"
    
    def front(self):
        return self.head.data
    
    def back(self):
        return self.tail.data

    def insert(self, index, value):
        if index == 0:
            self.push_front(value)
        # if index == self.size()-1:
        #     self.push_back(value)
        else:
            new_node = Node(value)
            start = self.head
            count = 1
            while count != index:
                start = start.next
                count += 1
            new_node.next = start.next
            start.next = new_node

    def reverse(self):
        prev = None
        next = None
        current = self.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def size(self):
        start = self.head
        count = 0
        while start:
            count += 1
            start = start.next
        return count
    
    def display(self):
        start = self.head
        while start:
            print(start.data, end=" ")
            start = start.next
        print()

if __name__ == "__main__":
    
    obj = LinkedList()
   
    obj.push_back(12)
    obj.push_back(13)
    obj.push_back(14)
    obj.push_front(11)
   
    obj.display()

    obj.insert(2, 100)
    obj.display()
    obj.insert(0, 200)
    obj.insert(5, 200)
    obj.display()
