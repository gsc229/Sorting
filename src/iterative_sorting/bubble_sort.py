# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    print(arr)

    passes = 0
    _sorted = False

    while not _sorted:
        for i in range(0, len(arr) - 1):
            passes += 1
            if passes == len(arr):
                _sorted = True
                print(f"SORTED: {arr}")
                return arr

            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                print(arr)
                passes = 0


bubble_sort([1, 5, 8, 4, 2, 9, 6, 0, 3, 7])
