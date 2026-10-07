def merge_sort(arr):
    if len(arr) <= 1:
        return arr, 0

    mid = len(arr) // 2

    left, c1 = merge_sort(arr[:mid])
    right, c2 = merge_sort(arr[mid:])

    merged, c3 = merge(left, right)

    return merged, c1 + c2 + c3


def merge(left, right):
    i = j = c = 0
    res = []

    while i < len(left) and j < len(right):
        c += 1

        if left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1

    res.extend(left[i:])
    res.extend(right[j:])

    return res, c


marks = [40, 45, 39, 38, 43, 41, 35, 42, 44, 37]

sorted_arr, comparisons = merge_sort(marks)

print("Original Array:", marks)
print("Sorted Array:", sorted_arr)
print("No of Comparisons:", comparisons)
