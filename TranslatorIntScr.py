from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def change(text = "type", source = "English", dest = "Hindi"):
    text1 = text
    source1 = source
    dest1 = dest
    trans = Translator()
    trans1 = trans.translate(text, src = source1, dest = dest1)
    return trans1.text

def fetch_data():
    s = combo_source.get()
    d = combo_dest.get()
    msg = source_txt.get(1.0,END)
    text_get = change(text = msg, source = s, dest = d)
    dest_txt.delete(1.0, END)
    dest_txt.insert(END,text_get)




root = Tk()
root.title("Translator")
root.geometry("500x600")
root.config(bg = "Light Blue")

label_txt = Label(root,text = "Translator", font = ("Times New Roman", 20, "bold"), bg = "Light Blue")
label_txt.place(x = 100, y = 40, height = 50, width = 300)

frame = Frame(root).pack(side = BOTTOM)

label_txt = Label(root,text = "Source", font = ("Times New Roman", 20, "bold"), bg = "Light Blue", fg = "Black")
label_txt.place(x = 100, y = 100, height = 20, width = 300)

source_txt = Text(frame, font = ("Times New Roman", 18, "bold"), wrap = WORD)
source_txt.place(x = 10, y = 140, height = 150, width = 480)

list_txt = list(LANGUAGES.values())

combo_source = ttk.Combobox(frame, value = list_txt)
combo_source.place(x = 10, y = 300, height = 40, width = 150)
combo_source.set("English")

button_change = Button(frame, text = "Translate", relief = RAISED, command = fetch_data)
button_change.place(x = 170, y = 300, height = 40, width = 150)

combo_dest = ttk.Combobox(frame, value = list_txt)
combo_dest.place(x = 330, y = 300, height = 40, width = 150)
combo_dest.set("English")

label_txt = Label(root,text = "Destination", font = ("Times New Roman", 20, "bold"), bg = "Light Blue", fg = "Black")
label_txt.place(x = 100, y = 360, height = 20, width = 300)

dest_txt = Text(frame, font = ("Times New Roman", 18, "bold"), wrap = WORD)
dest_txt.place(x = 10, y = 400, height = 150, width = 480)

root.mainloop()