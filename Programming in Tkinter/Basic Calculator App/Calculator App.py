import tkinter as tk
root = tk.Tk()
root.columnconfigure([x for x in range(4)],weight=1)
root.rowconfigure([x for x in range(6)],weight=1)
root.geometry("300x400")
root.title("Simple Calculator App - By Nyeya")
ent_output = tk.Entry(root)
ent_output.focus_set()
ent_output.grid(row=0,column=0,columnspan=4,ipady=15,ipadx=5,padx=5,sticky=tk.EW)

keypads = ["1","2","3","+","4","5","6","*","7","8","9","/",".","0","-","="]
key_index = 0
def display(event):
    value = event.widget.cget("text")
    if value in ["=","CE"]:
        if value=="=":
            try:
                ans = eval(ent_output.get())
            except:
                ans = "CALCULATION ERROR"
            ent_output.delete("0",tk.END)
            ent_output.insert("0",str(ans))
        elif value=="CE":
            ent_output.delete('0',tk.END)
        else:
            pass
    else:
        ent_output.insert(tk.END,value)
for i in range(1,5):
    for j in range(4):
        tp=tk.Button(root,text=keypads[key_index])
        tp.bind("<Button-1>",display)
        tp.grid(row=i,column=j,ipadx=5,ipady=5,sticky=tk.N+tk.S+tk.E+tk.W,padx=2,pady=2)
        if j==3 or i==4:
            tp.configure(bg="red",fg="yellow")
        else:
            tp.configure(bg="black",fg="white")
        key_index+=1
tp = tk.Button(root, text="CE",bg="yellow")
tp.grid(row=5, column=0,columnspan=4, ipadx=5, ipady=2, sticky=tk.N + tk.S + tk.E + tk.W, padx=2, pady=2)
tp.bind("<Button-1>", display)

root.mainloop()