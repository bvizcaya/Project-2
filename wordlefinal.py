from tkinter import *
from tkinter import messagebox
import random

word_list = [
    'hence', 'gross', 'dowse', 'taxis', 'shove',
    'brawl', 'breed', 'lives', 'sinew', 'cream',
    'icing', 'guild', 'spoke', 'decay', 'total',
    'crust', 'shalt', 'scoff', 'flush', 'glout',
    'mixer', 'glare', 'scour', 'sugar', 'clock',
    'quark', 'gyros', 'nasty', 'style', 'queer',
    'queue', 'zebra', 'ample', 'vague', 'hello',
    'trout', 'entry', 'jinks', 'oozed', 'cyber',
    'apple', 'erect', 'nonce', 'idiot', 'goofy'

]

word = word_list[random.randint(0, len(word_list) - 1)]

window = Tk()
window.title('WORDLE')

green = '#32a852'
yellow = '#fffb14'
grey = '#262622'
black = '#080808'
white = '#f2f3f5'

window.config(bg=black)
app_title = Label(window, text = 'WORDLE', font = ('Arial Bold', 30), bg = black, fg = white)
app_title.grid(row = 0, column = 0, columnspan = 5, padx = 15, pady = 15)

user_input = Entry(window)
user_input.grid(row = 100, column = 0, padx = 15, pady = 15, columnspan = 3)

round_num = 1


def Guess():
    global word, round_num
    user_guess = user_input.get()

    if round_num <= 5:
        if len(user_guess) == 5:
            if user_guess == word:
                for i, guessLetter in enumerate(user_guess):
                    guessLabel = Label(window, text=guessLetter.upper())
                    guessLabel.grid(row=round_num, column=i, padx=15, pady=15)
                    guessLabel.config(bg=green, fg=grey)

                messagebox.showinfo(f'CONGRATS', f'YOU GUESSED THE WORD IN {round_num} TRIES!')

            else:
                for i, guessLetter in enumerate(user_guess):
                    guessLabel = Label(window, text=guessLetter.upper())
                    guessLabel.grid(row = round_num, column = i, padx = 15, pady = 15)

                    if guessLetter == word[i]:
                        guessLabel.config(bg = green, fg = grey)

                    if guessLetter in word and not guessLetter == word[i]:
                        guessLabel.config(bg = yellow, fg = grey)

                    if guessLetter not in word:
                        guessLabel.config(bg = white, fg = grey)
        else:
            messagebox.showinfo('ERROR', 'TYPE IN WORDS WITH 5 CHARACTERS')

        round_num += 1

    elif round_num == 6:
        messagebox.showinfo('YOU LOSE', f'THE WORD WAS: {word}')


user_guessButton = Button(window, text='GUESS', command=Guess)
user_guessButton.grid(row=100, column=3, columnspan=2)

window.mainloop()