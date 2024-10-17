import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton, QLineEdit, QVBoxLayout
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kalkulyator")
        self.setGeometry(150, 150, 400, 300)

        self.display = QLineEdit()
        self.display.setAlignment(Qt.AlignRight)
        self.display.setFixedHeight(50)
        self.display.setReadOnly(True)
        self.display.setStyleSheet("background: gray ; color : yellow;font-size :50px")
        


        self.main_layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        
        self.main_layout.addWidget(self.display)

        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C'
        ]
        

        
        row, col = 0, 0
        for button in buttons:
            btn = QPushButton(button)
            btn.setFixedSize(60, 60)
            btn.clicked.connect(self.on_button_click)
            self.grid_layout.addWidget(btn, row, col)

            col += 1
            if col > 3:
                col = 0
                row += 1

        self.main_layout.addLayout(self.grid_layout)


        self.setLayout(self.main_layout)

        self.current_input = ''

    def on_button_click(self):
        button_text = self.sender().text()

        if button_text == "=":
            try:
                result = str(eval(self.current_input))
                self.display.setText(result)
                self.current_input = result
            except Exception as e:
                self.display.setText("Xato")
                self.current_input = ''
        else:
            self.current_input += button_text
            self.display.setText(self.current_input)
            
            
        if button_text == "C":
            self.display.setText("")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Calculator()
    window.show()
    sys.exit(app.exec_())
