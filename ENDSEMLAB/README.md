Merge Sort – Student Marks
1. Problem Statement

A university stores the marks of N students in an unsorted array. The examination cell needs to arrange the marks in ascending order before generating the rank list.

This project implements Merge Sort using the Divide-and-Conquer technique.


2. Algorithm Used
Merge Sort

Merge Sort follows the Divide-and-Conquer approach:
Divide the array into two halves.
Recursively sort both halves.
Merge the two sorted halves.
Count each comparison between elements during merging.

3. Program
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

4. Sample Input
[40, 45, 39, 38, 43, 41, 35, 42, 44, 37]

5. Sample Output
Original Array: [40, 45, 39, 38, 43, 41, 35, 42, 44, 37]
Sorted Array: [35, 37, 38, 39, 40, 41, 42, 43, 44, 45]
No of Comparisons: 21
