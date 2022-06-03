def reverse(arr, index):
    if index >= len(arr):
        return
    else:
        reverse(arr, index + 1)
        print(arr[index])


def getReverseString(arr, index):
    if index >= len(arr): # no recursive call here.....
        return "----end----"
    else:
        nextChar = getReverseString(arr, index + 1)
        return nextChar + arr[index]


if __name__ == "__main__":
    print(getReverseString(list("hello"), 0))
