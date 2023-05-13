from shutil import which
from tkinter import *
import math

print("Pomodoro timer using tkinter.")

break_time = 5*60
work_time = 25*60
long_break_time = 20*60
reps = 0
timer = None

window = Tk()
# window.minsize(width = 500 , height = 400)
window.title("Pomodoro Project")
window.config(padx = 20, pady = 20)


# # COUNTDOWWN MECHANISM :-

def say_something(thing) :
    print(thing)
    window.after(2000, say_something , thing)
# after 2000 miliseconds (2 sec) say_something will operate and print(thing) here , "hello"
# by putting this 'after' inside the say_something() function 
# the function will be executed repeatedly 
# so this prints hello after every 2 seconds.

# say_something("hello")

# countdown function :-

def null() :
    pass

def countdown(count) :
    count_min = math.floor(count / 60)  # returns the largest whole number less the (count/60)
    count_sec = count % 60 # retrns the remainder of (count/60)
    
    # solving the problem of single digit no. 
    if count_sec <10 :
        count_sec = f"0{count_sec}"
    count_display = f"{count_min}:{count_sec}"
    canvas.itemconfig(timer_text , text = count_display)

    if count > 0 :
        global timer
        print(f"{count_min}:{count_sec}")   
        timer = window.after(1000, countdown, count-1)
    else :
        start_command()
        mark = ""
        # work_sessions = work time + break time
        work_session = math.floor(reps/2) # gives the whole no. of reps/2
        for _ in range(work_session) :
            mark += "✔"
        check_marks.config(text = mark)

def start_command() :
    global reps
    reps += 1
    start_button.config(fg = "grey" , command = null)
    if reps % 8 == 0 :
        title_label.config(text = "Long Break")
        countdown(long_break_time)
        # start_button.pack_forget()
    elif reps % 2 == 0 :
        title_label.config(text = "Short Break")
        countdown(break_time)
        # start_button.pack_forget()
    else :
        title_label.config(text = "Work time")
        countdown(work_time)
        # start_button.grid_forget()

def reset_command() :
    window.after_cancel(timer)
    # this cancels the after command by the start command 
    # but the time stops at where we command reset 
    # and not 00:00
    # this is because the reps are still counting
    start_button.config(fg = "black" , command = start_command)
    canvas.itemconfig(timer_text , text = "00:00")
    check_marks.config(text = "")
    global reps 
    reps = 0
    # now everything is reseted


# UI setup :-
canvas = Canvas(width = 206 , height = 224)
my_photo = PhotoImage(file = "tomato.png")
canvas.create_image(103, 112, image = my_photo)
timer_text = canvas.create_text(103, 130, text = "00:00", font =("arial",25,"bold"))
canvas.grid(column = 1, row = 1)

# canvas.config(padx = 20, pady = 20)

title_label = Label(text = "Pomodoro Timer", font =("Rubik",25,"bold"))
title_label.grid(column = 1, row = 0)
title_label.config(padx = 10, pady = 10)

start_button = Button(text = "Start",font =("arial",10,"bold"), command = start_command)
start_button.grid(column = 0, row = 2)

reset_button = Button(text = "Reset", font =("arial",10,"bold"), command = reset_command)
reset_button.grid(column = 2, row = 2)

check_marks = Label(text = "", font =("arial",10,"bold"))
check_marks.config(fg = "green")
check_marks.grid(column = 1 , row = 3)


window.mainloop()
