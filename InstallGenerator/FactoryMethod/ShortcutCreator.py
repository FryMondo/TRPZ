class ShortcutCreator:
    def __init__(self):
        self.factory = None

    def factory_method(self, name, path):
        raise NotImplementedError("Метод factory_method() має бути реалізований у підкласі")

    def create_shortcut(self, name, path):
        shortcut = self.factory_method(name, path)
        shortcut.create()