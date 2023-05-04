import tkinter as tk

window = tk.Tk()
window.title("Nyeya Address Book")
window.resizable(False, False)
contact_list = []

# create a label for the name field
tk.Label(window, text="Name:").grid(row=0, column=0, padx=10, pady=10)

# create an entry field for the name
name = tk.Entry(window, width=30)
name.grid(row=0, column=1, padx=10, pady=10)

# create a label for the email field
tk.Label(window, text="Contact:").grid(row=1, column=0, padx=10, pady=10)

# create an entry field for the email
email = tk.Entry(window, width=30)
email.grid(row=1, column=1, padx=10, pady=10)


def add_contact():
    nme = name.get()
    eml = email.get()
    if nme != "" and eml != "":
        contact_list.append((nme, eml))
        contact_update()
        empty_inputs()


def contact_update():
    display.delete("1.0", tk.END)
    for name, email in contact_list:
        display.insert(tk.END, f"{name}: {email}\n")


def empty_inputs():
    name.delete(0, tk.END)
    email.delete(0, tk.END)


# create a button to add the contact
tk.Button(window, text="Add Contact", bg="blue", fg="white", command=add_contact).grid(row=2, column=0, columnspan=2,
                                                                                       ipady=5, padx=10, pady=10,
                                                                                       sticky=tk.EW)

# create a label for the contact list
tk.Label(window, text="My Contacts:").grid(row=3, column=0, padx=10, pady=10)

# create a text area to display the contact list
display = tk.Text(window, width=30, height=10)
display.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

window.mainloop()
