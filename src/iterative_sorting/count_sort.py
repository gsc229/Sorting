import random
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
            print("Error, negative numbers not allowed in Count Sort")
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


arr4 = random.sample(range(200), 50)

count_sort(arr4, 200)
# [1,2,3,3]
