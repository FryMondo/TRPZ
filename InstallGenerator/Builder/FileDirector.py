from InstallGenerator.Builder.FileBuilder import FileBuilder

class FileDirector:
    def __init__(self, builder: FileBuilder):
        self.builder = builder

    def construct_file(self, file_name, path, file_type):
        return (
            self.builder
            .set_name(file_name)
            .set_path(path)
            .set_type(file_type)
            .build()
        )