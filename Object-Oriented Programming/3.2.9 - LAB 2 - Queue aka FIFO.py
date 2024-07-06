class QueueError(???):  # Choose base class for the new exception.
    #
    #  Write code here
    #


class Queue:
    def __init__(self):
        #
        # Write code here
        #

    def put(self, elem):
        #
        # Write code here
        #

    def get(self):
        #
        # Write code here
        #


que = Queue()
que.put(1)
que.put("dog")
que.put(False)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")
    