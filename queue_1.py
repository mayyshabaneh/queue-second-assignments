class Queue:

    # define an empty queue as a list
    def __init__(self) :
        self.queue = []

    # if you want to add item in the queue use enqueue to append an item
    def enqueue(self,item):
        self.queue.append(item)


    # when you use dequeue it removes the first item in queue
    def dequeue(self):
        if self.isEmpty() :
            print("empty queue")
        return self.queue.pop(0)
    
    # check the queue if empty or not by len function return true if empty , false if it having items
    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        return False


    # return the size of queue using len function
    def size(self):
        return len(self.queue)
    
    # peek function to return first index in queue without remove it
    def peek(self):
        if self.isEmpty():
            print("queue is empty")
        else :
            return self.queue[0]
    
    # a print function for testing before and after applying methods
    def print(self):
        for i in range(len(self.queue)):
            print (self.queue[i],end=" , ")
        print("\n")