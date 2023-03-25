import tkinter as tk
from tkinter import ttk


class BMI(tk.Tk):
    def __init__(self, appName, width, height):
        super().__init__()
        self.geometry(f"{width}x{height}")  # Specify the geometry of the window
        self.resizable(0, 0)  # Make the window not resizable.
        self.title(appName)  # Give my window a title
        self.bgcolor = "#A0BFE5"  # Store the background theme color in a variable
        self["background"] = self.bgcolor  # Sets the background color
        self.drawInterface()  # Calls the drawInterface() method

    def drawInterface(self):
        # **************************** CREATES THE LAYOUT AND INTERFACE OF THE WINDOW **************
        lbl_settings = {
            "font": "arial 15 bold",
            "bg": self.bgcolor,
        }
        tk.Label(self, text="Instruction to the user: Enter weight in kg, and height in cm", font="arial 12 bold",
                 bg=self.bgcolor).place(x=50, y=10)
        tk.Label(self, text="BMI", **lbl_settings).place(x=610, y=30)
        tk.Label(self, text="Weight", **lbl_settings).place(x=120, y=80)

        self.ent_weight = tk.Entry(self, font="arial 15", justify=tk.CENTER)
        self.ent_weight.place(x=220, y=70, height=60)
        self.ent_weight.focus_set()

        result_frame = tk.Frame(self, background=self.bgcolor, highlightbackground="black", highlightthickness=2)
        result_frame.place(x=500, y=70, height=300, width=250)

        self.output = tk.Label(result_frame, font="arial 23", bg=self.bgcolor)
        self.output.pack(fill=tk.BOTH, expand=True)

        tk.Label(self, text="Height", **lbl_settings).place(x=120, y=160)

        self.ent_height = tk.Entry(self, font="arial 15", justify=tk.CENTER)
        self.ent_height.place(x=220, y=150, height=60)

        ttk.Button(self, text="Calculate", command=self.calculate).place(x=120, y=230, width=325, height=60)
        ttk.Button(self, text="Clear", command=self.clear).place(x=120, y=310, width=325, height=60)

    def calculate(self):
        # Get the values of weight and height from their text boxes
        weight, height = self.ent_weight.get(), self.ent_height.get()
        # A condition to make sure the values are not empty
        if weight != "" and height != "":
            try:
                # Try to convert the values of the weight and height, then calculates the bmi
                bmi = float(weight) / (float(height) ** 2)
                result = round(bmi, 2)
            except:
                # If the conversion of the values fail, it should display invalid entry
                result = "Invalid Entry"
            self.output.config(text=result)

    def clear(self):
        # Clears the height and weight entry box and set the mouse focus on the weight entry
        self.ent_weight.delete(0, tk.END)
        self.ent_weight.focus_set()
        self.ent_height.delete(0, tk.END)


# Creates an instance of the class BMI and loop it.
if __name__ == '__main__':
    bmi = BMI(appName="UTAS BMI CALCULATOR", width=770, height=420)
    bmi.mainloop()
