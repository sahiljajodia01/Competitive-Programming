class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, val):
        if self.head == None:
            new_node = Node(val)
            self.head = new_node
        else:
            new_node = Node(val)
            current = self.head

            while current.next != None:
                current = current.next
            
            current.next = new_node

    def size(self):
        current = self.head
        count = 0

        while current != None:
            count += 1
            current = current.next

        return count

    def display(self):
        current = self.head

        while current != None:
            print(current.val, end=" ")
            current = current.next
        print()

    def delete_idx(self, idx):
        current = self.head
        index = 0
        prev = None
        while True:
            if index == idx:
                prev.next = current.next
            
            prev = current
            current = current.next
            index += 1
        



l = LinkedList()

l.append(1)
l.append(6)
l.append(3)
a = l.size()
print(a)

l.display()
l.delete_idx(1)
l.display()
