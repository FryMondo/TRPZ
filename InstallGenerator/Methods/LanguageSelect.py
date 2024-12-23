from InstallGenerator.Bridge.EnglishLanguage import EnglishLanguage
from InstallGenerator.Bridge.InstallerLanguage import InstallerLanguage
from InstallGenerator.Bridge.UkrainianLanguage import UkrainianLanguage

# Метод для вибору мови інсталятора
def languageSelect(language):
    implementor = EnglishLanguage()

    if language == "Українська":
        implementor = UkrainianLanguage()

    return InstallerLanguage(implementor)

def set_language(language):
    global selected_language
    selected_language = language

def get_language():
    global selected_language
    return selected_language