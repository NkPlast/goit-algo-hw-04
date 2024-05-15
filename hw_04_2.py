import heapq

def merge_k_lists(lists):
    # Ініціалізація мін-кучі
    min_heap = []
    
    # Додавання першого елементу кожного списку до кучі
    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))
    
    result = []
    
    # Поки купа не порожня
    while min_heap:
        # Отримуємо найменший елемент
        val, list_idx, element_idx = heapq.heappop(min_heap)
        result.append(val)
        
        # Якщо в списку залишилися елементи, додаємо наступний елемент до кучі
        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(min_heap, next_tuple)
    
    return result

# Приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
