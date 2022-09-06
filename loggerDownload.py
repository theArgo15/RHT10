import pyautogui
import time
def singleLogger(loggerNumber):
    #Click connect (890,470)
    pyautogui.click(890,470)
    time.sleep(.3)
    #Click download icon (416, 283)
    pyautogui.click(416, 283)
    time.sleep(.3)
    #click download box (858,586)
    pyautogui.click(858,586)
    #wait for download
    print('Searching for completed status bar...')
    while True:
        px = pyautogui.pixel(1123, 356)
        if px[0]==0:
            print('Status bar full!')
            break
    time.sleep(.3) 
    #type Logger# ENTER
    loggerName = f'Logger{loggerNumber}'
    pyautogui.typewrite(loggerName)
    pyautogui.press('enter')
    #click view (965,586)
    pyautogui.click(965,586)
    time.sleep(.3)
    #click save (510,286)
    pyautogui.click(510,286)
    time.sleep(.3)
    # type logger# ENTER
    pyautogui.typewrite(loggerName.lower())
    pyautogui.press('enter')
    time.sleep(.3)
    #click logger settings (446,282)
    pyautogui.click(446,282)
    time.sleep(2)
    #Click logger name text field (918,452)
    pyautogui.click(918,452)
    time.sleep(2)
    #type backspace 9 times, type Logger#
    pyautogui.press(['backspace']*9)
    pyautogui.typewrite(loggerName)
    #click setup (1066,707)
    pyautogui.click(1066,707)
    time.sleep(1)
    #click Okay (954,586)
    pyautogui.click(954,586)
    time.sleep(.3)
    #click close (1503, 230)
    # x=input('Done?')
    # pyautogui.click(1503, 230)
    # time.sleep(.3)
def tester():
    pass
if __name__ == "__main__":
    #loggerNumber = '5'
    print('Do the first one manually for now')
    for loggerNumber in range(1,20):
        singleLogger(loggerNumber)
        #click close (1503, 230)
        x=input('Done?')
        pyautogui.click(1503, 230)
        if loggerNumber <19:
            x=input(f'Load logger {loggerNumber+1} now:')
