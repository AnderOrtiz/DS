def sequential_search_steps(data_list, target):
    iterations = 0
    for i in range(len(data_list)):
        iterations += 1
        if data_list[i] == target:
            return (i, iterations)
    
    return (-1, iterations)

def binary_search_steps(data_list, target):
    start = 0
    end = len(data_list) - 1
    iterations = 0
    
    while start <= end:
        iterations += 1
        middle = (start + end) // 2
        
        if data_list[middle] == target:
            return (middle, iterations)
        elif data_list[middle] < target:
            start = middle + 1
        else:
            end = middle - 1
            
    return (-1, iterations)

data_1000 = list(range(1, 1001))
number_to_find = 998 

print("--- Comparativa de Rendimiento ---")
seq_result, seq_steps = sequential_search_steps(data_1000, number_to_find)
print(f"Secuencial -> Posición: {seq_result}, Iteraciones requeridas: {seq_steps}")

bin_result, bin_steps = binary_search_steps(data_1000, number_to_find)
print(f"Binaria    -> Posición: {bin_result}, Iteraciones requeridas: {bin_steps}")