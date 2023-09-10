import sys
import random

from PyQt5.QtWidgets import QApplication, QMainWindow
from QuotesUI import Ui_MainWindow


class QuoteGeneratorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.generate_quote)
        
        

    def generate_quote(self):

        self.ui.pushButton.setText("Refresh")

        file = open("Quotes.txt", "r")
        content = file.readlines()
       
        quotes = content
        random_quote = random.choice(quotes)
        self.ui.label.setText(random_quote)
        file.close()



def main():
    app = QApplication(sys.argv)
    window = QuoteGeneratorApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()






