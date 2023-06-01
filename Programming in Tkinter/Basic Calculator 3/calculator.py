from tkinter import *
root = Tk()
root.title("Calculator - @Nyeya")
root.config(bg="grey")
root.resizable(False,False)

equ = StringVar()
input_value = ""

def display(value):
    global input_value
    input_value+=str(value)
    equ.set(input_value)

def clear():
    global input_value
    input_value=""
    equ.set(input_value)

def answer():
    ans=eval(input_value)
    equ.set(ans)

Entry(bg="#435",fg="white",font=("Arial",22),textvariable=equ).grid(row=0,column=0,columnspan=4,sticky=EW,ipady=10)

Button(text="1",width=10,height=4,relief='flat',bg="white",command=lambda:display(1)).grid(row=2,padx=1,pady=1,column=0)
Button(text="2",width=10,height=4,relief='flat',bg="white",command=lambda:display(2)).grid(row=2,padx=1,pady=1,column=1)
Button(text="3",width=10,height=4,relief='flat',bg="white",command=lambda:display(3)).grid(row=2,padx=1,pady=1,column=2)
Button(text="4",width=10,height=4,relief='flat',bg="white",command=lambda:display(4)).grid(row=3,padx=1,pady=1,column=0)
Button(text="5",width=10,height=4,relief='flat',bg="white",command=lambda:display(5)).grid(row=3,padx=1,pady=1,column=1)
Button(text="6",width=10,height=4,relief='flat',bg="white",command=lambda:display(6)).grid(row=3,padx=1,pady=1,column=2)
Button(text="7",width=10,height=4,relief='flat',bg="white",command=lambda:display(7)).grid(row=4,padx=1,pady=1,column=0)
Button(text="8",width=10,height=4,relief='flat',bg="white",command=lambda:display(8)).grid(row=4,padx=1,pady=1,column=1)
Button(text="9",width=10,height=4,relief='flat',bg="white",command=lambda:display(9)).grid(row=4,padx=1,pady=1,column=2)
Button(text="0",width=10,height=4,relief='flat',bg="white",command=lambda:display(0)).grid(row=5,padx=1,pady=1,column=0)
Button(text=".",width=10,height=4,relief='flat',bg="white",command=lambda:display(".")).grid(row=5,padx=1,pady=1,column=1)

Button(text="%",width=10,height=4,relief='flat',bg="lightblue",fg="black",command=lambda:display("%")).grid(row=1,padx=1,pady=1,column=0)
Button(text="+",width=10,height=4,relief='flat',bg="lightblue",fg="black",command=lambda:display("+")).grid(row=1,padx=1,pady=1,column=1)
Button(text="-",width=10,height=4,relief='flat',bg="lightblue",fg="black",command=lambda:display("-")).grid(row=1,padx=1,pady=1,column=2)
Button(text="/",width=10,height=4,relief='flat',bg="lightblue",fg="black",command=lambda:display("/")).grid(row=1,padx=1,pady=1,column=3)
Button(text="x",width=10,height=4,relief='flat',bg="lightblue",fg="black",command=lambda:display("*")).grid(row=2,padx=1,pady=1,column=3)

Button(text="=",height=4,relief='flat',bg="seagreen",fg="white",command=answer).grid(row=5,padx=1,pady=1,column=2,columnspan=2,sticky=EW)
Button(text="CE",width=10,relief='flat',bg="seagreen",fg="white",command=clear).grid(row=3,padx=1,pady=1,column=3,rowspan=2,sticky=NS)


root.mainloop()