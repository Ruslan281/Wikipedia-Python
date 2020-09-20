from tkinter import *
from tkinter.scrolledtext import ScrolledText
import wikipedia as wiki
root=Tk()
root.title("Axtarış Sistemi")
root.geometry("320x480")
root.configure(bg="white")

def search():
    search_data=ent.get()
    data=wiki.summary(search_data,sentences=8)

    ent.set("")
    text.delete(0.0,END)

    search_lbl["text"]="Axtarışın Nəticələri : {}".format(search_data)
    text.insert(0.0,data)

def enter_pressed(event):
    search()

ent=StringVar()
search_entry=Entry(root,width=30,font=("arial",12),bg="white",relief=RIDGE,
                   textvariable=ent)
search_entry.bind("<Return>",enter_pressed)
search_entry.place(x=15,y=20)

search_lbl=Label(root,text="Axtarışın Nəticələri : ",font=("arial",
                                                           12,"bold"),
                 bg="white")
search_lbl.place(x=15,y=70)

text=ScrolledText(root,font=("times",12),bd=4,relief=SUNKEN,wrap=WORD)
text.place(x=15,y=100,height=300,width=300)


search_btn=Button(root,text="Axtar",font=("arial",12,"bold"),width=8,command=search)
search_btn.place(x=10,y=420)

clear_btn=Button(root,text="Təmizlə",font=("arial",12,"bold"),width=7,
                 command=lambda :text.delete(0.0,END))
clear_btn.place(x=145,y=420)

exit_btn=Button(root,text="Çıxış",font=("arial",12,"bold"),
                width=8,command=root.quit)
exit_btn.place(x=250,y=420)


root.mainloop()
