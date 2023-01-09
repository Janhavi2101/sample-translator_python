from tkinter import *
from tkinter import ttk
from googletrans import Translator ,LANGUAGES

def change(text="type",src="English",dest="Marathi"):
    text1 = text
    src1 = src
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text, src=src1, dest=dest1)
    return trans1.text

def data():
    s = comb_sor.get()
    d = comb_dest.get()
    msg = Sor_txt.get(1.0,END)
    textget = change(text=msg, src=s, dest=d)
    dest_txt.delete(1.0,END)
    dest_txt.insert(END,textget)


root = Tk()
root.title("Translator")
root.geometry("500x650")
root.config(bg='light grey')

lab_txt = Label(root, text="Translator", font=("Cooper Black", 30, "bold"))
lab_txt.place(x=90, y=50, height=100, width=333)

frame = Frame(root).pack(side=BOTTOM)

lab_txt = Label(root, text="SOURCE CODE", font=("Cooper Black", 9,), bg="light grey")
lab_txt.place(x=90, y=160, height=10, width=333)

Sor_txt = Text(frame, font=("Cooper Black", 15, "bold"),wrap=WORD)
Sor_txt .place(x=75, y=180, height= 150, width= 380)

list_text= list(LANGUAGES.values())

comb_sor = ttk.Combobox(frame, value=list_text)
comb_sor.place(x=10,y=350, height=40,width=160 )
comb_sor.set("english")

button_change = Button(frame, text="Translate", relief=RAISED, command= data)
button_change.place(x=180,y=350, height=40,width=100 )

comb_dest = ttk.Combobox(frame, value=list_text)
comb_dest.place(x=290,y=350, height=40,width=160 )
comb_dest.set("english")

dest_txt = Text(frame, font=("Cooper Black", 15, "bold"),wrap=WORD)
dest_txt .place(x=75, y=420, height= 150, width= 380)

lab_txt = Label(root, text="DESTINATION CODE", font=("Cooper Black", 9,), bg="light grey")
lab_txt.place(x=90, y=400, height=10, width=333)



root.mainloop()
