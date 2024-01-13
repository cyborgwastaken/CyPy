from tkinter import *
from tkinter import ttk
import textwrap
from ttkthemes import ThemedStyle

class GamessGenerator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1600x800")  # Set the window size
        self.root.title("Gamess Input Generator")

        # Apply the materialistic theme
        style = ThemedStyle(self.root)
        style.set_theme("arc")

        # Configure the style to match the theme
        button_bg_color = style.lookup("TButton", "background")
        style.configure("TLabel", background=button_bg_color, font=("APTOS", 12), foreground="black")
        style.configure("TCombobox", background=button_bg_color, font=("APTOS", 12), foreground="black")
        style.configure("TButton", background=button_bg_color, font=("APTOS", 12), foreground="black")
        self.root.configure(background=button_bg_color)  # Set the window background

        # Default optimization information
        self.optInfo = {
            'guess': 'HUCKEL',
            'runtyp': 'Optimize',
            'scfmeth': 'RHF',
            'lvl': 'MPLEVL=2',
            'charge': '0',
            'spin': '1',
            'memory': '10',
            'memddi': '1',
            'basis': 'cc-pVDZ',
            'geom': ' ',
        }

        # Define the Gamess input file template
        self.gamess_template = textwrap.dedent('''
            $CONTRL SCFTYP={scfmeth} {lvl} RUNTYP={runtyp} ICHARG={charge}
            COORD=UNIQUE MULT={spin} MAXIT=200 ISPHER=1 $END
            $SYSTEM MWORDS={memory} MEMDDI ={memddi} $END
            $SCF DIRSCF=.TRUE. $END $CPHF CPHF=AO $END
            $STATPT NSTEP=100 HSSEND=.T. $END
            $BASIS  GBASIS={basis} $END
            $GUESS  GUESS={guess} $END
            $DATA
            optg and freq
            C1
            {geom}
            $END
        ''')

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Dictionary of options for each parameter
        options_dict = {
            'guess': ['HUCKEL', 'HCore'],
            'runtyp': ['Energy', 'Hessian', 'Optimisation'],
            'scfmeth': ['RHF', 'UHF', 'ROHF', 'GVB', 'MCSCF'],
            'lvl': ['MPLEVL=2', 'DFT'],
            'charge': ['0', '1', '2', '3', '4', '5'],
            'spin': ['1', '2'],
            'memory': ['10', '20', '30'],
            'memddi': ['1', '2', '3'],
            'basis': ['cc-pVDZ', 'cc-pVTZ', 'cc-pVQZ'],
            'geom': ['']          
        }

        row_counter = 0
        column_counter = 0

        # Create and place labels and comboboxes
        for param, param_options in options_dict.items():
            label = ttk.Label(self.root, text=f"Choose {param.capitalize()}:")
            label.grid(row=row_counter, column=column_counter * 2, sticky=W, pady=5, padx=10)  # Align to the left with some padding
            var = StringVar()
            var.set(param_options[0])
            drop = ttk.Combobox(self.root, textvariable=var, values=param_options, state='readonly', width=15)
            drop.grid(row=row_counter, column=column_counter * 2 + 1, sticky=E+W, pady=5, padx=10)  # Align to the left and right with some padding
            setattr(self, f"{param}_var", var)

            column_counter += 1

            # Move to the next row after every three parameters
            if column_counter == 3:
                column_counter = 0
                row_counter += 1

        row_counter += 1

        # Text widget to display generated code
        self.preview = Text(self.root, height=15, width=100, wrap=WORD, font=("APTOS", 12), foreground="black")
        self.preview.grid(row=row_counter, column=0, columnspan=6, sticky=N+E+S+W, pady=5, padx=10)  # Align to the top, left, right, and bottom with some padding

        # Label for the preview title
        preview_title = ttk.Label(self.root, text="Preview", font=("APTOS", 16, "bold"), foreground="black")
        preview_title.grid(row=row_counter, column=0, columnspan=6, sticky=N, pady=10)

        row_counter += 1

        # Button to generate Gamess input
        generate_button = ttk.Button(self.root, text="Generate Gamess Input", command=self.generate_gamess_input)
        generate_button.grid(row=row_counter, column=0, columnspan=6, sticky=N+E+S+W, pady=10, padx=10)  # Align to the top, left, right, and bottom with some padding

        # Configure row and column weights
        for i in range(row_counter + 1):
            self.root.rowconfigure(i, weight=1)
        for i in range(6):
            self.root.columnconfigure(i, weight=1)

    def generate_gamess_input(self):
        parameters = {param: getattr(self, f"{param}_var").get() for param in self.optInfo}
        parameters['pre'] = '$SCF DIRSCF=.TRUE. $END $CPHF CPHF=AO $END'
        parameters['post'] = ''
        gamess_input = self.gamess_template.format(**parameters)

        # Clear previous content
        self.preview.delete(1.0, END)
        # Insert the generated code into the preview
        self.preview.insert(1.0, gamess_input)

        # Save the Gamess input to a text file
        with open('gamess_input.txt', 'w') as file:
            file.write(gamess_input)

if __name__ == "__main__":
    root = Tk()
    app = GamessGenerator(root)
    root.resizable(False, False)  # Allow the window to be resizable in both directions
    root.mainloop()
