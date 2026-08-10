from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QVBoxLayout, QHBoxLayout, QLabel, QMessageBox, QCheckBox, QRadioButton, QComboBox, QListWidget
import json

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.v_main_lay = QVBoxLayout()
        self.h_jins_lay = QHBoxLayout()
        self.h_viloyat_lay = QHBoxLayout()
        self.h_tuman_lay = QHBoxLayout()
        self.btn_lay = QHBoxLayout()

        self.setStyleSheet("font-size: 20px")


        self.lbl_information = QLabel("INFORMATION")
        self.lbl_information.setStyleSheet("font-size: 22px")
        self.lbl_information.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
    
        self.edit_name = QLineEdit()
        self.edit_name.setPlaceholderText("ism....")
        self.edit_second = QLineEdit()
        self.edit_second.setPlaceholderText("familiya....")
        self.edit_age = QLineEdit()
        self.edit_age.setPlaceholderText("yosh....")

        self.lbl_jins = QLabel("Jins: ")
        self.radio_b_male = QRadioButton("Erkak")
        self.radio_b_male.setChecked(True)
        self.radio_b_female = QRadioButton("Ayol")

        self.lbl_viloyat = QLabel("Viloyat: ")
        self.cmb_viloyat = QComboBox()
        self.cmb_viloyat.addItems(["Andijon", "Buxoro", "Farg'ona", "Jizzax", "Namangan", "Navoiy", "Qashqadaryo", "Samarqand", "Sirdaryo", "Surxondaryo", "Toshkent shahri", "Toshkent viloyati", "Xorazm"])
        self.cmb_viloyat.activated[str].connect(self.Tuman)
        self.lbl_tuman = QLabel("Shaxar: ")
        self.cmb_tuman = QComboBox()

        self.btn_submit = QPushButton("SUBMIT")
        self.btn_submit.clicked.connect(self.Submit)
        self.btn_exit = QPushButton("EXIT")
        self.btn_exit.clicked.connect(exit)

        self.h_jins_lay.addWidget(self.lbl_jins)
        self.h_jins_lay.addWidget(self.radio_b_male)
        self.h_jins_lay.addWidget(self.radio_b_female)

        self.h_viloyat_lay.addWidget(self.lbl_viloyat)
        self.h_viloyat_lay.addWidget(self.cmb_viloyat)

        self.h_tuman_lay.addWidget(self.lbl_tuman)
        self.h_tuman_lay.addWidget(self.cmb_tuman)

        self.btn_lay.addWidget(self.btn_submit)
        self.btn_lay.addWidget(self.btn_exit)

        self.v_main_lay.addWidget(self.lbl_information)
        self.v_main_lay.addWidget(self.edit_name)
        self.v_main_lay.addWidget(self.edit_second)
        self.v_main_lay.addWidget(self.edit_age)

        self.v_main_lay.addLayout(self.h_jins_lay)
        self.v_main_lay.addLayout(self.h_viloyat_lay)
        self.v_main_lay.addLayout(self.h_tuman_lay)
        self.v_main_lay.addLayout(self.btn_lay)

        self.setLayout(self.v_main_lay)


    def Tuman(self, obj):
        self.cmb_tuman.clear()
        self.cmb_tuman.setSizeAdjustPolicy(self.cmb_tuman.AdjustToContents)
        self.dct = {
    "Andijon": [
        "Andijon", "Asaka", "Baliqchi", "Bo'ston", "Buloqboshi", 
        "Izboskan", "Jalaquduq", "Marhamat", "Oltinko'l", "Paxtaobod", 
        "Shahrixon", "Ulug'nor", "Xo'jaobod"
    ],
    "Buxoro": [
        "Buxoro", "G'ijduvon", "Jondor", "Kogon", "Olot", "Peshku",
        "Qorako'l", "Qorovulbozor", "Romitan", "Shofirkon", "Vobkent"
    ],
    "Farg'ona": [
        "Bag'dod", "Beshariq", "Buvayda", "Dang'ara", "Farg'ona", 
        "Oltiariq", "O'zbekiston", "Qo'shtepa", "Quva", "Rishton", 
        "So'x", "Toshloq", "Uchko'prik", "Yozyovon"
    ],
    "Jizzax": [
        "Arnasoy", "Baxmal", "Do'stlik", "Forish", "G'allaorol", 
        "Mirzacho'l", "Paxtakor", "Sharof Rashidov", "Yangiobod", 
        "Zafarobod", "Zarbdor", "Zomin"
    ],
    "Namangan": [
        "Chortoq", "Chust", "Kosonsoy", "Mingbuloq", "Namangan", 
        "Norin", "Pop", "To'raqo'rg'on", "Uchqo'rg'on", "Uychi", "Yangiqo'rg'on"
    ],
    "Navoiy": [
        "Karmana", "Konimex", "Navbahor", "Nurota", "Qiziltepa", 
        "Tomdi", "Uchquduq", "Xatirchi"
    ],
    "Qashqadaryo": [
        "Chiroqchi", "Dehqonobod", "G'uzor", "Kasbi", "Kitob", 
        "Koson", "Ko'kdala", "Mirishkor", "Muborak", "Nishon", 
        "Qamashi", "Qarshi", "Shahrisabz", "Yakkabog'"
    ],
    "Samarqand": [
        "Bulung'ur", "Ishtixon", "Jomboy", "Kattaqo'rg'on", "Narpay", 
        "Nurobod", "Oqdaryo", "Pastdarg'om", "Paxtachi", "Payariq", 
        "Qo'shrabot", "Samarqand", "Toyloq", "Urgut"
    ],
    "Sirdaryo": [
        "Boyovut", "Guliston", "Mirzaobod", "Oqoltin", "Sardoba", 
        "Sayxunobod", "Sirdaryo", "Xovos"
    ],
    "Surxondaryo": [
        "Angor", "Bandixon", "Boysun", "Denov", "Jarqo'rg'on", 
        "Muzrabot", "Oltinsoy", "Qiziriq", "Qumqo'rg'on", "Sariosiyo", 
        "Sherobod", "Sho'rchi", "Termiz", "Uzun"
    ],
    "Toshkent viloyati": [
        "Bekobod", "Bo'ka", "Bo'stonliq", "Chinoz", "Ohangaron", 
        "Olmaliq", "Oqqo'rg'on", "O'rtachirchiq", "Parkent", "Pskent", 
        "Qibray", "Toshkent", "Yangiqo'rg'on", "Yuqori Chirchiq", "Zangiota"
    ],
    "Xorazm": [
        "Bog'ot", "Gurlan", "Hazorasp", "Xiva", "Xonqa", 
        "Qo'shko'pir", "Shovot", "Tuproqqal'a", "Urganch", "Yangiariq", "Yangibozor"
    ],
    "Toshkent shahri": [
        "Bektemir", "Chilonzor", "Mirobod", "Mirzo Ulug'bek", "Olmazor", 
        "Sergeli", "Shayxontohur", "Uchtepa", "Yakkasaroy", "Yangi Hayot", 
        "Yashnobod", "Yunusobod"
    ]
}
        self.cmb_tuman.addItems(self.dct[obj])

    def Submit(self):
        name = self.edit_name.text().capitalize()
        second = self.edit_second.text().capitalize()
        age = self.edit_age.text()
        if age.isdigit():
            age = int(age)

            if self.radio_b_male.isChecked():
                jins = self.radio_b_male.text()
            else:
                jins = self.radio_b_female.text()
            viloyat = self.cmb_viloyat.currentText()
            tuman = self.cmb_tuman.currentText()


            if name and second and age and tuman:
                self.edit_name.clear()
                self.edit_second.clear()
                self.edit_age.clear()
                if self.radio_b_female.isChecked():
                    self.radio_b_male.setChecked(True)
                self.cmb_viloyat.setCurrentIndex(0)
                self.cmb_tuman.clear()

                with open("test.json", "r+") as f:
                    data = json.load(f)
                    data.append({"Ism": name, "Famailiya": second, "Yosh": age, "Jinsi": jins, "Viloyat": viloyat, "Tuman": tuman})
                    f.seek(0)
                    json.dump(data, f, indent = 4)
            else:
                QMessageBox.warning(self, "Ogohlantirish!", "Barcha maydonlar to'ldirilgan bo'lishi kerak!")
        else:
            QMessageBox.warning(self, "Ogohlantirish", "Yosh qismiga son kiritmadingiz!")

app = QApplication([])
win = MyWindow()
win.show()
app.exec_()