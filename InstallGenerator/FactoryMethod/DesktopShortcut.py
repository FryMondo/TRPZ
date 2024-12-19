from InstallGenerator.FactoryMethod.Shortcut import Shortcut

class DesktopShortcut(Shortcut):
    def __init__(self, name, path):
        self.name = name
        self.path = path

    def create(self):
        print(f"Creating shortcut...")
        print(f"Shortcut '{self.name}' created in '{self.path}'")