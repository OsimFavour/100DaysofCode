from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
            "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
            "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J",
            "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
            "W", "X", "Y", "Z"]

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search_password():
    search_data = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        messagebox.showerror(title="No data found", message="There is no data in the database")
        website_entry.delete(0, END)
    else:
        if search_data in data:
            email = data[search_data]["email"]
            password = data[search_data]["password"]
            password_entry.delete(0, END)
            password_entry.insert(0, password)
            messagebox.showinfo(title=f"{website_entry.get()}", message=f"Email: {email}\nPassword: {password}")
            search_button.clipboard_clear()
            search_button.clipboard_append(password)
        else:
            messagebox.showerror(title="Website not found", message="The website you searched for cannot be found, try again!")
    finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)


# ---------------------------- ADD DATA TO JSON ------------------------------- #

def add_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if website != "" and email != "" and password != "":
        correct_info = messagebox.askokcancel(title=website, message=f"These are the details you entered:\n"
                                                                     f"Email: {email}\nPassword: {password}\n"
                                                                     f"Is it OK to save?")
        if correct_info:
            try:
                with open("data.json", mode="r") as data_file:
                    # Reading old data
                    data = json.load(data_file)
                    # Updating old data with new data
                    data.update(new_data)
            except (FileNotFoundError, json.decoder.JSONDecodeError):
                with open("data.json", mode="w") as data_file:
                    # Saving the updated data
                    json.dump(new_data, data_file, indent=4)
            else:
                with open("data.json", mode="w") as data_file:
                    # Saving the updated data
                    json.dump(data, data_file, indent=4)
            finally:
                website_entry.delete(0, END)
                # email_entry.delete(0, END)
                password_entry.delete(0, END)
        else:
            messagebox.showerror(title="Insufficient information", message="Please don't leave any fields empty")

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img) 
canvas.grid(row=0, column=1) 

# Labels
website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

# Entries
website_entry = Entry(width=31)
website_entry.grid(row=1, column=1, pady=2)
website_entry.focus()

email_entry = Entry(width=51)
email_entry.grid(row=2, column=1, columnspan=2, pady=2)
email_entry.insert(0, "famos204@gmail.com")

password_entry = Entry(width=32)
password_entry.grid(row=3, column=1)
# password_entry.insert(0, password)

# Buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

search_button = Button(text="Search", fg="black", width=15, height=1, command=search_password)
search_button.grid(row=1, column=2, pady=2)

add_button = Button(text="Add", bg="white", width=44, command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()