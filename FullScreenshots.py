# By GA
# Pre-install pyautogui, psutil, pillow (pip install <name>)
import os
import pyautogui
import psutil
import sys
import time 

def checkIfProcessRunning(processName):
    '''
    Check if there is any running process that contains the given name processName.
    '''
    #Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if processName.lower() in proc.name().lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False;

def checkIfWindowMax(windowTitle):
    '''
    Check if the active window is maximized given the window title. 
    It will maximize it in case it is not.
    '''
    WinTitle = pyautogui.getWindowsWithTitle(windowTitle)[0] 
    if WinTitle.isMaximized is False:
        return WinTitle.maximize()
    else:
        print('It was already maximized.')

# Check if any Steam process was running or not.
if checkIfProcessRunning('Steam'):
    print('Yes, a Steam process was running')
    checkIfWindowMax('steam')
    
else:
    print('No Steam process was running \n ...')
    print('Proceeding to open Steam...')
    
    # If no process was running, it will open the app using the appPath provided.
    appPath = 'C:\Program Files (x86)\Steam\steam.exe'
    os.startfile(appPath) 
    time.sleep(3)
    getWinTitle = pyautogui.getWindowsWithTitle('steam')[0] 
    getActWin = pyautogui.getActiveWindow()
    #Login window
    if getWinTitle == getActWin:
        userName = pyautogui.prompt('What is your username?' + '\n' + 'Press Cancel if the username is already typed in the box.')
        password = pyautogui.password ('What is your password?')
        if userName and password != None: #TODO: If the username is there but is wrong. Replace the username.
            time.sleep(1)
            pyautogui.click(567,299)
            pyautogui.write(userName +'\t')
            pyautogui.write(password)
            pyautogui.write('\n')
            time.sleep(5)
            checkIfWindowMax('steam')
        elif userName == None and password != None:
            time.sleep(1)
            pyautogui.click(565,332);pyautogui.write(password)
            pyautogui.write('\n')
            time.sleep(5)
            checkIfWindowMax('steam')
        elif userName != None and password == None:
            print('No password was provided.\n'+'Ending program.')
            sys.exit()
        else:
            print('No username nor password was provided.\n'+'Ending program.')
            sys.exit()
    else:
        print('The window is not active.')
        sys.exit()
time.sleep(3)

def locateImageOnScreen(ImageName):
    """Locates the image on the active screen. The image must be saved in the current directory.
    It will exit the program if the image is not found.

    Args:
        ImageName (string): Name of the image that should be locates on the screen.
        Example ('Profile.png')
    """
    location =   pyautogui.locateOnScreen(ImageName)  
    try: 
        for x in location:
            return location
    except:
        sys.exit('The image could not be found in the active screen. \n'+'Stopping program.')
        
# Go to the 'PROFILE' section on the page and take a screenshot.
imageName = 'Profile.PNG'
locateImageOnScreen(imageName)
print('Image found.')
pyautogui.moveTo(imageName)
pyautogui.write(['down','down','\n'],interval=0.2)
pyautogui.sleep(3)
myScreen = pyautogui.screenshot(region=(189,82,669,234))
myScreen.save('ProfileScreenshot.png')
print('Screenshot saved.')

# Save image to a Word Doc
