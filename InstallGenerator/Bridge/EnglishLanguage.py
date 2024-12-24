from InstallGenerator.Bridge.LanguageImplementor import LanguageImplementor

# ConcreteImplementorA (English)
class EnglishLanguage(LanguageImplementor):
    messages = {
        "checking_files": "Checking installed files...",
        "files_checked": "All files checked.",
        "creating_shortcut": "Creating shortcut...",
        "shortcut_created": "Shortcut '{name}' created in '{path}'",
        "enter_license_key": "Enter the licence key: ",
        "license_key_valid": "Licence key is valid. Installation continues...",
        "license_key_invalid": "Invalid licence key. Please try again."
    }

    def get_message(self, key):
        return self.messages.get(key, "Unknown message")
