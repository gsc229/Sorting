# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        print(f"i loop\n{arr}")
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(cur_index + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    return arr


# TO-DO:  implement the Bubble Sort function below


def bubble_sort(arr):
    print(arr)

    passes = 0
    _sorted = False
    if not len(arr):
        return arr
    else:
        while not _sorted:
            for i in range(0, len(arr) - 1):
                passes += 1
                if passes == len(arr):
                    _sorted = True
                    print(f"SORTED: {arr}")

                if arr[i] > arr[i+1]:
                    arr[i], arr[i+1] = arr[i+1], arr[i]
                    print(arr)
                    passes = 0
        return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):
    num_range = {}
    new_arr = []
    if not maximum == -1:
        for i in range(0, maximum + 1):
            num_range[i] = 0

    else:
        for i in range(0, len(arr) + 1):
            num_range[i] = 0

    for i in range(0, len(arr)):
        if arr[i] < 0:
            return "Error, negative numbers not allowed in Count Sort"
        num_range[arr[i]] += 1
        new_arr.append(0)
    print(num_range)

    for i in range(1, len(num_range)):
        num_range[i] = num_range[i-1] + num_range[i]
    print(num_range)

    for i in range(0, len(arr)):
        new_arr[num_range[arr[i]]-1] = arr[i]
        num_range[arr[i]] -= 1

    print(new_arr)
    return new_arr
