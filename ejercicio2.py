def descending_selection_sort(grades):
    n = len(grades)
    
    for i in range(n):
        max_idx = i
        
        for j in range(i + 1, n):
            if grades[j] > grades[max_idx]:
                max_idx = j
                
        grades[i], grades[max_idx] = grades[max_idx], grades[i]
        
    return grades

scores = [7.5, 9.0, 6.2, 10.0, 5.5, 8.8]
print(f"Calificaciones originales: {scores}")
print(f"Calificaciones de mayor a menor: {descending_selection_sort(scores)}")