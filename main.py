import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTreeView, QVBoxLayout, QPushButton, QFileSystemModel, QWidget, QInputDialog, QMessageBox, QHBoxLayout
from PyQt5.QtGui import QIcon


class FileExplorer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Explorer")
        self.setGeometry(100, 100, 800, 600)

        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.model = QFileSystemModel()
        self.model.setRootPath("")
        
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setRootIndex(self.model.index(""))
        
        layout.addWidget(self.tree)

        # Find File button
        find_btn_layout = QHBoxLayout()
        find_btn = QPushButton(QIcon("icons/find.png"), "Find File")
        find_btn.clicked.connect(self.find_file)
        find_btn_layout.addWidget(find_btn)
        layout.addLayout(find_btn_layout)

        # Buttons (Divided into two rows)
        btn_layout_1 = QHBoxLayout()
        btn_layout_2 = QHBoxLayout()

        copy_btn = QPushButton(QIcon("icons/copy.png"), "Copy")
        copy_btn.clicked.connect(self.copy_file)
        delete_btn = QPushButton(QIcon("icons/delete.png"), "Delete")
        delete_btn.clicked.connect(self.delete_file)
        rename_btn = QPushButton(QIcon("icons/rename.png"), "Rename")
        rename_btn.clicked.connect(self.rename_file)
        create_btn = QPushButton(QIcon("icons/create.png"), "Create")
        create_btn.clicked.connect(self.create_file)
        view_btn = QPushButton(QIcon("icons/view.png"), "View Content")
        view_btn.clicked.connect(self.view_content)
        
        btn_layout_1.addWidget(copy_btn)
        btn_layout_1.addWidget(delete_btn)
        btn_layout_1.addWidget(rename_btn)
        btn_layout_1.addWidget(create_btn)
        btn_layout_1.addWidget(view_btn)
        
        move_btn = QPushButton(QIcon("icons/move.png"), "Move")
        move_btn.clicked.connect(self.move_file)
        zip_btn = QPushButton(QIcon("icons/zip.png"), "Zip")
        zip_btn.clicked.connect(self.zip_file)
        unzip_btn = QPushButton(QIcon("icons/unzip.png"), "Unzip")
        unzip_btn.clicked.connect(self.unzip_file)
        chmod_btn = QPushButton(QIcon("icons/permissions.png"), "Change Permissions")
        chmod_btn.clicked.connect(self.change_permissions)
        ls_btn = QPushButton(QIcon("icons/list.png"), "List Directory")
        ls_btn.clicked.connect(self.list_directory)
        mkdir_btn = QPushButton(QIcon("icons/mkdir.png"), "Make Directory")
        mkdir_btn.clicked.connect(self.make_directory)
        rmdir_btn = QPushButton(QIcon("icons/rmdir.png"), "Remove Directory")
        rmdir_btn.clicked.connect(self.remove_directory)
        
        btn_layout_2.addWidget(move_btn)
        btn_layout_2.addWidget(zip_btn)
        btn_layout_2.addWidget(unzip_btn)
        btn_layout_2.addWidget(chmod_btn)
        btn_layout_2.addWidget(ls_btn)
        btn_layout_2.addWidget(mkdir_btn)
        btn_layout_2.addWidget(rmdir_btn)

        layout.addLayout(btn_layout_1)
        layout.addLayout(btn_layout_2)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

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

#fun ti create file
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

    def list_directory(self):
        current_index = self.tree.currentIndex()
        directory_path = self.model.filePath(current_index)
        os.system(f"ls {directory_path}")

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


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileExplorer()
    window.show()
    sys.exit(app.exec_())
