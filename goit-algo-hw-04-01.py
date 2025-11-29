import random
import timeit


def insertion_sort(arr):
    """Реалізація сортування вставками."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    """Реалізація сортування злиттям."""
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)


def merge(left, right):
    """Допоміжна функція для злиття двох відсортованих масивів."""
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


# Вимірювання часу сортування для різних розмірів масивів
sizes = [1000, 5000, 10000]

for n in sizes:
    data = [random.randint(0, 10000) for _ in range(n)]
    print(f"\nРозмір масиву: {n}")

    t_insertion = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)
    print(f"Час сортування вставками: {t_insertion:.6f} секунд")

    t_merge = timeit.timeit(lambda: merge_sort(data.copy()), number=1)
    print(f"Час сортування злиттям: {t_merge:.6f} секунд")

    t_timsort = timeit.timeit(lambda: sorted(data.copy()), number=1)
    print(f"Час вбудованого сортування (Timsort): {t_timsort:.6f} секунд")