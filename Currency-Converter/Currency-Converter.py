from currency_converter import CurrencyConverter
import tkinter as tk

a = CurrencyConverter()

window = tk.Tk()
window.geometry("500x360")

# Function to perform currency conversion
def clicked():
    try:
        amount = int(amount_entry.get())
        first_currency = first_currency_entry.get().upper()
        second_currency = second_currency_entry.get().upper()
        data = a.convert(amount, first_currency, second_currency)
        label_result.config(text=f"{data:.2f}")
    except Exception as e:
        label_result.config(text=f"Error: {e}")

# Title
title_label = tk.Label(window, text='Currency Converter', font="Times 25 bold")
title_label.place(x=100, y=30)

# Amount
amount_label = tk.Label(window, text='Enter amount here -> ', font='Times 18 bold')
amount_label.place(x=50, y=80)
amount_entry = tk.Entry(window)
amount_entry.place(x=280, y=80)

# First Currency
first_currency_label = tk.Label(window, text="Convert Currency  -> ", font='Times 18 bold')
first_currency_label.place(x=50, y=110)
first_currency_entry = tk.Entry(window)
first_currency_entry.place(x=280, y=110)

# Second Currency
second_currency_label = tk.Label(window, text="into req currency -> ", font="Time 15 bold")
second_currency_label.place(x=50, y=140)
second_currency_entry = tk.Entry(window)
second_currency_entry.place(x=280, y=140)

# Button
convert_button = tk.Button(window, text="Convert", command=clicked)
convert_button.place(x=200, y=180)

# Result Label
label_result = tk.Label(window, text="", font='Times 20 bold')
label_result.place(x=210, y=220)

window.mainloop()
