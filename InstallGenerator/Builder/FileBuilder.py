from InstallGenerator.Builder.Builder import Builder

class FileBuilder(Builder):
    def __init__(self):
        super().__init__()

    def set_name(self, file_name):
        self.buildPart("file_name", file_name)
        return self

    def set_path(self, path):
        self.buildPart("file_path", path)
        return self

    def set_type(self, file_type):
        self.buildPart("file_type", file_type)
        return self

    def build(self):
        if not self.data:
            raise ValueError("File details are incomplete.")
        return self.get()