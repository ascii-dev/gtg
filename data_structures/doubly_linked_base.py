from utils.exceptions import Empty


class _DoublyLinkedBase(object):
    """A base class providing a doubly linked list representation"""
    class _Node:
        """Lightweight, no-public class for storing a doubly linked node
        """

        __slots__ = "_element", "_previous", "_next"  # streamline memory

        def __init__(self, element, previous, next):  # initialize node's fields
            self._element = element
            self._previous = previous
            self._next = next

    def __init__(self):
        """Create an empty list
        """
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._previous = self._header
        self._size = 0

    def __len__(self):
        """Return the number of elements in the list
        """
        return self._size

    def is_empty(self):
        """Return True if list is empty
        """
        return self._size == 0

    def _insert_between(self, element, predecessor, successor):
        """Add element between two existing nodes and return new node
        """
        newest = self._Node(element, predecessor, successor)  # linked to neighbors
        predecessor._next = newest
        successor._previous = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """Delete non-sentinel node from the list and return its element
        """
        predecessor = node._previous
        successor = node._next
        predecessor._next = successor
        successor._previous = predecessor
        self._size -= 1
        element = node._element  # record deleted element
        node._previous = node._next = node._element = None  # deprecate node
        return element  # return deleted element


class LinkedDeque(_DoublyLinkedBase):
    """Double-ended queue implementation based on a doubly linked list
    """

    def first(self):
        """Return (but do not remove) the element at the front of the deque
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._header._next._element  # real item just after header

    def last(self):
        """Return (but do not remove) the element at the back of the deque
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._trailer._previous._element  # real item just before trailer

    def insert_first(self, element):
        """Add an element to the front of the deque
        """
        self._insert_between(element, self._header, self._header._next)  # after header

    def insert_last(self, element):
        """Add an element to the back of the deque
        """
        self._insert_between(element, self._trailer._previous, self._trailer)  # before trailer

    def delete_first(self):
        """Remove and return the element from the front of the deque

        :raise: Empty exception if the deque is empty
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._header._next)

    def delete_last(self):
        """Remove and return the element from the back of the deque

        :raise: Empty exception if the deque is empty
        """
        if self.is_empty():
            raise Empty("Deque is empty")
        return self._delete_node(self._trailer._previous)
