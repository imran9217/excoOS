from tkinter import *
from PIL import Image , ImageTk
from time import strftime
from datetime import date
from tkinter.font import Font
root=Tk()
root.state('zoomed')
root.resizable(False,False)
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen',True)
root.title("excoOS")
# lock_pic=PhotoImage(file='LOCK.PNG')
image2 =Image.open('on.png')
image1 = ImageTk.PhotoImage(image2)
labelText = StringVar()
labelText.set("Welcome !!!!")
label1 = Label(root, image=image1, textvariable=labelText,
               font=("Times New Roman", 24),
               justify=CENTER, height=800, bg="lightblue")
label1.pack(fill=BOTH,expand=10)


def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

from datetime import datetime
now = datetime.now()

w = Label(root, text=f"{datetime.now():%a, %b %d %Y}", fg="white", bg="black", font=("helvetica", 40))

w.place(x=15,y=700)


lbl = Label(root, font=('calibri', 72, 'bold'),
            background='black',
            foreground='white')

lbl.place(x=15,y=550)
time()
# main_btn=Button(root,image=lock_pic)
# main_btn.pack(fill=BOTH)


root.mainloop()