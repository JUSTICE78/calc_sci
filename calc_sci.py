from tkinter import *
from winsound import *
import math
root = Tk()
root.title("calculator")
e = Entry(root, width=42, borderwidth=10)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_add(number):
  #  e.delete(5, END)
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def button_click():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global math
    math ="addition"
    e.delete(0, END)
def button_clear():
    e.delete(0, END)

# def button_min():
#     first_number2 = e.get()
#     global f_num2
#     f_num2 = int(first_number2)
#     e.delete(0, END)
def button_equal():
    second_number = e.get()
    e.delete(0, END)
    if math == "addition":
        e.insert(0, f_num + int(second_number))
    if math == "division":
        e.insert(0, f_num / int(second_number))
    if math == "subtraction":
        e.insert(0, f_num - int(second_number))
    if math == "multiplication":
        e.insert(0, f_num * int(second_number))
    if math == "os":
        e.insert(0, f_num * f_num)
def button_devide():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global math
    math ="division"
    e.delete(0, END)
def button_min():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global math
    math ="subtraction"
    e.delete(0, END)
def button_multiply():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global math
    math ="multiplication"
    e.delete(0, END)
def buuttoon_os():
    first_number = e.get()
    global f_num
    f_num = int(first_number)
    global math
    math ="os"
    e.delete(0, END)
def sci():
    sci_calc = Toplevel(root)
    sci_calc.title("scientific calculator")
    f = Entry(sci_calc, width=42, borderwidth=10)
    f.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
    def button_add(number):
  #  e.delete(5, END)
        current = f.get()
        f.delete(0, END)
        f.insert(0, str(current) + str(number))
    def button_click():
        first_number = f.get()
        global f_num
        f_num = int(first_number)
        global math
        math ="addition"
        f.delete(0, END)
    def button_clear():
        f.delete(0, END)

    # def button_min():
    #     first_number2 = e.get()
    #     global f_num2
    #     f_num2 = int(first_number2)
    #     e.delete(0, END)
    def button_equal():
        second_number = f.get()
        f.delete(0, END)
        if math == "addition":
            f.insert(0, f_num + int(second_number))
        if math == "division":
            f.insert(0, f_num / int(second_number))
        if math == "subtraction":
            f.insert(0, f_num - int(second_number))
        if math == "multiplication":
            f.insert(0, f_num * int(second_number))
        if math == "x²":
            f.insert(0, f_num * f_num)
        if math == "xⁿ":
            f.insert(0, f_num ** int(second_number))
        if math == "√":
            f.insert(0, f_num ** 0.5)
    def button_devide():
        first_number = f.get()
        global f_num
        f_num = int(first_number)
        global math
        math ="division"
        f.delete(0, END)
    def button_min():
        first_number = f.get()
        global f_num
        f_num = int(first_number)
        global math
        math ="subtraction"
        f.delete(0, END)
    def button_multiply():
        first_number = f.get()
        global f_num
        f_num = int(first_number)
        global math
        math ="multiplication"
        f.delete(0, END)
    def buuttoon_os():
        first_number = f.get()
        global f_num
        f_num = int(first_number)
        global math
        math ="x²"
        f.delete(0, END)
    def buutton_power():
        first_number = f.get()
        global f_num
        f_num = int(first_number)
        global math
        math ="xⁿ"
        f.delete(0, END)
    def buutton_gazer():
        first_number = f.get()
        global f_num
        f_num = int(first_number)
        global math
        math ="√"
        f.delete(0, END)
    button_1s = Button(sci_calc, text="1", padx=40, pady=20, command=lambda:button_add(1))
    button_2s = Button(sci_calc, text="2", padx=40, pady=20, command=lambda:button_add(2))
    button_3s = Button(sci_calc, text="3", padx=40, pady=20, command=lambda:button_add(3))
    button_4s = Button(sci_calc, text="4", padx=40, pady=20, command=lambda:button_add(4))
    button_5s = Button(sci_calc, text="5", padx=40, pady=20, command=lambda:button_add(5))
    button_6s = Button(sci_calc, text="6", padx=40, pady=20, command=lambda:button_add(6))
    button_7s = Button(sci_calc, text="7", padx=40, pady=20, command=lambda:button_add(7))
    button_8s = Button(sci_calc, text="8", padx=40, pady=20, command=lambda:button_add(8))
    button_9s = Button(sci_calc, text="9", padx=40, pady=20, command=lambda:button_add(9))
    button_0s = Button(sci_calc, text="0", padx=40, pady=20, command=lambda:button_add(0))
    button_ds = Button(sci_calc, text=".", padx=40, pady=20, command=lambda:button_add("."))
    button_mins = Button(sci_calc, text="-", padx=40, pady=20, command=button_min)
    button_plus = Button(sci_calc, text="+", padx=39, pady=20, command=button_click)
    button_equals = Button(sci_calc, text="=", padx=91, pady=20, command=button_equal)
    button_clears = Button(sci_calc, text="c", font='Helvetica 24 bold', padx=77, pady=5, bg = "red", command=button_clear)
    button_power = Button(sci_calc, text="xⁿ", padx=39, pady=20, command=buutton_power)
    button_gazer = Button(sci_calc, text="√ⁿ", padx=39, pady=20, command=buutton_gazer)

    button_multiplys = Button(sci_calc, text="x", padx=39, pady=20, command=button_multiply)
    button_devides = Button(sci_calc, text="/", padx=39, pady=20, command=button_devide)
    button_oss = Button(sci_calc, text="x²", padx=39, pady=20, command=buuttoon_os)
    button_1s.grid(row=1, column=0)
    button_2s.grid(row=1, column=1)
    button_3s.grid(row=1, column=2)

    button_4s.grid(row=2, column=0)
    button_5s.grid(row=2, column=1)
    button_6s.grid(row=2, column=2)

    button_7s.grid(row=3, column=0)
    button_8s.grid(row=3, column=1)
    button_9s.grid(row=3, column=2)
    button_ds.grid(row=5, column=1)
    button_0s.grid(row=4, column=0)
    button_clears.grid(row=4, column=1, columnspan=5)

    button_plus.grid(row=5, column=0)
    button_equals.grid(row=5, column=1, columnspan=5)

    button_mins.grid(row=6, column=0)
    button_multiplys.grid(row=6, column=1)
    button_devides.grid(row=6, column=2)
    button_oss.grid(row=6, column=3)
    button_power.grid(row=5, column=4)
    button_gazer.grid(row=5, column=5)

