from LinkedList.SinglyLinkedList.node import Node

node1 = Node(5)
node2 = Node(6)
node1.nextNode = node2

head = node1

currentNode = head
while True:
    print(currentNode.data)
    currentNode = currentNode.nextNode

    if currentNode.nextNode == None:
        break
