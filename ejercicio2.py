import sys
import time

sys.setrecursionlimit(2000)

def quicksort_first_pivot(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]
    
    less = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]
    
    return quicksort_first_pivot(less) + equal + quicksort_first_pivot(greater)

sorted_list = list(range(1, 1001))

start = time.time()
quicksort_first_pivot(sorted_list)
end = time.time()

print(f"Tiempo QuickSort (Primer pivote / Lista ordenada): {end - start:.4f} segundos")