class InstallerRepository:
    def __init__(self, uninstaller_repo, file_repo, licence_key_repo, language_repo):
        self.id = None
        self.isShortcut = False
        self.file_type = None
        self.uninstaller_repo = uninstaller_repo
        self.file_repo = file_repo
        self.licence_key_repo = licence_key_repo
        self.language_repo = language_repo

    def save(self):
        pass

    def get(self, installer_id):
        pass
