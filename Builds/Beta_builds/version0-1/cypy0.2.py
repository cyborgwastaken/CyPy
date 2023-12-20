from tkinter import *
import textwrap

class GamessGenerator:
    def __init__(self, root):
        self.root = root
        self.root.geometry("400x400")  # Set the window size
        self.root.title("Gamess Input Generator")

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
            label = Label(self.root, text=f"Choose {param.capitalize()}:")
            label.pack()
            var = StringVar()
            var.set(param_options[0])
            drop = OptionMenu(self.root, var, *param_options)
            drop.pack()

            setattr(self, f"{param}_var", var)

        # Button to generate Gamess input
        generate_button = Button(self.root, text="Generate Gamess Input", command=self.generate_gamess_input)
        generate_button.pack()

        # Label to display generated Gamess input
        self.label = Label(self.root, text="")
        self.label.pack()

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
    root.mainloop()
