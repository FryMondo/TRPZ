from InstallGenerator.FactoryMethod.DesktopShortcut import DesktopShortcut
from InstallGenerator.FactoryMethod.ShortcutCreator import ShortcutCreator


class DesktopShortcutCreator(ShortcutCreator):
    def factory_method(self, name, path):
        return DesktopShortcut(name, path)