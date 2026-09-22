from typing import List


from typing import List   # NeetCode provides this; only needed to run locally


class Node:
    def __init__(self, key, val):
        self.right = None
        self.left = None
        self.key = key
        self.val = val

class TreeMap:
    
    def __init__(self):
        self.rootNode = None

    def insert(self, key: int, val: int) -> None:
        if self.rootNode is not None:
            iter = self.rootNode
            while True:
                if(iter.key < key):
                    if(iter.right is None):
                        iter.right = Node(key,val)
                        return
                    else:
                        iter = iter.right
                elif(iter.key > key):
                    if(iter.left is None):
                        iter.left = Node(key,val)
                        return
                    else:
                        iter = iter.left
                else:
                    iter.val = val
                    return
        else:
            self.rootNode = Node(key, val)

    def get(self, key: int) -> int:
        if self.rootNode is not None:
            iter = self.rootNode
            while True:
                if(iter.key < key):
                    if(iter.right is None):
                        return -1
                    else:
                        iter = iter.right
                elif(iter.key > key):
                    if(iter.left is None):
                        return -1
                    else:
                        iter = iter.left
                else:
                    return iter.val
        else:
            return -1

    def getMin(self) -> int:
        if self.rootNode is not None:
            iter = self.rootNode
            while True:
                if(iter.left is None):
                    return iter.val
                else:
                    iter = iter.left
        else:
            return -1

    def findSuccessor(self, node) -> Node:
        successorParent = node
        successor = node.right
        while successor.left is not None:
            successorParent = successor
            successor = successor.left
        return successorParent, successor

    def getMax(self) -> int:
        if self.rootNode is not None:
            iter = self.rootNode
            while True:
                if(iter.right is None):
                    return iter.val
                else:
                    iter = iter.right
        else:
            return -1

    def remove(self, key: int) -> None:
        iter = None
        parent = None
        if self.rootNode is not None:
            iter = self.rootNode
            parent = None
            while True:
                if(iter.key < key):
                    if(iter.right is None):
                        return              # not found: remove promises None
                    else:
                        parent = iter
                        iter = iter.right
                elif(iter.key > key):
                    if(iter.left is None):
                        return              # not found: remove promises None
                    else:
                        parent = iter
                        iter = iter.left
                else:
                    #found the mark
                    break
        else:
            return                          # empty tree: nothing to remove

        #found the mark and going to do the delete
        if(iter.left is not None and iter.right is not None):#2 children first
            successorParent, successor = self.findSuccessor(iter)
            iter.key = successor.key             # copy the successor's payload up
            iter.val = successor.val
            parent = successorParent             # re-aim the fingers at the successor:
            iter = successor                     #   deleting IT is now the easy case

        #0 or 1 child: splice iter out
        child = iter.left if iter.left is not None else iter.right
        if parent is None:                  # nobody holds it: it was the root
            self.rootNode = child
        elif parent.left is iter:           # which hand of the parent holds it?
            parent.left = child
        else:
            parent.right = child

    def getInorderKeys(self) -> List[int]:
        tempList = []
        self._inorder(self.rootNode, tempList)
        return tempList
        
    def _inorder(self, node, out: List[int]) -> None:
        if node is None:
            return
        self._inorder(node.left, out)
        out.append(node.key)
        self._inorder(node.right, out)
        return