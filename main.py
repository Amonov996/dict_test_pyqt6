from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QLabel
from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QLineEdit, QListWidget, QTextEdit
from PyQt6.QtWidgets import QMessageBox

class NewWord(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.v_lang_lay = QVBoxLayout()
        self.h_lang_btn_lay = QHBoxLayout()
        self.h_btn_lay = QHBoxLayout()
        self.v_main_lay = QVBoxLayout()
        self.message = QMessageBox()

        self.eng_edit = QLineEdit()
        self.eng_edit.setPlaceholderText("Eng...")

        self.uz_edit = QLineEdit()
        self.uz_edit.setPlaceholderText("Uz...")

        self.v_lang_lay.addWidget(self.eng_edit)
        self.v_lang_lay.addWidget(self.uz_edit)

        self.add_btn = QPushButton("send")
        self.add_btn.clicked.connect(self.write_to_file)

        self.h_lang_btn_lay.addLayout(self.v_lang_lay)
        self.h_lang_btn_lay.addWidget(self.add_btn)

        self.result_label = QLabel("")

        self.menu_btn = QPushButton("MENU")
        self.menu_btn.clicked.connect(self.menu)
        self.h_btn_lay.addWidget(self.menu_btn)

        self.v_main_lay.addLayout(self.h_lang_btn_lay)
        self.v_main_lay.addWidget(self.result_label)
        self.v_main_lay.addLayout(self.h_btn_lay)

        self.setLayout(self.v_main_lay)

    def write_to_file(self):
        with open('dict_file.txt', "a+") as f:
            f.write(f"{self.eng_edit.text().title()}|{self.uz_edit.text().title()}\n")
            self.eng_edit.clear()
            self.uz_edit.clear()
            self.message.setText("Yangi so'z qo'shildi")
            self.message.show()

    def menu(self):
        self.close()


class ListWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()

        self.h_lang_lay = QHBoxLayout()
        self.h_list_wdg_lay = QHBoxLayout()
        self.h_btn_lay = QHBoxLayout()
        self.v_main_lay = QVBoxLayout()

        self.eng_lb = QLabel("English")
        self.uz_lb = QLabel("Uzbek")

        self.h_lang_lay.addWidget(self.eng_lb)
        self.h_lang_lay.addWidget(self.uz_lb)

        self.eng_wdg = QListWidget()
        self.uz_wdg = QListWidget()
        self.add_items()

        self.h_list_wdg_lay.addWidget(self.eng_wdg)
        self.h_list_wdg_lay.addWidget(self.uz_wdg)



        self.menu_btn = QPushButton("MENU")
        self.menu_btn.clicked.connect(self.menu)
        self.h_btn_lay.addWidget(self.menu_btn)

        self.v_main_lay.addLayout(self.h_lang_lay)
        self.v_main_lay.addLayout(self.h_list_wdg_lay)
        self.v_main_lay.addLayout(self.h_btn_lay)

        self.setLayout(self.v_main_lay)

    def add_items(self):
        with open('dict_file.txt') as f:
            line = f.read().split('\n')
            for i in line[1:-1]:
                word = i.split('|')
                self.eng_wdg.addItem(word[0])
                self.uz_wdg.addItem(word[1])


    def menu(self):
        self.close()


class Search_Word(QWidget):
    def __init__(self):
        super().__init__()
        self.v_lay = QVBoxLayout()
        self.h_lay = QHBoxLayout()
        self.result_message = QMessageBox()

        self.search_text = QLineEdit()
        self.search_btn = QPushButton('search')
        self.menu_btn = QPushButton('menu')

        self.h_lay.addWidget(self.search_text)
        self.h_lay.addWidget(self.search_btn)
        self.v_lay.addLayout(self.h_lay)
        self.v_lay.addWidget(self.menu_btn)
        self.setLayout(self.v_lay)

        #push btn

        self.menu_btn.clicked.connect(self.menu)
        self.search_btn.clicked.connect(self.search_word)

    def search_word(self):
        with open('dict_file.txt') as f:
            line = f.read().split('\n')
            for i in line[:-1]:
                word = i.split('|')
                if word[0] == self.search_text.text().title() or word[1] == self.search_text.text().title():
                    self.result_message.setFixedWidth(100)
                    self.result_message.setText(f"{word[0]} --- {word[1]}")
                    self.result_message.show()
        self.search_text.clear()


    def check_btn(self):
        print(self.search_btn.text())



    def menu(self):
        self.close()

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.new_word_window = NewWord()
        self.list_window = ListWindow()
        self.search_window = Search_Word()

        self.setFixedSize(300, 400)
        self.add_btn = QPushButton("ADD", self)
        self.list_btn = QPushButton("LIST", self)
        self.search_btn = QPushButton("SEARCH", self)
        self.exit_btn = QPushButton("EXIT", self)

        self.add_btn.setGeometry(100, 100, 90, 65)
        self.list_btn.setGeometry(100, 170, 90, 65)
        self.search_btn.setGeometry(100, 240, 90, 65)
        self.exit_btn.setGeometry(100, 310, 90, 65)

        self.add_btn.clicked.connect(self.win1_connect)
        self.list_btn.clicked.connect(self.win2_connect)
        self.search_btn.clicked.connect(self.win3_connect)
        self.exit_btn.clicked.connect(self.close)

        self.show()

    def win1_connect(self):
        self.new_word_window.show()

    def win2_connect(self):
        self.list_window.show()

    def win3_connect(self):
        self.search_window.show()


app = QApplication([])
win = MainWindow()
app.exec()
