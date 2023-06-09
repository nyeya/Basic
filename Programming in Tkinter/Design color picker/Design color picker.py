import tkinter.messagebox
from tkinter import *

# colors---------------------
dark_color = "#444466"
light_color = "#aaa"

# INITAL SETUP ----------
root = Tk()
root.title("DESIGN COLOR PICKER - NYEYA")
root.geometry("516x370")
root.configure(bg=light_color)
root.resizable(width=FALSE, height=FALSE)

#  HEADER SECTION ------------
headers = {
    "fg": "white",
    "bg": "black",
    "font": ("sans-serif", 18, "bold"),
}
Label(root, text="Slider Pane", **headers).grid(row=0, column=0, sticky=EW, padx=2)
Label(root, text="Color Screen", **headers).grid(row=0, column=1, sticky=EW)

#  COLOR SLIDER ------------
slider_pane = Frame(root, bg=light_color, relief=RAISED, borderwidth=5)
slider_pane.grid(row=1, column=0, sticky=W)

sliders = {
    "width": 7,
    "anchor": CENTER,
    "fg": "white",
    "font": ("sans-serif", 12, "bold"),
}

red_btn = Button(slider_pane, text="Red", bg="red", **sliders)
red_btn.grid(row=0, column=0, sticky=EW)
green_btn = Button(slider_pane, text="Green", bg="green", **sliders)
green_btn.grid(row=0, column=1, sticky=EW)
blue_btn = Button(slider_pane, text="Blue", bg="blue", **sliders)
blue_btn.grid(row=0, column=2, sticky=EW)

# slider color slides
red_scale = Scale(slider_pane, bg=light_color, fg="red", command=lambda num=1: change_color(num), from_=255, to=0,
                  length=150, orient=VERTICAL, cursor="hand2")
red_scale.grid(row=1, column=0, sticky=EW)
green_scale = Scale(slider_pane, bg=light_color, fg="green", command=lambda num=2: change_color(num), from_=255, to=0,
                    length=150, orient=VERTICAL, cursor="hand2")
green_scale.grid(row=1, column=1, sticky=EW)
blue_scale = Scale(slider_pane, bg=light_color, fg="blue", command=lambda num=3: change_color(num), from_=255, to=0,
                   length=150, orient=VERTICAL, cursor="hand2")
blue_scale.grid(row=1, column=2, sticky=EW)

#  COLOR SCREEN DISPLAY-------------
output_scr = Label(root, text="Color Picker", bg=dark_color, fg="white", font=("sans-serif", 11, "bold"), height=11,
                   borderwidth=5, relief=RIDGE)
output_scr.grid(row=1, column=1, sticky=EW)

# DASHBOARD -----------------
dashboard = Frame(root, bg=dark_color, borderwidth=5, relief=SUNKEN)
dashboard.grid(row=2, column=0, columnspan=2, padx=0, pady=5, sticky=EW)

hex_label = Label(dashboard, text="HEX COLOR CODE :", bg=dark_color, fg=light_color, anchor=NW,
                  font=("sans-serif", 10, "bold"))
hex_label.grid(row=0, column=0, pady=15)

color_entry1 = Entry(dashboard, width=17, font=("sans-serif", 10, "bold"), justify=CENTER)
color_entry1.grid(row=0, column=1, padx=5)

copy_button1 = Button(dashboard, text="Copy Color", bg=dark_color, fg=light_color, font=("sans-serif", 10, "bold"),
                      command=lambda num=1: copy_clipboard(num))
copy_button1.grid(row=0, column=2, padx=5)


rgb_label = Label(dashboard, text="RGB COLOR CODE :", bg=dark_color, fg=light_color, anchor=NW,
                  font=("sans-serif", 10, "bold"))
rgb_label.grid(row=1, column=0, pady=15)

color_entry2 = Entry(dashboard, width=17, font=("sans-serif", 10, "bold"), justify=CENTER)
color_entry2.grid(row=1, column=1, padx=5)

copy_button2 = Button(dashboard, text="Copy Color", bg=dark_color, fg=light_color, font=("sans-serif", 10, "bold"),
                      command=lambda num=2: copy_clipboard(num))
copy_button2.grid(row=1, column=2, padx=5)

brand = Label(dashboard, text="By: Nyeya", bg=dark_color, anchor=E, font=("sans-serif", 13, "bold"))
brand.grid(row=1, column=3, padx=30, sticky=E)


# APP FUNCTIONS --------------------
def change_color(num):
    r = red_scale.get()
    g = green_scale.get()
    b = blue_scale.get()
    output_col = "black"
    if (int(r) + int(b) + int(g)) < 400:
        output_col = "white"
    red_col = "#%02x0000" % r
    red_btn["bg"] = red_col
    blue_col = "#0000%02x" % b
    blue_btn["bg"] = blue_col
    grn_col = "#00%02x00" % g
    green_btn["bg"] = grn_col

    hexadecimal = "#%02x%02x%02x" % (r, g, b)
    rgb = f"rgb({r}, {g}, {b})"
    output_scr['bg'] = hexadecimal
    output_scr['fg'] = output_col
    brand['fg'] = hexadecimal

    color_entry1.delete(0, END)
    color_entry1.insert(0, hexadecimal)
    color_entry2.delete(0, END)
    color_entry2.insert(0, rgb)


def copy_clipboard(val):
    clip = Tk()
    clip.withdraw()
    color_entry = [color_entry1, color_entry2]
    clip.clipboard_clear()
    clip.clipboard_append(color_entry[val - 1].get())
    tkinter.messagebox.showinfo('Color', "Copied Successfully!")
    clip.destroy()


root.mainloop()
