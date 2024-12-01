class Node:
    def __init__(self, color):
        self.color = color
        self.next = None

class CircularLinkedList:
    def __init__(self, colors):
        self.head = None
        self.tail = None
        self.build_list(colors)

    def build_list(self, colors):
        for color in colors:
            new_node = Node(color)
            if not self.head:
                self.head = new_node
                self.tail = new_node
                self.head.next = self.head  # Point to itself
            else:
                self.tail.next = new_node
                self.tail = new_node
                self.tail.next = self.head  # Make it circular

    def next_color(self):
        self.head = self.head.next
        return self.head.color

    def prev_color(self):
        # Move backward by traversing to the node before the head
        current = self.head
        while current.next != self.head:
            current = current.next
        self.head = current
        return self.head.color
