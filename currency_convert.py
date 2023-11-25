from tkinter import *
import math

def to_ngn():
    rate = float(current_input.get())
    amount = float(amount_input.get())
    result = rate * amount
    formatted_amount = format(result, ',')
    result_label.config(text=f"₦{formatted_amount}")
    result_code_label.config(text="NGN", pady=10)


def to_usd():
    rate = float(current_input.get())
    amount = float(amount_input.get())
    result = amount / rate
    formatted_amount = format(result, ',')
    result_label.config(text=f"${formatted_amount}")
    result_code_label.config(text="USD", pady=10)


window = Tk()
window.title("USD <> NGN")
window.config(padx=20, pady=20, bg="green")

current_value = Label(text="What is the current Naira value to $1 ?   ₦", font=("Arial", 14, "bold"), bg="green")
current_value.grid(row=0, column=0)

current_input = Entry(width=7, bg="green", highlightthickness=1)
current_input.grid(row=0, column=1)
current_input.focus()

amount_label = Label(text="Amount to Convert:", font=("Arial", 14, "bold"), bg="green")
amount_label.grid(row=1, column=0)

amount_input = Entry(width=12, bg="green",highlightthickness=0)
amount_input.grid(row=1, column=1)


# currency_label = Label(text=f"Code", font=("Arial", 14, "bold"))
# currency_label.grid(row=1, column=2)

to_naira = Button(text="To NGN", command=to_ngn, highlightbackground="green")
to_naira.grid(row=2, column=1)

to_dollar = Button(text="To USD", command=to_usd, highlightbackground="green")
to_dollar.grid(row=2, column=2)

equal_to_label = Label(text="Is Equal to:", font=("Arial", 14, "bold"), bg="green")
equal_to_label.grid(row=3, column=0)

result_label = Label(text="0", font=("Arial", 14, "bold"), bg="green")
result_label.grid(row=3, column=1)

result_code_label = Label(text="Code", font=("Arial", 14, "bold"), bg="green")
result_code_label.grid(row=3, column=2)

# exit_btn = Button(text="Exit")
# exit_btn.grid(row=4, column=1)





window.mainloop()