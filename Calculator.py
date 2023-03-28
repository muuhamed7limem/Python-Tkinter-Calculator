from tkinter import *

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.display = Entry(master, width=35, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        self.button_1 = Button(master, text="1", padx=40, pady=20, command=lambda: self.button_click(1))
        self.button_2 = Button(master, text="2", padx=40, pady=20, command=lambda: self.button_click(2))
        self.button_3 = Button(master, text="3", padx=40, pady=20, command=lambda: self.button_click(3))
        self.button_4 = Button(master, text="4", padx=40, pady=20, command=lambda: self.button_click(4))
        self.button_5 = Button(master, text="5", padx=40, pady=20, command=lambda: self.button_click(5))
        self.button_6 = Button(master, text="6", padx=40, pady=20, command=lambda: self.button_click(6))
        self.button_7 = Button(master, text="7", padx=40, pady=20, command=lambda: self.button_click(7))
        self.button_8 = Button(master, text="8", padx=40, pady=20, command=lambda: self.button_click(8))
        self.button_9 = Button(master, text="9", padx=40, pady=20, command=lambda: self.button_click(9))
        self.button_0 = Button(master, text="0", padx=40, pady=20, command=lambda: self.button_click(0))
        self.button_add = Button(master, text="+", padx=39, pady=20, command=self.button_add)
        self.button_subtract = Button(master, text="-", padx=41, pady=20, command=self.button_subtract)
        self.button_multiply = Button(master, text="*", padx=40, pady=20, command=self.button_multiply)
        self.button_divide = Button(master, text="/", padx=41, pady=20, command=self.button_divide)
        self.button_clear = Button(master, text="Clear", padx=79, pady=20, command=self.button_clear)
        self.button_equal = Button(master, text="=", padx=91, pady=20, command=self.button_equal)

        self.button_1.grid(row=3, column=0)
        self.button_2.grid(row=3, column=1)
        self.button_3.grid(row=3, column=2)

        self.button_4.grid(row=2, column=0)
        self.button_5.grid(row=2, column=1)
        self.button_6.grid(row=2, column=2)

        self.button_7.grid(row=1, column=0)
        self.button_8.grid(row=1, column=1)
        self.button_9.grid(row=1, column=2)

        self.button_0.grid(row=4, column=0)
        self.button_clear.grid(row=4, column=1, columnspan=2)
        self.button_add.grid(row=5, column=0)
        self.button_equal.grid(row=5, column=1, columnspan=2)

        self.button_subtract.grid(row=6, column=0)
        self.button_multiply.grid(row=6, column=1)
        self.button_divide.grid(row=6, column=2)

    def button_click(self, number):
        current = self.display.get()
        self.display.delete(0, END)
        self.display.insert(0, str(current) + str(number))

    def button_clear(self):
        self.display.delete(0, END)

    def button_add(self):
        first_number = self.display.get()
        global f_num
        global math
        math = "addition"
        f_num = int(first_number)
        self.display.delete(0, END)

    def button_subtract(self):
        first_number = self.display.get()
        global f_num
        global math
        math = "subtraction"
        f_num = int(first_number)
        self.display.delete(0, END)

    def button_multiply(self):
        first_number = self.display.get()
        global f_num
        global math
        math = "multiplication"
        f_num = int(first_number)
        self.display.delete(0, END)

    def button_divide(self):
        first_number = self.display.get()
        global f_num
        global math
        math = "division"
        f_num = int(first_number)
        self.display.delete(0, END)

    def button_equal(self):
        second_number = self.display.get()
        self.display.delete(0, END)

        if math == "addition":
            self.display.insert(0, f_num + int(second_number))

        if math == "subtraction":
            self.display.insert(0, f_num - int(second_number))

        if math == "multiplication":
            self.display.insert(0, f_num * int(second_number))

        if math == "division":
            self.display.insert(0, f_num / int(second_number))

root = Tk()
calculator = Calculator(root)
root.mainloop()