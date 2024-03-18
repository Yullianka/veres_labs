class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority


class HeapQueue:
    def __init__(self):
        self.queue = []

    def swap(self, arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]

    def insert(self, value, priority):
        new_node = Node(value, priority)
        self.queue.append(new_node)
        if len(self.queue) > 1:
            for i in range((len(self.queue) - 2) // 2, -1, -1):
                self.heapify(self.queue, i, len(self.queue))

    def heapify(self, arr, node, heap_len):
        left_child = node * 2 + 1
        right_child = node * 2 + 2

        if left_child < heap_len:
            if arr[left_child].priority > arr[node].priority:
                self.swap(arr, left_child, node)
                self.heapify(arr, left_child, heap_len)
        if right_child < heap_len:
            if arr[right_child].priority > arr[node].priority:
                self.swap(arr, right_child, node)
                self.heapify(arr, right_child, heap_len)

    def delete(self):
        if len(self.queue) == 0:
            return None
        if len(self.queue) == 1:
            return self.queue.pop()
        else:
            max_value = self.queue[0]
            self.queue[0] = self.queue.pop()
            for i in range(0, (len(self.queue) - 2) // 2):
                self.heapify(self.queue, i, len(self.queue))
            return max_value.priority

    def print_queue(self):
        for i in self.queue:
            print("Next task priority:", i.priority)


if __name__ == "__main__":
    heap = HeapQueue()
    heap.insert("Buy groceries", 2)
    heap.insert("Pay bills", 1)
    heap.insert("Study for exam", 3)
    heap.insert("Go to gym", 2)
    heap.insert("exam", 10)
    heap.insert("Study", 5)

    print("Heap Queue:")
    heap.print_queue()
    print(heap.delete())
    heap.print_queue()
    print(heap.delete())
    heap.print_queue()
