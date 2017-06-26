"""Module implements binary heap data structure."""


class Binheap(list):
    """Create binary heap."""

    def __init__(self,  iterable=None):
        """Initalize with or without iterable."""
        if not iterable:
            pass
        elif iterable and self.check_iterable(iterable):
            for num in iterable:
                self.push(num)
        else:
            raise TypeError('Must be iterable and all numbers.')

    def push(self, val):
        """."""
        if val not in self:
            list.append(self, val)
            self.bubble_up(len(self) - 1)

    def pop(self):
        """."""
        if len(self) > 0:
            temp = self[0]
            self[0], self[-1] = self[-1], temp
            temp = list.pop(self, -1)
            self.bubbule_down()
            return temp
        return None

    def bubble_up(self, i):
        """."""
        while True:
            if self[i] < self[(i - 1) // 2]:
                temp = self[i]
                self[i], self[(i - 1) // 2] = self[(i - 1) // 2], temp
            i = (i - 1) // 2
            if i < 1:
                break

    def bubbule_down(self):
        """."""
        i = 0
        while i * 2 + 1 <= len(self) - 1:
            i_smallest_child = self.get_smallest_childs_index(i)
            if self[i] > self[i_smallest_child]:
                temp = self[i]
                self[i], self[i_smallest_child] = self[i_smallest_child], temp
            i = i_smallest_child

    def get_smallest_childs_index(self, i):
        """."""
        if i * 2 + 2 > len(self) - 1:
            return i * 2 + 1
        else:
            if self[i * 2 + 1] < self[i * 2 + 2]:
                return i * 2 + 1
            else:
                return i * 2 + 2

    def check_iterable(self, iterable):
        """."""
        allnumeric = True
        for item in iterable:
            if type(item) not in [int, float]:
                allnumeric = False
        return allnumeric
