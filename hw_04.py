import timeit
import random

# Реалізація Merge Sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Реалізація Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Функція для вимірювання часу виконання
def measure_time(sort_function, arr):
    start_time = timeit.default_timer()
    sort_function(arr)
    end_time = timeit.default_timer()
    return end_time - start_time

# Порівняння алгоритмів на різних наборах даних
sizes = [100, 1000, 10000]
results = {}

for size in sizes:
    random_data = random.sample(range(size*10), size)
    sorted_data = sorted(random_data)
    reversed_data = sorted_data[::-1]

    # Випадкові дані
    results[f'Random - Size {size}'] = {
        'Merge Sort': measure_time(merge_sort, random_data[:]),
        'Insertion Sort': measure_time(insertion_sort, random_data[:]),
        'Timsort': measure_time(sorted, random_data[:])
    }

    # Відсортовані дані
    results[f'Sorted - Size {size}'] = {
        'Merge Sort': measure_time(merge_sort, sorted_data[:]),
        'Insertion Sort': measure_time(insertion_sort, sorted_data[:]),
        'Timsort': measure_time(sorted, sorted_data[:])
    }

    # Зворотно відсортовані дані
    results[f'Reversed - Size {size}'] = {
        'Merge Sort': measure_time(merge_sort, reversed_data[:]),
        'Insertion Sort': measure_time(insertion_sort, reversed_data[:]),
        'Timsort': measure_time(sorted, reversed_data[:])
    }

# Виведення результатів
for data_type, times in results.items():
    print(f'{data_type}:')
    for sort_type, time_taken in times.items():
        print(f'  {sort_type}: {time_taken:.6f} seconds')
    print()

# Аналіз складності алгоритмів
print("Теоретична складність алгоритмів:")
print("Merge Sort: O(n log n)")
print("Insertion Sort: O(n^2)")
print("Timsort: O(n log n) в середньому випадку, O(n) в найкращому випадку (для майже відсортованих даних)")

# Висновок
print("Висновок:")
print("Результати показують, що Timsort є найбільш ефективним алгоритмом серед трьох розглянутих.")
print("Це підтверджує, що поєднання сортування злиттям та сортування вставками робить Timsort ефективнішим.")
print("Програмісти використовують вбудовані алгоритми сортування в Python, оскільки вони є оптимізованими та забезпечують кращу продуктивність у більшості випадків.")
