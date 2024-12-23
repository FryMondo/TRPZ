class LanguageRepository:
    def __init__(self):
        self.id = None
        self.language_eng = "English"
        self.language_ukr = "Українська"

    def getEnglish(self):
        return self.language_eng

    def getUkrainian(self):
        return self.language_ukr