from InstallGenerator.Methods.LanguageSelect import get_language

# Метод для перевірки встановлених файлів
def check_installed_files(file_repository):
    print(get_language().get_message("checking_files"))
    iterator = file_repository.create_iterator()
    iterator.first()

    while not iterator.is_done():
        iterator.next()
    print(get_language().get_message("files_checked"))