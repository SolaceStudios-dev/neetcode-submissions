#nullable disable

// Reconstructed from the Saxon BST increments through the root edge case.
// GetInorderKeys is the next increment and is not in this file yet.
class TreeMap {
    public class Node {
        public int key;
        public int val;
        public Node left;
        public Node right;
        public Node(int _key, int _val) {
            key = _key;
            val = _val;
            left = null;
            right = null;
        }
    }

    Node head;
    int size;

    public TreeMap() {
        head = null;
        size = 0;
    }

    public void Insert(int key, int val) {
        if (size == 0) {
            head = new Node(key, val);
            size++;
            return;
        }

        Node iter = head;
        Node prevIter = iter;

        while (iter != null) {
            prevIter = iter;
            if (iter.key == key) {
                iter.val = val;
                return;
            }
            iter = key > iter.key ? iter.right : iter.left;//walk down the tree left or right
        }

        if (key > prevIter.key) prevIter.right = new Node(key, val);//insert new node at right subtree
        else prevIter.left = new Node(key, val);//insert new node at left subtree
        size++;//increment size of tree
    }

    public int Get(int key) {
        Node iter = head;

        while (iter != null) {
            if (iter.key == key) return iter.val;//return value if key is found
            iter = key > iter.key ? iter.right : iter.left;//walk down the tree left or right
        }
        return -1;//return -1 if key is not found
    }

    public int GetMin() {
        if (size == 0) return -1;
        Node iter = head;
        while (iter.left != null) iter = iter.left;//walk down the tree left
        return iter.val;
    }

    public int GetMax() {
        if (size == 0) return -1;
        Node iter = head;
        while (iter.right != null) iter = iter.right;//walk down the tree right
        return iter.val;
    }

    public void Remove(int key) {
        if (size == 0) return;

        Node iter = head;
        Node prevIter = iter;

        while (iter != null) {
            if (iter.key == key) break;
            prevIter = iter;
            iter = key > iter.key ? iter.right : iter.left;
        }

        if (iter == null) return;

        // Case 1: leaf. A root leaf has no parent, so head itself becomes null.
        if (iter.left == null && iter.right == null) {
            if (iter == head) head = null;
            else if (prevIter.left == iter) prevIter.left = null;
            else prevIter.right = null;
            size--;
        }
        // Case 2: one child. A root with one child is replaced by that child.
        else if (iter.left == null || iter.right == null) {
            Node child = iter.left != null ? iter.left : iter.right;
            if (iter == head) head = child;
            else if (prevIter.left == iter) prevIter.left = child;
            else prevIter.right = child;
            size--;
        }
        // Case 3: two children. Overwrite this node, then unlink the successor.
        // head stays put, because the same node object keeps the new key and val.
        else {
            Node succParent = iter;
            Node succ = iter.right;
            while (succ.left != null) {
                succParent = succ;
                succ = succ.left;
            }

            iter.key = succ.key;
            iter.val = succ.val;

            if (succParent.left == succ) succParent.left = succ.right;
            else succParent.right = succ.right;
            size--;
        }
    }

    public List<int> GetInorderKeys() {
        List<int> keys = new List<int>();
        CollectKeys(head, keys);
        return keys;
    }

    private void CollectKeys(Node node, List<int> keys) {
        if (node == null) return;
        CollectKeys(node.left, keys);
        keys.Add(node.key);
        CollectKeys(node.right, keys);
    }
}
