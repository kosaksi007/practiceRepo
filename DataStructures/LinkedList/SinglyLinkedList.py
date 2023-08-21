class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insretElement(self, data):
        if self.head is None:
            newNode = Node(data)
            self.head = newNode
            self.tail = self.head
        else:
            newnode = Node(data)
            self.tail.next = newnode
            self.prev = self.tail
            self.tail = self.tail.next


obj = linkedList()
obj.insretElement(4)
obj.insretElement(5)
obj.insretElement(6)
obj.insretElement(7)
