public class LinkedList {

    private class Node
    {
        public int val;
        public Node next;
        public Node(int _val)
        {
            val = _val;
            next = null;
        }
    }

    Node head;
    int size;

    public LinkedList() {
        head = null;
        size = 0;
    }    

    public int Get(int index) {
        Node iter = head;
        int currentIndex = 0;
        if(size == 0 || index >= size)
            return -1;
        while(iter != null)
        {
            if(currentIndex == index)            
                return iter.val;            
            iter = iter.next;
            currentIndex++;
        }
        return -1;
    }

    public void InsertHead(int val) {
        if(size == 0)
            head = new Node(val);
        else
        {
            Node newHead = new Node(val);
            Node oldHead = head;
            newHead.next = oldHead;
            head = newHead;
        }
        size++;
    }

    public void InsertTail(int val) {
        if(size == 0)
            head = new Node(val);
        else
        {
            Node iter = head;
            while (iter.next != null)
            {
                iter = iter.next;
            }
            iter.next = new Node(val);
        }
        size++;

    }

    public bool Remove(int index) 
    {
        if(size == 0 || index >= size)
            return false;
        else if(index == 0)
        {
            head = head.next;
        }
        else
        {
            Node iter = head;
            int curIndex = 0;
            while (curIndex != (index -1))
            {
                iter = iter.next;
                curIndex++;
            }
            iter.next = iter.next.next;
        }
        size--;
        return true;
    }

    public List<int> GetValues() {
        List<int> retList = new List<int>(size);
        Node iter = head;
        for(int i = 0; i < size; i++)
        {
            retList.Add(iter.val);
            iter = iter.next;
        }
        return retList;
    }
}