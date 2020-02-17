# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        print(f"i loop {arr}")
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[cur_index]:
                smallest_index = j
                print(
                    f"arr[j]: {arr[j]} < arr[cur_index]: {arr[cur_index]} TRUE. smallest index: {smallest_index}")
                arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
                print(f"SWAP: {arr}")
            else:
                print(
                    f"arr[j]: {arr[j]} < arr[cur_index]: {arr[cur_index]} FALSE")

    # TO-DO: swap

    return arr


selection_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])

# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):

    return arr


bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
