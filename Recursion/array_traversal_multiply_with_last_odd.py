# find the last odd and multiply each elements before...
array = [2, 4, 6, 7, 8, 10, 13 ,14,16,17,18,20,21]


def traverseMultiply(arr, index):

    if index >= len(arr):
        return -1 #after 21
    elif arr[index] % 2 != 0: #21,17
        last_odd = arr[index]
        traverseMultiply(arr, index + 1)
        print(f'---{arr[index]}---')
    else:
        last_odd = traverseMultiply(arr, index + 1) #20,18,16,14
        if last_odd > 0:
            print(last_odd * arr[index])

    return last_odd


if __name__ == "__main__":
    traverseMultiply(array, 0)
