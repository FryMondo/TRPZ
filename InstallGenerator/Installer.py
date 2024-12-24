from InstallGenerator.Methods.CreateFile import createFile
from InstallGenerator.Methods.CheckInstalledFiles import check_installed_files
from InstallGenerator.Methods.CheckLicense import CheckLicense
from InstallGenerator.Methods.CreateShortcut import createShortcut
from InstallGenerator.Methods.LanguageSelect import languageSelect
from InstallGenerator.Methods.UninstallFile import uninstallFile
from InstallGenerator.Methods.LanguageSelect import set_language

from InstallGenerator.Repositories.FileRepository import FileRepository
from InstallGenerator.Repositories.DirectoryRepository import DirectoryRepository
from InstallGenerator.Repositories.LicenseKeyRepository import LicenseKeyRepository
from InstallGenerator.Repositories.LanguageRepository import LanguageRepository
from InstallGenerator.Repositories.UninstallerRepository import UninstallerRepository
from InstallGenerator.Repositories.InstallerRepository import InstallerRepository

class Installer:
    def __init__(self, installer_repository):
        self._installer_repository = installer_repository

    def check_license(self):
        client = CheckLicense(self._installer_repository.get_license_key_repo())
        client.checkLicense()

    def create_file(self, file_name, path, file_type):
        createFile(self._installer_repository.get_file_repo(), file_name, path, file_type)

    def create_shortcut(self, shortcut_name, shortcut_path):
        createShortcut(shortcut_name, shortcut_path)

    def uninstall_file(self):
        uninstallFile()

    def language_select(self, language):
        set_language(languageSelect(language))

    def check_installed_files(self):
        check_installed_files(self._installer_repository.get_file_repo())


# Демонстрація функціоналу
if __name__ == "__main__":
    # Створення репозиторію
    installer_repo = InstallerRepository(FileRepository(),
                                         DirectoryRepository(),
                                         LicenseKeyRepository(),
                                         LanguageRepository(),
                                         UninstallerRepository(DirectoryRepository))

    # Створення інсталятора
    installer = Installer(installer_repo)

    # Вибір мови
    language_repo = installer_repo.get_language_repo()
    selected_language = installer.language_select(language_repo.getUkrainian())

    # Перевірка ліцензії
    installer.check_license()

    # Додавання шляху
    installer_repo.get_directory_repo().add_path('C:/')
    installer_repo.get_directory_repo().add_path('C:/Users/Username/Desktop')

    # Додавання файлів у репозиторій
    installer.create_file("readme", installer_repo.get_directory_repo().get_path(0), ".txt")
    installer.create_file("installer", installer_repo.get_directory_repo().get_path(0), ".exe")

    # Створення ярлика
    installer.create_shortcut("File", installer_repo.get_directory_repo().get_path(1))

    # Перевірка встановлених файлів
    installer.check_installed_files()
