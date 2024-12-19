from InstallGenerator.FactoryMethod.DesktopShortcutCreator import DesktopShortcutCreator

def createShortcut(name, path):
    creator = DesktopShortcutCreator()
    creator.create_shortcut(name, path)