button_1 = Button(root, text="1", padx=40, pady=20, command=lambda:button_add(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda:button_add(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda:button_add(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda:button_add(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda:button_add(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda:button_add(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda:button_add(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda:button_add(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda:button_add(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda:button_add(0))
button_min = Button(root, text="-", padx=40, pady=20, command=button_min)
button_plu = Button(root, text="+", padx=39, pady=20, command=button_click)
button_equal = Button(root, text="=", padx=91, pady=20, command=button_equal)
button_clear = Button(root, text="c", font='Helvetica 24 bold', padx=77, pady=5, bg = "red", command=button_clear)
button_multiply = Button(root, text="x", padx=39, pady=20, command=button_multiply)
button_devide = Button(root, text="/", padx=39, pady=20, command=button_devide)
# button_os = Button(root, text="os", padx=39, pady=20, command=buuttoon_os)
button_sci = Button(root, text="sci calc", padx=39, pady=20, command=sci)


button_1.grid(row=1, column=0)
button_2.grid(row=1, column=1)
button_3.grid(row=1, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_0.grid(row=4, column=0)
button_clear.grid(row=4, column=1, columnspan=10)
button_plu.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=10)
button_min.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_devide.grid(row=6, column=2)
button_sci.grid(row=6, column=3)
# button_os.grid(row=6, column=3)



root.mainloop()