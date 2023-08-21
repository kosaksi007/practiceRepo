class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insertBeginning(self, data):
        n = self.head
        if n is not None:
            newNode = Node(data)
            newNode.next = self.head
            self.head = newNode
        else:
            newNode = Node(data)
            self.head = newNode

    def traverseLL(self):
        if self.head is None:
            print('Linked List is Empty!')
        else:
            n = self.head
            while n is not None:
                print(n.data, end=',')
                n = n.next

    def addAtEnd(self, data):
        n = self.head
        while n is not None:
            if n.next is not None:
                n = n.next
            else:
                n.next = Node(data)
                break






temp = LinkedList()
temp.insertBeginning(10)
temp.insertBeginning(10)
temp.insertBeginning(10)
temp.insertBeginning(10)
temp.addAtEnd(25)
temp.insertBeginning(10)
temp.traverseLL()
