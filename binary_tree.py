class Node:
    def __init__(self, key, value=None, left=None, right=None):
        """
        Class to define a binary tree.

        Key: Integer
        Index of value in the node

        Value: Integer
        Value associated to the key in the node

        Right: Integer
        Right child of the node

        Left: Integer
        Left child of the node
        """
        self.key = key
        self.value = value
        self.left = left
        self.right = right


def insert(root, key, value):
    """
    Function to insert a [key, value] pair in a node of the tree.

    Root: Class object
    Root of the binary tree

    Key: Integer
    Index of value in the node

    Value: Integer
    Value associated to the key in the node
    """

    if root.key is None:
        root.key = key
        root.value = value
        # Assign key & value to current node if node is empty.
    elif key > root.key:
        insert(root.right, key, value)
        # Insert key & value in right child node.
    elif key < root.key:
        insert(root.left, key, value)
        # Insert key & value in left child node.
    else:
        return -1


def search(root, key):
    """
    Function to search keys in a binary tree.

    Root: Class object
    Root of the binary tree

    Key: Integer
    Index of value in the node
    """
    if root.key == key:
        return root.value
        # Return value of selected key.
    elif key < root.key:
        search(root.left, key)
    elif key > root.key:
        search(root.right, key)
    else:
        return -1
