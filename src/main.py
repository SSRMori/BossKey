import tkinter
import keyboard
import win32gui, win32con
import functools
import ctypes, sys
import json

windowList = []
selectList = []
selectedList = []
win = None
checkButtons = []
confirmButton = None
updateButton = None
# showAll = None
log_file = 'bossKey.log'

def write_log(string):
    f = open(log_file, "a+")
    f.write(string)
    f.write('\n')

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def addWindow(window, windowList):
    if (win32gui.IsWindow(window) 
    and win32gui.IsWindowEnabled(window) 
    and win32gui.IsWindowVisible(window) 
    and win32gui.GetWindowText(window) != ""):
        write_log('Add window ' + str(window) + ' to windowList')
        windowList.append(window)

def get_all_windows():
    write_log('Start get all windows')
    windowList = []
    win32gui.EnumWindows(addWindow, windowList)
    return windowList

def get_checked_window():
    write_log('Start get seleted windows')
    global selectedList
    global windowList
    selectedList = []
    for i in range(len(selectList)):
        if selectList[i].get() == 1:
            write_log('window ' + str(windowList[i]) + " is selected")
            selectedList.append(windowList[i])
    # print(selectedList)

def init_window():
    global win
    global windowList
    global checkButtons
    global confirmButton
    global updateButton
    global selectList
    global selectedList
    selectList = []
    selectedList = []
    windowList = []
    # global showAll
    write_log("init window")
    windowList = get_all_windows()
    for i in range(len(windowList)):
        tempVar = tkinter.IntVar()
        checkButtons.append(tkinter.Checkbutton(win, text=win32gui.GetWindowText(windowList[i]), variable=tempVar))
        # print(len(checkButtons))
        checkButtons[len(checkButtons)-1].grid(row=i, sticky=tkinter.W)
        selectList.append(tempVar)
    confirmButton = tkinter.Button(win, text="Confirm", command=get_checked_window)
    confirmButton.grid(row=len(windowList) + 1)
    updateButton = tkinter.Button(win, text="update", command=update_window)
    updateButton.grid(row=len(windowList) + 2)
    # showAll = tkinter.Button(win, text="showAll", command=showAllWindow)
    # showAll.grid(row=len(windowList) + 3)

def exit_boss_key():
    global windowList
    for window in windowList:
        win32gui.ShowWindow(window, win32con.SW_SHOW)
        write_log("show window " + str(window))
        # win32gui.ShowWindow(window, win32con.SW_MAXIMIZE)
        # win32gui.SetForegroundWindow(window)

def update_window():
    write_log("update window")
    global checkButtons
    global confirmButton
    global updateButton
    # global showAll
    for button in checkButtons:
        button.destroy()
    checkButtons = []
    confirmButton.destroy()
    confirmButton = None
    updateButton.destroy()
    updateButton = None
    # showAll.destroy()
    # showAll = None
    init_window()


def boss_key():
    # print("boss_key")
    global selectedList
    currentWindowList = get_all_windows()
    for window in currentWindowList:
        win32gui.ShowWindow(window, win32con.SW_HIDE)
        write_log("hide window " + str(window))
    for window in selectedList:
        write_log("show window " + str(window))
        # print(window)
        win32gui.ShowWindow(window, win32con.SW_SHOW)
        win32gui.ShowWindow(window, win32con.SW_MAXIMIZE)
        win32gui.SetForegroundWindow(window)

def hideWindow():
    # win.iconify()
    global win
    win.withdraw()

def showWindow():
    global win
    win.deiconify()

if __name__ == "__main__":
    if is_admin():# or True:
    # Code of your program here
        win = tkinter.Tk()
        win.iconbitmap('./../image/icon.ico')
        win.title("BOSSKEY")
        f = open('hotkey.json')
        if f is None:
            keyboard.add_hotkey('alt+d', boss_key)
            keyboard.add_hotkey('esc+alt+d', exit_boss_key)
            keyboard.add_hotkey('ctrl+alt+shift+h', hideWindow)
            keyboard.add_hotkey('ctrl+alt+shift+s', showWindow)
        else:
            settings = json.load(f)
            # print(settings)
            keyboard.add_hotkey(settings['bossKey'], boss_key)
            keyboard.add_hotkey(settings['exitBossKey'], exit_boss_key)
            keyboard.add_hotkey(settings['hide'], hideWindow)
            keyboard.add_hotkey(settings['show'], showWindow)
        # win.iconify()
        init_window()
        win.mainloop()
    else:
    # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    
