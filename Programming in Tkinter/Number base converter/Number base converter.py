from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.title('NUMBER BASE CONVERTER - NYEYA')
root.geometry('380x380')
root.resizable(width=False, height=False)
root.grid_columnconfigure(1, weight=4)

body_bg = "black"
text1 = "white"
text2 = "grey"
btn_color = "green"

root.configure(bg=body_bg, padx=20)
ttk.Separator(root, orient=HORIZONTAL).grid(row=0, columnspan=1, padx=3, pady=5, sticky=EW)
base_list = ['BINARY', 'OCTAL', 'DECIMAL', 'HEXADECIMAL']


def convert():
    def number_to_decimal(number, base_val):

        decimal = int(number, base_val)

        binary = bin(decimal)
        octal = oct(decimal)
        hexadecimal = hex(decimal)

        lbl_bin['text'] = str(binary[2:])
        lbl_oct['text'] = str(octal[2:])
        lbl_dec['text'] = str(decimal)
        lbl_hex['text'] = str(hexadecimal[2:]).upper()

    base_val = cmb_base.get()
    number = e_value.get()
    if (base_val.upper() in base_list) and number.isdecimal():
        pass
    else:
        messagebox.showinfo("WARNING", "Choose a base, and enter an integer value")
        return
    if base_val == 'BINARY':
        base_val = 2
    elif base_val == 'OCTAL':
        base_val = 8
    elif base_val == 'DECIMAL':
        base_val = 10
    else:
        base_val = 16

    number_to_decimal(number, base_val)

application_title = Label(root,
                          text="Number Base Converter",
                          pady=0,
                          anchor="center",
                          font=("sans-serif 20"),
                          bg="red",
                          fg=text1)
application_title.grid(row=1, column=0, sticky=EW)

main_body = Frame(root, bg=body_bg)
main_body.grid(row=2, column=0, sticky=EW, pady=12)

Label(main_body, text="Choose Number System", bg=body_bg, fg=text2).grid(row=0, column=0, sticky=EW)
cmb_base = ttk.Combobox(main_body, justify="center", font=('Ivy 12 bold'), values=base_list)
cmb_base.grid(row=0, column=1, pady=3, sticky=EW)

Label(main_body, text="Enter value: ", bg=body_bg, fg=text2).grid(row=1, column=0, sticky=EW)
e_value = Entry(main_body, text="Enter digit", justify="center", font=("", 13), highlightthickness=1, relief=SOLID)
e_value.grid(row=1, column=1, sticky=EW)

b_converter = Button(main_body, command=convert, text="CONVERT", bg="blue", fg=text1, font=('Ivy 8 bold'),
                     relief=RAISED, overrelief=RIDGE)
b_converter.grid(row=2, column=0, columnspan=2, sticky=EW, pady=10, ipady=3)

b_converter = Label(main_body, text="OUTPUT", bg=body_bg, fg=text1, font=('Ivy 12 bold'))
b_converter.grid(row=3, column=0, columnspan=2, sticky=EW, pady=3, ipady=3)

lbl_bin = Label(main_body, text="BINARY", height=1, relief="flat", anchor='nw', font=('Verdana 13'), bg=btn_color,
                fg=body_bg)
lbl_bin.grid(row=4, column=0, sticky=EW)
lbl_bin = Label(main_body, text="", height=1, relief="flat", anchor='center', font=('Verdana 13'), fg=text2)
lbl_bin.grid(row=4, column=1, pady=3, sticky=EW)

lbl_oct = Label(main_body, text="OCTAL", height=1, relief="flat", anchor='nw', font=('Verdana 13'), bg=btn_color,
                fg=body_bg)
lbl_oct.grid(row=5, column=0, pady=3, sticky=EW)
lbl_oct = Label(main_body, text="", height=1, relief="flat", anchor='center', font=('Verdana 13'), fg=text2)
lbl_oct.grid(row=5, column=1, sticky=EW)

lbl_dec = Label(main_body, text="DECIMAL", height=1, relief="flat", anchor='nw', font=('Verdana 13'), bg=btn_color,
                fg=body_bg)
lbl_dec.grid(row=6, column=0, pady=3, sticky=EW)
lbl_dec = Label(main_body, text="", height=1, relief="flat", anchor='center', font=('Verdana 13'), fg=text2)
lbl_dec.grid(row=6, column=1, sticky=EW)

lbl_hex = Label(main_body, text="HEXADECIMAL", height=1, relief="flat", anchor='nw', font=('Verdana 13'), bg=btn_color,
                fg=body_bg)
lbl_hex.grid(row=7, column=0, pady=3, sticky=EW)
lbl_hex = Label(main_body, text="", height=1, relief="flat", anchor='center', font=('Verdana 13'), fg=text2)
lbl_hex.grid(row=7, column=1, sticky=EW)

Label(root, text="By: Nyeya", font=('Verdana 10'), fg="yellow", bg=body_bg).place(x=250, y=340)

root.mainloop()
