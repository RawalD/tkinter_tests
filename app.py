from tkinter import *

window = Tk()


def km_to_miles():
    # print(entry_value.get())
    miles = float(entry_value.get()) * 1.6
    text_one.insert(END, miles)


btn_one = Button(window, text="Run", command=km_to_miles)
btn_one.grid(row=0, column=0)

entry_value = StringVar()
entry = Entry(window, textvariable=entry_value)
entry.grid(row=0, column=1)

text_one = Text(window, height=1, width=20)
text_one.grid(row=0, column=2)

window.mainloop()
