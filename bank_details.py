#   Ashton Martin Class-1.
#   importing the tkinter module.
import json
import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import getpass
from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

#   The Creation of the tkinter window.
window = Tk()
window.geometry("350x320")
window.title("It's Your Lucky Day!")
window.resizable(False, False)


def send_email():
    with open("lotto_info.txt", "r", encoding="utf-8-sig", errors="ignore")as file:
        info_object = json.load(file, strict=False)
        name = info_object["name"]
        print(name)
    sender_email = "ashtonmartingoliath@gmail.com"
    receiver_email = info_object["email"]
    print(receiver_email)
    password = input("Password: ")

    message = MIMEMultipart("alternative")
    message["Subject"] = "Lotto Winner"
    message["From"] = sender_email
    message["To"] = ", ".join(receiver_email)

    email_message = "Hi" + info_object["name"] +"you have won" + "R10" +"it will be transferred to your bank account" + "10"+"\n" + "\n" + \
                    "Thanks for playing"
    text = MIMEText(email_message)
    message.attach(text)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


def clear():
    account_holder_entry.delete(0, END)
    bank_number_entry.delete(0, END)
    banks.delete(0, END)


def exit_program():
    msg = messagebox.askquestion("YOU SURE?", "You Are Exiting The Program!")
    if msg == "yes":
        messagebox.showinfo("Thank You", "Thank You For Using The Application")
        window.destroy()
    else:
        print("You Returned")


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
send_btn = Button(frame, text="Send", width=10, command=send_email)
send_btn.place(x=20, y=10)

#   The button to clear all the entries.
clear_btn = Button(frame, text="Clear", width=10, command=clear)
clear_btn.place(x=170, y=10)

#   The button to exit the program.
exit_btn = Button(frame, text="Exit Program", width=20, command=exit_program)
exit_btn.place(x=60, y=60)

window.mainloop()
