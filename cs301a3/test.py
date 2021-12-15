import ll
import dll
import stack
import queue
import dequeue
import rpn

# setup of all collections
ll = ll.ll()
dll = dll.dll()
stack = stack.stack()
queue = queue.queue()
dequeue = dequeue.dequeue()

# testing rpn
print("\n Testing reverse polish notation \n")

print(rpn.rpn(""))
print(rpn.rpn("3"))
print(rpn.rpn("1 3 3 * +"))
print(rpn.rpn("3 3 *"))
print(rpn.rpn("3.25 3 *"))
print(rpn.rpn("1 2 * 3 + 4"))
print(rpn.rpn("10000000000000000 99 *"))

# testing ll
print("\n Testing linked list \n")

print(ll.isEmpty())
ll.add("testing, testing")
print(ll.search("testing, testing"))
ll.append("2")
ll.append(3)
ll.append(4)
print(ll.isEmpty())
print(ll.size())
print(ll.index(3))
ll.insert(1,"fore!")
print(ll.pop())
print(ll.delete(3))

# testing dll
print("\n Testing doubly linked list \n")

dll.add("testing, testing")
print(dll.search("testing, testing"))
dll.append("2")
dll.append(3)
dll.append(4)
print(dll.isEmpty())
print(dll.size())
print(dll.index(3))
dll.insert(1,"fore!")
print(dll.pop())
print(dll.delete(3))

# testing stack
print("\n Testing stack \n")

stack.push("aoeu")
print(stack.pop())
stack.push(123)
print(stack.peek())
print(stack.isEmpty())
print(stack.size())

# testing queue
print("\n Testing queue \n")

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
print(queue.isEmpty())
print(queue.size())
queue.enqueue("eu")
print(queue.size())

# testing dequeue
print("\n Testing dequeue \n")

dequeue.addFront("item1")
dequeue.addRear("item2")
print(dequeue.removeFront())
print(dequeue.removeRear())
print(dequeue.isEmpty())
print(dequeue.size())
dequeue.addFront(12)
print(dequeue.isEmpty())
print(dequeue.size())
