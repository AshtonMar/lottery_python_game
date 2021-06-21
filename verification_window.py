#   Ashton Martin Class-1.
#   Importing all the modules.
from tkinter import *
import json
import re
import random
from playsound import playsound
from tkinter import messagebox
from datetime import date, timedelta


#   The creation of the tkinter window.
window = Tk()
window.geometry("350x360")
window.title("Is It Your Lucky Day?")
window.resizable(False, False)


#   The age, name and email validation function that checks if the user is eligible to play.
def validate():
    #   The Extraction of the date of birth.
    id_num = list(id_number_entry.get())
    #   The Date Of Birth from the id number.
    year = id_num[0] + id_num[1]
    month = id_num[2] + id_num[3]
    day = id_num[4] + id_num[5]

    #   Using the Date Of Birth to calculate the age.
    date_of_birth = date(int(year), int(month), int(day))
    age = str((date.today() - date_of_birth) // timedelta(days=365.245))
    age = list(age)
    age = age[2] + age[3]
    age = int(age)
    years_left = 18 - age
    #   Email verification.
    regex = "domain@gmail.com"
    try:
        #   Verification of the name entry.
        if name_entry.get() == "":
            playsound("error_sound.mp3")
            messagebox.showinfo("NAME ENTRY", "Enter Your Name Please")
        #   Verification of the email entry and the email(if it is valid or not).
        elif email_entry.get() == "":
            playsound("error_sound.mp3")
            messagebox.showerror("EMAIL ENTRY", "Enter An Email Please")
        elif re.search(regex, email_entry.get()):
            playsound("error_sound.mp3")
            messagebox.showerror("EMAIL ENTRY", "Enter A Valid Email Please")
        #   Verification of the id number entry and the verification of the age of the user via the id number.
        elif id_number_entry.get() == "":
            playsound("error_sound.mp3")
            messagebox.showerror("ID ENTRY", "Please Enter Your Id Number")
        #     Checks the age of the user.
        elif age >= 18:
            player_id = random.sample(range(1, 10), 1)
            player_id = str(player_id)
            #   Where the object with all the users info is taken and stored in the text file.
            info = {"name": name_entry.get(), "player": "Player " + player_id[1], "email": email_entry.get(),
                    "age": age}
            text_to_file(info)

            playsound("winning_sound.mp3")
            messagebox.showinfo("You Are Allowed To Play", "You Are Of Age To Play!" + "\n" + "\n" + "  You Are Player "
                                + player_id[1])
            messagebox.showinfo("Rules", "You Need To Enter 6 Numbers Between 1 And 49, With No Duplicates.")
            window.destroy()
            import play_window
        else:
            playsound("not_valid.mp3")
            messagebox.showinfo("You Are Too Young!", "Wait " + str(years_left) + " more years")
            window.destroy()
    except ValueError:
        playsound("error_sound.mp3")
        messagebox.showerror("Error!", "Something Went Wrong!")


#   The Creation the text file and adding to it.
def text_to_file(adding_obj):
    adding_obj = json.dumps(adding_obj)
    with open("lotto_info.txt", "w+") as lotto_info:
        lotto_info.write(adding_obj)


#    The clear function that clears all the entries.
def clear():
    name_entry.delete(0, END)
    email_entry.delete(0, END)
    id_number_entry.delete(0, END)


#   The exit program for the window.
def leave():
    msg = messagebox.askquestion("YOU SURE?" "You Are Exiting The Program!")
    if msg == "yes":
        messagebox.showinfo("THANK YOU", "Thank You For Using The Application")
        window.destroy()
    else:
        messagebox.showinfo("WHY?", "Then Why Did You Click The Exit Button")


#   The Information to get the game started and validate the player.
#   The Heading.
head = Label(window, text="Enter Your Details To Play The Lotto")
head.place(x=90, y=10)
#   The Label and Entry for the users name.
name = Label(window, text="Name      :")
name.place(x=70, y=50)
name_entry = Entry(window, width=20)
name_entry.place(x=150, y=50)
#   The Label and Entry for the email entry.
email = Label(window, text="Email      :")
email.place(x=70, y=100)
email_entry = Entry(window, width=20)
email_entry.place(x=150, y=100)
#   The Label and Entry for the id number entry.
id_number = Label(window, text="Id Number:")
id_number.place(x=70, y=150)
id_number_entry = Entry(window, width=20)
id_number_entry.place(x=150, y=150)
#   The frame where the buttons are placed.
frame = LabelFrame(window, width=300, height=100)
frame.place(x=20, y=250)
#   The Buttons to be used in this window.
#   The button to validate all the information in the entries and to see if the user is eligible to play.
valid_btn = Button(frame, text="Wanna Play?", width=10, command=validate)
valid_btn.place(x=20, y=10)
#   The button to clear all the entries.
clear_btn = Button(frame, text="Clear", width=10, command=clear)
clear_btn.place(x=170, y=10)
#   The button to exit the program.
exit_btn = Button(frame, text="Exit Program", width=20, command=leave)
exit_btn.place(x=60, y=60)

window.mainloop()
