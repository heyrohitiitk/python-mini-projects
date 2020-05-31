from tkinter import *
from tkinter import ttk
import tkinter as tk
from math import *
def isint(val):
	if (val-floor(val))==0:
		return True
	else:
		return False
def add(a,b):
	val=a+b
	if isint(val):
		return int(val)
	else:
		return val	
def sub(a,b):
	val=a-b
	if isint(val):
		return int(val)
	else:
		return val	
def mul(a,b):
	val=a*b
	if isint(val):
		return int(val)
	else:
		return val	
def div(a,b):
	if b==0:
		return 'Math Error'
	else:
		val=a/b
		if isint(val):
			return int(val)
		else:
			return val 
def mod(a,b):
	return int(a%b)
def expo(a,b):
	val=a**b
	if isint(val):
		return int(val)
	else:
		return val	
def lcm(a,b):
	big=a if a>b else b
	var=big
	while var<=a*b:
		if var%a==0 and var%b==0:
			break
		else:
			var=var+big
	return int(var)
def hcf(a,b):
	if a==0:
		return b
	return int(hcf(b%a,a))
def sqroot(a):
	val=sqrt(a)
	if isint(val):
		return int(val)
	else:
		return val	
def cuberoot(a):
	val=a**(1/3)
	val2=ceil(val)
	if (val2-val)<0.0001:
		return val2
	else:
		return val
def cube(a):
	val=a**3
	if isint(val):
		return int(val)
	else:
		return val
def square(a):
	val=a**2
	if isint(val):
		return int(val)
	else:
		return val
def factor(val):
	res=""
	val=int(val)
	for i in range(1,val//2+2):
		if (val%i)==0:
			res=res+str(i)+" "
	return res
def isprime(val):
	n=ceil(sqrt(val))
	for i in range(2,n+1):
		if val%i==0:
			return False	
	return True
def primefactor(val):
	val=int(val)
	res=""
	for i in range(2,ceil(sqrt(val))+1):
		if (val%i==0):
			res=res+str(i)+" "
			while(val%i==0):
				val=val//i
	if val>1:
		res=res+str(val)
	return res

def extract_from_text(text):
	li=[]
	for t in text.split():
		try:
			li.append(float(t))
		except:
			pass
	return li

def calculate():
	text=textin.get()
	for word in text.split():
		if word.upper() in operations.keys():
			try:
				if word.upper() in singleopr.keys():
					li=extract_from_text(text)
					r=singleopr[word.upper()](li[0])
				else:
					li=extract_from_text(text)
					r=operations[word.upper()](li[0],li[1])
				list.delete(0,END)
				list.insert(END,r)
			except:
				list.delete(0,END)
				list.insert(END,'Something went wrong please try again')
			finally:
				break
		elif word.upper() not in operations.keys():
			list.delete(0,END)
			list.insert(END,'Something went wrong please try again')

operations={'ADD':add,'ADDITION':add,'SUM':add,'PLUS':add,'+':add,
            'SUB':sub,'SUBTRACT':sub,'MINUS':sub,'DIFFERENCE':sub,'-':sub,
            'LCM':lcm,'LOWEST COMMON MULTIPLE':lcm,'X':mul,'/':div,'%':mod,
             'HCF':hcf,'GREATEST COMMON DIVISOR':hcf,'GCD':hcf,
             'MUL':mul,'MULTIPLY':mul,'PRODUCT':mul,'MULTIPLICATION0':mul,'*':mul,
             'DIV':div,'DIVIDE':div,'DIVISION':div,'MOD':mod,'REMAINDER':mod,'MODULUS':mod,
             'POWER':expo,'RAISE':expo,'^':expo,'EXPONENT':expo,'BY':div,
             'SQUAREROOT':sqroot,'UNDERROOT':sqroot,'SQRT':sqroot,
             'CUBEROOT':cuberoot,'CUBE':cube,'SQUARE':square,
             'FACTORS':factor,'FACTOR':factor,'PRIMEFACTOR':primefactor,
             'PRIMEFACTORS':primefactor}

singleopr={'SQUAREROOT':sqroot,'UNDERROOT':sqroot,'SQUARE-ROOT':sqroot,'SQRT':sqroot,
           'CUBEROOT':cuberoot,'CUBE':cube,'SQUARE':square,
           'FACTORS':factor,'FACTOR':factor,'PRIMEFACTOR':primefactor,
           'PRIMEFACTORS':primefactor}

################################# FRONT-END ##########################################################
win=Tk()
win.title('Smart Calculator...')
win.geometry('500x300')
win.resizable(0,0)
win.configure(bg='sky blue')

label1=Label(win,text='I am a Smart Calculator',bg='white',font=("Helvetica", 16),relief=RAISED,padx=10,width=20)
label1.place(x=130,y=10)

label2=Label(win,text='My Name is TiKi',bg='white',font=("Helvetica", 16),relief=RAISED,padx=10,width=15)
label2.place(x=156,y=50)

label3=Label(win,text='How can i Help you',bg='white',font=("Helvetica", 16),relief=RAISED,padx=10,width=20)
label3.place(x=126,y=130)

textin=StringVar()
entry1=ttk.Entry(win,width=50,textvariable=textin,justify=CENTER)
entry1.focus_force()
entry1.place(x=103,y=180)

but1=Button(win,text='Just this!',bg='cyan',relief=RIDGE,padx=5,activebackground='sky blue',command=calculate)
but1.place(x=218,y=210)

list=Listbox(win,width=20,height=3)
list.place(x=187,y=240)

win.mainloop()