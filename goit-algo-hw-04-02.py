def merge_sort(arr):
    """Рекурсивне сортування злиттям."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    return merge(merge_sort(left_half), merge_sort(right_half))


def merge(left, right):
    """Зливає два відсортовані списки в один."""
    merged = []
    left_index = 0
    right_index = 0

    # Спочатку об'єднуємо менші елементи
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Додаємо залишки
    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged


def merge_k_lists(lists):
    """Об'єднує k відсортованих списків у один відсортований."""
    combined = []
    for lst in lists:
        combined.extend(lst)

    return merge_sort(combined)


if __name__ == "__main__":
    lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
    merged_list = merge_k_lists(lists)
    print("Відсортований список:", merged_list)
