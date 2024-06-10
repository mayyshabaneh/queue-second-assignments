from linkedlist import LinkedList
class queueLinkedList():
    # when code initialize they create a linked list by default
    def __init__(self) :
       self.quell = LinkedList()
    

    # when you want to add a node / item the code call add_last_node method from linked list file
    def enqueuell(self,value):
        self.quell.add_Last_Node(value)


    # when you use dequeue it removes the first item in queue
    def dequeuell(self):
        self.quell.delete_First()

    
    # check the queue if empty or not by len function return true if empty , false if it having items
    def isEmptyll(self):
        if self.quell.count_Item() == 0 :
            return True
        else :
            return False


    # return the size of queue using len function
    def sizell(self):
        return self.quell.count_Item()

    
    # peek function to return first index in queue without remove it
    def peekll(self):
        return self.quell.head.value

    
    # a print function for testing before and after applying methods
    def print(self):
        return self.quell.display_List()
