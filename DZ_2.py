# Реализовать алгоритм пирамидальной сортировки (сортировка кучей).

from random import randint

def heapify(array, heap_size, root_index):
    largest = root_index
    left_child = 2 * root_index + 1
    right_child = 2 * root_index + 2
    
    if (left_child < heap_size and array[left_child] > array[largest]):
        largest = left_child
    
    if (right_child < heap_size and array[right_child] > array[largest]):
        largest = right_child
    
    if largest != root_index:
        array[root_index],array[largest] = array[largest],array[root_index]

        heapify(array, heap_size, largest)

def heap_sort(array):
    n = len(array)

    for i in range(n, -1, -1):
        heapify(array, n, i)

    for i in range(n-1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)

upper = 10
array = []
for i in range(upper):
    array.append(randint(0,100))

print(array)
heap_sort(array)
print(array)
