array = [2, 4, 6, 7, 8]


def traverse(arr, index):
    if index >= len(arr):
        return
    else:
        print(arr[index])
        traverse(arr, index + 1)
        print(arr[index])

if __name__ == "__main__":
    traverse(array, 0)
