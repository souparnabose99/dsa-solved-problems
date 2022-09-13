

"""
@TODO:
Construct an algorithm to compare 2 binary search trees.
"""


class BSTComparator:

    def compare_bst(self, node_1, node_2):
        if not node_1 or not node_2:
            return node_1 == node_2

        if node_1.data is not node_2.data:
            return False

        return self.compare_bst(node_1.left_child, node_2.left_child) and self.compare_bst(node_1.right_child, node_2.right_child)


class Node:

    def __init__(self, data, parent):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.parent = parent


class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        # Visit left subtree
        if data < node.data:
            if node.left_child:
                self.insert_node(data, node.left_child)
            else:
                node.left_child = Node(data, node)
        # Visit right subtree
        else:
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                node.right_child = Node(data, node)

    def traverse(self):
        if self.root is not None:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left_child:
            self.traverse_in_order(node.left_child)

        print("Node Data : ", node.data)

        if node.right_child:
            self.traverse_in_order(node.right_child)

    def get_max_value(self):
        if self.root:
            return self.get_max(self.root)

    def get_max(self, node):
        if node.right_child:
            return self.get_max(node.right_child)

        return node.data

    def get_min_value(self):
        if self.root:
            return self.get_min(self.root)

    def get_min(self, node):
        if node.left_child:
            return self.get_min(node.left_child)

        return node.data

    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)

    def get_predecessor(self, node):
        if node.right_node:
            return self.get_predecessor(node.right_node)
        return node

    def remove_node(self, data, node):

        if node is None:
            return

        if data < node.data:
            self.remove_node(data, node.left_node)
        elif data > node.data:
            self.remove_node(data, node.right_node)
        else:

            if node.left_node is None and node.right_node is None:
                print("Removing a leaf node...%d" % node.data)

                parent = node.parent

                if parent is not None and parent.left_node == node:
                    parent.left_node = None
                if parent is not None and parent.right_node == node:
                    parent.right_node = None

                if parent is None:
                    self.root = None

                del node

            elif node.left_node is None and node.right_node is not None:  # node !!!
                print("Removing a node with single right child...")

                parent = node.parent

                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.right_node
                    if parent.rightChild == node:
                        parent.right_node = node.right_node
                else:
                    self.root = node.right_node

                node.right_node.parent = parent
                del node

            elif node.right_node is None and node.left_node is not None:
                print("Removing a node with single left child...")

                parent = node.parent

                if parent is not None:
                    if parent.left_node == node:
                        parent.left_node = node.left_node
                    if parent.right_node == node:
                        parent.right_node = node.left_node
                else:
                    self.root = node.left_node

                node.left_node.parent = parent
                del node

            else:
                print('Removing node with two children....')

                predecessor = self.get_predecessor(node.left_node)

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self.remove_node(data, predecessor)


bst_1 = BinarySearchTree()
bst_2 = BinarySearchTree()

bst_1.insert(10)
bst_1.insert(35)
bst_1.insert(10)
bst_1.insert(35)

bst_2.insert(10)
bst_2.insert(37)
bst_2.insert(18)
bst_2.insert(101)

tree_comparator = BSTComparator()
print(tree_comparator.compare_bst(bst_1.root, bst_2.root))


