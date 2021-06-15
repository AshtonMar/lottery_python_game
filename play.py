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
    random_number = []
    while len(random_number) < 6:
        numbers = random.randint(1, 49)
        if numbers not in random_number:
            random_number.append(numbers)
    random_1.insert(0, random_number[0])
    random_2.insert(0, random_number[1])
    random_3.insert(0, random_number[2])
    random_4.insert(0, random_number[3])
    random_5.insert(0, random_number[4])
    random_6.insert(0, random_number[5])


def rule_book():
    messagebox.showinfo("Rules", "You Need To enter 6 numbers between 1 and 49 and with no duplicates.")


#   The Information to get the game started and validate the player
#   The Heading.
head = Label(window, text="Enter Your 6-Digits")
head.place(x=105, y=10)

lotto_numbers = Label(window, text="Your Numbers")
lotto_numbers.place(x=120, y=30)

number_1 = Entry(window, width=3)
number_1.place(x=30, y=60)

number_2 = Entry(window, width=3)
number_2.place(x=80, y=60)

number_3 = Entry(window, width=3)
number_3.place(x=130, y=60)

number_4 = Entry(window, width=3)
number_4.place(x=180, y=60)

number_5 = Entry(window, width=3)
number_5.place(x=230, y=60)

number_6 = Entry(window, width=3)
number_6.place(x=280, y=60)


random_numbers = Label(window, text="Lotto Numbers")
random_numbers.place(x=120, y=100)

random_1 = Entry(window, width=3, justify="center")
random_1.place(x=30, y=130)

random_2 = Entry(window, width=3, justify="center")
random_2.place(x=80, y=130)

random_3 = Entry(window, width=3, )
random_3.place(x=130, y=130)

random_4 = Entry(window, width=3)
random_4.place(x=180, y=130)

random_5 = Entry(window, width=3)
random_5.place(x=230, y=130)

random_6 = Entry(window, width=3)
random_6.place(x=280, y=130)

result_lbl = Label(window, text="")
result_lbl.place(x=60, y=190)


#   The Buttons to be used in this window.
frame = LabelFrame(window, width=300, height=100)
frame.place(x=20, y=250)
#
#   The button to validate all the information in the entries and to see if the user is eligible to play.
play_btn = Button(frame, text="Play Again", width=10, command=play_game)
play_btn.place(x=20, y=10)
rules = Button(frame, text="What To Do?", width=10, command=rule_book)
rules.place(x=20, y=60)

#   The button to clear all the entries.
clear_btn = Button(frame, text="Claim Prize?", width=10)
clear_btn.place(x=170, y=10)

#   The button to exit the program.
exit_btn = Button(frame, text="Exit Program", width=10)
exit_btn.place(x=170, y=60)


window.mainloop()
