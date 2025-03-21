from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_list = []

    password_letters = [choice(letters) for char in range(randint(8, 10))]

    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_numbers = [choice(numbers) for num in range(randint(2, 4))]

    password_list = password_numbers + password_letters +password_symbols
    shuffle(password_list)

    shuffle(password_list)
    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password )
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }

    if len(web_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty" )

    else:
        try:
            with open('pw_file.json', 'r') as json_file:
                data = json.load(json_file)
                data.update(new_data)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            data = new_data
        finally:
            with open('pw_file.json', 'w') as json_file:
                json.dump(data, json_file, indent=4)
            web_entry.delete(0, END)
            password_entry.delete(0, END)

def search_website():
    web_name = web_entry.get()
    with open('pw_file.json', 'r') as json_file:
        data = json.load(json_file)
        for key, value in data.items():
            try:
                messagebox.showinfo(title=web_name, message=f"Email/Username: {data[web_name]["username"]}\nPassword: {data[web_name]["password"]}")
            except KeyError:
                messagebox.showinfo(title="Warning",
                                    message="There is no such website saved")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")

# Configure grid columns to expand properly
window.grid_columnconfigure(1, weight=1)
window.grid_columnconfigure(2, weight=1)

canvas = Canvas(width=200, height=200, highlightthickness=0)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=lock_img)
canvas.grid(row=0, column=1, padx=50, pady=50)

website_txt = Label(text="Website:")
website_txt.grid(row=1, column=0, padx=5, pady=5, sticky="E")

username_txt = Label(text="Email/Username:")
username_txt.grid(row=2, column=0, padx=5, pady=5, sticky="E")

password_txt = Label(text="Password:")
password_txt.grid(row=3, column=0, padx=5, pady=5, sticky="E")

web_entry = Entry(width=21)
web_entry.grid(row=1, column=1, sticky="EW")
web_entry.focus()

username_entry = Entry(width=35)
username_entry.grid(row=2, column=1, columnspan=2, sticky="EW")
username_entry.insert(0, "rahimonkomiljonov06@gmail.com")
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, sticky="EW")

search_button = Button(text="Search", width=15, command=search_website)
search_button.grid(row=1, column=2, sticky="EW", padx=5)

gen_pass_button = Button(text="Generate Password", width=15, command=generate_password)  # Set fixed width
gen_pass_button.grid(row=3, column=2, sticky="EW", padx=5)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2, padx=5, pady=10, sticky="EW")







window.mainloop()