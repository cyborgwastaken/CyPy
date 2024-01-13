# CyPy
CyPy-InputBuilder

Navigate to Builds/Stable_builds/CyPYInputBulider1.0.py 

**Gamess Input Generator with Tkinter GUI**

This Python script provides a Graphical User Interface (GUI) for generating input files for the GAMESS (General Atomic and Molecular Electronic Structure System) quantum chemistry software. The GUI is built using the Tkinter library and features a clean, materialistic design with adjustable themes.

### Features:
- **Parameter Selection:** Users can choose various parameters such as the initial guess method, run type (Energy, Hessian, Optimization), SCF method (RHF, UHF, ROHF, GVB, MCSCF), basis set, charge, spin, memory allocation, and more.
- **Preview:** The application displays a preview of the generated GAMESS input file based on the selected parameters.
- **File Generation:** Users can generate the GAMESS input file directly from the GUI, and the generated input is displayed in a text area. Additionally, the input is saved to a text file named "gamess_input.txt."

### Usage:
1. Run the script (`gamess_input_generator.py`).
2. Choose desired parameters using the provided drop-down menus.
3. Click the "Generate Gamess Input" button.
4. The generated input will be displayed in the preview area, and a corresponding text file will be saved.

### Dependencies:
- Tkinter: GUI library for Python.
- ttkthemes: ThemedStyle for customizing the Tkinter GUI theme.

### Installation:
- Install the required dependencies using:
  ```
  pip install tk ttkthemes
  ```

### How to Run:
1. Execute the script:
   ```
   python gamess_input_generator.py
   ```
2. The GUI window will appear, allowing users to interactively generate GAMESS input files.

### Customization:
- Users can easily customize the GUI theme by adjusting the `style.set_theme("arc")` line to their preferred theme from the available ttkthemes.

### Note:
- Ensure that the GAMESS software is installed on the system and that the generated input files are used within a compatible GAMESS environment.

Feel free to contribute, report issues, or suggest improvements!
