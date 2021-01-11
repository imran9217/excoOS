from tkinter import *
from PIL import Image , ImageTk
from time import strftime
from tkinter.font import Font
root=Tk()
root.state('zoomed')
root.resizable(False,False)
root.overrideredirect(True)
root.overrideredirect(False)
root.attributes('-fullscreen',True)



root.title("excoOS")
image2 =Image.open('deskpot.png')
image1 = ImageTk.PhotoImage(image2)
labelText = StringVar()
labelText.set("Welcome !!!!")
label1 = Label(root, image=image1, textvariable=labelText,
               font=("Times New Roman", 24),
               justify=CENTER, height=800, bg="lightblue")
label1.pack(fill=BOTH,expand=10)
chrome_icon=PhotoImage(file='chrome-icon.png')
########################################################################################
btn_chrome=Button(root,text="GOOGLE",image=chrome_icon,bg='black')
btn_chrome.place(x=1,y=5)
#######################################################################################
search_icon=PhotoImage(file='sh.png')
btn_search=Button(root,image=search_icon,bg='black')
btn_search.place(x=1320,y=720)

########################################################################################
bin_icon=PhotoImage(file='bin.png')
btn_bin=Button(root,image=bin_icon,bg='black')
btn_bin.place(x=1,y=70)

########################################################################################
mass_icon=PhotoImage(file='mass.PNG')
btn_mass=Button(root,image=mass_icon,bg='black')
btn_mass.place(x=1260,y=720)
########################################################################################
ai_icon=PhotoImage(file='ai.png')
btn_ai=Button(root,image=ai_icon,bg='black')
btn_ai.place(x=1,y=130)
########################################################################################
windo_icon=PhotoImage(file='windo.png')
btn_windo=Button(root,image=windo_icon,bg='black')
btn_windo.place(x=1,y=715)

########################################################################################
sys_icon=PhotoImage(file='sys.png')
btn_sys=Button(root,image=sys_icon,bg='black')
btn_sys.place(x=1200,y=715)
########################################################################################
acc_icon=PhotoImage(file='acc.png')
btn_acc=Button(root,image=acc_icon,bg='black')
btn_acc.place(x=1140,y=715)




























def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

from datetime import datetime
now = datetime.now()

w = Label(root, text=f"{datetime.now():%a, %b %d %Y}", fg="white", bg="black", font=("helvetica", 20))

w.place(x=1130,y=650)


lbl = Label(root, font=('calibri', 40, 'bold'),
            background='black',
            foreground='white')

lbl.place(x=1050,y=580)
time()









root.mainloop()
