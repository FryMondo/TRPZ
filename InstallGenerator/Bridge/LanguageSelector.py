from InstallGenerator.Bridge.LanguageImplementor import LanguageImplementor

# Abstraction
class LanguageSelector:
    def __init__(self, implementor: LanguageImplementor):
        self.implementor = implementor

    def get_message(self, key, **kwargs):
        message = self.implementor.get_message(key)
        return message.format(**kwargs)
