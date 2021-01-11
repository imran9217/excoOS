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
image2 =Image.open('ruf.png')
image1 = ImageTk.PhotoImage(image2)
labelText = StringVar()
labelText.set("Welcome !!!!")
label1 = Label(root, image=image1, textvariable=labelText,
               font=("Times New Roman", 24),
               justify=CENTER, height=800, bg="lightblue")
label1.pack(fill=BOTH,expand=10)





image92=Image.open('250.png')
image91 = ImageTk.PhotoImage(image92)
# img_avi=PhotoImage(file='250.png')
lbl_avi=Label(root,image=image91,bg='black')
lbl_avi.place(x=500,y=280)





img_p_btn=PhotoImage(file='p_btn.png')
p_btn=Button(root,image=img_p_btn,bg='black')
p_btn.place(x=1290,y=700)
heading_font_design = Font(family='Times New Roman', weight='bold',
                               size=24)  # FONT STYLE FOR HEADING LIKE ENTER DETAILS... & LINES
text_font_design = Font(family='Times New Roman', size=18)  # FONT STYLE FOR TEXT & TEXT BOXES
buttons_font_design = Font(family='Times New Roman', size=18)
last_button_font_design = Font(family='Times New Roman', size=12, slant="italic", underline=1)
username_label = Label(lbl_avi, text="Username", font=text_font_design,bg='Green',width=18,fg="white")
password_label = Label(lbl_avi, text="Password", font=text_font_design,bg='Green',width=18 ,fg="white")



un = Entry(lbl_avi, width=80, font=text_font_design,bg='Green')
pwd = Entry(lbl_avi, width=80, font=text_font_design,bg='Green')

    # BUTTONS

login_btn = Button(lbl_avi, text="Login", bg='Green', fg='White', width=10, font=buttons_font_design )
forget_password_btn = Button(lbl_avi, text="   Forget Password?   ", bg='Red', fg='White',
                                 font=buttons_font_design)
create_account_btn = Button(lbl_avi, text="  Create a New Account  ", bg='Green', fg='White',
                                font=buttons_font_design   )
close_btn = Button(lbl_avi, text="Close", bg='Black', fg='White', width=10, height=2,
                       font=last_button_font_design)


username_label.place(x = 350,y = 30)


un.place(x = 350,y = 60)
password_label.place(x = 350,y = 100)
pwd.place(x = 350,y = 130)
login_btn.place(x=230,y=170)






root.mainloop()