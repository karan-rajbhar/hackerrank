# Enter your code here. Read input from STDIN. Print output to STDOUT


class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def leftChild(self, i):
        return 2 * i + 1

    def rightChild(self, i):
        return 2 * i + 2

    def hasLeftChild(self, i):
        return self.leftChild(i) < len(self.heap)

    def hasRightChild(self, i):
        return self.rightChild(i) < len(self.heap)

    def swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def insertKey(self, key):
        self.heap.append(key)
        i = len(self.heap) - 1
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def decreaseKey(self, i, new_val):
        self.heap[i] = new_val
        while i != 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.swap(i, self.parent(i))
            i = self.parent(i)

    def extractMin(self):
        if len(self.heap) <= 0:
            return float("-inf")
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        if len(self.heap) > 1:
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.minHeapify(0)
        return root

    def minHeapify(self, i):
        l = self.leftChild(i)
        r = self.rightChild(i)
        smallest = i
        if l < len(self.heap) and self.heap[l] < self.heap[i]:
            smallest = l
        if r < len(self.heap) and self.heap[r] < self.heap[smallest]:
            smallest = r
        if smallest != i:
            self.swap(i, smallest)
            self.minHeapify(smallest)

    def deleteKey(self, value):
        try:
            i = self.heap.index(value)
            self.decreaseKey(i, float("-inf") - 1)
            self.extractMin()
        except ValueError:
            print("Value not found in the heap.")

    def peek(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]


operation = None
size = int(input())

heap_obj = MinHeap()

try:
    while True:
        std_in = input().split()
        if len(std_in) == 1:
            print(heap_obj.peek())
        else:
            operation = int(std_in[0])
            operator = int(std_in[1])

            if operation == 1:
                heap_obj.insertKey(operator)
            if operation == 2:
                heap_obj.deleteKey(operator)
except EOFError:
    pass


# python3 QHEAP.py < input/input10.txt > output/ansoutput10.txt