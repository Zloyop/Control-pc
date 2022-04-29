from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import webbrowser
import subprocess
import pyautogui
import platform
import requests
import keyboard
import logging
import getpass
import psutil
import socket
import config
import distro
import time
import os

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

markup1 = ReplyKeyboardMarkup(resize_keyboard=True)
btn1_1 = KeyboardButton("/screenshot")
btn1_2 = KeyboardButton("/shutdown")
btn1_3 = KeyboardButton("/restart")
btn1_4 = KeyboardButton("/ytfull")
btn1_5 = KeyboardButton("/ytnext")
btn1_6 = KeyboardButton("/status")
btn1_7 = KeyboardButton("/ip")
btn1_8 = KeyboardButton("/yt")
btn1_9 = KeyboardButton("/start")
btn1_10 = KeyboardButton("/remove")
markup1.row(btn1_9, btn1_10)
markup1.row(btn1_1, btn1_2)
markup1.row(btn1_3, btn1_4)
markup1.row(btn1_5, btn1_6)
markup1.row(btn1_7, btn1_8)

markup2 = ReplyKeyboardMarkup(resize_keyboard=True)
btn2_1 = KeyboardButton("📸Скриншот")
btn2_2 = KeyboardButton("📵Выключить")
btn2_3 = KeyboardButton("♻️Рестарт")
btn2_4 = KeyboardButton("🔰Айпи")
btn2_5 = KeyboardButton("🏧Статус")
markup2.row(btn1_9)
markup2.row(btn2_2, btn2_3)
markup2.row(btn2_4, btn2_5)
markup2.row(btn2_1)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    if message.from_user.id in config.IDS:
        await message.reply("""Мои команды:
/screenshot - сделать скриншот экрана на ПК
/pkeyboard - красивые кнопки комманд
/ckeyboard - кнопки команд
/shutdown - выключение ПК
/restart - перезагрузить ПК
/ytfull - открыть видео на весь экран (обязательно надо открыть ютуб на ПК)
/ytnext - следуйщее видео (обязательно надо открыть ютуб на ПК)
/status - статус ПК
/remove - убрать клавиатуру
/input [question] - отправить вопрос с ответом
/url [htpps://url] - перейти по ссылке
/msg [text] - вывести сообщение на ПК
/ip - узнать айпи
/yt - открыть ютуб""")

