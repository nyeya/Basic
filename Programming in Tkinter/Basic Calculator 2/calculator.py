#****************** THIS CODE IS WRITTEN BY NYEYA *********
#************ FEEL FREE TO USE THIS CODE FOR YOUR OWN PURPOSE
#********* OR FOR YOUR PROJECT WORKS
#******              HAPPY CODING       ****

import tkinter as tk


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Nyeya Calculator")
        self.resizable(width=False,height=False)
        
        # create an entry field for the input and set its width
        self.display_box = tk.Entry(self, width=40, borderwidth=5)
        self.display_box.grid(row=0, column=0, columnspan=4, padx=10,ipady=10, pady=10)

        # create buttons for the calculator
        self.btn_1 = tk.Button(self, text="1",bg="black",fg="white", padx=40, pady=20, command=lambda: self.keyPress("1"))
        self.btn_2 = tk.Button(self, text="2",bg="black",fg="white", padx=40, pady=20, command=lambda: self.keyPress("2"))
        self.btn_3 = tk.Button(self, text="3",bg="black",fg="white", padx=40, pady=20, command=lambda: self.keyPress("3"))
        self.btn_4 = tk.Button(self, text="4",bg="black",fg="white", padx=40, pady=20, command=lambda: self.keyPress("4"))
        self.btn_5 = tk.Button(self, text="5",bg="black",fg="white", padx=40, pady=20, command=lambda: self.keyPress("5"))
        self.btn_6 = tk.Button(self, text="6",bg="black",fg="white", padx=40, pady=20, command=lambda: self.keyPress("6"))
        self.btn_8 = tk.Button(self, text="8",bg="black",fg="white", padx=40, pady=20, command=lambda: self.keyPress("8"))
        self.btn_7 = tk.Button(self, text="7",bg="black",fg="white", padx=40, pady=20, command=lambda: self.keyPress("7"))
        self.btn_9 = tk.Button(self, text="9",bg="black",fg="white", padx=40, pady=20, command=lambda: self.keyPress("9"))
        self.btn_dec = tk.Button(self, text=".",bg="blue",fg="white", padx=42, pady=20, command=lambda: self.keyPress("."))
        self.btn_0 = tk.Button(self, text="0",bg="black",fg="white", padx=40, pady=20, command=lambda: self.keyPress("0"))
        self.btn_add = tk.Button(self, text="+", bg="blue",fg="white",padx=39, pady=20, command=self.add)
        self.btn_subtract = tk.Button(self, text="-", bg="blue",fg="white",padx=41, pady=20, command=self.subtract)
        self.btn_multiply = tk.Button(self, text="*", bg="blue",fg="white", padx=40, pady=20, command=self.multiply)
        self.btn_divide = tk.Button(self, text="/", bg="blue",fg="white",padx=41, pady=20, command=self.divide)
        self.btn_equal = tk.Button(self, text="=", bg="red",fg="white",padx=87, pady=20, command=self.calculate)
        self.btn_clear = tk.Button(self, text="CLS", bg="red",fg="white",padx=34, pady=20, command=self.clear_screen)

        # position the buttons on the calculator
        self.btn_1.grid(row=3, column=0)
        self.btn_2.grid(row=3, column=1)
        self.btn_3.grid(row=3, column=2)

        self.btn_4.grid(row=2, column=0)
        self.btn_5.grid(row=2, column=1)
        self.btn_6.grid(row=2, column=2)

        self.btn_7.grid(row=1, column=0)
        self.btn_8.grid(row=1, column=1)
        self.btn_9.grid(row=1, column=2)
        self.btn_dec.grid(row=4, column=0)
        self.btn_0.grid(row=4, column=1)
        self.btn_add.grid(row=4, column=2)
        self.btn_subtract.grid(row=5, column=0)
        self.btn_multiply.grid(row=5, column=1)
        self.btn_divide.grid(row=5, column=2)
        self.btn_clear.grid(row=6, column=2)

        self.btn_equal.grid(row=6, column=0, columnspan=2)

    def keyPress(self, number):
        self.display_box.insert("end", number)

    def clear_screen(self):
        self.display_box.delete(0, "end")

    def add(self):
        self.first_num = float(self.display_box.get())
        self.operation = "add"
        self.clear_screen()

    def subtract(self):
        self.first_num = float(self.display_box.get())
        self.operation = "subtract"
        self.clear_screen()

    def multiply(self):
        self.first_num = float(self.display_box.get())
        self.operation = "multiply"
        self.clear_screen()

    def divide(self):
        self.first_num = float(self.display_box.get())
        self.operation = "divide"
        self.clear_screen()

    def calculate(self):
        second_num = float(self.display_box.get())
        if self.operation == "add":
            result = self.first_num + second_num
        elif self.operation == "subtract":
            result = self.first_num - second_num
        elif self.operation == "multiply":
            result = self.first_num * second_num
        else:
            if second_num==0:
                result="DIVISION BY ZERO ERR"
            else:
                result = self.first_num / second_num

        self.clear_screen()
        self.display_box.insert(0, result)


calculator=Calculator()
calculator.mainloop()
