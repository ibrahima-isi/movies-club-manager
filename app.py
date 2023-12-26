import sqlite3
from PySide6 import QtWidgets as qts, QtCore as qtc
from PySide6 import QtWidgets

from movie import Movie, get_movies

class App(qts.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cine Club")
        self.setup_ui()
        self.set_connexions()
        self.populate_movies()


    def setup_ui(self):
        self.layout = qts.QVBoxLayout(self)

        self.txt_Box = qts.QLineEdit()
        self.btn_add = qts.QPushButton("Ajouter")
        self.list_zone = qts.QListWidget()
        self.list_zone.setSelectionMode(qts.QListWidget.ExtendedSelection)
        self.btn_remove = qts.QPushButton("Supprimer")

        self.layout.addWidget(self.txt_Box)
        self.layout.addWidget(self.btn_add)
        self.layout.addWidget(self.list_zone)
        self.layout.addWidget(self.btn_remove)


    def populate_movies(self):
        movies = get_movies()
        if movies:
            for movie in movies:
                self._add_to_list(movie)
            return True
        return False

    def set_connexions(self):
        self.btn_add.clicked.connect(self.add_movie)
        self.btn_remove.clicked.connect(self.remove_movie)
        self.txt_Box.returnPressed.connect(self.add_movie)


    def add_movie(self):
        title = self.txt_Box.text()
        if title:
            movie = Movie(title)
            if movie.add_to_movies():
                self._add_to_list(movie)
                print("Film Added")
                return True
        print("Fail to Add movie")
        return False


    def remove_movie(self):
        print("Removed")
        for item in self.list_zone.selectedItems():
            movie = item.data(qtc.Qt.UserRole)
            movie.remove_from_movies()
            self.list_zone.takeItem(self.list_zone.row(item))
        return self.list_zone.selectedItems()

    def _add_to_list(self, movie):
        lw_item = qts.QListWidgetItem(movie.title)
        lw_item.setData(qtc.Qt.UserRole, movie)
        self.list_zone.addItem(lw_item)
        self.txt_Box.setText("")



if __name__ == "__main__":
    app = qts.QApplication([])
    win = App()

    win.show()
    app.exec()
    