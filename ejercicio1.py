import time
import random

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    
    return quicksort(less) + equal + quicksort(greater)

random_data = [random.randint(1, 50000) for _ in range(10000)]

bubble_copy = random_data.copy()
quicksort_copy = random_data.copy()

print("Iniciando pruebas de rendimiento con 10,000 elementos...\n")

start_b = time.time()
bubble_sort(bubble_copy)
end_b = time.time()
bubble_time = end_b - start_b
print(f"Tiempo Burbuja: {bubble_time:.4f} segundos")

start_q = time.time()
quicksort(quicksort_copy)
end_q = time.time()
quicksort_time = end_q - start_q
print(f"Tiempo QuickSort: {quicksort_time:.4f} segundos")