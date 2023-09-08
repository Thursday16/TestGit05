class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return ("Stack is empty")
        popped_data = self.top.data
        self.top = self.top.next
        return popped_data

    def check(self):
        if self.is_empty():
            print("Stack is empty")
        return self.top.data

    def display(self):
        current = self.top
        while current:
            print(current.data)
            current = current.next
        print("No more stack")


def run():
    stack = Stack()
    stack.push(10)
    stack.push(2)
    stack.push(20)
    stack.push(30)
    stack.push(50)
    stack.display()

    #LIFO