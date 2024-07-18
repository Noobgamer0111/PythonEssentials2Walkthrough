class QueueError(IndexError):  # Choose base class for the new exception.
    pass

class Queue:
    def __init__(self):
        self.queue = []        

    def put(self, elem):
        self.queue.insert(0, elem)

    def get(self):
        if len(self.queue) == 0:
            raise QueueError
        return self.queue.pop()

que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
    