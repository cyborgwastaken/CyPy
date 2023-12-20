from tkinter import *
import textwrap

root = Tk()  # Create the main window

root.geometry("300x200")  # Set the window size

def show():
    gamess_input = gamess_template.format(charge=charge_var.get(), spin=spin_var.get())
    label.config(text=gamess_input)

    # Save the Gamess input to a text file
    with open('gamess_input.txt', 'w') as file:
        file.write(gamess_input)

# Create a list of charge and spin options
charge_options = ["0", "1", "2", "3", "4", "5"]
spin_options = ["1", "2"]

# Variable to store the selected charge and spin values
charge_var = StringVar()
spin_var = StringVar()

# Set default values
charge_var.set(charge_options[0])
spin_var.set(spin_options[0])

# Create dropdown menus for charge and spin
charge_drop = OptionMenu(root, charge_var, *charge_options)
spin_drop = OptionMenu(root, spin_var, *spin_options)

charge_label = Label(root, text="Choose Charge:")
charge_label.pack()
charge_drop.pack()

spin_label = Label(root, text="Choose Spin:")
spin_label.pack()
spin_drop.pack()

# Create a button that triggers the show function when clicked
button = Button(root, text="Generate Gamess Input", command=show)
button.pack()

# Define the Gamess input file template
gamess_template = textwrap.dedent('''
     $CONTRL SCFTYP=RHF RUNTYP=OPTIMIZE ICHARG={charge}
     COORD=UNIQUE MULT={spin} MAXIT=200 ISPHER=1 $END
     $SYSTEM MWORDS=10 MEMDDI=1 $END
     $STATPT NSTEP=100 HSSEND=.T. $END
     $BASIS GBASIS=rt $END
     $GUESS GUESS=HUCKEL $END
     $DATA
    optg and freq
    C1
    gggg
    $END
''')

# Create a label with the Gamess template
label = Label(root, text="")
label.pack()

root.mainloop()  # Start the main event loop
