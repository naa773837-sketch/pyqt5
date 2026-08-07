from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton,QVBoxLayout,QHBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.v_main_lay = QVBoxLayout()
        self.h_7_8_9_taqsim = QHBoxLayout()
        self.h_4_5_6_kopaytiruv = QHBoxLayout()
        self.h_1_2_3_minus = QHBoxLayout()
        self.h_clear_0_backspace_plus = QHBoxLayout()

        self.lbl = QLabel("0")
        self.lbl.setStyleSheet("color:blue; font size:24px;")

        self.btn_7 = QPushButton("7")
        self.btn_7.clicked.connect(self.Yetti)

        self.btn_8 = QPushButton("8")
        self.btn_8.clicked.connect(self.Sakkiz)
        self.btn_9 = QPushButton("9")
        self.btn_9.clicked.connect(self.Toqqiz)

        self.btn_taqsim = QPushButton("\u00F7")
        self.btn_taqsim.clicked.connect(self.Taqsim)


        self.btn_4 = QPushButton("4")
        self.btn_4.clicked.connect(self.Tort)
        
        self.btn_5 = QPushButton("5")
        self.btn_5.clicked.connect(self.Besh)
        
        self.btn_6 = QPushButton("6")
        self.btn_6.clicked.connect(self.Olti)

        self.btn_kopaytiruv = QPushButton("\u00D7")
        self.btn_kopaytiruv.clicked.connect(self.Kopaytiruv)


        self.btn_1 = QPushButton("1")
        self.btn_1.clicked.connect(self.Bir)

        self.btn_2 = QPushButton("2")
        self.btn_2.clicked.connect(self.Ikki)

        self.btn_3 = QPushButton("3")
        self.btn_3.clicked.connect(self.Uch)

        self.btn_minus = QPushButton("\u2212")
        self.btn_minus.clicked.connect(self.Minus)


        self.btn_clear = QPushButton("C")
        self.btn_clear.clicked.connect(self.Clear)

        self.btn_0 = QPushButton("0")
        self.btn_0.clicked.connect(self.Nol)

        self.btn_backspace = QPushButton("\u232B")
        self.btn_backspace.clicked.connect(self.Backspace)

        self.btn_plus = QPushButton("\u002B")
        self.btn_plus.clicked.connect(self.Plus)

        self.btn_teng = QPushButton(" = ")
        self.btn_teng.clicked.connect(self.Teng)

        self.h_7_8_9_taqsim.addWidget(self.btn_7)
        self.h_7_8_9_taqsim.addWidget(self.btn_8)
        self.h_7_8_9_taqsim.addWidget(self.btn_9)
        self.h_7_8_9_taqsim.addWidget(self.btn_taqsim)

        self.h_4_5_6_kopaytiruv.addWidget(self.btn_4)
        self.h_4_5_6_kopaytiruv.addWidget(self.btn_5)
        self.h_4_5_6_kopaytiruv.addWidget(self.btn_6)
        self.h_4_5_6_kopaytiruv.addWidget(self.btn_kopaytiruv)

        self.h_1_2_3_minus.addWidget(self.btn_1)
        self.h_1_2_3_minus.addWidget(self.btn_2)
        self.h_1_2_3_minus.addWidget(self.btn_3)
        self.h_1_2_3_minus.addWidget(self.btn_minus)

        self.h_clear_0_backspace_plus.addWidget(self.btn_clear)
        self.h_clear_0_backspace_plus.addWidget(self.btn_0)
        self.h_clear_0_backspace_plus.addWidget(self.btn_backspace)
        self.h_clear_0_backspace_plus.addWidget(self.btn_plus)

        self.v_main_lay.addWidget(self.lbl)
        self.v_main_lay.addLayout(self.h_7_8_9_taqsim)
        self.v_main_lay.addLayout(self.h_4_5_6_kopaytiruv)
        self.v_main_lay.addLayout(self.h_1_2_3_minus)
        self.v_main_lay.addLayout(self.h_clear_0_backspace_plus)
        self.v_main_lay.addWidget(self.btn_teng)

        self.setLayout(self.v_main_lay)
        self.first_num = None
        self.operation = None
        self.is_new_num = True

    def Nol(self):
        hozirgi_text  = self.lbl.text()
        if self.is_new_num:
            self.lbl.setText("0")
            self.is_new_num = False
        elif hozirgi_text != "0":
            self.lbl.setText(hozirgi_text+"0")


    def Bir(self):
        hozirgi_text = self.lbl.text()

        if self.is_new_num or hozirgi_text == "0":
            self.lbl.setText("1")
            self.is_new_num = False
        else:
            self.lbl.setText(hozirgi_text+"1")
             

    def Ikki(self):
        if self.is_new_num or self.lbl.text() == "0":
            self.lbl.setText("2")
            self.is_new_num = False
        else:
            self.lbl.setText(self.lbl.text()+"2")

    def Uch(self):
        if self.is_new_num or self.lbl.text() == "0":
            self.lbl.setText("3")
            self.is_new_num = False
        else:
            self.lbl.setText(self.lbl.text()+"3")

    def Tort(self):
        if self.is_new_num or self.lbl.text() == "0":
            self.lbl.setText("4")
            self.is_new_num = False
        else:
            self.lbl.setText(self.lbl.text()+"4")

    def Besh(self):
        if self.is_new_num or self.lbl.text() == "0":
            self.lbl.setText("5")
            self.is_new_num = False
        else:
            self.lbl.setText(self.lbl.text()+"5")

    def Olti(self):
        if self.is_new_num or self.lbl.text() == "0":
            self.lbl.setText("6")
            self.is_new_num = False
        else:
            self.lbl.setText(self.lbl.text()+"6")

    def Yetti(self):
        if self.is_new_num or self.lbl.text() == "0":
            self.lbl.setText("7")
            self.is_new_num = False
        else:
            self.lbl.setText(self.lbl.text()+"7")

    def Sakkiz(self):
        if self.is_new_num or self.lbl.text() == "0":
            self.lbl.setText("8")
            self.is_new_num = False
        else:
            self.lbl.setText(self.lbl.text()+"8")

    def Toqqiz(self):
        if self.is_new_num or self.lbl.text() == "0":
            self.lbl.setText("9")
            self.is_new_num = False
        else:
            self.lbl.setText(self.lbl.text()+"9")

    def Clear(self):
        self.lbl.setText("0")
        self.first_num = None
        self.operation = None
        self.is_new_num = True

    def Backspace(self):
        if self.lbl.text() != "0":
            self.lbl.setText(self.lbl.text()[:-1])
        if self.lbl.text() == "":
            self.lbl.setText("0") 

    def Taqsim(self):
        self.first_num = float(self.lbl.text())
        self.operation = "/"
        self.is_new_num = True

    def Kopaytiruv(self):
        self.first_num = float(self.lbl.text())
        self.operation = "*"
        self.is_new_num = True

    def Minus(self):
        self.first_num = float(self.lbl.text())
        self.operation = "-"
        self.is_new_num = True

    def Plus(self):
        self.first_num = float(self.lbl.text())
        self.operation = "+"
        self.is_new_num = True
            

    def Teng(self):
        if self.first_num is not None and self.operation is not None:
            second_num = float(self.lbl.text())

            if self.operation == "+":
                natija = self.first_num + second_num
            elif self.operation == "-":
                natija = self.first_num - second_num
            elif self.operation == "*":
                natija = self.first_num * second_num
            elif self.operation == "/":
                if second_num != 0:
                    natija = self.first_num / second_num
                else:
                    natija = "Xatolik 0 ga bo'lib bo'lmaydi!"
            if natija == "Xatolik 0 ga bo'lib bo'lmaydi!":
                self.lbl.setStyleSheet("color:red;")
            else:
                self.lbl.setStyleSheet("color:green;")

            self.lbl.setText(str(natija))
            self.is_new_num = True

app = QApplication([])
win = MyWindow()
win.show()
app.exec_() 