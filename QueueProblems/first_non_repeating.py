list = ['a', 'a', 'b', 'c', 'c', 'd', 'e', 'b', 'a']


def firstNonRepeating(list):
    # S - O(n) + O(n) == O(2n) == O(n)
    frequencyTable = dict()
    firstIndexTable = dict()

    # T - O(n)
    for index, item in enumerate(list):
        if item in frequencyTable:
            frequencyTable[item] += 1
            if item in firstIndexTable:
                firstIndexTable.pop(item)
        else:
            frequencyTable[item] = 1
            firstIndexTable[item] = index

    # finding the lowest index T - O(n)
    lowestIndex = -1
    for item in firstIndexTable:
        index = firstIndexTable.get(item)
        if lowestIndex == -1 or index < lowestIndex:
            lowestIndex = index

    print(firstIndexTable)
    print(f'lowest index {lowestIndex} first non repeating item {list[lowestIndex]}')


if __name__ == "__main__":
    firstNonRepeating(list)
