from tkinter import *
root = Tk()
e = Entry(root, width=25, borderwidth=4) #Acts as the screen of the calculator
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#region Calculation Functions
def add():
    first_number = e.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    e.delete(0, END)

def subtract():
    first_number = e.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    e.delete(0, END)

def multiply():
    first_number = e.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    e.delete(0, END)

def divide():
    first_number = e.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    e.delete(0, END)

def sum():
    second_number = e.get()
    e.delete(0, END)
    match math:
        case "addition":
            e.insert(0, f_num + int(second_number))
        case "subtraction":
            e.insert(0, f_num - int(second_number))
        case "multiplication":
            e.insert(0, f_num * int(second_number))
        case "division":
            checkIsDivisible(int(second_number))

#endregion

#region Calculator functions
def checkIsDivisible(secondNum):
    if secondNum == 0:
        e.insert(0, "Error! Cannot divide by 0!")
        for button in calculatorButtons:
            if button != button_clear:
                button["state"] = "disabled"
    else:
        e.insert(0, f_num / int(secondNum))

def clear():
    e.delete(0, END)
    for button in calculatorButtons:
        button["state"] = "normal"

def insertNumber(number):
    currentNum = e.get()
    e.delete(0, END)
    e.insert(0, str(currentNum) + str(number))
#endregion

def createButton(btnText, xPadding, yPadding, btnCommand):
    newButton = Button(root, text=btnText, padx=xPadding, pady=yPadding, font=("Arial 16"), command=btnCommand)
    return newButton

button_1 = createButton("1", 40, 20, lambda: insertNumber(1))
button_2 = createButton("2", 40, 20, lambda: insertNumber(2))
button_3 = createButton("3", 40, 20, lambda: insertNumber(3))
button_4 = createButton("4", 40, 20, lambda: insertNumber(4))
button_5 = createButton("5", 40, 20, lambda: insertNumber(5))
button_6 = createButton("6", 40, 20, lambda: insertNumber(6))
button_7 = createButton("7", 40, 20, lambda: insertNumber(7))
button_8 = createButton("8", 40, 20, lambda: insertNumber(8))
button_9 = createButton("9", 40, 20, lambda: insertNumber(9))
button_0 = createButton("0", 40, 20, lambda: insertNumber(0))

button_equal = createButton("=", 91, 20, sum)
button_clear = createButton("Clear", 79, 20, clear)

button_add = createButton("+", 39, 20, add)
button_subtract = createButton("-", 41, 20, subtract)
button_multiply = createButton("*", 40, 20, multiply)
button_divide = createButton("/", 41, 20,  divide)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)

button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

calculatorButtons = [button_0, button_1, button_2, button_3, button_4, button_5,
                     button_6, button_7, button_8, button_9, button_0, button_equal,
                     button_clear, button_add, button_subtract, button_multiply, button_divide]

root.mainloop()