@dp.message_handler()
async def keyboard(message: types.Message):
    if message.from_user.id in config.IDS:
        txt = message.text
        if txt == '📸Скриншот':
            filename = f"{time.time()}.jpg"
            pyautogui.screenshot(filename)
            with open(filename, "rb") as img:
                await bot.send_photo(message.chat.id, img)
            os.remove(filename)
        elif txt == '📵Выключить':
            if platform.system() == "Windows":
                subprocess.call('shutdown /s')
            else:
                subprocess.call('shutdown -h now')
            await message.reply("Выключение")
        elif txt == '♻️Рестарт':
            if platform.system() == "Windows":
                subprocess.call('shutdown /r')
            else:
                subprocess.call('reboot')
        elif txt == '🔰Айпи':
            a = requests.get("http://jsonip.com/").json()
            await message.reply(f"Айпи: {a['ip']}")
        elif txt == '🏧Статус':
            text = ""
            text += "Имя компа: " + socket.gethostname()
            text += "\nПользователь: " + getpass.getuser()
            if platform.system() == "Windows":
                text += "\nOS: Windows " + platform.win32_ver()[0]
            else:
                text += "\nOS: " + " ".join(distro.linux_distribution()[:2])
            text += "\nCPU: " + str(psutil.cpu_percent()) + "%"
            text += "\nОЗУ: " + str(
                int(psutil.virtual_memory().percent)) + "%"
            if psutil.sensors_battery():
                if psutil.sensors_battery().power_plugged is True:
                    text += "\nЗаряд: " + str(
                        format(psutil.sensors_battery().percent, ".0f")) \
                            + "% | Заряжается"
                else:
                    text += "\nБатарея: " + str(
                        format(psutil.sensors_battery().percent, ".0f")) + "%"
            await message.reply(f"{text}")
        elif txt == '/ckeyboard':
            await message.reply("Выполнено", reply_markup=markup1)
        elif txt == '/pkeyboard':
            await message.reply("Выполнено", reply_markup=markup2)
        elif txt == '/ip':
            a = requests.get("http://jsonip.com/").json()
            await message.reply(f"Айпи: {a['ip']}")
        elif txt == '/screenshot':
            filename = f"{time.time()}.jpg"
            pyautogui.screenshot(filename)
            with open(filename, "rb") as img:
                await bot.send_photo(message.chat.id, img)
            os.remove(filename)
        elif txt == '/msg':
            msg = message.text[5:]
            if msg == " ":
                await message.reply("Укажи сообщение")
            else:
                pyautogui.alert(msg, "~") 
                await message.reply("Выполнено")
        elif txt == '/input':
            input = message.text[7:]
            if input == " ":
                await message.reply("Укажи сообщение")
            else:
                try:
                    answer = pyautogui.prompt(input, "~")
                    await message.reply("Выполнено")
                    await bot.send_message(message.chat.id, answer)
                except Exception:
                    await bot.send_message(message.chat.id, "Что-то пошло не так...")
        elif txt == '/status':
            text = ""
            text += "Имя компа: " + socket.gethostname()
            text += "\nПользователь: " + getpass.getuser()
            if platform.system() == "Windows":
                text += "\nOS: Windows " + platform.win32_ver()[0]
            else:
                text += "\nOS: " + " ".join(distro.linux_distribution()[:2])
            text += "\nCPU: " + str(psutil.cpu_percent()) + "%"
            text += "\nОЗУ: " + str(
                int(psutil.virtual_memory().percent)) + "%"
            if psutil.sensors_battery():
                if psutil.sensors_battery().power_plugged is True:
                    text += "\nЗаряд: " + str(
                        format(psutil.sensors_battery().percent, ".0f")) \
                            + "% | Заряжается"
                else:
                    text += "\nБатарея: " + str(
                        format(psutil.sensors_battery().percent, ".0f")) + "%"
            await message.reply(f"{text}")
        elif txt == '/ytnext':
            keyboard.send('shift+n')
            await message.reply("Выполнено")
        elif txt == '/ytfull':
            keyboard.send('f')
            await message.reply("Выполнено")
        elif txt == '/close':
            keyboard.send('alt+f4')
            await message.reply("Выполнено")
        elif txt == '/shutdown':
            if platform.system() == "Windows":
                subprocess.call('shutdown /s')
            else:
                subprocess.call('shutdown -h now')
            await message.reply("Выключение")
        elif txt == '/restart':
            if platform.system() == "Windows":
                subprocess.call('shutdown /r')
            else:
                subprocess.call('reboot')
        elif txt == '/url':
            url = message.text[5:]
            if url == " ":
                await message.reply("Укажи ссылку")
            else:
                webbrowser.open(url)
                await message.reply("Выполнено")
        elif txt == '/yt':
            webbrowser.open('https://www.youtube.com')
            await message.reply("Выполнено")
        elif txt == '/start':
            await message.reply("""Мои команды:
/screenshot - сделать скриншот экрана на ПК
/pkeyboard - красивые кнопки комманд
/ckeyboard - кнопки команд
/shutdown - выключение ПК
/restart - перезагрузить ПК
/ytfull - открыть видео на весь экран (обязательно надо открыть ютуб на ПК)
/ytnext - следуйщее видео (обязательно надо открыть ютуб на ПК)
/status - статус ПК
/input [question] - отправить вопрос с ответом
/url [htpps://url] - перейти по ссылке
/msg [text] - вывести сообщение на ПК
/id - узнать свой ID в телеграм
/ip - узнать айпи
/yt - открыть ютуб""")
        elif message.text == '/id':
            await message.reply(f'Твой ID: `{message.from_user.id}`', parse_mode='MarkdownV2')
        elif txt =='/remove':
            await message.reply("Выполнено", reply_markup=ReplyKeyboardRemove())
    elif message.from_user.id not in config.IDS:
        if message.text == '/id':
            await message.reply(f'Твой ID: `{message.from_user.id}`', parse_mode='MarkdownV2')
        else:
            await message.reply("Вы не можете использовать данного бота")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
