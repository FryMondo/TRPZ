from InstallGenerator.Iterator.Aggregate import Aggregate

class FileRepository:
    def __init__(self):
        self.id = 0
        self.file_name = None
        self.directory_repository = None
        self.file_type = None
        self.files = []

    def add_file(self, file_name, path, file_type):
        self.id += 1
        self.file_name = file_name
        self.directory_repository = path
        self.file_type = file_type
        file = {
            "id": self.id,
            "file_name": file_name,
            "file_path": path,
            "file_type": file_type
        }
        self.files.append(file)

    # Використання Aggregate для створення ітератора
    def create_iterator(self):
        aggregate = Aggregate(self)
        return aggregate.create_iterator()