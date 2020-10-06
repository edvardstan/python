import pyautogui as pg


i = 1
while i < 5 :
    pg.leftClick(500, 10, 0.1)
    pg.press('down')
    pg.hotkey('ctrl', 'c')
    pg.leftClick(1670, 15, 0.1)
    pg.press('down')
    pg.hotkey('ctrl', 'v')
    i = i + 1