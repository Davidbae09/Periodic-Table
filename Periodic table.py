import tkinter as tk
from tkinter import messagebox


class PeriodicTableApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Periodic Table")
        
        # Set the window to a zoomed state
        self.state('zoomed')
        # self.state('zoomed')  # Alternative for some platforms

        self.elements = {
            'H': {'name': 'Hydrogen', 'atomic_number': 1, 'atomic_mass': 1.008, 'type': 'Non-metal', 'color': '#005db3'},
            'He': {'name': 'Helium', 'atomic_number': 2, 'atomic_mass': 4.002602, 'type': 'Noble Gas', 'color': '#996b77'},
            'Li': {'name': 'Lithium', 'atomic_number': 3, 'atomic_mass': 6.94, 'type': 'Alkali Metal', 'color': '#6b9899'},
            'Be': {'name': 'Beryllium', 'atomic_number': 4, 'atomic_mass': 9.0122, 'type': 'Alkaline Earth Metal', 'color': '#ad2b43'},
            'B': {'name': 'Boron', 'atomic_number': 5, 'atomic_mass': 10.81, 'type': 'Metalloid', 'color': '#8a6006'},
            'C': {'name': 'Carbon', 'atomic_number': 6, 'atomic_mass': 12.011, 'type': 'Non-metal', 'color': '#005db3'},
            'N': {'name': 'Nitrogen', 'atomic_number': 7, 'atomic_mass': 14.007, 'type': 'Non-metal', 'color': '#005db3'},
            'O': {'name': 'Oxygen', 'atomic_number': 8, 'atomic_mass': 15.999, 'type': 'Non-metal', 'color': '#005db3'},
            'F': {'name': 'Fluorine', 'atomic_number': 9, 'atomic_mass': 18.998, 'type': 'Halogen', 'color': '#005db3'},
            'Ne': {'name': 'Neon', 'atomic_number': 10, 'atomic_mass': 20.180, 'type': 'Noble Gas', 'color': '#996b77'},
            'Na': {'name': 'Sodium', 'atomic_number': 11, 'atomic_mass': 22.989769, 'type': 'Alkali Metal', 'color': '#6b9899'},
            'Mg': {'name': 'Magnesium', 'atomic_number': 12, 'atomic_mass': 24.305, 'type': 'Alkaline Earth Metal', 'color': '#ad2b43'},
            'Al': {'name': 'Aluminum', 'atomic_number': 13, 'atomic_mass': 26.981539, 'type': 'Post-transition Metal', 'color': '#47f5b5'},
            'Si': {'name': 'Silicon', 'atomic_number': 14, 'atomic_mass': 28.085, 'type': 'Metalloid', 'color': '#8a6006'},
            'P': {'name': 'Phosphorus', 'atomic_number': 15, 'atomic_mass': 30.973762, 'type': 'Non-metal', 'color': '#005db3'},
            'S': {'name': 'Sulfur', 'atomic_number': 16, 'atomic_mass': 32.06, 'type': 'Non-metal', 'color': '#005db3'},
            'Cl': {'name': 'Chlorine', 'atomic_number': 17, 'atomic_mass': 35.45, 'type': 'Halogen', 'color': '#005db3'},
            'Ar': {'name': 'Argon', 'atomic_number': 18, 'atomic_mass': 39.948, 'type': 'Noble Gas', 'color': '#996b77'},
            'K': {'name': 'Potassium', 'atomic_number': 19, 'atomic_mass': 39.098, 'type': 'Alkali Metal', 'color': '#6b9899'},
            'Ca': {'name': 'Calcium', 'atomic_number': 20, 'atomic_mass': 40.078, 'type': 'Alkaline Earth Metal', 'color': '#ad2b43'},
            'Sc': {'name': 'Scandium', 'atomic_number': 21, 'atomic_mass': 44.956, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Ti': {'name': 'Titanium', 'atomic_number': 22, 'atomic_mass': 47.867, 'type': 'Transition Metal', 'color': '#f439f7'},
            'V': {'name': 'Vanadium', 'atomic_number': 23, 'atomic_mass': 50.9415, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Cr': {'name': 'Chromium', 'atomic_number': 24, 'atomic_mass': 51.996, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Mn': {'name': 'Manganese', 'atomic_number': 25, 'atomic_mass': 54.938, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Fe': {'name': 'Iron', 'atomic_number': 26, 'atomic_mass': 55.845, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Co': {'name': 'Cobalt', 'atomic_number': 27, 'atomic_mass': 58.933, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Ni': {'name': 'Nickel', 'atomic_number': 28, 'atomic_mass': 58.933, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Cu': {'name': 'Copper', 'atomic_number': 29, 'atomic_mass': 63.546, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Zn': {'name': 'Zinc', 'atomic_number': 30, 'atomic_mass': 65.38, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Ga': {'name': 'Gallium', 'atomic_number': 31, 'atomic_mass': 69.723, 'type': 'Post-transition Metal', 'color': '#47f5b5'},
            'Ge': {'name': 'Germanium', 'atomic_number': 32, 'atomic_mass': 72.630, 'type': 'Metalloid', 'color': '#8a6006'},
            'As': {'name': 'Arsenic', 'atomic_number': 33, 'atomic_mass': 74.921595, 'type': 'Metalloid', 'color': '#8a6006'},
            'Se': {'name': 'Selenium', 'atomic_number': 34, 'atomic_mass': 78.971, 'type': 'Non-metal', 'color': '#005db3'},
            'Br': {'name': 'Bromine', 'atomic_number': 35, 'atomic_mass': 79.904, 'type': 'Halogen', 'color': '#005db3'},
            'Kr': {'name': 'Krypton', 'atomic_number': 36, 'atomic_mass': 83.798, 'type': 'Noble Gas', 'color': '#996b77'},
            'Rb': {'name': 'Rubidium', 'atomic_number': 37, 'atomic_mass': 85.4678, 'type': 'Alkali Metal', 'color': '#6b9899'},
            'Sr': {'name': 'Strontium', 'atomic_number': 38, 'atomic_mass': 87.621, 'type': 'Alkaline Earth Metal', 'color': '#ad2b43'},
            'Y': {'name': 'Yttrium', 'atomic_number': 39, 'atomic_mass': 88.90584, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Zr': {'name': 'Zirconium', 'atomic_number': 40, 'atomic_mass': 91.224, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Nb': {'name': 'Niobium', 'atomic_number': 41, 'atomic_mass': 92.90637, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Mo': {'name': 'Molybdenum', 'atomic_number': 42, 'atomic_mass': 95.961, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Tc': {'name': 'Technetium', 'atomic_number': 43, 'atomic_mass': 98, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Ru': {'name': 'Ruthenium', 'atomic_number': 44, 'atomic_mass': 101.07, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Rh': {'name': 'Rhodium', 'atomic_number': 45, 'atomic_mass': 102.90550, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Pd': {'name': 'Palladium', 'atomic_number': 46, 'atomic_mass': 106.42, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Ag': {'name': 'Silver', 'atomic_number': 47, 'atomic_mass': 107.8682, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Cd': {'name': 'Cadmium', 'atomic_number': 48, 'atomic_mass': 112.414, 'type': 'Transition Metal', 'color': '#f439f7'},
            'In': {'name': 'Indium', 'atomic_number': 49, 'atomic_mass': 114.818, 'type': 'Post-transition Metal', 'color': '#47f5b5'},
            'Sn': {'name': 'Tin', 'atomic_number': 50, 'atomic_mass': 118.710, 'type': 'Post-transition Metal', 'color': '#47f5b5'},
            'Sb': {'name': 'Antimony', 'atomic_number': 51, 'atomic_mass': 121.760, 'type': 'Metalloid', 'color': '#8a6006'},
            'Te': {'name': 'Tellurium', 'atomic_number': 52, 'atomic_mass': 127.60, 'type': 'Metalloid', 'color': '#8a6006'},
            'I': {'name': 'Iodine', 'atomic_number': 53, 'atomic_mass': 126.90447, 'type': 'Halogen', 'color': '#005db3'},
            'Xe': {'name': 'Xenon', 'atomic_number': 54, 'atomic_mass': 131.293, 'type': 'Noble Gas', 'color': '#996b77'},
            'Cs': {'name': 'Cesium', 'atomic_number': 55, 'atomic_mass': 132.90545196, 'type': 'Alkali Metal', 'color': '#6b9899'},
            'Ba': {'name': 'Barium', 'atomic_number': 56, 'atomic_mass': 137.327, 'type': 'Alkaline Earth Metal', 'color': '#ad2b43'},
            'La': {'name': 'Lanthanum', 'atomic_number': 57, 'atomic_mass': 138.904, 'type': 'Lanthanide', 'color': '#39d4f7'},
            'Ce': {'name': 'Cerium', 'atomic_number': 58, 'atomic_mass': 140.116, 'type': 'Lanthanide', 'color': '#39d4f7'},
            'Pr': {'name': 'Praseodymium', 'atomic_number': 59, 'atomic_mass': 140.90766, 'type': 'Lanthanide', 'color': '#39d4f7'},
            'Nd': {'name': 'Neodymium', 'atomic_number': 60, 'atomic_mass': 144.242, 'type': 'Lanthanide', 'color': '#39d4f7'},
            'Pm': {'name': 'Promethium', 'atomic_number': 61, 'atomic_mass': 145, 'type': 'Lanthanide', 'color': '#39d4f7'},
            'Sm': {'name': 'Samarium', 'atomic_number': 62, 'atomic_mass': 150.36, 'type': 'Lanthanide', 'color': '#39d4f7'},
            'Eu': {'name': 'Europium', 'atomic_number': 63, 'atomic_mass': 151.964, 'type': 'Lanthanide', 'color': '#39d4f7'},
            'Gd': {'name': 'Gadolinium', 'atomic_number': 64, 'atomic_mass': 157.25, 'type': 'Lanthanide', 'color': '#39d4f7'},
            'Tb': {'name': 'Terbium', 'atomic_number': 65, 'atomic_mass': 158.92535, 'type': 'Lanthanide', 'color': '#39d4f7'},
            'Dy': {'name': 'Dysprosium', 'atomic_number': 66, 'atomic_mass': 162.500, 'type': 'Lanthanide', 'color': '#39d4f7'},
            'Ho': {'name': 'Holmium', 'atomic_number': 67, 'atomic_mass': 164.93033, 'type': 'Lanthanide', 'color': '#39d4f7'},
            'Er': {'name': 'Erbium', 'atomic_number': 68, 'atomic_mass': 167.259, 'type': 'Lanthanide', 'color': '#39d4f7'},
            'Tm': {'name': 'Thulium', 'atomic_number': 69, 'atomic_mass': 168.93422, 'type': 'Lanthanide', 'color': '#39d4f7'},
            'Yb': {'name': 'Ytterbium', 'atomic_number': 70, 'atomic_mass': 173.04, 'type': 'Lanthanide', 'color': '#39d4f7'},
            'Lu': {'name': 'Lutetium', 'atomic_number': 71, 'atomic_mass': 174.9668, 'type': 'Lanthanide', 'color': '#39d4f7'},
            'Hf': {'name': 'Hafnium', 'atomic_number': 72, 'atomic_mass': 178.49, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Ta': {'name': 'Tantalum', 'atomic_number': 73, 'atomic_mass': 180.94788, 'type': 'Transition Metal', 'color': '#f439f7'},
            'W': {'name': 'Tungsten', 'atomic_number': 74, 'atomic_mass': 183.84, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Re': {'name': 'Rhenium', 'atomic_number': 75, 'atomic_mass': 186.207, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Os': {'name': 'Osmium', 'atomic_number': 76, 'atomic_mass': 190.23, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Ir': {'name': 'Iridium', 'atomic_number': 77, 'atomic_mass': 192.217, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Pt': {'name': 'Platinum', 'atomic_number': 78, 'atomic_mass': 195.084, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Au': {'name': 'Gold', 'atomic_number': 79, 'atomic_mass': 196.966569, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Hg': {'name': 'Mercury', 'atomic_number': 80, 'atomic_mass': 200.592, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Tl': {'name': 'Thallium', 'atomic_number': 81, 'atomic_mass': 204.38, 'type': 'Post-transition Metal', 'color': '#47f5b5'},
            'Pb': {'name': 'Lead', 'atomic_number': 82, 'atomic_mass': 207.2, 'type': 'Post-transition Metal', 'color': '#47f5b5'},
            'Bi': {'name': 'Bismuth', 'atomic_number': 83, 'atomic_mass': 208.98040, 'type': 'Post-transition Metal', 'color': '#47f5b5'},
            'Po': {'name': 'Polonium', 'atomic_number': 84, 'atomic_mass': 209, 'type': 'Metalloid', 'color': '#47f5b5'},
            'At': {'name': 'Astatine', 'atomic_number': 85, 'atomic_mass': 210, 'type': 'Halogen', 'color': '#47f5b5'},
            'Rn': {'name': 'Radon', 'atomic_number': 86, 'atomic_mass': 222, 'type': 'Noble Gas', 'color': '#996b77'},
            'Fr': {'name': 'Francium', 'atomic_number': 87, 'atomic_mass': 223, 'type': 'Alkali Metal', 'color': '#6b9899'},
            'Ra': {'name': 'Radium', 'atomic_number': 88, 'atomic_mass': 226, 'type': 'Alkaline Earth Metal', 'color': '#ad2b43'},
            'Ac': {'name': 'Actinium', 'atomic_number': 89, 'atomic_mass': 227, 'type': 'Actinide', 'color': '#694c45'},
            'Th': {'name': 'Thorium', 'atomic_number': 90, 'atomic_mass': 232.038, 'type': 'Actinide', 'color': '#694c45'},
            'Pa': {'name': 'Protactinium', 'atomic_number': 91, 'atomic_mass': 231.03588, 'type': 'Actinide', 'color': '#694c45'},
            'U': {'name': 'Uranium', 'atomic_number': 92, 'atomic_mass': 238.02891, 'type': 'Actinide', 'color': '#694c45'},
            'Np': {'name': 'Neptunium', 'atomic_number': 93, 'atomic_mass': 237.0482, 'type': 'Actinide', 'color': '#694c45'},
            'Pu': {'name': 'Plutonium', 'atomic_number': 94, 'atomic_mass': 244, 'type': 'Actinide', 'color': '#694c45'},
            'Am': {'name': 'Americium', 'atomic_number': 95, 'atomic_mass': 243.0614, 'type': 'Actinide', 'color': '#694c45'},
            'Cm': {'name': 'Curium', 'atomic_number': 96, 'atomic_mass': 247, 'type': 'Actinide', 'color': '#694c45'},
            'Bk': {'name': 'Berkelium', 'atomic_number': 97, 'atomic_mass': 247, 'type': 'Actinide', 'color': '#694c45'},
            'Cf': {'name': 'Californium', 'atomic_number': 98, 'atomic_mass': 251, 'type': 'Actinide', 'color': '#694c45'},
            'Es': {'name': 'Einsteinium', 'atomic_number': 99, 'atomic_mass': 252, 'type': 'Actinide', 'color': '#694c45'},
            'Fm': {'name': 'Fermium', 'atomic_number': 100, 'atomic_mass': 257, 'type': 'Actinide', 'color': '#694c45'},
            'Md': {'name': 'Mendelevium', 'atomic_number': 101, 'atomic_mass': 258, 'type': 'Actinide', 'color': '#694c45'},
            'No': {'name': 'Nobelium', 'atomic_number': 102, 'atomic_mass': 259, 'type': 'Actinide', 'color': '#694c45'},
            'Lr': {'name': 'Lawrencium', 'atomic_number': 103, 'atomic_mass': 262, 'type': 'Actinide', 'color': '#694c45'},
            'Rf': {'name': 'Rutherfordium', 'atomic_number': 104, 'atomic_mass': 267, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Db': {'name': 'Dubnium', 'atomic_number': 105, 'atomic_mass': 270, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Sg': {'name': 'Seaborgium', 'atomic_number': 106, 'atomic_mass': 271, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Bh': {'name': 'Bohrium', 'atomic_number': 107, 'atomic_mass': 270, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Hs': {'name': 'Hassium', 'atomic_number': 108, 'atomic_mass': 277, 'type': 'Transition Metal', 'color': '#f439f7'},
            'Mt': {'name': 'Meitnerium', 'atomic_number': 109, 'atomic_mass': 278, 'type': 'Transition Metal', 'color': '#d2d2d2'},
            'Ds': {'name': 'Darmstadtium', 'atomic_number': 110, 'atomic_mass': 281, 'type': 'Transition Metal', 'color': '#d2d2d2'},
            'Rg': {'name': 'Roentgenium', 'atomic_number': 111, 'atomic_mass': 282, 'type': 'Transition Metal', 'color': '#d2d2d2'},
            'Cn': {'name': 'Copernicium', 'atomic_number': 112, 'atomic_mass': 285, 'type': 'Transition Metal', 'color': '#d2d2d2'},
            'Nh': {'name': 'Nihonium', 'atomic_number': 113, 'atomic_mass': 286, 'type': 'Post-transition Metal', 'color': '#d2d2d2'},
            'Fl': {'name': 'Flerovium', 'atomic_number': 114, 'atomic_mass': 289, 'type': 'Post-transition Metal', 'color': '#d2d2d2'},
            'Mc': {'name': 'Moscovium', 'atomic_number': 115, 'atomic_mass': 288, 'type': 'Post-transition Metal', 'color': '#d2d2d2'},
            'Lv': {'name': 'Livermorium', 'atomic_number': 116, 'atomic_mass': 293, 'type': 'Post-transition Metal', 'color': '#d2d2d2'},
            'Ts': {'name': 'Tennessine', 'atomic_number': 117, 'atomic_mass': 294, 'type': 'Halogen', 'color': '#d2d2d2'},
            'Og': {'name': 'Oganesson', 'atomic_number': 118, 'atomic_mass': 294, 'type': 'Noble Gas', 'color': '#d2d2d2'},
        }
       # Define element positions with adjusted coordinates
        self.positions = {
            'H': (0, 0), 'He': (0, 18),
            'Li': (1, 0), 'Be': (1, 1), 'B': (1, 13), 'C': (1, 14), 'N': (1, 15), 'O': (1, 16), 'F': (1, 17), 'Ne': (1, 18),
            'Na': (2, 0), 'Mg': (2, 1), 'Al': (2, 13), 'Si': (2, 14), 'P': (2, 15), 'S': (2, 16), 'Cl': (2, 17), 'Ar': (2, 18),
            'K': (3, 0), 'Ca': (3, 1), 'Sc': (3, 2), 'Ti': (3, 4), 'V': (3, 5), 'Cr': (3, 6), 'Mn': (3, 7), 'Fe': (3, 8),
            'Co': (3, 9), 'Ni': (3, 10), 'Cu': (3, 11), 'Zn': (3, 12), 'Ga': (3, 13), 'Ge': (3, 14), 'As': (3, 15),
            'Se': (3, 16), 'Br': (3, 17), 'Kr': (3, 18),
            'Rb': (4, 0), 'Sr': (4, 1), 'Y': (4, 2), 'Zr': (4, 4), 'Nb': (4, 5), 'Mo': (4, 6), 'Tc': (4, 7), 'Ru': (4, 8),
            'Rh': (4, 9), 'Pd': (4, 10), 'Ag': (4, 11), 'Cd': (4, 12), 'In': (4, 13), 'Sn': (4, 14), 'Sb': (4, 15),
            'Te': (4, 16), 'I': (4, 17), 'Xe': (4, 18),
            'Cs': (5, 0), 'Ba': (5, 1), 'La': (5, 2), 'Ce': (8, 4), 'Pr': (8, 5), 'Nd': (8, 6), 'Pm': (8, 7),
            'Sm': (8, 8), 'Eu': (8, 9), 'Gd': (8, 10), 'Tb': (8, 11), 'Dy': (8, 12), 'Ho': (8, 13), 'Er': (8, 14),
            'Tm': (8, 15), 'Yb': (8, 16), 'Lu': (8, 17), 'Hf': (5, 4), 'Ta': (5, 5), 'W': (5, 6), 'Re': (5, 7),
            'Os': (5, 8), 'Ir': (5, 9), 'Pt': (5, 10), 'Au': (5, 11), 'Hg': (5, 12), 'Tl': (5, 13), 'Pb': (5, 14),
            'Bi': (5, 15), 'Po': (5, 16), 'At': (5, 17), 'Rn': (5, 18),
            'Fr': (6, 0), 'Ra': (6, 1), 'Ac': (6, 2), 'Th': (9, 4), 'Pa': (9, 5), 'U': (9, 6), 'Np': (9, 7),
            'Pu': (9, 8), 'Am': (9, 9), 'Cm': (9, 10), 'Bk': (9, 11), 'Cf': (9, 12), 'Es': (9, 13), 'Fm': (9, 14),
            'Md': (9, 15), 'No': (9, 16), 'Lr': (9, 17),
            'Rf': (6, 4), 'Db': (6, 5), 'Sg': (6, 6), 'Bh': (6, 7), 'Hs': (6, 8), 'Mt': (6, 9), 'Ds': (6, 10),
            'Rg': (6, 11), 'Cn': (6, 12), 'Nh': (6, 13), 'Fl': (6, 14), 'Mc': (6, 15), 'Lv': (6, 16), 'Ts': (6, 17), 'Og': (6, 18)
        }


        # Create periodic table layout
        for element, (row, col) in self.positions.items():
            button = tk.Button(self, text=element, width=5, height=2, bg=self.elements[element]['color'],
                               command=lambda el=element: self.show_element_info(el))
            button.grid(row=row, column=col, sticky='nsew')

        # Add empty cells for layout
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(6, weight=1)
        self.grid_rowconfigure(7, weight=1)
        self.grid_rowconfigure(8, weight=1)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.grid_columnconfigure(6, weight=1)
        self.grid_columnconfigure(7, weight=1)
        self.grid_columnconfigure(8, weight=1)
        self.grid_columnconfigure(9, weight=1)
        self.grid_columnconfigure(10, weight=1)
        self.grid_columnconfigure(11, weight=1)
        self.grid_columnconfigure(12, weight=1)
        self.grid_columnconfigure(13, weight=1)
        self.grid_columnconfigure(14, weight=1)
        self.grid_columnconfigure(15, weight=1)
        self.grid_columnconfigure(16, weight=1)
        self.grid_columnconfigure(17, weight=1)
        self.grid_columnconfigure(18, weight=1)

    def show_element_info(self, element):
        info = self.elements[element]
        messagebox.showinfo(
            f"{info['name']} (Z={info['atomic_number']})",
            f"Name: {info['name']}\nSymbol: {element}\nAtomic Number: {info['atomic_number']}\nAtomic Mass: {info['atomic_mass']}\nType: {info['type']}"
        )

if __name__ == "__main__":
    app = PeriodicTableApp()
    app.mainloop()