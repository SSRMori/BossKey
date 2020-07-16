import tkinter
import keyboard
import win32gui, win32con
import functools
import ctypes, sys

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
        windowList.append(window)


def get_all_windows():
    windowList = []
    win32gui.EnumWindows(addWindow, windowList)
    return windowList

windowList = get_all_windows()
selectList = []
selectedList = []
win = tkinter.Tk()

def get_checked_window():
    global selectedList
    selectedList = []
    for i in range(len(selectList)):
        if selectList[i].get() == 1:
            selectedList.append(windowList[i])
    # print(selectedList)

def boss_key():
    # print("boss_key")
    global selectedList
    currentWindowList = get_all_windows()
    for window in currentWindowList:
        win32gui.ShowWindow(window, win32con.SW_MINIMIZE)
    for window in selectedList:
        # print(window)
        win32gui.ShowWindow(window, win32con.SW_MAXIMIZE)
        win32gui.SetForegroundWindow(window)

if __name__ == "__main__":
    if is_admin():
    # Code of your program here
        keyboard.add_hotkey('alt+d', boss_key)
        win.title("BOSSKEY")
        win.iconify()
        for i in range(len(windowList)):
            tempVar = tkinter.IntVar()
            tkinter.Checkbutton(win, text=win32gui.GetWindowText(windowList[i]), variable=tempVar).grid(row=i, sticky=tkinter.W)
            selectList.append(tempVar)
        tkinter.Button(win, text="Confirm", command=get_checked_window).grid(row=len(windowList) + 1)
        win.mainloop()
    else:
    # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    
