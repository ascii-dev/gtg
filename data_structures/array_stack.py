from utils.exceptions import Empty


class ArrayStack(object):
    """LIFO Stack implementation using a Python list as underlying storage"""

    def __init__(self):
        """Create an empty stack
        """
        self._data = []  # non-public list instance

    def __len__(self):
        """Return the number of elements in the stack
        """
        return len(self._data)

    def is_empty(self):
        """Return True is the stack is empty
        """
        return len(self._data) == 0

    def push(self, item):
        """Add element, item, to the top of the stack
        """
        self._data.append(item)  # new item stored at end of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack

        :raise: Empty exception if the stack is empty
        :return: The top item on the stack
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]  # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack

        :raise: Empty exception if the stack is empty
        :return: The top item on the stack
        """
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()  # remove last item from the list
