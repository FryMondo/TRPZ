from InstallGenerator.FactoryMethod.Shortcut import Shortcut
from InstallGenerator.Methods.LanguageSelect import get_language

class DesktopShortcut(Shortcut):
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def create(self):
        print(get_language().get_message("shortcut_created", name=self.name, path=self.path))