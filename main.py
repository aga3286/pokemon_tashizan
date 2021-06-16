from tkinter import *
from calculator import Calculator
from pockemon import Pockemon

calc = Calculator()
pockemon = Pockemon(calc)

window = Tk()
window.title('pockemon')
window.config(padx=20, pady=20, bg='#a5e1ad')

title = Label(text='こうへいのたしざん', font=('Arial', 50, 'bold'), fg='#21094e', bg='#a5e1ad')
title.grid(row=0, column=0, columnspan=10)

canvas = Canvas(width=1000, height=200, bg='#4ca1a3', highlightthickness=0)
text = canvas.create_text(500, 100, text=calc.get_formula(), font=('Arial', 150, 'bold'))
canvas.grid(row=1, column=0, columnspan=10)

sentence_canvas = Canvas(width=1000, height=100, bg='#4ca1a3', highlightthickness=0)
sentence = sentence_canvas.create_text(500, 50, text="がんばってね！！", font=('Arial', 50, 'bold'))
sentence_canvas.grid(row=2, column=0, columnspan=10)

pockemon_canvas = Canvas(width=1000, height=200, highlightthickness=0, bg='#4ca1a3')
pockemon_canvas.grid(row=3, column=0, columnspan=10)

photoimages = []
for pockemon_name in pockemon.pockemons:
    photoimages.append(PhotoImage(file=f'img/{pockemon_name}.png').subsample(3))

def create_pockemon():
    if pockemon.cnt % 7 == 0 and pockemon.cnt > 6:
        pockemon_canvas.delete("all")
    pockemon_canvas.create_image(140 * ((pockemon.cnt % 7) + 1) - 50, 100, image=photoimages[pockemon.choose_pockemon()])

def delete_pockemon():
    pockemon_canvas.delete("all")

def pushed(input):
    def inner():
        calc.check_answer(input)
        if len(calc.answered_list) < 45:
            sentence_canvas.itemconfig(sentence, text=display_sentence())
            window.after(2000, next_formula)
        else:
            sentence_canvas.itemconfig(sentence, text='よくがんばったね！')
            canvas.itemconfig(text, text='')
    return inner

def display_sentence():
    if calc.true_or_false[-1]:
        create_pockemon()
        pockemon.cnt += 1

        canvas.itemconfig(text, text=f'{calc.displayed_combination[0]} + {calc.displayed_combination[1]} = {calc.displayed_answer}')
        return 'よくできました！'
    else:
        delete_pockemon()
        pockemon.cnt = 0
        return f'{calc.displayed_combination[0]} + {calc.displayed_combination[1]} =' \
               f' {calc.displayed_answer} です'


def next_formula():
    canvas.itemconfig(text, text=calc.get_formula())
    sentence_canvas.itemconfig(sentence, text='')


for i in range(1, 21):
    row = (i - 1) // 10 + 4
    column = (i - 1) % 10
    number_obj = Button(text=str(i), font=('Arial', 50, 'bold'), width=2, height=1,
                        command=pushed(i))
    number_obj.grid(row=row, column=column)

window.mainloop()
