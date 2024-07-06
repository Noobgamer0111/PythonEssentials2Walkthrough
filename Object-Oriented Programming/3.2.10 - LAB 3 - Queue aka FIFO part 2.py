class QueueError(???):
    pass


class Queue:
    #
    # Code from the previous lab.
    #


class SuperQueue(Queue):
    #
    # Write new code here.
    #


que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)
for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")
    