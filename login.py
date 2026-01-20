from tkinter import *

root=Tk()
root.title("Login app")
root.geometry("500x500")
frame=Frame(master=root,height=200,width=360,bg="pink")
frame.place(x=20,y=0)

lbl1=Label(frame,text="Full Name", bg="yellow", fg="red", width=12)
lbl1.place(x=20,y=20)
lbl2=Label(frame,text="Email", bg="yellow", fg="red", width=12)
lbl2.place(x=20,y=80)
lbl3=Label(frame,text="Password", bg="yellow", fg="red", width=12)
lbl3.place(x=20,y=140)

name_entry=Entry(frame)
name_entry.place(x=150,y=20)
email_entry=Entry(frame)
email_entry.place(x=150,y=80)
password_entry=Entry(frame,show="*")
password_entry.place(x=150,y=140)

def display():
    name=name_entry.get()
    greet="Hey "+name
    msg="Congrats, your account has been created"
    textbox.insert(END,greet)
    textbox.insert(END,msg)

btn=Button(text="Create Account",command=display)
btn.place(x=130,y=210)

textbox=Text()
textbox.place(x=0,y=250)

root.mainloop()