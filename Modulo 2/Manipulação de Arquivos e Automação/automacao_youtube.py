import pyautogui as pg
from time import sleep
#pip install
#pg.mouseInfo()

pg.press('win')
#pg.write('chrome')
pg.press('enter')
pg.write('www.youtube.com')
pg.press('enter')
sleep(3)
pg.moveTo(689,114, duration=1.5 )
pg.click()
pg.write('SZA-Snooze')
pg.press('enter')
pg.moveTo(696,632, duration=1.5 )
pg.click()