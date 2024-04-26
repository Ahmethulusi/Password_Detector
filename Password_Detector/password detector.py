from tkinter import *
from tkinter import messagebox
import os
import base64


def reset():
    code.set("")
    text1.delete(1.0,END)



def decyrpt():
    password =code.get()

    if password=="1234":
        screen2=Toplevel(screen)
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")

        message= text1.get(1.0,END)
        decode_message=message.encode("ascii")
        base64_bytes =base64.b64decode(decode_message)
        decrypt =base64_bytes.decode("ascii")
        Label(screen2,text="DECRYPT",font="arial",fg="white",bg="#00bd56").place(x=10,y=0)
        text2=Text(screen2,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,decrypt)

    elif password=="":
        messagebox.showerror("decryption","Input Password")
    elif password !="1234":
        messagebox.showerror("decrtption","Invalid Password")   

def encrypt():
    password =code.get()

    if password=="1234":
        screen1=Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")

        message= text1.get(1.0,END)
        encode_message=message.encode("ascii")
        base64_bytes =base64.b64encode(encode_message)
        encrypt =base64_bytes.decode("ascii")
        Label(screen1,text="ENCRYPT",font="arial",fg="white",bg="#ed3833").place(x=10,y=0)
        text2=Text(screen1,font="Rpbote 10",bg="white",relief=GROOVE,wrap=WORD,bd=0)
        text2.place(x=10,y=40,width=380,height=150)

        text2.insert(END,encrypt)

    elif password=="":
        messagebox.showerror("encryption","Input Password")
    elif password !="1234":
        messagebox.showerror("encrtption","Invalid Password")    

def main_screen():
    global screen
    global code,text1
    screen =Tk()
    screen.geometry("375x398+500+100")

    #icon
    image_icon =PhotoImage(file="C:/Users/90533/Downloads/keys.png")
    screen.iconphoto(False,image_icon)
    screen.title("Pctapp")

    Label(text="Enter text for encryption and decryption",fg="black",font=("calbri",13)).place(x=10,y=10)
    text1 =Text(font="Robote 15",bg="lightgray",relief=GROOVE,wrap=WORD,bd=5)
    text1.place(x=10,y=50,width=355,height=100)

    Label(text="Enter secret key for encryption and decryption",fg="black",font=("calibri",13)).place(x=10,y=170)

    code =StringVar()
    Entry(textvariable=code,width=19,bg="lightgray",bd=3,font=("arial",25),show="*").place(x=10,y=200)

    Button(text="ENCRYPT",height=2,width=23,bg="red",fg="white",bd=0,command=encrypt).place(x=10,y=250)
    Button(text="DECRYPT",height=2,width=23,bg="green",fg="white",bd=0,command=decyrpt).place(x=200,y=250)
    Button(text="RESET",height=2,width=50,bg="blue",fg="white",bd=0,command=reset).place(x=10,y=300)

    screen.mainloop()

main_screen()