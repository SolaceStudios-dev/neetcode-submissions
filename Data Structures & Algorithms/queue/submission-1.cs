class Deque {

    LinkedList<int> deque;

    public Deque() {
        deque = new LinkedList<int>();  
    }

    public bool isEmpty() {
        return (deque.Count == 0);
    }

    public void append(int value) {
        deque.AddLast(value);
    }

    public void appendleft(int value) {
        deque.AddFirst(value);
    }

    public int pop() {
        if (isEmpty()) {
            return -1;
        }
        int retValue = deque.Last.Value;
        deque.RemoveLast();
        return retValue;
    }

    public int popleft() {
        if (isEmpty()) {
            return -1;
        }
        int retValue = deque.First.Value;
        deque.RemoveFirst();
        return retValue;
    }
}
