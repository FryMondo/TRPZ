from InstallGenerator.Iterator.Aggregate import Aggregate

class FileRepository:
    def __init__(self):
        self.id = 0
        self.file_name = None
        self.path = None
        self.file_type = None
        self.files = []

    def add_file(self, files):
        self.id += 1
        self.file_name = files["file_name"]
        self.path = files["file_path"]
        self.file_type = files["file_type"]
        file = {
            "id": self.id,
            "file_name": self.file_name,
            "file_path": self.path,
            "file_type": self.file_type
        }
        self.files.append(file)

    # Використання Aggregate для створення ітератора
    def create_iterator(self):
        aggregate = Aggregate(self)
        return aggregate.create_iterator()