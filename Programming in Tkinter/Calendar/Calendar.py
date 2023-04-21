from calendar import calendar
from datetime import datetime
from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("600x670")
root.title("Calendar - Nyeya")

frm = LabelFrame(root, text="CHOOSE YEAR", pady=20)
frm.pack(fill=X)

lbl = Label(frm, text="CHOOSE YEAR")
lbl.pack(side=LEFT)

year = StringVar()
year.set(datetime.now().year)
spin = ttk.Combobox(frm, values=[str(x) for x in range(1900, 2050)], textvariable=year, state="readonly")
spin.pack(side=LEFT, padx=20)


def getCalendar(event=None):
    cal = calendar(int(year.get()))
    output.delete("1.0", END)
    output.insert("1.0", cal)


btn = Button(frm, text="Get Calendar", command=getCalendar)
root.bind("<Return>", getCalendar)
btn.pack(side=LEFT, padx=20)

output = Text(root, bg="#333", fg="white")
output.pack(fill=BOTH, expand=True)

root.mainloop()
