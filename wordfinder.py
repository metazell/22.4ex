"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    ...

    import random

    def __init__(self, filepath):
        """Reads words from a file and reports the number of words read."""
        self.words = self.read_words(filepath)
        print(f"{len(self.words)} words read")
    
    def read_words(self, filepath):
        """Read words from the file and remove any newlines."""
        with open(filepath) as file:
            return [line.strip() for line in file]
    
    def random(self):
        """Return a random word from the list."""
        return random.choice(self.words)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
    # Manual test
    wf = WordFinder("words.txt")
    print(wf.random())
    print(wf.random())
    print(wf.random())