import tkinter

#window
window = tkinter.Tk()
window.title('BMI Calculator')
window.config(bg='snow3')
window.minsize(300, 150)
window.update()

#weight label
weight_label = tkinter.Label(text='Enter Your Weight (kg)', bg='snow3', font=('Arial', 15, 'roman'))
weight_label.place(x=(window.winfo_width()/2)-(weight_label.winfo_reqwidth()/2),
                   y=(window.winfo_height())/2*0.2)

#weight entry
weight_entry = tkinter.Entry(width=20)
weight_entry.place(x=(window.winfo_width()/2) - (weight_entry.winfo_reqwidth()/2),
                   y=(window.winfo_height())/2*0.5)
weight_entry.focus()

#height label
height_label = tkinter.Label(text='Enter Your Height (cm)', bg='snow3', font=('Arial', 15, 'roman'))
height_label.place(x=(window.winfo_width()/2) - (height_label.winfo_reqwidth()/2),
                   y=(window.winfo_height())/2*0.8)

#height entry
height_entry = tkinter.Entry(width=20)
height_entry.place(x=(window.winfo_width()/2) - (height_entry.winfo_reqwidth()/2),
                   y=(window.winfo_height())/2*1.1)

#calculate button
user_bmi = 0
text = ''
def button_func():
    global user_bmi
    global text
    user_weight = weight_entry.get()
    user_height = height_entry.get()
    if user_weight.isnumeric() and user_height.isnumeric():
        user_weight = int(user_weight)
        user_height = int(user_height)
        user_bmi = user_weight / (user_height/100)**2
        print(info_text(user_bmi))
    elif user_weight == '' or user_height == '':
        info_label.config(text='Please fill in the blank fields')
    else:
        info_label.config(text= 'Please enter valid numbers')
    window.update_idletasks()
    info_label.place(x=(window.winfo_width() / 2) - (info_label.winfo_reqwidth() / 2),
                     y=(window.winfo_height()) / 2 * 1.7)

calculate_button = tkinter.Button(text='Calculate', command=button_func)
calculate_button.place(x=(window.winfo_width()/2) - (calculate_button.winfo_reqwidth()/2),
                       y=(window.winfo_height())/2*1.4)

#info label
def info_text(user_bmi):
    global text
    if 0 < user_bmi <= 18.4:
        info_label.config(text=f'Your BMI is {user_bmi: .2f}. You are underweight')
    elif 18.5 <= user_bmi <= 24.9:
        info_label.config(text=f'Your BMI is {user_bmi: .2f}. You are normal weight')
    elif 25.0 <= user_bmi <= 29.9:
        info_label.config(text=f'Your BMI is {user_bmi: .2f}. You are overweight')
    elif 30.0 <= user_bmi <= 34.9:
        info_label.config(text=f'Your BMI is {user_bmi: .2f}. You are class 1 obese')
    elif 35.0 <= user_bmi <= 39.9:
        info_label.config(text=f'Your BMI is {user_bmi: .2f}. You are class 2 obese')
    elif user_bmi >= 40.0:
        info_label.config(text=f'Your BMI is {user_bmi: .2f}. You are class 3 obese')

    window.update()
    info_label.place(x=(window.winfo_width() / 2) - (info_label.winfo_reqwidth() / 2),
                     y=(window.winfo_height()) / 2 * 1.7)

info_label = tkinter.Label(bg='snow3', font=('Arial', 12, 'normal'))
info_label.place(x=(window.winfo_width()/2) - (info_label.winfo_reqwidth()/2),
                 y=(window.winfo_height())/2*1.7)


window.mainloop()