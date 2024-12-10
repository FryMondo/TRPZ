from InstallGenerator.Iterator.Iterator import Iterator
from InstallGenerator.Iterator.FileIterator import FileIterator

# Aggregate: створення ітератора
class Aggregate:
    def __init__(self, repository):
        self.repository = repository

    def create_iterator(self):
        return Iterator(FileIterator(self.repository))
