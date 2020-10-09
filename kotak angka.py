from PyQt5.QtWidgets import*
from PyQt5.QtGui import*
import sys

def window():
    app = QApplication(sys.argv)
    window = QWidget()
    layout = QHBoxLayout()
    
    #set label pada window
    labelku = QLabel(window)
    labelku.setText('kotak angka :')
    labelku.setFont(QFont('Arial', 12))
    labelku.move(20, 0)

    #set button pertama pada window
    button1 = QPushButton(window)
    button1.setText('1')
    button1.move(20,20)
    button1.setFont(QFont('Sledge', 24))
    button1.setStyleSheet('background-color: cyan; color:red')

    #set button kedua pada window
    button2 = QPushButton(window)
    button2.setText('2')
    button2.move(100,20)
    button2.setFont(QFont('Sledge', 24))
    button2.setStyleSheet('background-color: cyan; color:red')

    #set button ketiga pada window
    button3 = QPushButton(window)
    button3.setText('3')
    button3.move(180,20)
    button3.setFont(QFont('Sledge', 24))
    button3.setStyleSheet('background-color: cyan; color:red')
    
    #set button keempat pada window
    button4 = QPushButton(window)
    button4.setText('4')
    button4.move(260,20)
    button4.setFont(QFont('Sledge', 24))
    button4.setStyleSheet('background-color: cyan; color:red')
    
    #set button kelima pada window
    button5 = QPushButton(window)
    button5.setText('5')
    button5.move(340,20)
    button5.setFont(QFont('Sledge', 24))
    button5.setStyleSheet('background-color: cyan; color:red')

    window.setGeometry(400,100,700,500)
    window.setWindowTitle('PyQt5 Example')
    window.show()
    sys.exit(app.exec_())


if __name__=='__main__':
    window()
