import PySimpleGUI as sg

sg.theme('Topanga')      # Add some color to the window

# Data entry.  Return values using auto numbered keys

layout = [
    [sg.Text('Please enter your account varialbles below.')],
    [sg.Text('Principle', size=(15, 1)), sg.InputText()],
    [sg.Text('Rate of Return', size=(15, 1)), sg.InputText()],
    [sg.Text('Compounding Schedule'),sg.InputCombo(('Annaually', 'Quarterly', 'Monthly', 'Daily'), size=(15, 1))],
    [sg.Text('Years to Invest', size=(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]

window = sg.Window('Compund Interest Calculator', layout)
event, values = window.read()

#print(event, values[0], values[1], values[2], values[3])    # the input data looks like a simple list when auto numbered

#Program Logic

principle = values[0]
intPrinciple = int(principle)
percent = values[1]
convert = float(percent)
rate = convert*.01
compound = values[2]
year = values[3]
intYear = int(year)

if compound == "Annaually":
    t = 1
elif compound == "Quarterly":
    t = 4
elif compound == "Monthly":
    t = 12
elif compound == "Daily":
    t = 360
else:
    print("Input not valid.")

intT = int(t)

ammount = intPrinciple*(1+(rate/intT))**(intT*intYear)

ammountRounded = round(ammount, 2)

window.close()

sg.popup("Your $"+ principle +" investment will be worth $" + str(ammountRounded) + "!")
#print("Your investment will be worth $" + str(ammountRounded) + "!") 
