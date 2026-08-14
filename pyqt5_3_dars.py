# --------------1-MISOL------------------------------
# def second_unique(nums:list):
#     unique_list = [i for i in nums if nums.count(i) == 1]
#     return -1 if len(unique_list) < 2 else -1 if unique_list == [] else unique_list[1]
# print(second_unique([7, 3, 5, 3, 7, 9, 11]))

# --------------2-MISOL------------------------------
# def missing_letter_index(nums:list)->int:
#     return [i for i in range(len(nums)+1) if i not in nums][0] if nums else -1

# --------------3-MISOL------------------------------
# def unique_phones(users:list):
#     return set([y for i in users for y in i["phones"]]) if users else set()

# --------------4-MISOL------------------------------
# def most_active_student(student:list)->str:
#     if student:
#         new = {i["name"]:i["subjects"] for i in student}
#         return max(new,key=lambda x:len(new[x]))
#     else:
#         return ""

# --------------5-MISOL------------------------------
# ---------------------1-SHART
# SELECT * FROM books ORDER BY borrow_date DESC;
# ---------------------2-SHART
# SELECT * FROM books ORDER BY dailly_price DESC LIMIT 3;
# ---------------------3-SHART
# SELECT * FROM books WHERE return_status = "not_returned";
# ---------------------4-SHART
# SELECT book_title as kitob_nomi, dailly_price as kunlik narxi FROM books WHERE dailly_price
# ---------------------5-SHART
# SELECT * FROM books WHERE days > 10;
# ---------------------6-SHART
# SELECT * FROM books ORDER BY days DESC LIMIT 1;
# ---------------------7-SHART
# SELECT * FROM books WHERE dailly_price > 30000;

# --------------6-MISOL------------------------------
# from PyQt5.QtWidgets import *
# import json

# class TaskManager(QWidget):
#     def __init__(self):
#         super().__init__()


#         self.setWindowTitle("Task Manager Lite")
#         self.setFixedSize(500,300)
#         self.setStyleSheet("font-size:18px")
#         self.v_main_lay = QVBoxLayout()

#         self.task_input = QLineEdit()
#         self.task_input.setPlaceholderText("Task nomi")
#         self.status_input = QLineEdit()
#         self.status_input.setPlaceholderText("Status (Done / Pending)")
#         self.search_input = QLineEdit()
#         self.search_input.setPlaceholderText("Qidiruv")

#         self.add_btn = QPushButton("Qo'shish")
#         self.add_btn.clicked.connect(self.Add)
#         self.search_btn = QPushButton("Qidirish")
#         self.search_btn.clicked.connect(self.Search)
#         self.total_btn = QPushButton("Umumiy son")
#         self.total_btn.clicked.connect(self.Total)

#         self.info_lbl = QLabel("Info: ")

#         self.v_main_lay.addWidget(self.task_input)
#         self.v_main_lay.addWidget(self.status_input)
#         self.v_main_lay.addWidget(self.search_input)
#         self.v_main_lay.addWidget(self.add_btn)
#         self.v_main_lay.addWidget(self.search_btn)
#         self.v_main_lay.addWidget(self.total_btn)
#         self.v_main_lay.addWidget(self.info_lbl)

#         self.setLayout(self.v_main_lay)

#     def Add(self):
#         task = self.task_input.text()
#         status = self.status_input.text()
#         if task and status:
#             if status.capitalize() == "Done" or status.capitalize() == "Pending":
#                 with open("task.json", "r+") as f:
#                     data = json.load(f)
#                     flag = False
#                     for i in data:
#                         if i["task"] == task.capitalize() and i["status"] == status.capitalize():
#                             flag = True
#                     if flag: 
#                         QMessageBox.information(self,"Info", "Bunaqa task mavjud")    
#                     else:
#                         data.append({"task": self.task_input.text().capitalize(), "status":self.status_input.text().capitalize()})
#                         f.seek(0)
#                         json.dump(data, f , indent = 4)
#                         self.task_input.clear()
#                         self.status_input.clear()
#                         QMessageBox.information(self, "Info", "Muvafaqqiyatli qo'shildi👌")
#                         self.info_lbl.setText(f"Jami tasklar soni: {len(data)}")
#             else:
#                 QMessageBox.information(self,"Info", "Status paneli (done / pending)dan boshqa so'zlar qabul qiinmaydi!")
#                 self.status_input.clear()
#         else:
#             QMessageBox.warning(self,"Xato", "Barcha maydonlarni to'ldiring!")


#     def Search(self):
#         if self.search_input.text():
#             search = self.search_input.text().capitalize()
#             self.search_input.clear()
#             with open("task.json") as f:
#                 data = json.load(f)
#                 topilganlar = []
#                 for i in data:
#                     if search in i.values():
#                         topilganlar.append(i)
#                 if topilganlar:
#                     natija = "\n".join(str(i) for i in topilganlar)
#                     QMessageBox.information(self,"Info",  f"\t{len(topilganlar)} ta task topildi!\n{natija}")        
#                 else:
#                     QMessageBox.information(self,"Info", "Bunaqa task mavjud emas")
#         else:
#             QMessageBox.warning(self,"Xato", "Qiduruv bo'limiga hech narsa kiritmadingiz!")

#     def Total(self):
#         with open("task.json") as f:
#             data = json.load(f)
#             self.info_lbl.setText(f"Jami tasklar soni: {len(data)}")
#             QMessageBox.information(self, "Info", f"Umumiy tasklar soni: {len(data)}")


# app = QApplication([])
# win = TaskManager()
# win.show()
# app.exec_()