print("flash card capstone project")

from tkinter import *
import csv
import pandas
import random

# ------- MEACHANISM -------

data = pandas.read_csv("french_words.csv")
# print(data)

data_list = data.to_dict(orient = 'records')
# converts to list of dictionaries
# [ {french : word} , {english : word} ]
print(data_list)

current_card = {}

def next_card_command() :
	global current_card
	card_canvas.grid(column = 0, row = 1, columnspan = 2)
	current_card = random.choice(data_list)
	french_word = current_card["French"]
	card_canvas.itemconfig(language_text, text = "French")
	card_canvas.itemconfig(word_text, text = french_word)
	card_canvas.itemconfig(canvas_image, image = card_img)


# next_card_command()

def flip_card_command() :
	french_word = current_card["French"]
	english_word = current_card["English"]
	card_canvas.itemconfig(language_text, text = "English")
	card_canvas.itemconfig(canvas_image, image = answer_img)
	card_canvas.itemconfig(word_text, text = english_word)
	print(f"revise about '{french_word}' which in english means '{english_word}'")

	# with open("revise_words.csv", mode = 'w') as revise_words_file :
	# 	revise

# ------- UI -------

window = Tk()
window.minsize(width = 300, height = 300)
window.title("Flashcard Project")
window.config(bg = "orange", padx = 20 , pady = 20)

# window.after(3000, func = flip_card_command)
# this flips the card after 3 seconds the window in created

title_label = Label(text = "FLASHCARD APP", font = ("arial", 20, "bold"), bg = "orange")
title_label.grid(column = 0, row = 0, columnspan = 2)

# ------- CANVAS -------

card_canvas = Canvas(width = 800 , height = 526)
card_canvas.config(bg = "orange",highlightthickness = 0)

answer_img = PhotoImage(file = "card_back.png")
card_img = PhotoImage(file = "card_front.png")
canvas_image = card_canvas.create_image(400, 263, image = card_img)

language_text = card_canvas.create_text(400,150 , text = "", font =("arial",30,"bold"))
word_text = card_canvas.create_text(400,263 , text = "", font =("arial",60,"bold"))


card_canvas.grid(column = 0, row = 1, columnspan = 2)  

# answer_canvas = Canvas(width = 800 , height = 526)
# answer_canvas.config(bg = "orange",highlightthickness = 0)
# answer_canvas.create_image(400, 263, image = answer_img)
# answer_text = answer_canvas.create_text(400,263 , text = "answer", font =("arial",60,"bold"))
# answer_canvas.grid(column = 0, row = 1, columnspan = 2)

# ------- BUTTONS -------

wrong_img = PhotoImage(file = "wrong.png")
right_img = PhotoImage(file = "right.png")

wrong_button = Button(image = wrong_img, highlightthickness = 0, bg = "orange", command = flip_card_command)
right_button = Button(image = right_img, highlightthickness = 0, bg = "orange", command = next_card_command)
wrong_button.grid(column = 0, row = 2)
right_button.grid(column = 1, row = 2)

next_card_command()

window.mainloop()