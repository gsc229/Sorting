# TO-DO: complete the helpe function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    # TO-DO
    i = 0  # arrA index
    j = 0  # arrB index
    k = 0  # merged_arr index
    while k <= len(merged_arr) - 1:
        print(
            f"WHILE i: {i} j: {j} k: {k} arrA: {arrA} arrB: {arrB} merged_arr: {merged_arr}")
        if i < len(arrA) and j < len(arrB):
            if arrA[i] <= arrB[j]:
                merged_arr[k] = arrA[i]
                i += 1
                k += 1

            else:
                merged_arr[k] = arrB[j]
                j += 1
                k += 1
        elif i < len(arrA):
            merged_arr[k] = arrA[i]
            i += 1
            k += 1
        elif j < len(arrB):
            merged_arr[k] = arrB[j]
            j += 1
            k += 1

        else:
            break

    print(f"WHILE DONE merged_arr: {merged_arr}")
    return merged_arr


# [1,7],[6,10]
# 1i0 < 6j0 i = 0, j = 0 --> i++, k++
# [1] i = 1, j = 0, k=1
# 7i1 > 6j0 i = 1, j = 0 --> j++, k++
# [1, 6] i = 1, j=1, k=2
# 7i1 < 10j1 i = 1, j = 1 --> i++, k++
# [1,6,7] i = 2, j = 1, k=3
# Nonei2 ? 10j1 i=2, j = 1 -->
# TO-DO: implement the Merge Sort function below USING RECURSION
merge_this = [10, 9, 3, 8, 7, 9, 9]


def merge_sort(arr):
    # TO-DO

    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    print(f"left: {left}")
    right = merge_sort(arr[middle:])
    print(f"right: {right}")
    return merge(left, right)


merge_sort(merge_this)
# STRETCH: implement an in-place merge sort algorithm


def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr


def merge_sort_in_place(arr, l, r):
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr
