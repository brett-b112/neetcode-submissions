class Node:
    def __init__(self,val, next=None):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = Node(0)

    def get(self, index: int) -> int:
        temp = self.head
        i = 0
        while temp.next:
            temp = temp.next
            if i == index:
                return temp.val
            i += 1
        return -1 

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        nxt = self.head.next
        self.head.next = newNode
        newNode.next = nxt


    def addAtTail(self, val: int) -> None:
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = Node(val)

    def addAtIndex(self, index: int, val: int) -> None:
        temp = self.head
        newNode = Node(val)
        i = 0
        while temp:
            if i == index:
                nxt = temp.next
                temp.next = newNode
                newNode.next = nxt
                break
            temp = temp.next
            i += 1

    def deleteAtIndex(self, index: int) -> None:
        temp = self.head
        i = 0
        while temp.next:
            if i == index:
                temp.next = temp.next.next
                break
            temp = temp.next
            i += 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)