from tkinter import ttk  
from tkinter import *  
# Initial setup  
root = Tk()  
root.title("Unit Converter")  
root.resizable(False,False)
root.geometry("400x400")  
root.config(bg="#EE82EE")  
def welcome_message():  


    welcome_window = Toplevel()  
    welcome_window.title("Welcome!")  
    welcome_window.geometry("350x350")  
    welcome_window.config(bg="black")  

 
    heart_label = Label(welcome_window, text="❤️", font=("bold", 60), bg="black", fg="#EE82EE")  
    heart_label.pack(pady=10)  

    message_label = Label(welcome_window, text="Welcome to the conversion app!\nThis program is created by A.P",  
                          font=("bold", 15),bg="black" ,fg="#EE82EE")  
    message_label.pack(pady=20)  

 
    close_button = Button(welcome_window, text="Close", command=welcome_window.destroy, bg="#EE82EE", fg="black",font="bold")  
    close_button.pack(pady=10)  

    welcome_window.transient(root)   
    welcome_window.grab_set()       

welcome_message()  

# Function to check if input is a number  
def checkValue(val):  
    try:  
        float(val)  
        return True  
    except ValueError:  
        return False  

# Function to convert units  
def convert():  
    value = entry1.get()  

    if value == '':  
        lbl.config(text="Input cannot be empty!")  
        return  

    if not checkValue(value):  
        lbl.config(text="This is not a number!")  
        return  

    value = float(value)  

    # Get selected values from comboboxes  
    combos1 = combo1.get()  
    combos2 = combo2.get()  
    combos3 = combo3.get()  

    result = 0  

    # Currency conversion  
    if combos1 == "MONEY":  
        if combos2 == "TOMAN" and combos3 == "DOLLAR":  
            result = value / 61000  
        elif combos2 == "DOLLAR" and combos3 == "TOMAN":  
            result = value * 61000  
        elif combos2 == "TOMAN" and combos3 == "EURO":  
            result = value / 68150  
        elif combos2 == "EURO" and combos3 == "TOMAN":  
            result = value * 68150  
        elif combos2 == "DOLLAR" and combos3 == "EURO":  
            result = value * 0.834  
        elif combos2 == "EURO" and combos3 == "DOLLAR":  
            result = value / 0.834  
        elif combos2 == "POUND" and combos3 == "DOLLAR":  
            result = value * 1.2  
        elif combos2 == "DOLLAR" and combos3 == "POUND":  
            result = value / 1.2  
        elif combos2 == combos3:  
            result = value  

    # Length conversion  
    elif combos1 == "LENGTH":  
        if combos2 == "METER" and combos3 == "CENTIMETER":  
            result = value * 100  
        elif combos2 == "CENTIMETER" and combos3 == "METER":  
            result = value / 100  
        elif combos2 == "METER" and combos3 == "MILIMETER":  
            result = value * 1000  
        elif combos2 == "MILIMETER" and combos3 == "METER":  
            result = value / 1000  
        elif combos2 == "KILOMETER" and combos3 == "METER":  
            result = value * 1000  
        elif combos2 == "METER" and combos3 == "KILOMETER":  
            result = value / 1000  
        elif combos2 == combos3:  
            result = value  

    # Temperature conversion  
    elif combos1 == "TEMPERATURE":  
        if combos2 == "CELSIUS" and combos3 == "FAHRENHEIT":  
            result = value * 1.8 + 32  
        elif combos2 == "FAHRENHEIT" and combos3 == "CELSIUS":  
            result = (value - 32) / 1.8  
        elif combos2 == "KELVIN" and combos3 == "CELSIUS":  
            result = value - 273.15  
        elif combos2 == "CELSIUS" and combos3 == "KELVIN":  
            result = value + 273.15  
        elif combos2 == "FAHRENHEIT" and combos3 == "KELVIN":  
            result = (value - 32) / 1.8 + 273.15  
        elif combos2 == "KELVIN" and combos3 == "FAHRENHEIT":  
            result = value * 1.8 - 459.67  
        elif combos2 == combos3:  
            result = value  

    lbl.config(text=f"Result: {result:.2f}")  

# Function to update comboboxes based on selection  
def get(event):  
    combo2['values'] = []  
    combo3['values'] = []  
    if combo1.get() == "MONEY":  
        combo2['values'] = ("DOLLAR", "EURO", "TOMAN", "POUND")  
        combo3['values'] = ("DOLLAR", "EURO", "TOMAN", "POUND")  
    elif combo1.get() == "LENGTH":  
        combo2['values'] = ("METER", "CENTIMETER", "MILIMETER", "KILOMETER")  
        combo3['values'] = ("METER", "CENTIMETER", "MILIMETER", "KILOMETER")  
    elif combo1.get() == "TEMPERATURE":  
        combo2['values'] = ("CELSIUS", "FAHRENHEIT", "KELVIN")  
        combo3['values'] = ("CELSIUS", "FAHRENHEIT", "KELVIN")  
    
    combo2.current(0)  
    combo3.current(0)  

combo1 = ttk.Combobox(root, state="readonly")  
combo1['values'] = ("MONEY", "LENGTH", "TEMPERATURE")  
combo1.current(0)  
combo1.bind("<<ComboboxSelected>>", get)  
combo1.pack()  

# Label for "FROM"  
lbl112 = Label(root, text="FROM", bg="#EE82EE")  
lbl112.pack()  

combo2 = ttk.Combobox(root, state="readonly")  
combo2.pack()  
# Label for "TO"  
lbl223 = Label(root, text="TO", bg="#EE82EE")  
lbl223.pack()  

# Combobox for second unit  
combo3 = ttk.Combobox(root)  
combo3.pack()  

# Input for number  
entry1 = Entry(root)  
entry1.pack()  

# Button to perform conversion  
btn = Button(root, command=convert, text="CONVERT", height=2, width=12, bg="black", fg="#EE82EE", font="bold")  
btn.pack()  

# Label to display result  
lbl = Label(root, bg="#EE82EE", font="bold")  
lbl.pack()  

# Initialize the comboboxes for the first time  
get(None)  

# Run the main loop  
root.mainloop()