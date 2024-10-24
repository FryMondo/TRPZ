from Methods.CheckLicence import checkLicence
from Methods.CreateFile import createFile
from Methods.CreateShortCut import createShortCut
from Methods.DeinstallFile import deinstallFile
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

    def deinstall_file(self):
        deinstallFile()

    def language_select(self):
        languageSelect()