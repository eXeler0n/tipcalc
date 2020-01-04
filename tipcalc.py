# Tip calculator GUI by eXeler0n

from tkinter import *
from tkinter.ttk import *

# Basic window properties
window = Tk()
window.title('Trinkgeldrechner')
window.geometry('350x150')

# Calculation and fill results
def calculate():
    amount = float(inp_amount.get().replace(',', '.')) # Get amount and change
                                                       # , to .
    tip05 = round((amount*1.05)-amount, 2)
    tip10 = round((amount*1.10)-amount, 2)
    tip15 = round((amount*1.15)-amount, 2)
    result05 = round((amount*1.05), 2)
    result10 = round((amount*1.10), 2)
    result15 = round((amount*1.15), 2)

    lbl_tip05 = Label(window, text=str(tip05).replace('.', ','), width=10)
    lbl_tip10 = Label(window, text=str(tip10).replace('.', ','), width=10)
    lbl_tip15 = Label(window, text=str(tip15).replace('.', ','), width=10)
    lbl_result05 = Label(window, text=str(result05).replace('.', ','), width=10)
    lbl_result10 = Label(window, text=str(result10).replace('.', ','), width=10)
    lbl_result15 = Label(window, text=str(result15).replace('.', ','), width=10)
    lbl_pay05 = Label(window, text=int(result05), width=10)
    lbl_pay10 = Label(window, text=int(result10), width=10)
    lbl_pay15 = Label(window, text=int(result15), width=10)

    lbl_tip05.grid(column=1, row=4)
    lbl_tip10.grid(column=2, row=4)
    lbl_tip15.grid(column=3, row=4)
    lbl_result05.grid(column=1, row=5)
    lbl_result10.grid(column=2, row=5)
    lbl_result15.grid(column=3, row=5)
    lbl_pay05.grid(column=1, row=6)
    lbl_pay10.grid(column=2, row=6)
    lbl_pay15.grid(column=3, row=6)

# Empty lines
lbl_empty0 = Label(window, text=' ', width=10)
lbl_empty1 = Label(window, text=' ', width=10)
lbl_empty2 = Label(window, text=' ', width=10)
lbl_empty0.grid(column=0, row=0)
lbl_empty1.grid(column=0, row=2)
lbl_empty2.grid(column=2, row=1)

# Ask for invoice amount
lbl_amount = Label(window, text='Rechnungsbetrag:', width=20)
inp_amount = Entry(window, width=10)
lbl_amount.grid(column=0, row=1)
inp_amount.grid(column=1, row=1)

# Result table texts
lbl_servicefactor = Label(window, text='Servicefaktor:', width=20)
lbl_tip = Label(window, text='Trinkgeld:', width=20)
lbl_result = Label(window, text='Gesamtbetrag:', width=20)
lbl_pay = Label(window, text='Rundungsbetrag:', width=20)
lbl_servicefactor05 = Label(window, text='5%', width=10)
lbl_servicefactor10 = Label(window, text='10%', width=10)
lbl_servicefactor15 = Label(window, text='15%', width=10)

lbl_servicefactor.grid(column=0, row=3)
lbl_tip.grid(column=0, row=4)
lbl_result.grid(column=0, row=5)
lbl_pay.grid(column=0, row=6)
lbl_servicefactor05.grid(column=1, row=3)
lbl_servicefactor10.grid(column=2, row=3)
lbl_servicefactor15.grid(column=3, row=3)

# Calculate button
btn_calc = Button(window, text='Berechnen', command=calculate, width=10)
btn_calc.grid(column=3, row=1)

# Create window
window.mainloop()