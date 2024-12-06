from Methods.CheckLicence import checkLicence
from Methods.CreateFile import createFile
from Methods.CreateShortCut import createShortCut
from Methods.UninstallFile import uninstallFile
from Methods.LanguageSelect import languageSelect


class Installer:
    def __init__(self, installer_repo):
        self.installer_repo = installer_repo

    def check_licence(self):
        checkLicence()

    def create_file(self):
        createFile()

    def create_shortcut(self):
        createShortCut()

    def uninstall_file(self):
        uninstallFile()

    def language_select(self):
        languageSelect()