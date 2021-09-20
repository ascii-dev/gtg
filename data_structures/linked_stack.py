from utils.exceptions import Empty


class LinkedStack(object):
    """LIFO Stack implementation using a singly linked list for storage
    """

    class _Node(object):
        """Lightweight, nonpublic class for storing a singly linked node
        """

        __slots__ = '_element', '_next'  # streamline memory usage

        def __init__(self, element, next):  # initialise node's fields
            self._element = element  # reference to user's element
            self._next = next  # reference to the next node

    def __init__(self):
        """Create an empty stack
        """
        self._head = None
        self._size = 0

    def __len__(self):
        """Return the number of elements in the stack
        """
        return self._size

    def is_empty(self):
        """Return True if the stack is empty
        """
        return self._size == 0

    def push(self, element):
        """Add element to the top of the stack
        """
        self._head = self._Node(element, self._head)  # create and link a new node
        self._size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack

        :raise: exception if stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._head._element  # top of stack is at head of list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO)

        :raise: exception if stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
