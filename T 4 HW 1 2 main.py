\Завдання 

import timeit
import random
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    return merge(left, right)
def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
def timsort(arr):
    return sorted(arr)
def generate_data(size):
    random.seed(42)
    data = list(range(1, size + 1))
    random.shuffle(data)
    return data
def test_algorithms():
    sizes = [10, 100, 1000, 10000]
    for size in sizes:
        data = generate_data(size)
        merge_sort_time = timeit.timeit(lambda: merge_sort(data.copy()), number=10)
        print(f"Merge Sort time for size {size}: {merge_sort_time}")
        insertion_sort_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=10)
        print(f"Insertion Sort time for size {size}: {insertion_sort_time}")
        timsort_time = timeit.timeit(lambda: timsort(data.copy()), number=10)
        print(f"Timsort time for size {size}: {timsort_time}")
        print()
test_algorithms() 




\Завдання (необовʼязкове) 

import heapq
def merge_k_lists(lists):
    merged = []
    heap = []
    # Додати перше значення кожного списку до купи
    for i, lst in enumerate(lists):
        if len(lst) > 0:
            heapq.heappush(heap, (lst[0], i, 0))
    while heap:
        val, list_index, element_index = heapq.heappop(heap)
        merged.append(val)
        if element_index + 1 < len(lists[list_index]):
            next_element = lists[list_index][element_index + 1]
            heapq.heappush(heap, (next_element, list_index, element_index + 1))
    return merged
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)

