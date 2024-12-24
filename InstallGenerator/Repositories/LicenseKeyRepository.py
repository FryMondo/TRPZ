class LicenseKeyRepository:
    def __init__(self):
        self.id = None
        self.licence_key = "1111"

    def get(self):
        return self.licence_key
