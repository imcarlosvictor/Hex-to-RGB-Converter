import sys
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout, QLabel


class HexCodeConverter(QDialog):
    def __init__(self, parent=None):
        super(HexCodeConverter, self).__init__(parent)
        self.setWindowTitle('Hex Code Converter')

        # Create widgets
        self.user_input = QLineEdit()
        self.user_input.setPlaceholderText('Enter hex code')
        self.button = QPushButton('Convert to rgb')
        self.label = QLabel()

        # Create layout and add widgets
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.user_input)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.label)

        # Add functionality to button slot
        rgb_code = self.button.clicked.connect(lambda: self.hex_in_rgb(self.user_input.text()))


    def hex_in_rgb(self, code) -> str:
        """Converts hex code (Base16) to RGB (Base 10).

        Args:
        hex code (str): Hex code of colour.

        Returns:
            str: Hex code in RGB format.
            """

        primary_hex_value: int = 0
        rgb = []

        for index, value in enumerate(code):
            if value == '#':
                pass
            elif index % 2 != 0:
                # ODD: Convert primary value (base16 -> base10)
                rgb_base10 = int(value, 16)
                result = rgb_base10 * 16
                primary_hex_value = result
            elif index % 2 == 0:
                # EVEN: Convert secondary value (base16 -> base10)
                value_in_base10 = int(value, 16)
                # Add to primary key
                result = primary_hex_value + value_in_base10
                rgb.append(result)

        rgb_values = f"rgb({', '.join(list(map(str, rgb)))})"

        # Update label with rgb values
        self.label.setText(rgb_values)

        return rgb_values


if __name__ == '__main__':
    # Create application
    app = QApplication(sys.argv)
    # Create form
    form = HexCodeConverter()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())