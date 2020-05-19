class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return "{0}".format(self.value)

class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.insert_node(self.root, value)

    def insert_node(self, node, value):
        if value <= node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self.insert_node(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self.insert_node(node.right, value)

    def search(self, value):
        return self.search_node(self.root, value)

    def search_node(self, node, value):
        if node is None:
            return None
        else:
            if value == node.value:
                return node
            else:
                if value < node.value:
                    return self.insert_node(node.left, value)
                else:
                    return self.insert_node(node.right, value)

if __name__ == "__main__":
    btree = BinaryTree()
    btree.insert(5)
    btree.insert(4)
    btree.insert(7)
    btree.insert(2)

    print(btree.search(4))

