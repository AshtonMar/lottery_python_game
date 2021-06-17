import requests
from tkinter import *
from tkinter import messagebox


window = Tk()
window.geometry("390x350")
window.title("Exchange Your Rate")
window.resizable(False, False)


def info():
    link = "https://v6.exchangerate-api.com/v6/21d57e3e0d14d58eee61f22c/latest/" + from_currency_entry.get()
    data = requests.get(link).json()
    exc_rate = float(amount_entry.get()) * data["conversion_rates"][to_currency_entry.get()]
    result_lb.config(text=exc_rate)


#  The clearing function.
def clear():
    from_currency_entry.delete(0, END)
    to_currency_entry.delete(0, END)
    amount_entry.delete(0, END)
    result_lb.config(text="")


#  The exiting function.
def exit_window():
    msg = messagebox.askquestion("You Sure?", "You want to return to bank details?")
    if msg == "yes":
        window.destroy()
        import bank_details
    else:
        print("You Returned")


heading = Label(window, text="/ Enter Your Amount /")
heading.place(x=125, y=10)

amount_lb = Label(window, text="Enter Amount : ")
amount_lb.place(x=50, y=80)
amount_entry = Entry(window, width=10)
amount_entry.place(x=220, y=80)

to_currency_lb = Label(window, text="To Currency(e.g ZAR):")
to_currency_lb.place(x=50, y=120)
to_currency_entry = Entry(window, width=10)
to_currency_entry.place(x=220, y=120)

from_currency_lb = Label(window, text="From Currency(e.g ZAR):")
from_currency_lb.place(x=50, y=40)
from_currency_entry = Entry(window, width=10)
from_currency_entry.place(x=220, y=40)

result_lb = Label(window, text="")
result_lb.place(x=180, y=170)

change_btn = Button(window, text="/ Change /", width=15, command=info)
change_btn.place(x=130, y=200)
clear_btn = Button(window, text="/ Clear /", width=15, command=clear)
clear_btn.place(x=130, y=250)
return_button = Button(window, text="/ Return /", width=20, command=exit_window)
return_button.place(x=110, y=300)

window.mainloop()
