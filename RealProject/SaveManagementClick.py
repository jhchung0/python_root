import pyautogui

# print (pyautogui.position())

# pyautogui.moveTo(x=226, y=160)
# pyautogui.click(x=226, y=160)
i = pyautogui.locateOnScreen('d:/dev/Python_root/RealProject/Save_Yesno.png')
print(i)
j = pyautogui.center(i)
print (j)
pyautogui.click(j)
pyautogui.click(j)
