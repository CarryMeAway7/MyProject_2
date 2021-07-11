from selenium import webdriver
import time
import pickle
from tkinter import *


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    executable_path="C:\\Users\\Aleksandr\\Documents\\ycheba\\selenium_python1\\chromedriver.exe",
    options=options
)

def btn_click():
    try:
        cookie = CokField.get()
        site = siteField.get()

        driver.get(site)
        time.sleep(3)

        for cookie in pickle.load(open(f"{cookie}_cookies", "rb")):
            driver.add_cookie(cookie)

        time.sleep(5)
        driver.refresh()
        time.sleep(20)

    except Exception as ex:
        print(ex)

root = Tk()

root['bg'] = '#fafafa'
root.title('куки')
root.wm_attributes('-alpha',0.7)
root.geometry('200x300')

root.resizable(width=False, height=False)

canvas = Canvas(root, height=200, width=300)
canvas.pack()

frame = Frame(root, bg='gray')
frame.place(relwidth=1,relheight=1)

title = Label(frame, text='Сайт:', font=10)
title.pack()
siteField=Entry(frame, bg='white')
siteField.pack()

btn = Button(frame, text='Сохранить', bg='white', command=btn_click)
btn.pack()

title = Label(frame, text='Название куки:', font=10)
title.pack()
CokField=Entry(frame, bg='white')
CokField.pack()

root.mainloop()