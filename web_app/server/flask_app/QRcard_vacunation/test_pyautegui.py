import pyautogui

screenWidth, screenHeight = pyautogui.size()
# Get the size of the primary monitor.
print(screenWidth)
print(screenHeight)

currentMouseX, currentMouseY = pyautogui.position()

print("x:"+str(currentMouseX)+" "+ "y: "+str(currentMouseY))

pyautogui.moveTo(10, 10)
# pyautogui.alert('This is the message to display.')

