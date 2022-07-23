# Generator
# By The.Ertor

# import
from tkinter import * 
import random 
from tkinter.messagebox import showerror, showinfo 
from tkinter import messagebox

root = Tk()
inputFieldOne = None
inputFieldTwo = None
errorTitle = None

# Localization
eng = {"loc": "Generate number", "loc1": "Number generator",  "loc2": "Enter the first number", "loc3": "Enter the second number", "loc4": "The entered value is not correct", "loc5": "Input Error"}
rus = {"loc": "Сгенерировать число", "loc1": "Генератор чисел", "loc2": "Введите первое число", "loc3": "Введите второе число", "loc4": "Введенное значение неверно", "loc5": "Ошибка ввода"}
lang_dict = eng
lang_dict["loc"]
is_eng = True


# Commands
def btn_click():
    inputFieldOneValue = inputFieldOne.get()
    inputFieldTwoValue = inputFieldTwo.get()
    try:
        randomNum = random.randint(int(inputFieldOneValue), int(inputFieldTwoValue))
        info["text"] = randomNum
        errorTitle["text"] = ""
    except ValueError:
        url = messagebox.showerror(title=lang_dict["loc5"], message=lang_dict["loc4"])

# Feature about user
def about_click(): 
    url = messagebox.showinfo(title='Generator build v3.1', message="Genrerator by The.Ertor build v3.1")

# Language change function
def change_lang():
    global is_eng
    global lang_dict
    is_eng = not is_eng
    if is_eng:
        lang_dict = eng
    else:
        lang_dict = rus

def update():
        btn["text"] = lang_dict["loc"]
        title1["text"] = lang_dict["loc1"]
        root.title(lang_dict["loc1"])   
        title3["text"] = lang_dict["loc2"]
        title4["text"] = lang_dict["loc3"]
        message = lang_dict["loc4"]
        title = lang_dict["loc5"]
        
# GUI
root["bg"] = "white"
root.title(lang_dict["loc1"])
root.geometry("370x450")
root.resizable(width=False, height=False)
color = "#eddda4"

rootmenu = Menu(root)
root.config(menu = rootmenu)
fm = Menu(rootmenu, tearoff = 0) 
fm1 = Menu(rootmenu, tearoff = 0) 

rootmenu.add_cascade(label = "Help" , menu = fm) # Help Menu
fm.add_command(label = 'About', command = about_click) # About Menu

rootmenu.add_cascade(label = "Settings" , menu = fm1) # Settings Menu
fm1.add_command(label = 'Switch language', command = change_lang) # language Menu

frame = Frame(root, bg="white")
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title1 = Label(frame, text=lang_dict["loc1"], bg="White", font=400) # Number Generator Text
title1.pack()

title2 = Label(frame, text="-----------------------------------------------------------------------------------------------------", bg="White", font=40)
title2.pack()

title3 = Label(frame, text="Введите первое число", bg="White", font=400) # Entering the first number
title3.pack()

inputFieldOne = Entry(frame, bg=color)
inputFieldOne.pack()

title4 = Label(frame, text="Введите второе число", bg="White", font=400) # Entering the second number
title4.pack()

inputFieldTwo = Entry(frame, bg=color)
inputFieldTwo.pack()

errorTitle = Label(frame, text="", bg="White", font=20)
errorTitle.pack()

title5 = Label(frame, text="-----------------------------------------------------------------------------------------------------", bg="White", font=40)
title5.pack()

frame_bottom = Frame(root, bg=color, bd=5)
frame_bottom.place(relx=0.15, rely=0.70, relwidth=0.7, relheight=0.1)

info = Label(frame_bottom, text=" ", bg=color, font=40) # Number output
info.pack()

btn = Button(frame, text=lang_dict["loc"], bg=color, command=btn_click) # Generate button Text
btn.pack()

while True:
    update()
    root.update()

root.mainloop()  

# END
# Captain Strannik was here
