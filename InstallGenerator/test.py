from repository import ConfigOptionsRepository, FilesRepository, InstallationsRepository

# Робота з таблицею ConfigOptions
config_repo = ConfigOptionsRepository()
config_id = config_repo.add(create_shortcut=True, install_directory='C:/Program Files/NewApp')
config = config_repo.get(config_id)
print(f"Config: {config}")

# Робота з таблицею Files
files_repo = FilesRepository()
file_id = files_repo.add(file_name='installer.exe', file_path='C:/Downloads/', file_type='exe', file_size=2048)
file_info = files_repo.get(file_id)
print(f"File: {file_info}")

# Робота з таблицею Installations
install_repo = InstallationsRepository()
install_id = install_repo.add(install_date='2024-10-19', config_id=config_id, file_id=file_id)
installation = install_repo.get(install_id)
print(f"Installation: {installation}")
