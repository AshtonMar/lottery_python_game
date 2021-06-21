#   Ashton Martin Class-1.
#   importing of the modules.
from tkinter import *
from tkinter import messagebox
import random
from playsound import playsound
import json

#   The Creation of the tkinter window.
window = Tk()
window.geometry("350x360")
window.title("Is It Your Lucky Day?")
window.resizable(False, False)


#   The Function to check all the playable entries and matches it to the lotto numbers and shows the user how much
#   money they won.
def play_game():
    try:
        #   Creation of a list of random numbers and the insertion of the numbers into the lotto entries.
        lotto_nums = random.sample(range(1, 49), 6)
        random_1.insert(0, lotto_nums[0])
        random_2.insert(0, lotto_nums[1])
        random_3.insert(0, lotto_nums[2])
        random_4.insert(0, lotto_nums[3])
        random_5.insert(0, lotto_nums[4])
        random_6.insert(0, lotto_nums[5])
        lotto_nums = set(lotto_nums)
        #   Putting the entered numbers into sets.
        set_1 = {int(number_1.get()), int(number_2.get()), int(number_3.get()), int(number_4.get()),
                 int(number_5.get()), int(number_6.get())}
        set_2 = {int(number_7.get()), int(number_8.get()), int(number_9.get()), int(number_10.get()),
                 int(number_11.get()), int(number_12.get())}
        #  The finding of the matching numbers in the users entries and the lotto nums.
        check_set_1 = lotto_nums.intersection(set_1)
        check_set_2 = lotto_nums.intersection(set_2)
        #   Checking the amount of matching numbers.
        amount_set_1 = len(check_set_1)
        amount_set_2 = len(check_set_2)
        #   The set to group all the numbers the user played.
        all_sets = [int(number_1.get()), int(number_2.get()), int(number_3.get()),
                    int(number_4.get()), int(number_5.get()), int(number_6.get()),
                    int(number_7.get()), int(number_8.get()), int(number_9.get()),
                    int(number_10.get()), int(number_11.get()), int(number_12.get())]
        if amount_set_1 == 6:
            amount_set_1 = 10000000
            result_lbl.config(text="Winner")
        elif amount_set_1 == 5:
            amount_set_1 = 10000
            result_lbl.config(text="Winner")
        elif amount_set_1 == 4:
            amount_set_1 = 5000
            result_lbl.config(text="Winner")
        elif amount_set_1 == 3:
            amount_set_1 = 1000
            result_lbl.config(text="Winner")
        elif amount_set_1 == 2:
            amount_set_1 = 20
        elif amount_set_1 == 1:
            amount_set_1 = 0
            result_lbl.config(text="Winner")
        elif amount_set_1 == 0:
            amount_set_1 = 0
            result_lbl.config(text="Winner")

        if amount_set_2 == 6:
            amount_set_2 = 10000000
            result_lbl.config(text="Winner")
        elif amount_set_2 == 5:
            amount_set_2 = 10000
            result_lbl.config(text="Winner")
        elif amount_set_2 == 4:
            amount_set_2 = 5000
            result_lbl.config(text="Winner")
        elif amount_set_2 == 3:
            amount_set_2 = 1000
            result_lbl.config(text="Winner")
        elif amount_set_2 == 2:
            amount_set_2 = 20
        elif amount_set_2 == 1:
            amount_set_2 = 0
            result_lbl.config(text="Winner")
        elif amount_set_2 == 0:
            amount_set_2 = 0
            result_lbl.config(text="Winner")
        prize = amount_set_1 + amount_set_2
        if prize != 0:
            prize = amount_set_1 + amount_set_2
            info = {"Played Numbers": all_sets, "Winning Amount": prize}
            file_dict = read_key_value_pairs()
            file_dict["info"] = info
            text_to_file(file_dict)
            playsound("winning_sound.mp3")
            msg = messagebox.askquestion("YOU WIN!", "You Won R" + str(prize) + "\n" + "\n"
                                         + "You Want To Convert From ZAR To Another Currency")
            if msg == "yes":
                window.destroy()
                import currency_converter
            else:
                window.destroy()
                import bank_details
        else:
            playsound("losing_sound.mp3")
            msg = messagebox.askquestion("Try Again?", "Sorry You Have Not Won You Can Try Again")
            if msg == 'yes':
                result_lbl.config(text="")
                #   Set_1
                number_1.delete(0, END)
                number_2.delete(0, END)
                number_3.delete(0, END)
                number_4.delete(0, END)
                number_5.delete(0, END)
                number_6.delete(0, END)
                #   Set_2
                number_7.delete(0, END)
                number_8.delete(0, END)
                number_9.delete(0, END)
                number_10.delete(0, END)
                number_11.delete(0, END)
                number_12.delete(0, END)
                #   Lotto Numbers
                random_1.delete(0, END)
                random_2.delete(0, END)
                random_3.delete(0, END)
                random_4.delete(0, END)
                random_5.delete(0, END)
                random_6.delete(0, END)
            else:
                window.destroy()
                messagebox.showinfo("Thanks", "Thanks For Playing!")
    except ValueError:
        playsound("error_sound.mp3")
        msg = messagebox.showerror("Error!", "Something Went Wrong With Entries")
        if msg == 'ok':
            result_lbl.config(text="")
            #   Set_1
            number_1.delete(0, END)
            number_2.delete(0, END)
            number_3.delete(0, END)
            number_4.delete(0, END)
            number_5.delete(0, END)
            number_6.delete(0, END)
            #   Set_2
            number_7.delete(0, END)
            number_8.delete(0, END)
            number_9.delete(0, END)
            number_10.delete(0, END)
            number_11.delete(0, END)
            number_12.delete(0, END)
            #   Lotto Numbers
            random_1.delete(0, END)
            random_2.delete(0, END)
            random_3.delete(0, END)
            random_4.delete(0, END)
            random_5.delete(0, END)
            random_6.delete(0, END)


