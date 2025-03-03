# This Python file uses the following encoding: utf-8
import sys
from data import density, dataset_town, dataset_temperature
from maths import calc_Button

from PySide6.QtWidgets import QApplication, QMainWindow

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.dict_density = density
        self.dict_town = dataset_town
        self.dict_temperature = dataset_temperature

        self.ui.comboBox.addItems(map(lambda x: x, self.dict_density.keys()))
        self.ui.comboBox.setCurrentIndex(16)
        self.ui.comboBox.activated.connect(self.update_temperature_in)
        self.ui.comboBox.activated.connect(self.update_answer)

        self.ui.comboBox_2.addItems(map(lambda x: x, self.dict_town.keys()))
        self.ui.comboBox_2.activated.connect(self.update_comboBox_3)
        self.ui.comboBox_2.activated.connect(self.update_label_6)
        self.ui.comboBox_2.activated.connect(self.update_answer)

        self.ui.comboBox_3.activated.connect(self.update_label_6)
        self.ui.comboBox_3.activated.connect(self.update_answer)

        self.ui.lineEdit.editingFinished.connect(self.update_answer)

        self.ui.pushButton.clicked.connect(self.update_answer)

        self.update_temperature_in()
        self.update_comboBox_3()
        self.update_label_6()

    def update_comboBox_3(self):
        if self.ui.comboBox_3.count() != 0:
            for _ in list(range(0, self.ui.comboBox_3.count())):
                self.ui.comboBox_3.removeItem(0)
        self.ui.comboBox_3.addItems(filter(lambda x: str(x) != '-', list(self.dict_town[self.ui.comboBox_2.currentText()].values())))

    def update_label_6(self):
        text = self.dict_temperature[self.ui.comboBox_2.currentText()][self.ui.comboBox_3.currentIndex()]
        self.temp_out = text
        self.ui.label_6.setText(str(text))

    def update_temperature_in(self):
        self.temp_in = self.ui.comboBox.currentIndex() + 5
        self.density_t = list(self.dict_density.values())[self.ui.comboBox.currentIndex()]

    def update_answer(self):
        if (self.ui.lineEdit.text() != ''):
            self.air_flow = int(self.ui.lineEdit.text())
            self.ui.label_18.setText(calc_Button(self.air_flow, self.temp_in, self.temp_out, self.density_t))
        else:
            self.ui.lineEdit.setText('0')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
