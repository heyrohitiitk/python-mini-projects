from itertools import cycle
from random import randrange 
from tkinter import Tk,	Canvas, messagebox, font
win=Tk()
win.title('Egg Catcher')

canvas_width=800
canvas_height=400

can=Canvas(win,width=canvas_width,height=canvas_height,bg='deep sky blue')
can.create_rectangle(-5,canvas_height-100,canvas_width+5,
	                       canvas_height+5,fill='sea green',width=0)
can.create_oval(-80,-80,120,120,fill='orange',width=0)
can.pack()

color_cycle=cycle(['sky blue','pink','yellow',
                 'red','blue','green',
             'black','white','grey','brown','cyan'])
egg_width=45
egg_height=55
egg_score=10
egg_speed=500
egg_interval=4000
difficulty_factor=0.95

catcher_color='dark blue'
catcher_width=100
catcher_height=100

catcher_start_x1 = canvas_width/2 - catcher_width/2
catcher_start_y1 = canvas_height - catcher_height -20 

catcher_start_x2 = catcher_start_x1 + catcher_width
catcher_start_y2 = catcher_start_y1 + catcher_height

catcher=can.create_arc(catcher_start_x1,catcher_start_y1,catcher_start_x2,
	                 catcher_start_y2,start=200,extent=140,style='arc',
	                  outline=catcher_color,width=3)

score=0
score_text=can.create_text(10,10,anchor='nw',font=['Arial',18,'bold'],
	                 fill='dark blue',text=f'Score: {score}')

lives_remaining=3
lives_text=can.create_text(canvas_width-10,10,anchor='ne',font=['Arial',18,'bold'],
	                 fill='dark blue',text=f'Lives: {lives_remaining}')


eggs=[]

def create_egg():
	x=randrange(10,740)
	y=40
	new_egg=can.create_oval(x,y,x+egg_width,y+egg_height,fill=next(color_cycle),width=0)
	eggs.append(new_egg)
	win.after(egg_interval,create_egg)

def move_eggs():
	for egg in eggs:
		(egg_x,egg_y,egg_x2,egg_y2)=can.coords(egg)
		can.move(egg,0,10)
		if egg_y2 > canvas_height:
			egg_dropped(egg)
	win.after(egg_speed,move_eggs)

def egg_dropped(egg):
	eggs.remove(egg)
	can.delete(egg)
	lose_a_life()
	if lives_remaining == 0:
		messagebox.showinfo('GAME OVER!',f'FINAL SCORE : {score}')
		win.destroy()

def lose_a_life():
	global lives_remaining
	lives_remaining -= 1
	can.itemconfig(lives_text,text=f'Lives : {lives_remaining}')

def check_catch():
	(catcher_x,catcher_y,catcher_x2,catcher_y2)=can.coords(catcher)
	for egg in eggs:
		(egg_x,egg_y,egg_x2,egg_y2)=can.coords(egg)
		if catcher_x < egg_x and egg_x2 < catcher_x2 and (catcher_y2-egg_y2)<40:
			eggs.remove(egg)
			can.delete(egg)
			increase_score(egg_score)
	win.after(100,check_catch)

def increase_score(egg_score):
	global score,egg_speed,egg_interval
	score += egg_score
	egg_speed = int(egg_speed*difficulty_factor)
	egg_interval = int(egg_interval*difficulty_factor)
	can.itemconfigure(score_text,text=f'Score: {score}')
 
def move_left(event):
	(x1,y1,x2,y2)=can.coords(catcher)
	if x1>0:
		can.move(catcher,-20,0)

def move_right(event):
	(x1,y1,x2,y2)=can.coords(catcher)
	if x2<canvas_width:
		can.move(catcher,20,0)

can.bind('<Left>',move_left)
can.bind('<Right>',move_right)
can.focus_set()

win.after(1000,create_egg)
win.after(1000,move_eggs)
win.after(1000,check_catch)

win.mainloop()