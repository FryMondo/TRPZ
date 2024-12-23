from InstallGenerator.FactoryMethod.DesktopShortcutCreator import DesktopShortcutCreator
from InstallGenerator.Methods.LanguageSelect import get_language

def createShortcut(name, path):
    creator = DesktopShortcutCreator()

    print(get_language().get_message("creating_shortcut"))
    creator.create_shortcut(name, path)
