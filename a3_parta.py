class MinHeap:
    def __init__(self, arr=None):
        if arr is None:
            arr = []
        self.heap = arr[:]
        self.build_heap()

    def build_heap(self):
        for i in reversed(range(len(self.heap)//2)):
            self._heapify_down(i)

    def insert(self, element):
        self.heap.append(element)
        self._heapify_up(len(self.heap)-1)

    def get_min(self):
        if self.is_empty():
            return None
        return self.heap[0]

    def extract_min(self):
        if self.is_empty():
            return None
        min_val = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return min_val

    def is_empty(self):
        return len(self.heap) == 0

    def __len__(self):
        return len(self.heap)

    def _heapify_up(self, i):
        parent = (i-1) // 2
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i-1) // 2

    def _heapify_down(self, i):
        left = 2*i + 1
        right = 2*i + 2
        smallest = i
        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)
