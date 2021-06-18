#   Ashton Martin Class-1.
#   importing the tkinter module.
import random
from tkinter import *
from tkinter import messagebox
import random

#   The Creation of the tkinter window.
window = Tk()
window.geometry("350x360")
window.title("Is It Your Lucky Day?")
window.resizable(False, False)


def play_game():
    lotto_nums = random.sample(range(1, 49), 6)
    random_1.insert(0, lotto_nums[0])
    random_2.insert(0, lotto_nums[1])
    random_3.insert(0, lotto_nums[2])
    random_4.insert(0, lotto_nums[3])
    random_5.insert(0, lotto_nums[4])
    random_6.insert(0, lotto_nums[5])
    lotto_nums = set(lotto_nums)

    players_nums = {int(number_1.get()), int(number_2.get()), int(number_3.get()), int(number_4.get()),
                    int(number_5.get()), int(number_6.get())}

    # players_nums_2 = {}

    check = lotto_nums.intersection(players_nums)

    amount = len(check)
    try:
        if amount == 6:
            result_lbl.config(text="Winner")
            msg = messagebox.askquestion("Congratulations", "You Have Won The Jackpot Of R10 000 000" + "\n" + "\n"
                                         + "You Want To Convert From ZAR To Another Currency")
            if msg == "yes":
                window.destroy()
                import currency_converter
            else:
                window.destroy()
                import bank_details
        elif amount == 5:
            result_lbl.config(text="Winner")
            msg = messagebox.askquestion("Congratulations", "You Have Won The 2nd Prize Of R10000 " + "\n" + "\n"
                                         + "You Want To Convert From ZAR To Another Currency")
            if msg == "yes":
                window.destroy()
                import currency_converter
            else:
                window.destroy()
                import bank_details
        elif amount == 4:
            result_lbl.config(text="Winner")
            msg = messagebox.askquestion("Congratulations", "You Have Won The 3rd Prize Of R5000 " + "\n" + "\n"
                                         + "You Want To Convert From ZAR To Another Currency")
            if msg == "yes":
                window.destroy()
                import currency_converter
            else:
                window.destroy()
                import bank_details
        elif amount == 1:
            result_lbl.config(text="Winner")
            msg = messagebox.askquestion("Congratulations", "You Have Won The 4th Prize Of R1000 " + "\n" + "\n"
                                         + "You Want To Convert From ZAR To Another Currency")
            if msg == "yes":
                window.destroy()
                import currency_converter
            else:
                window.destroy()
                import bank_details
        else:
            result_lbl.config(text="Loser")
            msg = messagebox.askquestion("Try Again?", "Sorry You Have Not Won You Can Try Again")
            if msg == 'yes':
                result_lbl.config(text="")

                number_1.delete(0, END)
                number_2.delete(0, END)
                number_3.delete(0, END)
                number_4.delete(0, END)
                number_5.delete(0, END)
                number_6.delete(0, END)

                random_1.delete(0, END)
                random_2.delete(0, END)
                random_3.delete(0, END)
                random_4.delete(0, END)
                random_5.delete(0, END)
                random_6.delete(0, END)
            else:
                window.destroy()
    except ValueError:
        messagebox.showerror("Error!", "Something Went Wrong")


def text_to_file(added_obj):
    import json
    added_obj = json.dumps(added_obj)
    with open("lotto_info.txt", "a+") as lotto_info:
        lotto_info.write(added_obj)


def rule_book():
    messagebox.showinfo("Rules", "You Need To enter 6 numbers between 1 and 49 and with no duplicates.")


def leave():
    msg = messagebox.askquestion("YOU SURE?", "You Are Exiting The Program!")
    if msg == "yes":
        messagebox.showinfo("Thank You", "Thank You For Using The Application")
        window.destroy()
    else:
        print("You Returned")


#   The Information to get the game started and validate the player
#   The Heading.
head = Label(window, text="Enter Your 6-Digits")
head.place(x=105, y=10)

lotto_numbers = Label(window, text="Your Numbers")
lotto_numbers.place(x=120, y=30)

number_1 = Entry(window, width=3, justify="center")
number_1.place(x=30, y=60)

number_2 = Entry(window, width=3, justify="center")
number_2.place(x=80, y=60)

number_3 = Entry(window, width=3, justify="center")
number_3.place(x=130, y=60)

number_4 = Entry(window, width=3, justify="center")
number_4.place(x=180, y=60)

number_5 = Entry(window, width=3, justify="center")
number_5.place(x=230, y=60)

number_6 = Entry(window, width=3, justify="center")
number_6.place(x=280, y=60)


random_numbers = Label(window, text="Lotto Numbers")
random_numbers.place(x=120, y=100)

random_1 = Entry(window, width=3, justify="center")
random_1.place(x=30, y=130)

random_2 = Entry(window, width=3, justify="center")
random_2.place(x=80, y=130)

random_3 = Entry(window, width=3, justify="center")
random_3.place(x=130, y=130)

random_4 = Entry(window, width=3, justify="center")
random_4.place(x=180, y=130)

random_5 = Entry(window, width=3, justify="center")
random_5.place(x=230, y=130)

random_6 = Entry(window, width=3, justify="center")
random_6.place(x=280, y=130)

result_lbl = Label(window, text="", justify="center")
result_lbl.place(x=150, y=190)


#   The Buttons to be used in this window.
frame = LabelFrame(window, width=300, height=100)
frame.place(x=20, y=250)

#   The button to validate all the information in the entries and to see if the user is eligible to play.
play_btn = Button(frame, text="Play", width=10, command=play_game)
play_btn.place(x=20, y=10)
rules = Button(frame, text="What To Do?", width=10, command=rule_book)
rules.place(x=170, y=10)

#   The button to exit the program.
exit_btn = Button(frame, text="Exit Program", width=20, command=leave)
exit_btn.place(x=50, y=60)


window.mainloop()
