from InstallGenerator.Bridge.LanguageImplementor import LanguageImplementor
from InstallGenerator.Bridge.LanguageSelector import LanguageSelector

# RefinedAbstraction
class InstallerLanguage(LanguageSelector):
    def __init__(self, implementor: LanguageImplementor):
        super().__init__(implementor)