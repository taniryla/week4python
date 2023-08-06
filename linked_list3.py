class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None  # no nodes and so head will be set to a value of None

    def append(self, value):
        # this new_node is floating out in space and not yet connected/docked to another Node
        new_node = Node(value)

        if self.head is None:  # if there is None value attached to the head
            self.head = new_node  # now we are creating a head since we now have 2 nodes
            print("Head Node created:", self.head.value)
            return

        node = self.head
        # traverse to the node.next that has a None value (till we reach the tail node)
        while node.next is not None:
            node = node.next

        node.next = new_node  # new_node is the new tail
        # node.next.value is the value of the tail
        print("Appended new Node with value:", node.next.value)


llist = LinkedList()
llist.append("First Node")
llist.append("Second Node")
llist.append("Third Node")
