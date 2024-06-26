class ArrayList:
    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def is_empty(self):
        return self.size() == 0

    def add(self, value):
        self.data.append(value)

    def get(self, index):
        if index < 0 or index >= self.size():
            raise IndexError("Index out of bounds")
        return self.data[index]

    def remove(self, index):
        if index < 0 or index >= self.size():
            raise IndexError("Index out of bounds")
        return self.data.pop(index)

