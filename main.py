import sys
from PyQt6 import QtWidgets
from tkinter import messagebox
from Utils.distance import Distance
from Utils.gas import Gas
from diesel import Diesel
from roady import Roady
from Utils.init_config import config
from roady_gui import Ui_MainWindow
import logging


LOGGER = logging .getLogger(__name__)
logging.basicConfig(level=logging.INFO,
					format="%(asctime)s- %(filename)s:%(lineno)d - %(levelname)s - %(message)s",
					datefmt="%d-%b-%Y-%H:%M:%S",
					handlers=[
						logging.FileHandler("app.log"),
						logging.StreamHandler()
					])


def is_input_checked():
	if ui.departure_city_lineEdit.text() and ui.destination_city_lineEdit.text():
		departure_city = ui.departure_city_lineEdit.text().capitalize()
		destination_city = ui.destination_city_lineEdit.text().capitalize()
		ui.departure_city_lineEdit.setText(departure_city)
		ui.destination_city_lineEdit.setText(destination_city)
		if ui.number_of_persons_lineEdit.text() and ui.consumption_lineEdit.text():
			if ui.number_of_persons_lineEdit.text().isnumeric() and ui.consumption_lineEdit.text().isnumeric():
				return True
			else:
				messagebox.showerror(title="Error" , message="Please input numbers for persons and consumption")
				LOGGER.error("Please input numbers for persons and consumption")
				return False
		else:
			messagebox.showerror(message="Please add number of persons and consumption")
			LOGGER.error("Please add number of persons and consumption")
			return False
	else:
		messagebox.showerror(title="Please enter cities")
		LOGGER.error("Please enter cities")
		return False




def calculate_price():
	if is_input_checked():

		dist = Distance(departure_city=ui.departure_city_lineEdit.text(),
						destination_city=ui.destination_city_lineEdit.text(),
						config=config)

		if ui.fuel_type_comboBox.currentTex() == "Gas":
			gas_price = Gas(config)
		elif ui.fuel_type_comboBox.currentText() == "Diesel":
			diesel_price = Diesel(config)
		else:
			messagebox.showerror(title="Error", message="Please select a fuel type")
			return



		roady = Roady(dist, gas_price)

		price = roady.calculate_price(int(ui.number_of_persons_lineEdit.text()),
									  float(ui.consumption_lineEdit.text()),
									  ui.with_returrn_radioButton.isChecked(),
									  ui.currency_comboBox.currentText())
		#QMessageBox.information(parent=ui, title="Pret de Persoana", text=f"Pretul calculat este de {int(price)}")
		messagebox.showinfo(title="Pret calculat", message=f"Fiecare persoana are de platit {int(price)}")
		LOGGER.info(f"Fiecare persoana are de platit {int(price)}")


		#print(ui.departure_city_lineEdit.text())





if __name__ == '__main__':

	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	ui = Ui_MainWindow()
	ui.setupUi(MainWindow)
	ui.calculate_btn.clicked.connect(calculate_price)
	MainWindow.show()
	sys.exit(app.exec())