#
def read_key_value_pairs():
    with open("lotto_info.txt", "r", encoding="utf-8-sig", errors="ignore")as file:
        info_object = json.load(file, strict=False)
        return info_object


#   Function to add the info on this window to the text file.
def text_to_file(adding_obj):
    adding_obj = json.dumps(adding_obj)
    with open("lotto_info.txt", "w") as lotto_info:
        lotto_info.write(adding_obj)


#   Displays the rulebook.
def rule_book():
    messagebox.showinfo("Rules", "You Need To enter 6 numbers between 1 and 49 and with no duplicates.")


#   Function to exit the program.
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
#  First Set Display.
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
#   Second set Display.
number_7 = Entry(window, width=3, justify="center")
number_7.place(x=30, y=110)
number_8 = Entry(window, width=3, justify="center")
number_8.place(x=80, y=110)
number_9 = Entry(window, width=3, justify="center")
number_9.place(x=130, y=110)
number_10 = Entry(window, width=3, justify="center")
number_10.place(x=180, y=110)
number_11 = Entry(window, width=3, justify="center")
number_11.place(x=230, y=110)
number_12 = Entry(window, width=3, justify="center")
number_12.place(x=280, y=110)
#   Where the lotto numbers are displayed.
random_numbers = Label(window, text="Lotto Numbers")
random_numbers.place(x=120, y=140)
random_1 = Entry(window, width=3, justify="center")
random_1.place(x=30, y=180)
random_2 = Entry(window, width=3, justify="center")
random_2.place(x=80, y=180)
random_3 = Entry(window, width=3, justify="center")
random_3.place(x=130, y=180)
random_4 = Entry(window, width=3, justify="center")
random_4.place(x=180, y=180)
random_5 = Entry(window, width=3, justify="center")
random_5.place(x=230, y=180)
random_6 = Entry(window, width=3, justify="center")
random_6.place(x=280, y=180)
#   Displays if you win or lose.
result_lbl = Label(window, text="", justify="center")
result_lbl.place(x=150, y=210)
#   The frame where the buttons are placed.
frame = LabelFrame(window, width=300, height=100)
frame.place(x=20, y=250)
#   The Buttons to be used in this window.
#   The button to validate all the information in the entries and to see if the user is eligible to play.
play_btn = Button(frame, text="Play", width=10, command=play_game)
play_btn.place(x=20, y=10)
#   Displays the rulebook.
rules = Button(frame, text="What To Do?", width=10, command=rule_book)
rules.place(x=170, y=10)
#   The button to exit the program.
exit_btn = Button(frame, text="Exit Program", width=20, command=leave)
exit_btn.place(x=50, y=60)

window.mainloop()
