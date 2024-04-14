import tkinter as tk
from functools import reduce
win = tk.Tk()
win.title('calculator 1.0')
win.geometry('292x454+1200+200')
win.resizable(False,False)
win.configure(bg='#595959',border=0)
def len_border():
	global result
	if len(result) < 14:
		return True
	else:
		False
def print_num():
	pass
def print_1():
	global result
	if len_border():
		result += '1'
		label_result['text'] = result
def print_2():
	global result

	if len_border():
		result += '2'
		label_result['text'] = result
def print_3():
	global result

	if len_border():
		result += '3'
		label_result['text'] = result
def print_4():
	global result
	if len_border():
		result += '4'
		label_result['text'] = result
def print_5():
	global result

	if len_border():
		result += '5'
		label_result['text'] = result
def print_6():
	global result
	if len_border():
		result += '6'
		label_result['text'] = result
def print_7():
	global result
	if len_border():
		result += '7'
		label_result['text'] = result
def print_8():
	global result
	if len_border():
		result += '8'
		label_result['text'] = result
def print_9():
	global result
	if len_border():
		result += '9'
		label_result['text'] = result
def print_0():
	global result
	if len_border() and result != '0':
		result += '0'
		label_result['text'] = result

def return_result():
	global result,operation,num2
	if btn_round.get() == '':
	    num_to_round = 2
	else:
		if int(btn_round.get())>8:
			num_to_round = 8
		else:
			num_to_round = int(btn_round.get())
	num2 = result
	otvet = round(operations[operation](num1, num2), num_to_round)
	if len(str(otvet))<14:
		label_result['text'] = otvet
		operation = ''
		result = otvet
	else:
		label_result['text'] = 'ERROR\nLenResult'

def print_minus():
	global result,operation,num1
	num1 = result
	operation = '-'
	result = ''
	label_result['text'] = operation
def print_plus():
	global result,operation,num1
	num1 = result
	operation = '+'
	result = ''
	label_result['text'] = operation
def print_multiply():
	global result,operation,num1
	num1 = result
	operation = '*'
	result = ''
	label_result['text'] = operation
def print_division():
	global result,operation,num1
	num1 = result
	operation = '/'
	result = ''
	label_result['text'] = operation

def del_sym():
	global result
	result = str(result)[:-1]
	label_result['text'] = result
def del_all():
	global result
	result = ''
	label_result['text'] = result

operations = {'-':lambda x,y: int(x)-int(y),'+':lambda x,y: int(x)+int(y),'/':lambda x,y: int(x)/int(y),'*':lambda x,y: int(x)*int(y)}
operation = ''
result = ''
num1=0
num2=0

#return result
label_result = tk.Label(win,text=f'{result}',background='gray',font=('unispace',25))
label_result.grid(row=0,column=0,stick='wesn',columnspan=4)


btn_return_result = tk.Button(win,text='=',background='#2c9c1f',border=1,borderwidth=2,command=return_result,width=9,height=4,font=('unispace',10,'bold'),activebackground='#363636',)
btn_return_result.grid(row=1,column=1,columnspan=3,stick='we')

