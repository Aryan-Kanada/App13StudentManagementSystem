from PyQt6.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QLineEdit, QPushButton, QComboBox
import sys


class AverageSpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()  #USE () wiht super
        self.setWindowTitle("Average Speed Calculator")
        grid = QGridLayout() # USE ()

        # Create Widget
        distance_label = QLabel("Distance:")
        self.distance_line_edit = QLineEdit()

        time_label = QLabel("Time(hours):")
        self.time_line_edit = QLineEdit()

        self.combo = QComboBox()
        self.combo.addItems(['Kilometer', 'Miles'])


        calulate_button = QPushButton("Calculate")
        calulate_button.clicked.connect(self.calculation)
        self.output_lable = QLabel("")


        # Add Widget to grid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)

        grid.addWidget(self.combo, 0, 2)

        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)

        grid.addWidget(calulate_button, 2, 1)

        grid.addWidget(self.output_lable, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculation(self):
        #Get the Distance and time value
        distance = float(self.distance_line_edit.text())
        time = float(self.time_line_edit.text())

        #Average Speed
        speed = distance / time

        # Select from Combo
        if self.combo.currentText() == "Kilometer":
            speed = round(speed, 2)
            unit = "km/hr"

        if self.combo.currentText() == "Miles":
            speed = round(speed * 0.621371, 2)
            unit = "mph"

        self.output_lable.setText(f"Average Speed: {speed} {unit} ")


app = QApplication(sys.argv)
speed_calculator = AverageSpeedCalculator() #use ()
speed_calculator.show()
sys.exit(app.exec())