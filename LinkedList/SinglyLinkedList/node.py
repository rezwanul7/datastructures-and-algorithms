class Node():
    def __init__(self, data):
        self.data = data
        self.nextNode = None

    def setData(self, data):
        self.data = data

    def setNextNode(self, node):
        self.nextNode = node