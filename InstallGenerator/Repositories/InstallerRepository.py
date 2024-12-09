class InstallerRepository:
    def __init__(self, file_repo, directory_repo, licence_key_repo, language_repo, uninstaller_repo):
        self.id = None
        self.isShortcut = False
        self._directory_repo = directory_repo
        self._uninstaller_repo = uninstaller_repo
        self._file_repo = file_repo
        self._licence_key_repo = licence_key_repo
        self._language_repo = language_repo

    def get_directory_repo(self):
        return self._directory_repo

    def get_uninstaller_repo(self):
        return self._uninstaller_repo

    def get_file_repo(self):
        return self._file_repo

    def get_licence_key_repo(self):
        return self._licence_key_repo

    def get_language_repo(self):
        return self._language_repo
