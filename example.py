import sys
from datetime import datetime
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QGridLayout


class AgeCalculator(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()

        # Create Widget
        name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()

        date_label = QLabel("Date of Birth DD/MM/YYYY:")
        self.date_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.calculate_age)
        self.output_label = QLabel("")

        # Add widgets to grid
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_label, 1, 0)
        grid.addWidget(self.date_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calculate_age(self):
        current_year = datetime.now().year
        date_of_birth = self.date_line_edit.text()
        year_of_birth = datetime.strptime(date_of_birth, "%d/%m/%Y").date().year
        current_age = current_year - year_of_birth
        self.output_label.setText(f"{self.name_line_edit.text()} is {current_age} years old")


app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())

