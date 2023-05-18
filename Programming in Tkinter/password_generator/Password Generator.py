import string
from random import choice
from tkinter import *

root = Tk()
root.geometry("300x300")
root.resizable(0, 0)
root.title("Password Generator - NYEYA")
root.columnconfigure([0, 1], weight=1)
root.rowconfigure([0, 1, 2, 3, 4], weight=1)

keys = {
    "upper": IntVar(),
    "numb": IntVar(),
    "punct": IntVar(),
}
pass_range = IntVar()


def generatePass(total=10, isUpper=0, isNumb=0, isPunct=0):
    coords = (1 * isUpper) + (3 * 1) + (2 * isNumb) + (2 * isPunct)
    u = round(1 / coords * total) if isUpper else 0
    l = round(3 / coords * total)
    n = round(2 / coords * total) if isNumb else 0
    p = round(2 / coords * total) if isPunct else 0
    summation = u + l + p + n
    if summation < total:
        l += total - summation
    elif summation > total:
        n -= summation - total
    wordlist = {
        "u": {
            "words": string.ascii_uppercase,
            "limit": u
        },
        "l": {
            "words": string.ascii_lowercase,
            "limit": l,
        },
        "n": {
            "words": string.digits,
            "limit": n,
        },
        "p": {
            "words": "!#$%&()*+-.:?@^_~",
            "limit": p,
        }
    }
    passw = ""

    def decider(chosen):
        if (wordlist[chosen]["limit"] != 0):
            wordlist[chosen]["limit"] -= 1
            return choice(wordlist[chosen]["words"])
        else:
            return "-1"

    for letter in range(total):
        start = "-1"
        while start == "-1":
            if letter < 2:
                start = decider(choice(["u", "l"]))
            else:
                start = decider(choice(list(wordlist.keys())))
        passw += start
    results.delete(0, END)
    results.insert(0, passw)


def show(val=None):
    generatePass(total=pass_range.get(), isUpper=keys["upper"].get(), isNumb=keys["numb"].get(),
                 isPunct=keys["punct"].get())


p_range = Scale(root, from_=8, to=18, orient=VERTICAL, variable=pass_range, command=show)
p_range.grid(row=0, column=0, rowspan=4, padx=10, pady=10, sticky=NS)

button1 = Checkbutton(root, text="UpperCase", variable=keys["upper"], command=show)
button2 = Checkbutton(root, text="LowerCase", state=DISABLED)
button2.select()
button3 = Checkbutton(root, text="Numbers", variable=keys["numb"], command=show)
button4 = Checkbutton(root, text="Punctuation", variable=keys["punct"], command=show)

btn_gen = Button(root, text="Generate", command=show, bg="red", fg="white")

results = Entry(root, font="arial 20", bg="#555", fg="white")

button1.grid(row=0, column=1, pady=5, sticky=W)
button2.grid(row=1, column=1, pady=5, sticky=W)
button3.grid(row=2, column=1, pady=5, sticky=W)
button4.grid(row=3, column=1, pady=5, sticky=W)
btn_gen.grid(row=4, column=0, sticky=EW, columnspan=2, padx=5, ipady=5, pady=10)

results.grid(row=5, column=0, columnspan=2, sticky=EW, padx=10, ipady=10, pady=5)
root.mainloop()