#numbers
btn_1 = tk.Button(win,text='1',command=print_1,width=8,height=4,background='#525252',foreground='#a3a3a3',border=1,borderwidth=2,activebackground='#4a4a4a',activeforeground='#8a8a8a',font=('unispace',10))
btn_1.grid(row=4,column=0)
btn_2 = tk.Button(win,text='2',command=print_2,width=8,height=4,background='#525252',foreground='#a3a3a3',border=1,borderwidth=2,activebackground='#4a4a4a',activeforeground='#8a8a8a',font=('unispace',10))
btn_2.grid(row=4,column=1)
btn_3 = tk.Button(win,text='3',command=print_3,width=8,height=4,background='#525252',foreground='#a3a3a3',border=1,borderwidth=2,activebackground='#4a4a4a',activeforeground='#8a8a8a',font=('unispace',10))
btn_3.grid(row=4,column=2)
btn_4 = tk.Button(win,text='4',command=print_4,width=8,height=4,background='#525252',foreground='#a3a3a3',border=1,borderwidth=2,activebackground='#4a4a4a',activeforeground='#8a8a8a',font=('unispace',10))
btn_4.grid(row=3,column=0)
btn_5 = tk.Button(win,text='5',command=print_5,width=8,height=4,background='#525252',foreground='#a3a3a3',border=1,borderwidth=2,activebackground='#4a4a4a',activeforeground='#8a8a8a',font=('unispace',10))
btn_5.grid(row=3,column=1)
btn_6 = tk.Button(win,text='6',command=print_6,width=8,height=4,background='#525252',foreground='#a3a3a3',border=1,borderwidth=2,activebackground='#4a4a4a',activeforeground='#8a8a8a',font=('unispace',10))
btn_6.grid(row=3,column=2)
btn_7 = tk.Button(win,text='7',command=print_7,width=8,height=4,background='#525252',foreground='#a3a3a3',border=1,borderwidth=2,activebackground='#4a4a4a',activeforeground='#8a8a8a',font=('unispace',10))
btn_7.grid(row=2,column=0)
btn_8 = tk.Button(win,text='8',command=print_8,width=8,height=4,background='#525252',foreground='#a3a3a3',border=1,borderwidth=2,activebackground='#4a4a4a',activeforeground='#8a8a8a',font=('unispace',10))
btn_8.grid(row=2,column=1)
btn_9 = tk.Button(win,text='9',command=print_9,width=8,height=4,background='#525252',foreground='#a3a3a3',border=1,borderwidth=2,activebackground='#4a4a4a',activeforeground='#8a8a8a',font=('unispace',10))
btn_9.grid(row=2,column=2)
btn_0 = tk.Button(win,text='0',command=print_0,width=8,height=4,background='#525252',foreground='#a3a3a3',border=1,borderwidth=2,activebackground='#4a4a4a',activeforeground='#8a8a8a',font=('unispace',10))
btn_0.grid(row=5,column=0)

#operations
btn_minus = tk.Button(win,text='-',command=print_minus,width=8,height=4,background='#363636',foreground='#a3a3a3',border=0,activebackground='#2e2e2e',activeforeground='#808080',borderwidth=2,font=('unispace',10))
btn_minus.grid(row=4,column=3)
btn_plus= tk.Button(win,text='+',command=print_plus,width=8,height=4,background='#363636',foreground='#a3a3a3',border=0,activebackground='#2e2e2e',activeforeground='#808080',borderwidth=2,font=('unispace',10))
btn_plus.grid(row=5,column=3)
btn_division = tk.Button(win,text='/',command=print_division,width=8,height=4,background='#363636',foreground='#a3a3a3',border=0,activebackground='#2e2e2e',activeforeground='#808080',borderwidth=2,font=('unispace',10))
btn_division.grid(row=2,column=3)
btn_multiply = tk.Button(win,text='*',command=print_multiply,width=8,height=4,background='#363636',foreground='#a3a3a3',border=0,activebackground='#2e2e2e',activeforeground='#808080',borderwidth=2,font=('unispace',10))
btn_multiply.grid(row=3,column=3)
btn_del= tk.Button(win,text='del',command=del_sym,width=8,height=4,background='#363636',foreground='#a3a3a3',border=0,activebackground='#2e2e2e',activeforeground='#808080',borderwidth=2,font=('unispace',10))
btn_del.grid(row=5,column=2)
btn_del_all = tk.Button(win,text='del_all',command=del_all,width=8,height=4,background='#363636',foreground='#a3a3a3',border=0,activebackground='#2e2e2e',activeforeground='#808080',borderwidth=2,font=('unispace',10))
btn_del_all.grid(row=5,column=1)

btn_round = tk.Entry(win,width=8,background='#363636',foreground='#a3a3a3',border=0,borderwidth=2,font=('unispace',10))
btn_round.grid(row=1,column=0)

label_round = tk.Label(win,text='Round to',background='#595959',foreground='#363636',font=('unispace',8))
label_round.place(x=0,y=105)
win.grid_rowconfigure(0,minsize=100)
win.mainloop()
