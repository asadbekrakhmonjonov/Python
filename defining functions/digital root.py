from tkinter import *
import tkinter as tk
from tkinter import ttk
from googletrans import Translator
from tkinter import messagebox

root = tk.Tk()
root.title('Language Translator')
root.geometry('590x370')

frame1 = Frame(root, width=590, height=370, relief=RIDGE, borderwidth=5, bg='#F7DC6F')
frame1.place(x=0, y=0)

from googletrans import Translator

def translate():
    lang_1 = text_entry1.get("1.0", "end-1c")
    cl = choose_language.get()
    if lang_1 == '':
        messagebox.showerror('Language Translator', 'Enter the words')
    else:
        text_entry2.delete(1.0, 'end')
        translator = Translator()
        output = translator.translate(lang_1, dest=cl)
        text_entry2.insert('end', output.text)


def clear():
    text_entry1.delete(1.0, 'end')
    text_entry2.delete(1.0, 'end')

a = tk.StringVar()
auto_select = ttk.Combobox(frame1, width=27, textvariable=a, state='randomly', font=('verdana', 10, 'bold'))
auto_select['values'] = ("Auto select")
auto_select.place(x=0, y=0)
auto_select.current(0)

l = tk.StringVar()
choose_language = ttk.Combobox(frame1, width=27, textvariable=l, state='randomly', font=('verdana', 10, 'bold'))
choose_language['values'] = ('Russian', 'English')
choose_language.place(x=10, y=100)
choose_language.current(0)

Label(root, text='Language Translator', font=("Helvetica 20 bold"), fg='black', bg='#F7DC6F').place(x=150, y=40)

text_entry1 = Text(frame1, width=20, height=7, borderwidth=5, relief=RIDGE, font=('verdana', 15))
text_entry1.place(x=10, y=150)

text_entry2 = Text(frame1, width=20, height=7, borderwidth=5, relief=RIDGE, font=('verdana', 15))
text_entry2.place(x=300, y=150)

btn_translate = Button(frame1, command=translate, text='Translate', relief='raised', borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2')
btn_translate.place(x=185, y=300)

btn_clear = Button(frame1, command=clear, text='Clear', relief='raised', borderwidth=2, font=('verdana', 10, 'bold'), bg='#248aa2')
btn_clear.place(x=300, y=300)

root.mainloop()
