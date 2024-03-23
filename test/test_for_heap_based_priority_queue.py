import unittest
from src.heap_based_priority_queue import HeapQueue


class TestHeapQueue(unittest.TestCase):
    def test_insert(self):
        heap = HeapQueue()
        heap.insert("Task 1", 3)
        heap.insert("Task 2", 1)
        heap.insert("Task 3", 2)

        self.assertEqual(heap.queue[0].priority, 3)

    def test_pop_element(self):
        heap = HeapQueue()
        heap.insert("Task 1", 5)
        heap.insert("Task 2", 9)
        heap.insert("Task 3", 10)
        heap.insert("Task 4", 4)
        heap.insert("Task 5", 4)
        heap.insert("Task 6", 4)
        heap.insert("Task 7", 4)

        self.assertEqual(heap.delete(), 10)

    def test_print_empty_queue(self):
        heap = HeapQueue()
        heap.print_queue()
        self.assertEqual(heap.print_queue(), None)


if __name__ == '__main__':
    unittest.main()
