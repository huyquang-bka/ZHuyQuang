from queue import Queue

count = 0

test_queue = Queue(maxsize=1)

for i in range(2):
    test_queue.put(i)

print(test_queue.get())
print(test_queue.get())
