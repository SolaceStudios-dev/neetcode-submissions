class Node:
    def __init__(self, key, value):
        self.leftChildNode = None
        self.rightChildNode = None
        self.key = key
        self.value = value


class TreeMap:
    def __init__(self):
        self.rootNode = None

    def insert(self, key: int, val: int) -> None:
        newNode = Node(key, val)
        
        # Handle empty tree
        if not self.rootNode:
            self.rootNode = newNode
            return
        
        # Traverse the tree to find insertion point
        current = self.rootNode
        while True:
            if key < current.key:
                if current.leftChildNode is None:
                    current.leftChildNode = newNode
                    return
                current = current.leftChildNode
            elif key > current.key:
                if current.rightChildNode is None:
                    current.rightChildNode = newNode
                    return
                current = current.rightChildNode
            else:
                # Duplicate key: update value
                current.value = val
                return

    def get(self, key: int) -> int:
        iter = self.rootNode
        while iter:
            if key < iter.key:
                iter = iter.leftChildNode
            elif key > iter.key:
                iter = iter.rightChildNode
            else:
                return iter.value
        return -1

    def getMin(self) -> int:
        if not self.rootNode:
            return -1
        iter = self.rootNode
        while iter.leftChildNode:
            iter = iter.leftChildNode
        return iter.value

    def getMax(self) -> int:
        if not self.rootNode:
            return -1
        iter = self.rootNode
        while iter.rightChildNode:
            iter = iter.rightChildNode
        return iter.value

    def remove(self, key: int) -> None:
        def _remove(node, key):
            if not node:
                return None
            if key < node.key:
                node.leftChildNode = _remove(node.leftChildNode, key)
            elif key > node.key:
                node.rightChildNode = _remove(node.rightChildNode, key)
            else:
                if not node.leftChildNode:
                    return node.rightChildNode
                if not node.rightChildNode:
                    return node.leftChildNode
                curr = node.rightChildNode
                while curr.leftChildNode:
                    curr = curr.leftChildNode
                node.key = curr.key
                node.value = curr.value
                node.rightChildNode = _remove(node.rightChildNode, curr.key)
            return node

        self.rootNode = _remove(self.rootNode, key)

    def getInorderKeys(self) -> List[int]:
        res = []
        def _inorder(node):
            if not node:
                return
            _inorder(node.leftChildNode)
            res.append(node.key)
            _inorder(node.rightChildNode)
        _inorder(self.rootNode)
        return res