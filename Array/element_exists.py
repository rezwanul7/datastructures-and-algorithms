def exists(arr, target_element):
    if len(arr) == 0:
        return False

    for element in arr:
        if element == target_element:
            return True

    return False


if __name__ == "__main__":
    print(exists([5, 4, 30, 2, 1], 3))
