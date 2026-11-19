def optimized_bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        if not swapped:
            print(f"Lista ordenada tempranamente en la pasada {i + 1}")
            break
            
    return arr

almost_sorted_list = [1, 2, 3, 5, 4, 6, 7]
print(f"Resultado: {optimized_bubble_sort(almost_sorted_list)}")