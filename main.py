# This is just for the UI portion
from PyQt5 import QtCore, QtGui, QtWidgets
import numpy as np
import sys
import solver
import ui
class SudokuSolver(QtWidgets.QMainWindow, ui.Ui_MainWindow):
    def __init__(self, parent=None):
        super(SudokuSolver, self).__init__(parent)
        self.setupUi(self)
        self.solveButton.clicked.connect(self.solve)
        self.clearButton.clicked.connect(self.clearArray)
        self.solver = solver.Solver()
    def buildArray(self):
        grid = []
        cellCount = 1
        for i in range(0,9):
            grid.append([])
            for j in range(0,9):
                widget = self.findChild(QtWidgets.QTextEdit, f"text{cellCount}")
                value = widget.toPlainText()
                if value == "":
                    grid[i].append(0)
                else:
                    grid[i].append(int(value))
                cellCount += 1
        grid = np.array(grid)
        return grid
    def displayArray(self, grid):
        cellCount = 1
        for i in range(0,9):
            for j in grid[i]:
                value = str(j)
                widget = self.findChild(QtWidgets.QTextEdit, f"text{cellCount}")
                widget.setPlainText(value)
                widget.setAlignment(QtCore.Qt.AlignCenter)
                cellCount += 1
    def clearArray(self):
        cellCount = 1
        for i in range(0,9):
            for j in range(0,9):
                widget = self.findChild(QtWidgets.QTextEdit, f"text{cellCount}")
                widget.setPlainText('')
                widget.setAlignment(QtCore.Qt.AlignCenter)
                cellCount += 1
    def solve(self):
        print("Solving...")
        grid = self.buildArray()
        self.solveButton.setEnabled(False)
        self.clearButton.setEnabled(False)
        solvedGrid = self.solver.solve(grid)
        self.displayArray(solvedGrid)
        self.solveButton.setEnabled(True)
        self.clearButton.setEnabled(True)
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = SudokuSolver()
    window.show()
    app.exec_()
if __name__ == '__main__':
    main()