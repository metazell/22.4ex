"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        self.start = start
        self.next = start
    
    def generate(self):
        self.next += 1
        return self.next - 1
    
    def reset(self):
        self.next = self.start
    
    def __repr__(self):
        return f"<SerialGenerator start={self.start} next={self.next}>"

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    serial = SerialGenerator(start=100)
    print(serial.generate())  # Output: 100
    print(serial.generate())  # Output: 101
    print(serial.generate())  # Output: 102
    serial.reset()
    print(serial.generate())  # Output: 100

