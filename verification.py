#   Ashton Martin Class-1.
#   importing the tkinter module.
from tkinter import *

#   The Creation of the tkinter window.
window = Tk()
window.geometry("350x360")
window.title("Is It Your Lucky Day?")
window.resizable(False, False)


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

born_date = Label(window, text="Birthdate:")
born_date.place(x=70, y=200)
born_date = Label(window, text="/")
born_date.place(x=185, y=200)
born_date = Label(window, text="/")
born_date.place(x=235, y=200)

year_entry = Entry(window, width=3)
year_entry.place(x=150, y=200)

month_entry = Entry(window, width=3)
month_entry.place(x=200, y=200)

day_entry = Entry(window, width=3)
day_entry.place(x=250, y=200)

#   The Buttons to be used in this window.
frame = LabelFrame(window, width=300, height=100)
frame.place(x=20, y=250)
#
#   The button to validate all the information in the entries and to see if the user is eligible to play.
valid_btn = Button(frame, text="Play?", width=10)
valid_btn.place(x=20, y=10)

#   The button to clear all the entries.
clear_btn = Button(frame, text="Clear", width=10)
clear_btn.place(x=170, y=10)

#   The button to exit the program.
exit_btn = Button(frame, text="Exit Program", width=20)
exit_btn.place(x=60, y=60)

window.mainloop()
