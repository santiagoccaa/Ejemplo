import pyautogui, webbrowser
from time import sleep

webbrowser.open("https://web.whatsapp.com/send?phone=+573017022274")
sleep(10)

pyautogui.typewrite("Hola Como estas? \n Te ves igual, te ves igual")
pyautogui.press("enter")
'''
with open ("spam.txt", "r") as file:
	for line in file:
		pyautogui.typewrite(line)
		pyautogui.press("enter")

'''