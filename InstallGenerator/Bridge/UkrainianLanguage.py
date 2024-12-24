from InstallGenerator.Bridge.LanguageImplementor import LanguageImplementor

# ConcreteImplementorB (Ukrainian)
class UkrainianLanguage(LanguageImplementor):
    messages = {
        "checking_files": "Перевірка встановлених файлів...",
        "files_checked": "Всі файли перевірено",
        "creating_shortcut": "Створення ярлика...",
        "shortcut_created": "Ярлик '{name}' створено в '{path}'",
        "enter_license_key": "Введіть ліцензійний ключ: ",
        "license_key_valid": "Ліцензійний ключ вірний. Продовження інсталяції...",
        "license_key_invalid": "Невірний ліцензійний ключ. Спробуйте ще раз."
    }

    def get_message(self, key):
        return self.messages.get(key, "Невідоме повідомлення")