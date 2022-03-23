from PyQt5.QtWidgets import QWidget, QLabel, QComboBox, QPushButton, QTableWidget, QTableWidgetItem, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPixmap
from main import paint_first_plot, paint_second_plot


class MainWidgetPart(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.label_plot = QLabel(self)
        self.label_plot.setStyleSheet('''
            min-width: 640px;
            min-height: 480px;
        ''')
        self.out_data = QTableWidget(self)
        self.out_data.setColumnCount(2)
        self.out_data.setRowCount(207)
        label_info = QLabel("Выберите из выпадающего списка данные для представления сведений:")
        self.combo = QComboBox(self)
        self.combo.addItems(["Количество позиций по каждой номенклатуре", "Количество позиций по каждой номенклатуре в процентах", "Количество позиций по каждой модели", "Количество позиций по каждой модели в процентах", "Распределение каждого поставщика в позициях", "Соотношение все позиции/позиции с этим поставщиком"])
        button_confirm = QPushButton("Ознакомиться")
        button_confirm.clicked.connect(self.show_data)
        hbox_1 = QHBoxLayout()
        hbox_1.addWidget(self.label_plot)
        hbox_1.addWidget(self.out_data)
        vbox_1 = QVBoxLayout()
        vbox_1.addLayout(hbox_1)
        hbox_2 = QHBoxLayout()
        hbox_2.addWidget(label_info)
        vbox_1.addLayout(hbox_2)
        hbox_3 = QHBoxLayout()
        hbox_3.addWidget(self.combo)
        vbox_1.addLayout(hbox_3)
        hbox_4 = QHBoxLayout()
        hbox_4.addWidget(button_confirm)
        vbox_1.addLayout(hbox_4)
        self.setLayout(vbox_1)
    
    def show_data(self):
        if self.combo.currentIndex() == 0:
            dict_of_percents = paint_first_plot()
            i = 0
            for _ in dict_of_percents:
                self.out_data.setItem(i, 0, QTableWidgetItem(_))
                self.out_data.setItem(i, 1, QTableWidgetItem(dict_of_percents[_] + "%"))
                i += 1
        elif self.combo.currentIndex() == 1:
            paint_second_plot()
        self.label_plot.setPixmap(QPixmap("assets/tmp/tmp_pic.png"))
        