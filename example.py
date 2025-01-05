import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QGridLayout


class AgeCalculator(QWidget):

    def __init__(self):
        super().__init__()
        grid = QGridLayout()

        # Create Widget
        name_lable = QLabel("Name:")
        name_line_edit = QLineEdit()

        date_lable = QLabel("Date of Birth DD/MM/YY:")
        date_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate")
        output_lable = QLabel("")

        # Add widgets to grid
        grid.addWidget(name_lable, 0, 0)
        grid.addWidget(name_line_edit, 0, 1)
        grid.addWidget(date_lable, 1, 0)
        grid.addWidget(date_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(output_lable, 3, 0, 1, 2)

        self.setLayout(grid)


app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())

