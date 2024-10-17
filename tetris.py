import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QGridLayout, QHBoxLayout

class TetrisWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Tetris shakllari")
        self.setGeometry(100, 100, 400, 400)

        main_layout = QVBoxLayout()


        btn1 = QPushButton("1")
        btn2 = QPushButton("2")
        btn3 = QPushButton("3")
        btn4 = QPushButton("4")

        btn1.clicked.connect(lambda: self.draw_shape(1))
        btn2.clicked.connect(lambda: self.draw_shape(2))
        btn3.clicked.connect(lambda: self.draw_shape(3))
        btn4.clicked.connect(lambda: self.draw_shape(4))


        button_layout = QHBoxLayout()
        button_layout.addWidget(btn1)
        button_layout.addWidget(btn2)
        button_layout.addWidget(btn3)
        button_layout.addWidget(btn4)


        self.grid_layout = QGridLayout()  

        main_layout.addLayout(button_layout)
        main_layout.addLayout(self.grid_layout)

        self.setLayout(main_layout)

    def draw_shape(self, shape_num):
        for i in reversed(range(self.grid_layout.count())):
            widget = self.grid_layout.itemAt(i).widget()
            if widget:
                widget.setParent(None)

        if shape_num == 1:
            self.grid_layout.addWidget(QPushButton(), 1, 1)
            self.grid_layout.addWidget(QPushButton(), 1, 0)
            self.grid_layout.addWidget(QPushButton(), 2, 0)
            self.grid_layout.addWidget(QPushButton(), 3, 0)
            self.grid_layout.addWidget(QPushButton(), 4, 0)
            
        elif shape_num == 2:
            
            self.grid_layout.addWidget(QPushButton(), 0, 0)
            self.grid_layout.addWidget(QPushButton(), 0, 1)
            self.grid_layout.addWidget(QPushButton(), 1, 0)
            self.grid_layout.addWidget(QPushButton(), 1, 1)
        elif shape_num == 3:
            
            self.grid_layout.addWidget(QPushButton(), 0, 0)
            self.grid_layout.addWidget(QPushButton(), 0, 1)
            self.grid_layout.addWidget(QPushButton(), 0, 2)
            self.grid_layout.addWidget(QPushButton(), 0, 3)
        elif shape_num == 4:
    
            self.grid_layout.addWidget(QPushButton(), 0, 1)
            self.grid_layout.addWidget(QPushButton(), 1, 1)
            self.grid_layout.addWidget(QPushButton(), 1, 0)
            self.grid_layout.addWidget(QPushButton(), 2, 0)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TetrisWindow()
    window.show()
    sys.exit(app.exec_())
