from InstallGenerator.Builder.FileBuilder import FileBuilder
from InstallGenerator.Builder.FileDirector import FileDirector

def createFile(file_repository, file_name, path, file_type):
    builder = FileBuilder()
    director = FileDirector(builder)

    file = director.construct_file(file_name, path, file_type)

    file_repository.add_file(file)
