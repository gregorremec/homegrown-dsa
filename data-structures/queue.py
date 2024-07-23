
class Queue():

    def __init__(self):
        self.internal_list = []

    def __init__(self, queue = []):
        self.internal_list = [queue]

    def push(self, item):
        """Adds item to the back of queue."""
        self.internal_list.insert(0, item)


    def pop(self):
        """Removes and returns item at the front of queue."""
        if self.internal_list == []:
            return None

        pos = len(self.internal_list) - 1        
        toReturn = self.internal_list[pos]
        self.internal_list = self.internal_list[:pos]

        return toReturn


if __name__ == "__main__":
    q = Queue()
    q.push(4)
    print(q.pop())