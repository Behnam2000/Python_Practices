from tkinter import *
from tkcalendar import Calendar


to_do_form = Tk()
# to_do_form.geometry("600x400")
to_do_form.title("Behnam To Do List App")
to_do_form.resizable(False, False)


txt_task = StringVar()
txt_discription = StringVar()
txt_date = StringVar()
cal = Calendar(to_do_form, selectmode = 'day',
               year = 2020, month = 5,
               day = 22)

cal.pack(pady = 20)

def addTask():

	a1 = txt_task.get()
	a2 = txt_discription.get()
	a3 = date.config(text = cal.get_date())

	import sqlite3

	conn = sqlite3.connect('./tasks.db')
	conn.cursor()

	create_table = """create table if not exists tasks (
		task TEXT(20),
		discription TEXT(120),
		date DATE
	)
	"""

	params = [a1, a2, a3]
	query = "insert into tasks values (?,?,?)"

	try:
		conn.execute(create_table)
		conn.commit()
		try:
			conn.execute(query, params)
			conn.commit()
		
		except:
			print("error form execution of query and params")
			conn.rollback()
	except:
		print("Error!")
		conn.rollback()


label_task = Label(to_do_form , text="Task")
label_task.grid(column=0, row=0 , padx=10, pady=10)

label_discription = Label(to_do_form , text="Discription")
label_discription.grid(column=0, row=1 , padx=10, pady=10)

label_date = Label(to_do_form , text="Date")
label_date.grid(column=0, row=2 , padx=10, pady=10)

# Entries
ent_task = Entry(to_do_form , width=25 , textvariable=txt_task)
ent_task.grid(column=1, row=0 , padx=10, pady=10)

ent_discription = Entry(to_do_form , width=25 , textvariable=txt_discription)
ent_discription.grid(column=1, row=1 , padx=10, pady=10)

ent_date = Entry(to_do_form , width=25 , textvariable=txt_date)
ent_date.grid(column=1, row=2 , padx=10, pady=10)


btn_set = Button(to_do_form , text="Add Task" , width=20 , command=addTask)
btn_set.grid(column=1, row=10)


to_do_form.mainloop()