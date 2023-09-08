class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.tail = None

    def is_empty(self):
        if self.front is None:
            return None

    def enqueue(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.front = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        dequeued_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.tail = None
        return dequeued_data

    def check(self):
        if self.is_empty():
            print("Queue is empty")
        return self.front.data

    def display(self):
        current = self.front
        while current:
            print(current.data)
            current = current.next
        print("No more queue")


def run():
    queue = Queue()
    queue.enqueue(10)
    queue.enqueue(30)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()
    queue.dequeue()
    queue.dequeue()
    queue.display()

    #FIFO

