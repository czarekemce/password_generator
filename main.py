from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import random

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
all_numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
all_special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{', '}', '[', ']', '|', ';', ':', '<', '>', ',', '.', '?', '/']

nr_letters = random.randint(5, 8)
nr_numbers = random.randint(2, 4)
nr_special = random.randint(2, 4)

pass_letters = [random.choice(all_letters) for letters in range(nr_letters)]
pass_numbers = [random.choice(all_numbers) for numb in range(nr_numbers)]
pass_special = [random.choice(all_special_characters) for signs in range(nr_special)]

def create_pass():
    pass_input.delete(0, END)
    password_list = pass_letters + pass_numbers + pass_special
    random.shuffle(password_list)
    password = ''.join(password_list)
    pass_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def addToFile():
    files = [
        ('Text Document', '*.txt')
    ]
    get_web_input = web_input.get()
    get_email_input = email_input.get()
    get_pass_input = pass_input.get()

    if len(get_web_input) == 0 or len(get_pass_input) == 0:
        messagebox.showerror('error', 'Empty field!')
        return

    filename = fd.asksaveasfile(mode='a', filetypes=files, defaultextension='.txt')

    if filename:
        with open(filename.name, 'a') as data:
            data.write(get_email_input + '  |  ')
            data.write(get_web_input + '  |  ')
            data.write(get_pass_input + '  |  ')
            data.write('\n')

    web_input.delete(0, END)
    pass_input.delete(0, END)
    web_input.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password manager')
window.minsize(width=600, height=500)
window.config(padx=20, pady=20)

canvas = Canvas(width=250, height=250, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(80, 80, image=logo)
canvas.place(x=200, y=80)

website = Label()
website.configure(text='Website:', font=('Courier', 11))
website.place(x=80, y=280)

email = Label()
email.configure(text='Email/Username:', font=('Courier', 11))
email.place(x=50, y=310)

password = Label()
password.configure(text='Password:', font=('Courier', 11))
password.place(x=75, y=340)

web_input = Entry()
web_input.configure(width=45)
web_input.place(x=220, y=281)
web_input.focus()


email_input = Entry()
email_input.configure(width=45)
email_input.place(x=220, y=311)
email_input.insert(0, 'your@email')


pass_input = Entry()
pass_input.configure(width=45)
pass_input.place(x=220, y=341)


gen_button = Button(text='Generate Password', command=create_pass)
gen_button.place(x=385, y=371)

add_button = Button(text='Add to file', width=15, command=addToFile)
add_button.place(x=220, y=371)

window.mainloop()








