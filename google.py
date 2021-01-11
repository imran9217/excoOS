from tkinter import *
from PIL import Image , ImageTk
from tkinter.font import Font
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
igt_pic=PhotoImage(file='igt.png')
lbl_1_1=Label(label1,bg='black',image=igt_pic)
lbl_1_1.place(x=500,y=200)
import webbrowser


url=""


# url='C:\Windows\System32\cmd.exe'
r_r = Entry(label1, width=80,bg='Green',textvariable=url)

r_r.place(x=450,y=400)

def start():
    # userInput.get()

    webbrowser.open(url)
sh_pic=PhotoImage(file='sh.png')
btn_sh=Button(label1,bg='black',image=sh_pic,command=start)
btn_sh.place(x=500,y=500)




root.mainloop()