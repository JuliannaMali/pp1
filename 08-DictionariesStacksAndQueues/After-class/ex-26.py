#####
# Queue definition
##

queue = []

# add value at the top of the queue
def push(value):
    queue.append(value)
    
# remove the topmost element of the queue
# and return its value    
def pop():
    if not empty():
        return queue.pop()
    else:
        return None
    
# return true if the queue is empty
def empty():
    return len(queue) == 0

# display queue
def display():
    for i in queue:
        print(i)
    print()
