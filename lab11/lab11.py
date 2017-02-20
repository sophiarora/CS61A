#############
# Iterators #
#############

# Q2
class IteratorRestart:
    """
    >>> iterator = IteratorRestart(2, 7)
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        self.end = end
        self.start = start
        self.current = self.start - 1

    def __next__(self):
        if self.current > self.end - 1:
            self.current = self.start - 1
            raise StopIteration
        self.current += 1
        return self.current

    def __iter__(self):
        return self


# Q3
class Str:
    """
    >>> s = Str("hello")
    >>> for char in s:
    ...     print(char)
    ...
    h
    e
    l
    l
    o
    >>> for char in s:    # a standard iterator does not restart
    ...     print(char)
    """
    def __init__(self, string):
        self.len = len(string)
        self.str = string
        self.index = 0

    def __next__(self):
        if self.index >= self.len:
            raise StopIteration
        self.index += 1
        return self.str[self.index - 1]

    def __iter__(self):
        return self



##############
# Generators #
##############

# Q4
def countdown(n):
    """
    >>> from types import GeneratorType
    >>> type(countdown(0)) is GeneratorType # countdown is a generator
    True
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    while n >= 0:
        yield n
        n -= 1


class Countdown:
    """
    >>> from types import GeneratorType
    >>> type(Countdown(0)) is GeneratorType # Countdown is an iterator
    False
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    def __init__(self, start):
        self.current = start + 1

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current

    def __iter__(self):
        return self

# Q5
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    def hailstone_check(s):
        if s%2 == 0:
            s = int(s/2)
        else:
            s = int(s*3 +1)
        return s
    while n > 1:
        yield n
        n = hailstone_check(n)
    yield n

spiral_function(4, 10, 227, 66, 52, 255, 232, 131)
