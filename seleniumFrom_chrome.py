from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        site = siteField.get()
        htmllog = htmllogField.get()
        login = loginInput.get()
        htmlpas = htmlpasField.get()
        password = passField.get()
        cookie = CokField.get()

        driver.get(site)
        time.sleep(10)

        email_input = driver.find_element_by_id(htmllog)
        email_input.clear()
        email_input.send_keys(login)
        time.sleep(5)

        password_input = driver.find_element_by_id(htmlpas)
        password_input.clear()
        password_input.send_keys(password)
        time.sleep(5)
        password_input.send_keys(Keys.ENTER)
        time.sleep(10)

        pickle.dump(driver.get_cookies(), open(f"{cookie}_cookies", "wb"))

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

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

title = Label(frame, text='Логин:', font=10)
title.pack()
loginInput = Entry(frame, bg='white')
loginInput.pack()

title = Label(frame, text='Пароль:', font=10)
title.pack()
passField=Entry(frame, bg='white',show='*')
passField.pack()

title = Label(frame, text='Сайт:', font=10)
title.pack()
siteField=Entry(frame, bg='white')
siteField.pack()

title = Label(frame, text='HtmlLoginId:', font=10)
title.pack()
htmllogField=Entry(frame, bg='white')
htmllogField.pack()

title = Label(frame, text='HtmlPasId:', font=10)
title.pack()
htmlpasField=Entry(frame, bg='white')
htmlpasField.pack()

btn = Button(frame, text='Сохранить', bg='white', command=btn_click)
btn.pack()

title = Label(frame, text='Название куки:', font=10)
title.pack()
CokField=Entry(frame, bg='white')
CokField.pack()

root.mainloop()