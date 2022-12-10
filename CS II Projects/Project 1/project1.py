from tkinter import *
from tkinter import ttk

# creating window
window = Tk()
# window title
window.title('Project 1 - The Christmas List Builder')
# dimensions, non re-sizeable
window.geometry("500x500")
window.resizable(False, False)

label_title = Label(window, text='Christmas List Builder!', font=('Sitka Small Semibold', 14), fg='dark red')
label_title.pack()

label_directions = Label(window, text='Enter up to five items to add to your Christmas list :)', fg='dark green',
                         font=('Sitka Text', 12))
label_directions.pack(pady=5)

wishlist = []


def append(text):
    priority.append(text)


frame_item = Frame(window)
label_item = Label(frame_item, text='Item\t', font=('Sitka Text', 12))
entry_item = Entry(frame_item, width=40)
label_item.pack(padx=20, side='left')
entry_item.pack(padx=10, side='left')
frame_item.pack(anchor='w', pady=10)

frame_buttons = Frame(window)

count = 0
if count == 0:
    listTitle = Label(window, text='Your Christmas List:', font=('Sitka Text', 12))
    listTitle.pack()


def entry():
    global entry_item
    entry_item.delete(0, END)


def click():
    global count
    if count < 5:
        listing = " - " + entry_item.get()
        listinglabel = Label(window, text=listing, anchor='w')
        listinglabel.pack()
        count += 1
        entry()
    elif count == 5:
        exitbutton = Button(window, text='Exit', command=window.destroy(), bg='dark red')
        exitbutton.pack()


button_save = Button(frame_buttons, width=30, text='Add to list', font=('Sitka Text', 10), fg='white', bg='dark green',
                     command=click)
button_save.pack()

frame_buttons.pack()

window.mainloop()
