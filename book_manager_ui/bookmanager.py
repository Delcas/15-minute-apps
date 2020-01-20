from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import random, string


class WidgetItem(QWidget):
    def __init__(self, text, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)
        
        self.setAutoFillBackground(True)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        checkbox = QCheckBox()
        book_name = QLabel()
        book_name.setText(text)
        # lable_pic.setPixmap(QPixmap('ma-icon-256.png'))

        layout.addWidget(checkbox)
        layout.addWidget(book_name)
        # layout.addWidget(lable_pic)


class SortBookInfoModel(QSortFilterProxyModel):
    def lessThan(self, source_left, source_right):
        return True


class ConfirmDialog(QDialog):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)

        


class MainWindow(QMainWindow):
    def __init__(self, parent=None, flags=Qt.WindowFlags()):
        super().__init__(parent=parent, flags=flags)

        widget = QWidget()
        self.resize(1200, 600)

        # layout
        vblayout_left = QVBoxLayout()
        vblayout_middle = QVBoxLayout()
        vblayout_right = QVBoxLayout()

        hblayout_main = QHBoxLayout()

        # kfz name and list
        self.store_name_kfz = QLabel()
        self.store_name_kfz.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.store_name_kfz.setText("KFZ")

        self.list_kfz = QListView()
        self.list_kfz.setEditTriggers(QListView.NoEditTriggers)
        self.list_kfz.set

        # 7788 name and list
        self.store_name_7788 = QLabel()
        self.store_name_7788.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.store_name_7788.setText("7788")

        self.list_7788 = QListView()
        self.list_7788.setEditTriggers(QListView.NoEditTriggers)

        # button
        self.button_upload = QPushButton()
        self.button_upload.setText("UPLOAD")

        self.button_takeoff = QPushButton()
        self.button_takeoff.setText("UPLOAD")

        # arrange the layout
        vblayout_left.addWidget(self.store_name_kfz)
        vblayout_left.addWidget(self.list_kfz)

        vblayout_middle.addWidget(self.button_upload)
        vblayout_middle.addWidget(self.button_takeoff)

        vblayout_right.addWidget(self.store_name_7788)
        vblayout_right.addWidget(self.list_7788)

        hblayout_main.addLayout(vblayout_left)
        hblayout_main.addLayout(vblayout_middle)
        hblayout_main.addLayout(vblayout_right)

        # init and show window
        widget.setLayout(hblayout_main)
        self.setCentralWidget(widget)

        self._init()
        self.show()

    def _init(self):
        self.model_kfz = QStandardItemModel(self.list_kfz)
        self.sort_model_kfz = SortBookInfoModel(self.list_kfz)
        self.sort_model_kfz.setSourceModel(self.model_kfz)
        self.list_kfz.setModel(self.sort_model_kfz)
        for _ in range(50):
            name = ''.join(random.choice(string.ascii_uppercase +\
                string.digits) for _ in range(20))
            item = QStandardItem(name)
            self.model_kfz.appendRow(item)
            item.setSizeHint(QSize(300, 100))
            index = self.sort_model_kfz.mapFromSource(item.index())
            w = WidgetItem(name, self)
            self.list_kfz.setIndexWidget(index, w)

        self.model_7788 = QStandardItemModel(self.list_7788)
        self.sort_model_7788 = SortBookInfoModel(self.model_7788)
        self.sort_model_7788.setSourceModel(self.model_7788)
        self.list_7788.setModel(self.sort_model_7788)
        for _ in range(50):
            name = ''.join(random.choice(string.ascii_uppercase +\
                string.digits) for _ in range(20))
            item = QStandardItem(name)
            self.model_7788.appendRow(item)
            item.setSizeHint(QSize(300, 100))
            index = self.sort_model_7788.mapFromSource(item.index())
            w = WidgetItem(name, self)
            self.list_7788.setIndexWidget(index, w)


if __name__ == '__main__':
    import sys
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit( app.exec_())