import tkinter as tk
from tkinter import *
import time
import random as rnd
import tkinter.font as font
win=Tk()
win.title('MATCH-MAKER')
#################################
def show_symbol(x,y):
	global first,match_color
	global previousx,previousy
	buttons[x,y]['text']=button_symbol[x,y]
	buttons[x,y].update_idletasks()

	if first:
		previousx=x
		previousy=y
		first=False
	elif previousx!=x or previousy!=y:
		if buttons[previousx,previousy]['text']!=buttons[x,y]['text']:
			time.sleep(0.5)
			buttons[previousx,previousy]['text']=' '
			buttons[x,y]['text']=' '
		else:
			buttons[previousx,previousy]['background']=match_color
			buttons[x,y]['background']=match_color
			buttons[previousx,previousy]['command']=DISABLED
			buttons[x,y]['command']=DISABLED
		first=True

win.resizable(width=False,height=False)    #To fix the size of window
first=True
previousx=0
previousy=0
match_color='deep sky blue'
buttons={}
button_symbol={}
symbols=[u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
         u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728',
         u'\u2702',u'\u2705',u'\u2708',u'\u2709',u'\u270A',u'\u270B',
         u'\u270C',u'\u270F',u'\u2712',u'\u2714',u'\u2716',u'\u2728']
rnd.shuffle(symbols)
myFont = font.Font(size=30)
for x in range(6):
	for y in range(4):
		button=Button(width=3,height=2,command=lambda x=x,y=y:show_symbol(x,y),activebackground='cyan')
		button['font']=myFont
		button.grid(column=x,row=y)
		buttons[x,y]=button
		button_symbol[x,y]=symbols.pop()

#################################
win.mainloop()