#   Ashton Martin Class-1.
#   importing the tkinter module.
from tkinter import *
from tkinter.ttk import Combobox

#   The Creation of the tkinter window.
window = Tk()
window.geometry("350x320")
window.title("Is It Your Lucky Day?")
window.resizable(False, False)


#   The Information to get the game started and validate the player
#   The Heading.
head = Label(window, text="Enter Your Details To Get Paid!!")
head.place(x=70, y=10)

#   The Label and Entry for the users name.
account_holder = Label(window, text="Account Holder Name:")
account_holder.place(x=30, y=100)
account_holder_entry = Entry(window, width=12)
account_holder_entry.place(x=180, y=100)

bank_number = Label(window, text="Bank Account Number:")
bank_number.place(x=30, y=150)
bank_number_entry = Entry(window, width=12)
bank_number_entry.place(x=180, y=150)

bank_name = Label(window, text="Your Bank:")
bank_name.place(x=30, y=50)
banks = Combobox(window, width=12)
banks.place(x=180, y=50)

banks["values"] = "Nedbank", "ABSA", "Capitec", "FNB"


#   The Buttons to be used in this window.
frame = LabelFrame(window, width=300, height=100)
frame.place(x=20, y=200)
#
#   The button to validate all the information in the entries and to see if the user is eligible to play.
send_btn = Button(frame, text="Send", width=10)
send_btn.place(x=20, y=10)

#   The button to clear all the entries.
clear_btn = Button(frame, text="Clear", width=10)
clear_btn.place(x=170, y=10)

#   The button to exit the program.
exit_btn = Button(frame, text="Exit Program", width=20)
exit_btn.place(x=60, y=60)

window.mainloop()
