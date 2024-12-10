# Метод для перевірки встановлених файлів
def check_installed_files(file_repository):
    print("Checking installed files...")
    iterator = file_repository.create_iterator()
    iterator.first()

    while not iterator.is_done():
        iterator.next()
    print("All files checked.")