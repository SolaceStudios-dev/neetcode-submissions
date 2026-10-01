public class DynamicArray {

    private List<int> array;    
    
    public DynamicArray(int capacity) {
        array = new List<int>(capacity);

    }

    private bool validIndex(int i)
    {
        return (i >= array.Count || i < 0) ? true : false;
    }

    public int Get(int i) {
        return array[i];
    }

    public void Set(int i, int n) {
        array[i] = n;
    }

    public void PushBack(int n) {
        array.Add(n);
    }

    public int PopBack() {
        int ret = array[array.Count - 1];
        array.RemoveAt(array.Count - 1);
        return ret;
    }

    private void Resize() {
        array.Capacity *= 2;

    }

    public int GetSize() {
        return array.Count;
    }

    public int GetCapacity() {
        return array.Capacity;
    }
}
