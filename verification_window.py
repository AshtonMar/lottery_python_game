#   Ashton Martin Class-1.
#   Importing the tkinter module.
from tkinter import *
import random
from tkinter import messagebox
from datetime import date, timedelta


#   The creation of the tkinter window.
window = Tk()
window.geometry("350x360")
window.title("Is It Your Lucky Day?")
window.resizable(False, False)


#   The functions used to make the verification window function.
def entry_validation():
    try:
        if name_entry.get() == " ":
            messagebox.showinfo("Name", "Enter your name")
        elif id_number_entry.get() == " ":
            messagebox.showinfo("Name", "Enter your id number")
        elif id_number_entry.get() != 13:
            messagebox.showinfo("", "Please Enter An ID Number")
        elif email_entry.get() == " ":
            messagebox.showinfo("Name", "Enter your email")
        else:
            print("everything is fine")
    except ValueError:
        messagebox.showerror("Error!", "Something Went Wrong")


def valid_email():
    if "@" not in email_entry.get():
        messagebox.showinfo("Proper Email", "Enter Valid Email")
    elif ".com" not in email_entry.get():
        messagebox.showinfo("Proper Email", "Enter Valid Email")
    else:
        print("Its Valid")


#   The age validation function that checks if the user is eligible to play.
def age_valid():
    try:
        entry_validation()
        id_num = id_number_entry.get()
        id_num = list(id_num)
        year = id_num[0] + id_num[1]
        month = id_num[2] + id_num[3]
        day = id_num[4] + id_num[5]
        date_of_birth = date(int(year), int(month), int(day))
        age = (date.today()-date_of_birth) // timedelta(days=365.245)
        age = str(age)
        age = list(age)
        age = age[2] + age[3]
        age = int(age)
        years_left = 18 - age
        if age >= 18:
            player_id = random.sample(range(1, 10), 1)
            player_id = str(player_id)
            info = {"name": name_entry.get(), "player": "Player " + player_id[1], "email": email_entry.get(),
                    "age": age}
            text_to_file(info)
            messagebox.showinfo("You Are Valid", "You are of age young squire!" + "\n" + "\n" + "       You are player "
                                + player_id[1])
            messagebox.showinfo("Rules", "You Need To enter 6 numbers between 1 and 49 and with no duplicates.")
            window.destroy()
            import play_window
        else:
            messagebox.showinfo("You Are Too Young!", "Wait " + str(years_left) + " more years")
    except ValueError:
        messagebox.showerror("Error!", "Something Went Wrong!")


def text_to_file(added_obj):
    import json
    added_obj = json.dumps(added_obj)
    with open("lotto_info.txt", "a+") as lotto_info:
        lotto_info.write(added_obj)


# The clear function that clears all the entries.
def clear():
    name_entry.delete(0, END)
    address_entry.delete(0, END)
    email_entry.delete(0, END)
    id_number_entry.delete(0, END)


def leave():
    msg = messagebox.askquestion("YOU SURE?" "You Are Exiting The Program!")
    if msg == "yes":
        messagebox.showinfo("Thank You", "Thank You For Using The Application")
        window.destroy()
    else:
        print("You Returned")


#   The Information to get the game started and validate the player
#   The Heading.
head = Label(window, text="Enter Your Details To Play")
head.place(x=90, y=10)

#   The Label and Entry for the users name.
name = Label(window, text="Name      :")
name.place(x=70, y=50)
name_entry = Entry(window, width=16)
name_entry.place(x=150, y=50)

address = Label(window, text="Address   :")
address.place(x=70, y=100)
address_entry = Entry(window, width=16)
address_entry.place(x=150, y=100)

email = Label(window, text="Email      :")
email.place(x=70, y=150)
email_entry = Entry(window, width=16)
email_entry.place(x=150, y=150)

id_number = Label(window, text="ID Number:")
id_number.place(x=70, y=200)

id_number_entry = Entry(window, width=16)
id_number_entry.place(x=150, y=200)

#   The Buttons to be used in this window.
frame = LabelFrame(window, width=300, height=100)
frame.place(x=20, y=250)
#
#   The button to validate all the information in the entries and to see if the user is eligible to play.
valid_btn = Button(frame, text="Play?", width=10, command=age_valid)
valid_btn.place(x=20, y=10)

#   The button to clear all the entries.
clear_btn = Button(frame, text="Clear", width=10, command=clear)
clear_btn.place(x=170, y=10)

#   The button to exit the program.
exit_btn = Button(frame, text="Exit Program", width=20, command=leave)
exit_btn.place(x=60, y=60)

window.mainloop()
