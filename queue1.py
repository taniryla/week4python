class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.num_nodes = 0

    def size(self):
        return self.num_nodes

    def enqueue(self, value):
        new_node = Node(value)

        if self.head is None:  # is the queue empty
            # self.head = new_node
            # self.tail = new_node
            self.head = self.tail = new_node  # Same as above two lines
        else:  # if the queue is not empty
            # previous tail is linked to the new node and the new node is now the new tail
            self.tail.next = new_node
            self.tail = new_node

        self.num_nodes += 1

    def dequeue(self):
        if self.head is None:  # if the queue is empty
            return None

        # dequeue_node = self.head.value
        # if the queue is not empty... returning the node's value
        dequeue_node_value = self.head.value
        self.head = self.head.next  # sets the next head as the new head
        self.num_nodes -= 1
        return dequeue_node_value


q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')

print("Pass" if (q.size() == 3) else "Fail")
q.enqueue(4)
print("Pass" if (q.size() == 4) else "Fail")

print("Pass" if (q.dequeue() == 'a') else "Fail")
print("Pass" if (q.dequeue() == 'd') else "Fail")
print("Pass" if (q.size() == 2) else "Fail")
