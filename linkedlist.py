class Node:

    
    def __init__(self, data = None, prev = None, next = None):

        self.data = data
        self.prev = prev
        self.next = next


    def __repr__(self):

        output = f"Node(data={self.data})"
        return output


def iterate(start):

    node = start

    while (node.next != None):

        # if node is starting node
        if (node.data == None):
            node = node.next
            print("start -> ", end = '')
            continue

        print(f"{node.data} -> ", end = '')
        node = node.next

    print("end")


a = Node(data = 2)
b = Node(data = 3)

sum = a.data + b.data
c = Node(data = sum, prev = (a, b))
a.next = c
b.next = c

start = Node(next = a)
end = Node(prev = c)
c.next = end

iterate(start)

