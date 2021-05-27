import pyautogui
# Don't forget to use aTry and Except statements in case 
# the program can't find the img.
# try: 
#   location = pyautogui.locateOnScreen('notes.png')
# except:
#   print ('The image could not be found.')

getWindow = pyautogui.getWindowsWithTitle('Notepad') #gets all the windows with the string in the title
assignWindow = getWindow[0] #bc is a list, pass the first value of the list to the var assignWindow

while assignWindow.isMinimized == True:
    print('It is minimized! Proceeding to maximize...')
    assignWindow.maximize()
else:
    print('It is maximized.')

# print (assignWindow.isActive)

pyautogui.click(65,104);  pyautogui.write('Holi :)')

