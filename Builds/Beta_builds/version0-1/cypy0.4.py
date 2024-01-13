from tkinter import *
from tkinter import ttk
import textwrap
from ttkthemes import ThemedStyle

class GamessGenerator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")  # Set the window size
        self.root.title("Gamess Input Generator")

        # Apply the materialistic theme
        style = ThemedStyle(self.root)
        style.set_theme("equilux")

        # Configure the style to match the theme
        button_bg_color = style.lookup("TButton", "background")
        style.configure("TLabel", background=button_bg_color)
        style.configure("TCombobox", background=button_bg_color)
        style.configure("TButton", background=button_bg_color)
        self.root.configure(background=button_bg_color)  # Set the window background

        # Default optimization information
        self.optInfo = {
            'scfmeth': 'RHF',
            'lvl': 'MPLEVL=2',
            'charge': '0',
            'spin': '1',
            'memory': '10',
            'memddi': '1',
            'pre': '$SCF DIRSCF=.TRUE. $END\n$CPHF CPHF=AO $END',
            'post': '',
            'basis': 'cc-pVDZ',
            'geom': ''
        }

        # Define the Gamess input file template
        self.gamess_template = textwrap.dedent('''
            $CONTRL SCFTYP={scfmeth} {lvl} RUNTYP=OPTIMIZE ICHARG={charge}
            COORD=UNIQUE MULT={spin} MAXIT=200 ISPHER=1 $END
            $SYSTEM MWORDS={memory} MEMDDI ={memddi} $END
            {pre}
            $STATPT NSTEP=100 HSSEND=.T. $END
            {post}
            $BASIS  GBASIS={basis} $END
            $GUESS  GUESS=HUCKEL $END
            $DATA
            optg and freq
            C1
            {geom}
            $END
        ''')

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        # Create a treeview
        tree = ttk.Treeview(self.root, columns=('Value',), show='headings')
        tree.heading('Value', text='Value')
        tree.pack(expand=YES, fill=BOTH)

        # Dictionary of options for each parameter
        options_dict = {
            'scfmeth': ['RHF', 'UHF', 'ROHF'],
            'lvl': ['MPLEVL=2', ''],
            'charge': ['0', '1', '2', '3', '4', '5'],
            'spin': ['1', '2'],
            'memory': ['10', '20', '30'],
            'memddi': ['1', '2', '3'],
            'pre': ['$SCF DIRSCF=.TRUE. $END $CPHF CPHF=AO $END', ''],
            'post': ['', '$CCINP MAXCC=100 $END $FORCE METHOD=FULLNUM $END'],
            'basis': ['cc-pVDZ', 'cc-pVTZ', 'cc-pVQZ'],
            'geom': ['']  # Replace with your actual geometry options
        }

        for param, param_options in options_dict.items():
            label = ttk.Label(self.root, text=f"Choose {param.capitalize()}:")
            label.pack(anchor=W, pady=5, padx=10)  # Align to the left with some padding
            var = StringVar()
            var.set(param_options[0])
            drop = ttk.Combobox(self.root, textvariable=var, values=param_options, state='readonly', width=15)
            drop.pack(anchor=W, pady=5, padx=10)  # Align to the left with some padding

            # Insert the parameter into the treeview
            tree.insert('', 'end', values=(f"{param.capitalize()}: {var.get()}",))

        # Button to generate Gamess input
        generate_button = ttk.Button(self.root, text="Generate Gamess Input", command=self.generate_gamess_input)
        generate_button.pack(anchor=W, pady=10, padx=10)  # Align to the left with some padding

        # Label to display generated Gamess input
        self.label = ttk.Label(self.root, text="")
        self.label.pack(anchor=W, pady=10, padx=10)  # Align to the left with some padding

    def generate_gamess_input(self):
        parameters = {param: getattr(self, f"{param}_var").get() for param in self.optInfo}
        gamess_input = self.gamess_template.format(**parameters)
        self.label.config(text=gamess_input)

        # Save the Gamess input to a text file
        with open('gamess_input.txt', 'w') as file:
            file.write(gamess_input)

if __name__ == "__main__":
    root = Tk()
    app = GamessGenerator(root)
    root.resizable(True, True)  # Allow the window to be resizable in both directions
    root.mainloop()
