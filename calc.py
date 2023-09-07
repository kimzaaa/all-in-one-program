import PyQt5.QtWidgets as qtw
import sys


class Mainwin(
    qtw.QWidget
):  # creating class will inherit from qwidget and it will perform all the elements
    def __init__(self):
        super().__init__()  # needed to make it func propperly

        self.setWindowTitle("Calculator")  # this creates a title for the app

        self.setLayout(qtw.QVBoxLayout())  # creates a grid latout
        self.keypad()
        self.temp_nums = []  # creates 2 empty lists and a variable
        self.fin_nums = []
        # btn1 = qtw.QPushButton('test') #creates a button
        # self.layout().addWidget(btn1) #makes the widget shown in the window
        self.setGeometry(0, 0, 300, 600)  # set screen dimentions

        self.show()  # obj will create after the main window class

    def keypad(self):  # the GUI stuffs
        container = qtw.QWidget()  # this will hold all the other elements
        container.setLayout(qtw.QGridLayout())  # creates emppty container
        # now we need to connect the main window and the empty container together

        # button lists
        rf = (
            self.result_field
        ) = (
            qtw.QLineEdit()
        )  # it will displays the text and put it in a variable called result_field
        btn_result = qtw.QPushButton("Result", clicked=self.func_result)
        btn_clear = qtw.QPushButton("Clear", clicked=self.clear_calc)
        btn_9 = qtw.QPushButton("9", clicked=lambda: self.num_press("9"))
        btn_8 = qtw.QPushButton("8", clicked=lambda: self.num_press("8"))
        btn_7 = qtw.QPushButton("7", clicked=lambda: self.num_press("7"))
        btn_6 = qtw.QPushButton("6", clicked=lambda: self.num_press("6"))
        btn_5 = qtw.QPushButton("5", clicked=lambda: self.num_press("5"))
        btn_4 = qtw.QPushButton("4", clicked=lambda: self.num_press("4"))
        btn_3 = qtw.QPushButton("3", clicked=lambda: self.num_press("3"))
        btn_2 = qtw.QPushButton("2", clicked=lambda: self.num_press("2"))
        btn_1 = qtw.QPushButton("1", clicked=lambda: self.num_press("1"))
        btn_0 = qtw.QPushButton("0", clicked=lambda: self.num_press("0"))
        btn_plus = qtw.QPushButton("+", clicked=lambda: self.func_press("+"))
        btn_mins = qtw.QPushButton("-", clicked=lambda: self.func_press("-"))
        btn_mult = qtw.QPushButton("*", clicked=lambda: self.func_press("*"))
        btn_divd = qtw.QPushButton("/", clicked=lambda: self.func_press("/"))
        # the rest are plain buttons

        # setting button geometry
        btn_9.setFixedSize(100, 100)
        btn_8.setFixedSize(100, 100)
        btn_7.setFixedSize(100, 100)
        btn_6.setFixedSize(100, 100)
        btn_5.setFixedSize(100, 100)
        btn_4.setFixedSize(100, 100)
        btn_3.setFixedSize(100, 100)
        btn_2.setFixedSize(100, 100)
        btn_1.setFixedSize(100, 100)
        btn_0.setFixedSize(315, 100)
        btn_plus.setFixedSize(100, 100)
        btn_mins.setFixedSize(100, 100)
        btn_mult.setFixedSize(100, 100)
        btn_divd.setFixedSize(100, 100)
        btn_result.setFixedSize(205, 100)
        btn_clear.setFixedSize(205, 100)

        # adding buttons to the layout
        container.layout().addWidget(
            self.result_field, 0, 0, 1, 4
        )  # self is to touch the result field with the widgets inside it
        container.layout().addWidget(btn_result, 1, 0, 1, 2)
        container.layout().addWidget(btn_clear, 1, 2, 1, 2)
        container.layout().addWidget(btn_9, 2, 0)
        container.layout().addWidget(btn_8, 2, 1)
        container.layout().addWidget(btn_7, 2, 2)
        container.layout().addWidget(btn_plus, 2, 3)
        container.layout().addWidget(btn_6, 3, 0)
        container.layout().addWidget(btn_5, 3, 1)
        container.layout().addWidget(btn_4, 3, 2)
        container.layout().addWidget(btn_mins, 3, 3)
        container.layout().addWidget(btn_3, 4, 0)
        container.layout().addWidget(btn_2, 4, 1)
        container.layout().addWidget(btn_1, 4, 2)
        container.layout().addWidget(btn_mult, 4, 3)
        container.layout().addWidget(btn_0, 5, 0, 1, 3)
        container.layout().addWidget(btn_divd, 5, 3)
        self.layout().addWidget(container)  # puts the widget in the main window
        # how the num works?
        # ex: 1,3,4,1 : the first num = row second num = column the final 2 (4,1) means 4 high and 1 length

    def num_press(self, key_number):
        self.temp_nums.append(key_number)
        temp_string = "".join(self.temp_nums)
        if self.fin_nums:
            self.result_field.setText("".join(self.fin_nums) + temp_string)
        else:
            self.result_field.setText(temp_string)

    def func_press(self, operator):
        temp_strings = "".join(self.temp_nums)
        self.fin_nums.append(temp_strings)
        self.fin_nums.append(operator)
        self.temp_nums = []
        self.result_field.setText("".join(self.fin_nums))

    def func_result(self):
        fin_string = "".join(self.fin_nums) + "".join(self.temp_nums)
        result_string = eval(fin_string)
        fin_string += "="
        fin_string += str(result_string)
        self.result_field.setText(fin_string)

    def clear_calc(self):
        self.result_field.clear()
        self.temp_nums = []
        self.fin_nums = []


app = qtw.QApplication([])  # creates a QApp which will tracks the application code
mainwind = Mainwin()  # create an object which in this case is an empty window
app.setStyle(qtw.QStyleFactory.create("Fusion"))  # set theme fusion
app.exec_()  # tells python to run the app
# all of this will create a window
