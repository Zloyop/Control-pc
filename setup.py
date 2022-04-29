import subprocess
import tkinter
import config

def run_bot(root):
    root.destroy()
    subprocess.call("python main.py")

def submit():
    global token
    global id
    config.TOKEN += token
    config.IDS += id
    success = tkinter.Label(root, text="Настройки сохранены!")
    success.pack()

root = tkinter.Tk()
root.title("Конфигурация бота")
root.geometry("370x230")
root[ 'bg' ] = '#082757'
label = tkinter.Label(root, text="\n\nКонтроллер ПК с помощью бота\nЗаполни все поля ниже\n\nВведи токен бота:", bg='#082757', fg='#fff')
token = tkinter.Entry(root, width=50)
labol = tkinter.Label(root, text="Введи свой айди:", bg='#082757',fg='#fff')
id = tkinter.Entry(root)
tombolsubmit = tkinter.Button(root, text="Сохранить настройки", command=submit, bg='#133d7d', fg='#fff')
tombolrun = tkinter.Button(root, text="Запустить бота!", command= lambda: run_bot(root), bg='#133d7d', fg='#fff')

label.pack()
token.pack()
labol.pack()
id.pack()
tombolsubmit.pack()
tombolrun.pack()
root.mainloop()
