class Node :
    def __init__(self,value) :
        self.value = value
        self.next = None

class QueueScratch :
    def __init__(self) :
        self.head = None

    def display_Queue(self):
        currentNode = self.head
        while currentNode :
            print(currentNode.value,end="-")
            currentNode = currentNode.next

    def enqueuesc(self,value):
        newIndex = Node(value)
        if self.head is None :
            newIndex.next = self.head
            self.head = newIndex
        else :
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = newIndex
    
    def dequeue(self):
        if self.head is None :
            return None
        self.head = self.head.next
    
    def isEmpty(self):
        if self.head is None:
            return True
        else :
            return False


    def size(self):
        count = 0
        currentNode = self.head
        while currentNode:
            count += 1
            currentNode = currentNode.next
        return count
    
    def peek(self):
        if self.isEmpty() :
            return None
        return self.head.value