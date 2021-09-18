import ctypes


class DynamicArray(object):
    """
    A dynamic array class akin to a simplified Python list
    """

    def __init__(self):
        """
        Create an empty array
        """
        self._n = 0  # count of actual elements
        self._capacity = 1  # default array capacity
        self._A = self._make_array(self._capacity)  # low level array

    def __len__(self):
        """
        Return number of elements stored in the array
        """
        return self._n

    def __getitem__(self, index):
        """
        Return element at index
        """
        # Didn't know this could be done in Python, need to do more research about it
        if not 0 <= index < self._n:
            raise IndexError("Invalid index")
        return self._A[index]  # retrieve from array

    def insert(self, index, item):
        """
        Insert an item at index, shifting subsequent elements rightward
        """
        # for simplicity, we assume 0 <= index <= n
        if self._n == self._capacity:  # not enough room
            self._resize(2 * self._capacity)  # so double capacity

        for j in range(self._n, index, -1):
            self._A[j] = self._A[j-1]  # shift rightmost first, followed by others

        self._A[index] = item  # store newest element
        self._n += 1

    def remove(self, value):
        """
        Remove first occurrence of value or raise ValueError
        """
        # we do not consider shrinking the dynamic array in this version
        # TODO: create a newer version that handles shrinking the dynamic array
        for k in range(self._n):
            if self._A[k] == value:  # we found a match!
                for j in range(k, self._n - 1):  # shift others to fill the gap
                    self._A[j] = self._A[j+1]
                self._A[self._n - 1] = None  # help garbage collection
                self._n -= 1  # we have one less item
                return  # exit immediately
        raise ValueError("Value not found")  # only reach if no match

    def _resize(self, capacity):
        """
        Resize internal array to capacity
        """
        B = self._make_array(capacity)  # new (bigger) array
        for k in range(self._n):  # for each existing value
            B[k] = self._A[k]
        self._a = B  # user the newer (bigger) array
        self._capacity = capacity

    def _make_array(self, capacity):
        """
        Return the new array with capacity
        """
        return (capacity * ctypes.py_object)()  # see ctypes documentation
