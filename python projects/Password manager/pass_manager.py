print("password manager by using tkinter")

# --------------- basics ---------------

from tkinter import *
from tkinter import messagebox
import pyperclip	

window = Tk()
window.minsize(width = 500 , height = 500)
window.title("password manager")
window.config(padx = 20, pady = 20)

#---------------Generating Password---------------

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generate_password_command() :
	nr_letters = random.randint(8, 10)
	nr_symbols = random.randint(2, 4)
	nr_numbers = random.randint(2, 4)

	password_list = []

	for char in range(nr_letters):
	  password_list.append(random.choice(letters))

	for char in range(nr_symbols):
	  password_list += random.choice(symbols)

	for char in range(nr_numbers):
	  password_list += random.choice(numbers)

	random.shuffle(password_list)

	password = ""
	for char in password_list:
	  password += char
	entry_password.delete(0, END)
	entry_password.insert(0, password)
	print(password)




#---------------Saving password to file---------------

def add_password() :
	password_value = entry_password.get()
	website_value = entry_website.get()
	email_value = entry_email.get()
	data = f"\nWebsite : {website_value}\nEmail : {email_value}\nPassword : {password_value}\n-----------------"

	if password_value == "" or website_value == "" or email_value == "" :
		messagebox.showerror(title = "Error", message = "You left some entry empty !")
	
	else :
		# mesage box
		# messagebox.showinfo(title = "Confirm", message = "Are you confirm with the data entered ?")
		proceed = messagebox.askokcancel(title = "Confirm ?", message = "Are you sure to proceed ?")
		if proceed : # if proceed is 'ok' or True
			with open("password_data.txt", mode = 'a') as data_file :
				data_file.write(f"{data}")
			# data_file.close()
			entry_password.delete(0, END)
			entry_email.delete(0, END)
			entry_website.delete(0, END)
			# print 
			print(data)
			pyperclip.copy(password_value)
		else :
			pass





#--------------- UI ---------------

title_label = Label(text = "Password Manager!", font = ("Comic Sans MS", 20, "bold"))
title_label.grid(column = 1, row = 0, columnspan = 2)

# canvas :
canvas = Canvas(width = 100 , height = 100)
lock_image = PhotoImage(file = "lock-img.png")
canvas.create_image(50, 50, image = lock_image)
canvas.grid(column = 1, row = 1, columnspan = 2)

# entries :

website_label = Label(text = "Website name : ", font = ("Arial", 12, "bold"))
email_user_label = Label(text = "Email/Username : ", font = ("Arial", 12, "bold"))
password_label = Label(text = "Password : ", font = ("Arial", 12, "bold"))

website_label.grid(column = 0, row = 2)
email_user_label.grid(column = 0, row = 3)
password_label.grid(column = 0, row = 4)

entry_website = Entry(font = ("arial", 12, "bold"), width = 35)
entry_website.focus()	# this focuses the cursor on the WEBSITE entry box the time the program starts
entry_email = Entry(font = ("arial", 12, "bold"), width = 35)
entry_password = Entry(font = ("arial", 12, "bold"), width = 35 )

entry_website.grid(column = 1, row = 2)
entry_email.grid(column = 1, row = 3)
entry_password.grid(column = 1, row = 4)

# buttons : 

generate_button = Button(text = "Generate Password", font = ("arial", 10, "bold"), command = generate_password_command)
add_button = Button(text = "Add to Database", font = ("arial", 10, "bold"), command = add_password)

generate_button.grid(column = 3, row = 4)
add_button.grid(column = 0, row = 5, columnspan = 4)


window.mainloop()