from tkinter import *
root = Tk()
root.title("Temperature Converter")
root.geometry("200x210")

def tempConvert():
    temp = float(temp_entry.get())
    result_fahren = 9/5*temp+32
    result_kelv = 273.15+temp
    results_label.configure(text="Converted: \n{:3.1f}F\n{:3.1f}K".format(result_fahren,result_kelv))

lbl1 = Label(root,text="Temperature in degrees")
lbl1.place(x=30,y=0)

temp_entry = Entry(root)
temp_entry.place(x=40,y=30,width=110)

convert_butn = Button(root,text="Convert",command=tempConvert)
convert_butn.place(x=30,y=70,width=130)

results_label = Label(root,text="Results")
results_label.place(x=70,y=110)

root.mainloop()
