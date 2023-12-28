from tkinter import *
import random
#import pyperclip as clipboard

# создание окна
window = Tk()
window.title('Генератор паролей')
window.resizable(width=False, height=False)
w = window.winfo_screenwidth()
h = window.winfo_screenheight()
w = w // 2
h = h // 2
w = w - 150
h = h - 100
window.geometry(f'300x200+{w}+{h}')

# объявление необходимых переменных
upper_state = IntVar()
lower_state = IntVar()
symbol_state = IntVar()
numbers_state = IntVar()
len_pass = IntVar()
numbers = [str(i) for i in range(10)]
abc_upper = [chr(c) for c in range(ord('A'), ord('Z') - 1)]
abc_lower = [chr(c) for c in range(ord('a'), ord('z') - 1)]
symbol = ['!', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', ':', ';', '=', '>', '<', '?', '@']

# описание работы генератора пароля
def chek_setting():
    password = []
    for i in range(len_pass.get()):
        if numbers_state.get():
            password.append(numbers[random.randint(0, len(numbers) - 1)])
        if upper_state.get():
            password.append(abc_upper[random.randint(0, len(abc_upper) - 1)])
        if lower_state.get():
            password.append(abc_lower[random.randint(0, len(abc_lower) - 1)])
        if symbol_state.get():
            password.append(symbol[random.randint(0, len(symbol) - 1)])

    for i in range(5):
        random.shuffle(password)

    password = password[:len_pass.get()]
    lbl2.configure(text=''.join(password))


lbl1 = Label(window, text='Количество символов:')
lbl1.grid(row=0, column=0, sticky=W, padx=10)

len_password = Spinbox(window, from_=5, to=20, width=5, textvariable=len_pass, state="readonly")
len_password.grid(row=1, column=0, sticky=W, padx=15)

chk_chars_upper = Checkbutton(window, text='Добавить цифры', variable=numbers_state)
chk_chars_upper.grid(row=2, column=0, sticky=W, padx=10)

chk_chars_upper = Checkbutton(window, text='Добавить заглавные английские буквы', variable=upper_state)
chk_chars_upper.grid(row=3, column=0, sticky=W, padx=10)

chk_chars_lower = Checkbutton(window, text='Добавить прописные английские буквы', variable=lower_state)
chk_chars_lower.grid(row=4, column=0, sticky=W, padx=10)

chk_spec_symbol = Checkbutton(window, text='Добавить спецсимволы !#$%^&*()-_+:;=><?@', variable=symbol_state)
chk_spec_symbol.grid(row=5, column=0, sticky=W, padx=10)

btn = Button(window, text='Сгенерировать', bg='blue', fg="yellow", font=("Arial Bold", 10), command=chek_setting)
btn.grid(column=0, row=6, sticky=W, padx=15)

lbl2 = Label(window, text='', font=("Arial", 15))
lbl2.grid(column=0, row=7, sticky=W, padx=10)


window.mainloop()