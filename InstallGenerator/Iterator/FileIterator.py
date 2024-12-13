# Реалізація FileIterator
class FileIterator:
    def __init__(self, file_repository):
        self.file_repository = file_repository
        self.index = 0

    def first(self):
        self.index = 0

    def next(self):
        self.index += 1

    def is_done(self):
        return self.index >= len(self.file_repository.files)

    def current_item(self):
        if not self.is_done():
            return self.file_repository.files[self.index]
        else:
            raise StopIteration("No more files in the repository.")
