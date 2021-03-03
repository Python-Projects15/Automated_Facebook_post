# this project is created by vaibhav 
import webbrowser
import time
import pyautogui
def open_browser():
    webbrowser.open_new('http://www.facebook.com')
#opening browser    
open_browser()
time.sleep(15)

#opening post box
pyautogui.typewrite('p')
time.sleep(15)

#Writing and uploading post
pyautogui.typewrite('This post is automated done')
pyautogui.hotkey('ctrl', '\n')