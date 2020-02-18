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
            if arr[j] < arr[smallest_index]:
                smallest_index = j
                print(
                    f"arr[j{j})] = {arr[j]} < arr[smallest_index] = {arr[smallest_index]} TRUE. smallest_index= {smallest_index}")

            else:
                print(
                    f"arr[j({j})] = {arr[j]} < arr[smallest_index] = {arr[smallest_index]} FALSE. smallest_index= {smallest_index}")
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]

    # TO-DO: swap

    return arr


selection_sort([7, 5, 8, 4, 2, 9, 6, 0, 3, 1])
