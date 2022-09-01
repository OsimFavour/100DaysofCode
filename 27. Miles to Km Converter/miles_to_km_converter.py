from tkinter import *

def miles_to_km():
    miles = miles_input.get()
    km = round(float(miles) * 1.609)
    km_answer.config(text=km)


window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

# Entry
miles_input = Entry(width=7)
print(miles_input.get())
miles_input.grid(column=1, row=0)

# Label widgets

miles = Label(text="Miles", font=("Consolas", 12, "bold")) 
miles.grid(column=2, row=0)     

km = Label(text="km", font=("Consolas", 10, "bold"))
km.grid(column=2, row=1)

is_equal_to = Label(text="is equal to", font=("Consolas", 10, "bold"))
is_equal_to.grid(column=0, row=1)

km_answer = Label(text="0")
km_answer.grid(column=1, row=1)

# Button 

calculate = Button(text="Calculate", command=miles_to_km)
calculate.grid(column=1, row=3)



window.mainloop()