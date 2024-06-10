from queue_1 import Queue
from queue_linked_list import queueLinkedList

queue1 = Queue()
queell = queueLinkedList()

def enqueue_test():
        queue1.enqueue(10)
        queue1.enqueue(20)
        queue1.enqueue(30)
        queue1.enqueue(40)
        queue1.enqueue(50)
        queue1.enqueue(60)
        queue1.enqueue(70)
        queue1.enqueue(80)
        queue1.enqueue(90)
        queue1.print()


def dequeue_test():
    queue1.dequeue()
    queue1.print()


def isEmpty_test():
    if queue1.isEmpty() == False:
        print("queue is not empty")
    else :
         print("queue is empty")


def size_test():
    print(f"queue size = {queue1.size()}")    


def peek_test():
    print(f"the first item is {queue1.peek()}")

def enqueuell_test():
    queell.enqueuell(10)
    queell.enqueuell(20)
    queell.enqueuell(30)
    queell.enqueuell(40)
    queell.enqueuell(50)
    queell.enqueuell(60)
    queell.enqueuell(70)
    queell.enqueuell(80)
    queell.enqueuell(90)

def dequeuell_test():
    queell.dequeuell()


def isEmptyll_test():
    if queell.isEmptyll() == True :
        print("the queue is empty")
    else :
        print(f"the queue has ({queell.sizell()}) nodes")


def peekll_test():
    print(f"the first item in queue is {queell.peekll()}")


def printqueell_test():
    queell.print()

isEmptyll_test()
print("the queue after enqueue items is :")
enqueuell_test()
printqueell_test()
isEmptyll_test()
peekll_test()
print("the queue after dequeue items is :")
dequeuell_test()
printqueell_test()
peekll_test()
# isEmpty_test()
# enqueue_test()
# peek_test()
# dequeue_test()
# isEmpty_test()
# size_test()
# peek_test()