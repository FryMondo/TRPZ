class DirectoryRepository:
    def __init__(self):
        self.id = 0
        self.path = None
        self.directories = []

    def add_path(self, path):
        self.id += 1
        self.path = path
        directory = {
            "id": self.id,
            "path": self.path,
        }
        self.directories.append(directory)

    def get_path(self, id):
        return self.directories[id]["path"]