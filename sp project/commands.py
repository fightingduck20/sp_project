import os
from PyQt5.QtWidgets import QInputDialog, QMessageBox

def copy_file(self):
        current_index = self.tree.currentIndex()
        file_path = self.model.filePath(current_index)
        destination_path, _ = QInputDialog.getText(self, "Copy File", "Enter destination path:")
        
        if destination_path:
            os.system(f"cp -r {file_path} {destination_path}")

def delete_file(self):
    current_index = self.tree.currentIndex()
    file_path = self.model.filePath(current_index)
    confirm = QMessageBox.question(self, "Delete File", f"Are you sure you want to delete {file_path}?", QMessageBox.Yes | QMessageBox.No)

    if confirm == QMessageBox.Yes:
        os.system(f"rm -r {file_path}")

def rename_file(self):
    current_index = self.tree.currentIndex()
    file_path = self.model.filePath(current_index)
    new_name, ok = QInputDialog.getText(self, "Rename File", "Enter new name:")
    
    if ok:
        os.system(f"mv {file_path} {os.path.join(os.path.dirname(file_path), new_name)}")

def create_file(self):
    current_index = self.tree.currentIndex()
    folder_path = self.model.filePath(current_index)
    file_name, ok = QInputDialog.getText(self, "Create File", "Enter file name:")

    if ok:
        with open(os.path.join(folder_path, file_name), "w"):
            pass

def move_file(self):
    current_index = self.tree.currentIndex()
    file_path = self.model.filePath(current_index)
    destination_path, _ = QInputDialog.getText(self, "Move File", "Enter destination path:")
    
    if destination_path:
        os.system(f"mv {file_path} {destination_path}")

def zip_file(self):
    current_index = self.tree.currentIndex()
    file_path = self.model.filePath(current_index)
    zip_name, ok = QInputDialog.getText(self, "Zip File", "Enter zip file name:")

    if ok:
        os.system(f"zip -r {zip_name} {file_path}")

def unzip_file(self):
    zip_file, _ = QInputDialog.getText(self, "Unzip File", "Enter zip file name:")

    if zip_file:
        os.system(f"unzip {zip_file}")

def view_content(self):
    current_index = self.tree.currentIndex()
    file_path = self.model.filePath(current_index)
    os.system(f"cat {file_path}")

def change_permissions(self):
    current_index = self.tree.currentIndex()
    file_path = self.model.filePath(current_index)
    permissions, ok = QInputDialog.getText(self, "Change Permissions", "Enter new permissions (e.g., 755):")

    if ok:
        os.system(f"chmod {permissions} {file_path}")

def make_directory(self):
    current_index = self.tree.currentIndex()
    directory_path = self.model.filePath(current_index)
    dir_name, ok = QInputDialog.getText(self, "Make Directory", "Enter directory name:")

    if ok:
        os.system(f"mkdir {os.path.join(directory_path, dir_name)}")

def remove_directory(self):
    current_index = self.tree.currentIndex()
    directory_path = self.model.filePath(current_index)
    os.system(f"rmdir {directory_path}")

def find_file(self):
    file_name, ok = QInputDialog.getText(self, "Find File", "Enter file name:")
    if ok:
        starting_dir, _ = QInputDialog.getText(self, "Find File", "Enter starting directory:")
        if starting_dir:
            os.system(f"find {starting_dir} -name '{file_name}'")