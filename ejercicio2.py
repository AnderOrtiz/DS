def recursive_binary_search(data_list, target, start, end):
    if start > end:
        return -1
    
    middle = (start + end) // 2
    
    if data_list[middle] == target:
        return middle
    elif data_list[middle] < target:
        return recursive_binary_search(data_list, target, middle + 1, end)
    else:
        return recursive_binary_search(data_list, target, start, middle - 1)


sorted_list = [90,80,10,25,15,95]
target = 10

index = recursive_binary_search(sorted_list, target, 0, len(sorted_list) - 1)

print(f"\n--- Búsqueda Recursiva ---")
if index != -1:
    print(f"El número {target} está en el índice {index}")
else:
    print(f"El número {target} no se encuentra en la lista")