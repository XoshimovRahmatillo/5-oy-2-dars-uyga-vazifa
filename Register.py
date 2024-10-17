import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox,
                             QComboBox, QRadioButton, QPushButton, QMessageBox, QLineEdit)
from PyQt5.QtGui import QFont

class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ro'yxatdan o'tish")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet("background: #a5b1c2")

        main_layout = QVBoxLayout()


        name_label = QLabel("Ismingizni tanlang:")
        name_label.setFont(QFont("Comic Sans MS", 12))
        name_label.setStyleSheet("color: white; background-color: black; border: 1px solid white")
        self.name_combo = QComboBox()
        self.name_combo.addItems(["A'zamjon", "Asadbek", "Rasulbek", "Hayotbek"])
        self.name_combo.setFont(QFont("Comic Sans MS", 12))
        self.name_combo.setStyleSheet("color: black; background-color: #4b6584; border: 1px solid white")

        
        birth_label = QLabel("Tug'ilgan kuningiz:")
        birth_label.setFont(QFont("Comic Sans MS", 12))
        birth_label.setStyleSheet("color: white; background-color: black; border: 1px solid white")

        self.day_combo = QComboBox()
        self.day_combo.addItems([str(i) for i in range(1, 32)])  
        self.day_combo.setFont(QFont("Comic Sans MS", 12))
        self.day_combo.setStyleSheet("color: black; background-color: yellow; border: 1px solid white")

        self.month_combo = QComboBox()
        self.month_combo.addItems(["Yanvar", "Fevral", "Mart", "Aprel", "May", "Iyun", 
                                   "Iyul", "Avgust", "Sentyabr", "Oktyabr", "Noyabr", "Dekabr"])  
        self.month_combo.setFont(QFont("Comic Sans MS", 12))
        self.month_combo.setStyleSheet("color: white; background-color: purple; border: 1px solid white")

        self.year_combo = QComboBox()
        self.year_combo.addItems([str(i) for i in range(1980, 2025)])  
        self.year_combo.setFont(QFont("Comic Sans MS", 12))
        self.year_combo.setStyleSheet("color: white; background-color: green; border: 1px solid white")

        
        self.terms_check1 = QCheckBox("Robot emasligizni tasdiqlang!")
        self.terms_check1.setFont(QFont("Arial", 12))
        self.terms_check1.setStyleSheet("background: black; color: red; border: 2px solid red")
        self.terms_check2 = QCheckBox("Foydalanish shartlarini qabul qiling!")
        self.terms_check2.setFont(QFont("Arial", 12))
        self.terms_check2.setStyleSheet("background: black; color: yellow; border: 2px solid yellow")

        
        self.male_radio = QRadioButton("Erkak")
        self.male_radio.setFont(QFont("Arial", 15))
        self.male_radio.setStyleSheet("background: black; color: blue; border: 2px solid blue")
        self.female_radio = QRadioButton("Ayol")
        self.female_radio.setFont(QFont("Arial", 15))
        self.female_radio.setStyleSheet("background: black; color: red; border: 2px solid red")


        register_button = QPushButton("Ro'yxatdan o'tish")
        register_button.setFont(QFont("Comic Sans MS", 12))
        register_button.clicked.connect(self.register)

        cancel_button = QPushButton("Bekor qilish")
        cancel_button.setFont(QFont("Comic Sans MS", 12))
        cancel_button.clicked.connect(self.cancel)


        combo_layout = QHBoxLayout()
        combo_layout.addWidget(name_label)
        combo_layout.addWidget(self.name_combo)

        birth_layout = QHBoxLayout()
        birth_layout.addWidget(birth_label)
        birth_layout.addWidget(self.day_combo)
        birth_layout.addWidget(self.month_combo)
        birth_layout.addWidget(self.year_combo)

        radio_layout = QHBoxLayout()
        radio_layout.addWidget(self.male_radio)
        radio_layout.addWidget(self.female_radio)

        button_layout = QHBoxLayout()
        button_layout.addWidget(register_button)
        button_layout.addWidget(cancel_button)

        
        main_layout.addLayout(combo_layout)
        main_layout.addLayout(birth_layout)
        main_layout.addWidget(self.terms_check1)
        main_layout.addWidget(self.terms_check2)
        main_layout.addLayout(radio_layout)
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def register(self):
        
        if not self.terms_check1.isChecked():
            QMessageBox.warning(self, "Xato", "Iltimos, robot emasligizni tasdiqlang!")
            return
        if not self.terms_check2.isChecked():
            QMessageBox.warning(self, "Xato", "Iltimos, foydalanish shartlarini tasdiqlang!")
            return
        
        if self.male_radio.isChecked():
            gender = "Erkak"   
        elif self.female_radio.isChecked():
            gender = "Ayol"
        else:
            QMessageBox.warning(self, "Xato", "Iltimos, jinsni tanlang")
            return      

        selected_name = self.name_combo.currentText()
        selected_day = self.day_combo.currentText()
        selected_month = self.month_combo.currentText()
        selected_year = self.year_combo.currentText()

        
        birth_date = f"{selected_day} {selected_month} {selected_year}"

        QMessageBox.information(self, "Ro'yxatdan o'tish", f"Siz muvaffaqiyatli ro'yxatdan o'tdingiz:\n"
                                                           f"Ism: {selected_name}\n"
                                                           f"Jinsi: {gender}\n"
                                                           f"Tug'ilgan sana: {birth_date}")

    def cancel(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegisterWindow()
    window.show()
    sys.exit(app.exec_())
