import random
import colorama
import time

colorama.init()

#· Periodic Table
indexelements = {"Hydrogen" : 0, "Helium" : 1, "Lithium" : 2, "Beryllium" : 3,
    "Boron" : 4, "Carbon" : 5, "Nitrogen" : 6, "Oxygen" : 7, "Fluorine" : 8,
    "Neon" : 9, "Sodium" : 10, "Magnesium" : 11, "Aluminium" : 12, "Silicon" : 13,
    "Phosphorus" : 14, "Sulfur" : 15, "Chlorine" : 16, "Argon" : 17, "Potassium" : 18,
    "Calcium" : 19, "Scandium" : 20, "Titanium" : 21, "Vanadium" : 22, "Chromium" : 23,
    "Manganese" : 24, "Iron" : 25, "Cobalt" : 26, "Nickel" : 27, "Copper" : 28, "Zinc" : 29,
    "Gallium" : 30, "Germanium" : 31, "Arsenic" : 32, "Selenium" : 33, "Bromine" : 34,
    "Krypton" : 35, "Rubidium" : 36, "Strontium" : 37, "Yttrium" : 38, "Zirconium" : 39, 
    "Niobium" : 40, "Molybdenum" : 41, "Technetium" : 42, "Ruthenium" : 43, "Rhodium" : 44,
    "Palladium" : 45, "Silver" : 46, "Cadmium" : 47, "Indium" : 48, "Tin" : 49, "Antimony" : 50,
    "Tellurium" : 51, "Iodine" : 52, "Xenon" : 53, "Cesium" : 54, "Barium" : 55, "Lanthanum" : 56, 
    "Cerium" : 57, "Praseodymium" : 58, "Neodymium" : 59, "Promethium" : 60, "Samarium" : 61,
    "Europium" : 62, "Gadolinium" : 63, "Terbium" : 64, "Dysprosium" : 65, "Holmium" : 66, 
    "Erbium" : 67, "Thulium" : 68, "Ytterbium" : 69, "Lutetium" : 70, "Hafnium" : 71,
    "Tantalum" : 72, "Tungsten" : 73, "Rhenium" : 74, "Osmium" : 75, "Iridium" : 76,
    "Platinum" : 77, "Gold" : 78, "Mercury" : 79, "Thallium" : 80, "Lead" : 81, 
    "Bismuth" : 82, "Polonium" : 83, "Astatine" : 84, "Radon" : 85, "Francium" : 86, 
    "Radium" : 87, "Actinium" : 88, "Thorium" : 89, "Protactinium" : 90, "Uranium" : 91, 
    "Neptunium" : 92, "Plutonium" : 93, "Americium" : 94, "Curium" : 95, "Berkelium" : 96,
    "Californium" : 97, "Einsteinium" : 98, "Fermium" : 99, "Mendelevium" : 100, 
    "Nobelium" : 101, "Lawrencium" : 102, "Rutherfordium" : 103, "Dubnium" : 104, 
    "Seaborgium" : 105, "Bohrium" : 106, "Hassium" : 107, "Meitnerium" : 108, 
    "Darmstadtium" : 109, "Roentgenium" : 110, "Copernicium" : 111, "Nihonium" : 112,
    "Flerovium" : 113, "Moscovium" : 114, "Livermorium" : 115, "Tennessine" : 116, 
    "Oganesson" : 117}

elements = [
    {'Name': 'Hydrogen', 'Symbol': 'H', 'Atomic mass (u)': 1.00784 , 'Density (when liquid at melting point) (g/cm3)': 0.07099 , 'Melting (°C)' : -259.16 , 'Boiling (°C)' : -252.879 , 'Protons' : 1 , 'Neutrons' : 0 , 'Binary': "1"},
    {'Name': 'Helium', 'Symbol': 'He', 'Atomic mass (u)': 4.002602 , 'Density (when liquid at melting point) (g/cm3)': 0.145 , 'Melting (°C)' : -272.2 , 'Boiling (°C)' : -268.93 , 'Protons' : 2 , 'Neutrons' : 2 , 'Binary': "10"},
    {'Name': 'Lithium', 'Symbol': 'Li', 'Atomic mass (u)': 6.941 , 'Density (when liquid at melting point) (g/cm3)': 0.512 , 'Melting (°C)' : 180.54 , 'Boiling (°C)' : 1330 , 'Protons' : 3 , 'Neutrons' : 4 , 'Binary': "11"},
    {'Name': 'Beryllium', 'Symbol': 'Be', 'Atomic mass (u)': 9.012182 , 'Density (when liquid at melting point) (g/cm3)': 1.690 , 'Melting (°C)' : 1287 , 'Boiling (°C)' : 2969.85 , 'Protons' : 4 , 'Neutrons' : 5 , 'Binary': "100"},
    {'Name': 'Boron', 'Symbol': 'B', 'Atomic mass (u)': 10.811 , 'Density (when liquid at melting point) (g/cm3)': 2.08 , 'Melting (°C)' : 2076 , 'Boiling (°C)' : 3927 , 'Protons' : 5 , 'Neutrons' : 6 , 'Binary': "101"},
    {'Name': 'Carbon', 'Symbol': 'C', 'Atomic mass (u)': 12.0107 , 'Density (when liquid at melting point) (g/cm3) (diamond)': 3.515 , 'Boiling (°C)' : 4827 , 'Protons' : 6 , 'Neutrons' : 6 , 'Binary': "110"},
    {'Name': 'Nitrogen', 'Symbol': 'N', 'Atomic mass (u)': 14.0067 , 'Density (when liquid at melting point) (g/cm3)': 0.808 , 'Melting (°C)' : -210.01 , 'Boiling (°C)' : -195.79 , 'Protons' : 7 , 'Neutrons' : 7 , 'Binary': "111"},
    {'Name': 'Oxygen', 'Symbol': 'O', 'Atomic mass (u)': 15.999 , 'Density (when liquid at melting point) (g/cm3)': 1.141 , 'Melting (°C)' : -218.79 , 'Boiling (°C)' : -182.962 , 'Protons' : 8 , 'Neutrons' : 8 , 'Binary': "1000"},
    {'Name': 'Fluorine', 'Symbol': 'F', 'Atomic mass (u)': 18.9984032 , 'Melting (°C)' : -219.62 , 'Boiling (°C)' : -188.11 , 'Protons' : 9 , 'Neutrons' : 10 , 'Binary': "1001"},
    {'Name': 'Neon', 'Symbol': 'Ne', 'Atomic mass (u)': 20.1797 , 'Melting (°C)' : -248.59 , 'Boiling (°C)' : -246.046 , 'Protons' : 10 , 'Neutrons' : 10 , 'Binary': "1010"},
    {'Name': 'Sodium', 'Symbol': 'Na', 'Atomic mass (u)': 22.98976928 , 'Density (when liquid at melting point) (g/cm3)': 0.927 , 'Melting (°C)' : 97.794 , 'Boiling (°C)' : 882.85 , 'Protons' : 11 , 'Neutrons' : 12 , 'Binary': "1011"},
    {'Name': 'Magnesium', 'Symbol': 'Mg', 'Atomic mass (u)': 24.305 , 'Density (when liquid at melting point) (g/cm3)': 1.584 , 'Melting (°C)' : 650 , 'Boiling (°C)' : 1091 , 'Protons' : 12 , 'Neutrons' : 12 , 'Binary': "1100"},
    {'Name': 'Aluminium', 'Symbol': 'Al', 'Atomic mass (u)': 26.9815386 , 'Density (when liquid at melting point) (g/cm3)': 2.375 , 'Melting (°C)' : 660.32 , 'Boiling (°C)' : 2470, 'Protons' : 13 , 'Neutrons' : 14 , 'Binary': "1101"},
    {'Name': 'Silicon', 'Symbol': 'Si', 'Atomic mass (u)': 28.0855 , 'Density (when liquid at melting point) (g/cm3)': 2.57 , 'Melting (°C)' : 1414 , 'Boiling (°C)' : 3265 , 'Protons' : 14 , 'Neutrons' : 14 , 'Binary': "1110"},
    {'Name': 'Phosphorus', 'Symbol': 'P', 'Atomic mass (u)': 30.973762 , 'Boiling (°C)' : 280.5 , 'Protons' : 15 , 'Neutrons' : 16 , 'Binary': "1111"},
    {'Name': 'Sulfur', 'Symbol': 'S', 'Atomic mass (u)': 32.065 , 'Density (when liquid at melting point) (g/cm3)': 1.819 , 'Melting (°C)' : 115.21 , 'Boiling (°C)' : 444.6 , 'Protons' : 16 , 'Neutrons' : 16 , 'Binary': "10000"},
    {'Name': 'Chlorine', 'Symbol': 'Cl', 'Atomic mass (u)': 35.453 , 'Boiling (°C)' : -34.04 , 'Protons' : 17 , 'Neutrons' : 18 , 'Binary': "10001"},
    {'Name': 'Argon', 'Symbol': 'Ar', 'Atomic mass (u)': 39.948 , 'Density (when liquid at melting point) (g/cm3)': 1.3954 , 'Melting (°C)' : -189.35 , 'Boiling (°C)' : -185.85 , 'Protons' : 18 , 'Neutrons' : 22 , 'Binary': "10010"},
    {'Name': 'Potassium', 'Symbol': 'K', 'Atomic mass (u)': 39.0983 , 'Density (when liquid at melting point) (g/cm3)': 0.828 , 'Melting (°C)' : 63.5 , 'Boiling (°C)' : 758.85 , 'Protons' : 19 , 'Neutrons' : 20 , 'Binary': "10011"},
    {'Name': 'Calcium', 'Symbol': 'Ca', 'Atomic mass (u)': 40.078 , 'Density (when liquid at melting point) (g/cm3)': 1.378 , 'Melting (°C)' : 842 , 'Boiling (°C)' : 1483.85 , 'Protons' : 20 , 'Neutrons' : 20 , 'Binary': "10100"},
    {'Name': 'Scandium', 'Symbol': 'Sc', 'Atomic mass (u)': 44.955912 , 'Density (when liquid at melting point) (g/cm3)': 2.80 , 'Melting (°C)' : 1541 , 'Boiling (°C)' : 2835.85 , 'Protons' : 21 , 'Neutrons' : 24 , 'Binary': "10101"},
    {'Name': 'Titanium', 'Symbol': 'Ti', 'Atomic mass (u)': 47.867 , 'Density (when liquid at melting point) (g/cm3)': 4.11 , 'Melting (°C)' : 1668 , 'Boiling (°C)' : 3286.85 , 'Protons' : 22 , 'Neutrons' : 26 , 'Binary': "10110"},
    {'Name': 'Vanadium', 'Symbol': 'V', 'Atomic mass (u)': 50.9415 , 'Density (when liquid at melting point) (g/cm3)': 5.5 , 'Melting (°C)' : 1910 , 'Boiling (°C)' : 3407 , 'Protons' : 23 , 'Neutrons' : 28 , 'Binary': "10111"},
    {'Name': 'Chromium', 'Symbol': 'Cr', 'Atomic mass (u)': 51.9961 , 'Density (when liquid at melting point) (g/cm3)': 6.3 , 'Melting (°C)' : 1907 , 'Boiling (°C)' : 2671.85 , 'Protons' : 24 , 'Neutrons' : 28 , 'Binary': "11000"},
    {'Name': 'Manganese', 'Symbol': 'Mn', 'Atomic mass (u)': 54.938044  , 'Density (when liquid at melting point) (g/cm3)': 5.95 , 'Melting (°C)' : 1246 , 'Boiling (°C)' : 2061 , 'Protons' : 25 , 'Neutrons' : 30 , 'Binary': "11001"},
    {'Name': 'Iron', 'Symbol': 'Fe', 'Atomic mass (u)': 55.845 , 'Density (when liquid at melting point) (g/cm3)': 6.98 , 'Melting (°C)' : 1538 , 'Boiling (°C)' : 2862 , 'Protons' : 26 , 'Neutrons' : 30 , 'Binary': "11010"},
    {'Name': 'Cobalt', 'Symbol': 'Co', 'Atomic mass (u)': 58.933195 , 'Density (when liquid at melting point) (g/cm3)': 8.86 , 'Melting (°C)' : 1495 , 'Boiling (°C)' : 2869.85 , 'Protons' : 27 , 'Neutrons' : 32 , 'Binary': "11011"},
    {'Name': 'Nickel', 'Symbol': 'Ni', 'Atomic mass (u)': 58.6934 , 'Density (when liquid at melting point) (g/cm3)': 7.81 , 'Melting (°C)' : 1455 , 'Protons' : 28 , 'Neutrons' : 31 , 'Binary': "11100"},
    {'Name': 'Copper', 'Symbol': 'Cu', 'Atomic mass (u)': 63.546 , 'Density (when liquid at melting point) (g/cm3)': 8.02 , 'Melting (°C)' : 1084.62 , 'Boiling (°C)' : 2562 , 'Protons' : 29 , 'Neutrons' : 35 , 'Binary': "11101"},
    {'Name': 'Zinc', 'Symbol': 'Zn', 'Atomic mass (u)': 65.38 , 'Density (when liquid at melting point) (g/cm3)': 6.57 , 'Melting (°C)' : 419.53 , 'Boiling (°C)' : 907 , 'Protons' : 30 , 'Neutrons' : 35 , 'Binary': "11110"},
    {'Name': 'Gallium', 'Symbol': 'Ga', 'Atomic mass (u)': 69.723 , 'Density (when liquid at melting point) (g/cm3)': 6.095 , 'Melting (°C)' : 29.7646 , 'Boiling (°C)' : 2400 , 'Protons' : 31 , 'Neutrons' : 39 , 'Binary': "11111"},
    {'Name': 'Germanium', 'Symbol': 'Ge', 'Atomic mass (u)': 72.64 , 'Density (when liquid at melting point) (g/cm3)': 5.60 , 'Melting (°C)' : 938.25 , 'Boiling (°C)' : 2833 , 'Protons' : 32 , 'Neutrons' : 41 , 'Binary': "100000"},
    {'Name': 'Arsenic', 'Symbol': 'As', 'Atomic mass (u)': 74.9216 , 'Density (when liquid at melting point) (g/cm3)': 5.22 , 'Melting (°C)' : 816.85 , 'Boiling (°C)' : 613 , 'Protons' : 33 , 'Neutrons' : 42 , 'Binary': "100001"},
    {'Name': 'Selenium', 'Symbol': 'Se', 'Atomic mass (u)': 78.96 , 'Density (when liquid at melting point) (g/cm3)': 3.99 , 'Melting (°C)' : 220 , 'Boiling (°C)' : 684.85 , 'Protons' : 34 , 'Neutrons' : 45 , 'Binary': "100010"},
    {'Name': 'Bromine', 'Symbol': 'Br', 'Atomic mass (u)': 79.904 , 'Melting (°C)' : -7.2 , 'Boiling (°C)': 58.8 , 'Protons' : 35 , 'Neutrons' : 45 , 'Binary': "100011"},
    {'Name': 'Krypton', 'Symbol': 'Kr', 'Atomic mass (u)': 83.798 , 'Melting (°C)' : -157.36 , 'Boiling (°C)': -153.415 , 'Protons' : 36 , 'Neutrons' : 48 , 'Binary': "100100"},
    {'Name': 'Rubidium', 'Symbol': 'Rb', 'Atomic mass (u)': 85.4678 , 'Density (when liquid at melting point) (g/cm3)': 1.46 , 'Melting (°C)' : 39.3 , 'Boiling (°C)' : 688 , 'Protons' : 37 , 'Neutrons' : 48 , 'Binary': "100101"},
    {'Name': 'Strontium', 'Symbol': 'Sr', 'Atomic mass (u)': 87.62 , 'Density (when liquid at melting point) (g/cm3)': 2.375 , 'Melting (°C)' : 777 , 'Boiling (°C)' : 1381.85 , 'Protons' : 38 , 'Neutrons' : 50 , 'Binary': "100110"},
    {'Name': 'Yttrium', 'Symbol': 'Y', 'Atomic mass (u)': 88.90585 , 'Density (when liquid at melting point) (g/cm3)': 4.24 , 'Melting (°C)' : 1526 , 'Boiling (°C)' : 3337.85 , 'Protons' : 39 , 'Neutrons' : 50 , 'Binary': "100111"},
    {'Name': 'Zirconium', 'Symbol': 'Zr', 'Atomic mass (u)': 91.224 , 'Density (when liquid at melting point) (g/cm3)': 5.8 , 'Melting (°C)' : 1855 , 'Boiling (°C)' : 4408.85 , 'Protons' : 40 , 'Neutrons' : 51 , 'Binary': "101000"},
    {'Name': 'Niobium', 'Symbol': 'Nb', 'Atomic mass (u)': 92.90638 , 'Density (when liquid at melting point) (g/cm3)': 8.57 , 'Melting (°C)' : 2477 , 'Boiling (°C)' : 4927 , 'Protons' : 41 , 'Neutrons' : 52 , 'Binary': "101001"},
    {'Name': 'Molybdenum', 'Symbol': 'Mo', 'Atomic mass (u)': 95.95 , 'Density (when liquid at melting point) (g/cm3)': 9.33 , 'Melting (°C)' : 2623 , 'Boiling (°C)' : 4638.85 , 'Protons' : 42 , 'Neutrons' : 54 , 'Binary': "101010"},
    {'Name': 'Technetium', 'Symbol': 'Tc', 'Atomic mass (u)': 98 , 'Melting (°C)' : 2157 , 'Boiling (°C)' : 4264.85 , 'Protons' : 43 , 'Neutrons' : 55 , 'Binary': "101011"},
    {'Name': 'Ruthenium', 'Symbol': 'Ru', 'Atomic mass (u)': 101.07 , 'Density (when liquid at melting point) (g/cm3)': 10.65 , 'Melting (°C)' : 2334 , 'Boiling (°C)' : 4150 , 'Protons' : 44 , 'Neutrons' : 57 , 'Binary': "101100"},
    {'Name': 'Rhodium', 'Symbol': 'Rh', 'Atomic mass (u)': 102.9055 , 'Density (when liquid at melting point) (g/cm3)': 10.7 , 'Melting (°C)' : 1964 , 'Boiling (°C)' : 3696.85 , 'Protons' : 45 , 'Neutrons' : 58 , 'Binary': "101101"},
    {'Name': 'Palladium', 'Symbol': 'Pd', 'Atomic mass (u)': 106.42 , 'Density (when liquid at melting point) (g/cm3)': 10.38 , 'Melting (°C)' : 1554.9 , 'Boiling (°C)' : 2963 , 'Protons' : 46, 'Neutrons' : 60 , 'Binary': "101110"},
    {'Name': 'Silver', 'Symbol': 'Ag', 'Atomic mass (u)': 107.8682 , 'Density (when liquid at melting point) (g/cm3)': 9.320 , 'Melting (°C)' : 961.78 , 'Boiling (°C)' : 2162 , 'Protons' : 47 , 'Neutrons' : 61 , 'Binary': "101111"},
    {'Name': 'Cadmium', 'Symbol': 'Cd', 'Atomic mass (u)': 112.411 , 'Density (when liquid at melting point) (g/cm3)': 7.996 , 'Melting (°C)' : 321.07 , 'Boiling (°C)' : 766.85 , 'Protons' : 48 , 'Neutrons' : 64 , 'Binary': "110000"},
    {'Name': 'Indium', 'Symbol': 'In', 'Atomic mass (u)': 114.818 , 'Density (when liquid at melting point) (g/cm3)': 7.02 , 'Melting (°C)' : 156.6 , 'Boiling (°C)' : 2072 , 'Protons' : 49 , 'Neutrons' : 66 , 'Binary': "110001"},
    {'Name': 'Tin', 'Symbol': 'Sn', 'Atomic mass (u)': 118.71 , 'Density (when liquid at melting point) (g/cm3)': 6.99 , 'Melting (°C)' : 231.93 , 'Boiling (°C)' : 2602 , 'Protons' : 50 , 'Neutrons' : 69 , 'Binary': "110010"},
    {'Name': 'Antimony', 'Symbol': 'Sb', 'Atomic mass (u)': 121.76 , 'Density (when liquid at melting point) (g/cm3)': 6.53 , 'Melting (°C)' : 630.63 , 'Boiling (°C)' : 1586.85 , 'Protons' : 51 , 'Neutrons' : 71 , 'Binary': "110011"},
    {'Name': 'Tellurium', 'Symbol': 'Te', 'Atomic mass (u)': 127.6 , 'Density (when liquid at melting point) (g/cm3)': 5.70 , 'Melting (°C)' : 449.51 , 'Boiling (°C)' : 987.85 , 'Protons' : 52 , 'Neutrons' : 76 , 'Binary': "110100"},
    {'Name': 'Iodine', 'Symbol': 'I', 'Atomic mass (u)': 126.90447 , 'Density (when liquid at melting point) (g/cm3)': 4.933 , 'Melting (°C)' : 113.7 , 'Boiling (°C)' : 184.3 , 'Protons' : 53 , 'Neutrons' : 74 , 'Binary': "110101"},
    {'Name': 'Xenon', 'Symbol': 'Xe', 'Atomic mass (u)': 131.293 , 'Melting (°C)' : -111.75 , 'Boiling (°C)' : -108.12 , 'Protons' : 54 , 'Neutrons' : 77 , 'Binary': "110110"},
    {'Name': 'Cesium', 'Symbol': 'Cs', 'Atomic mass (u)': 132.9054519 , 'Density (when liquid at melting point) (g/cm3)': 1.843 , 'Melting (°C)' : 28.44 , 'Boiling (°C)' : 670.85 , 'Protons' : 55 , 'Neutrons' : 78 , 'Binary': "110111"},
    {'Name': 'Barium', 'Symbol': 'Ba', 'Atomic mass (u)': 137.327 , 'Density (when liquid at melting point) (g/cm3)': 3.338 , 'Melting (°C)' : 727 , 'Boiling (°C)' : 1897 , 'Protons' : 56 , 'Neutrons' : 81 , 'Binary': "111000"},
    {'Name': 'Lanthanum', 'Symbol': 'La', 'Atomic mass (u)': 138.90547 , 'Density (when liquid at melting point) (g/cm3)': 5.94 , 'Melting (°C)' : 920 , 'Boiling (°C)' : 3463.85 , 'Protons' : 57 , 'Neutrons' : 82 , 'Binary': "111001"},
    {'Name': 'Cerium', 'Symbol': 'Ce', 'Atomic mass (u)': 140.116 , 'Density (when liquid at melting point) (g/cm3)': 6.55 , 'Melting (°C)' : 795 , 'Boiling (°C)' : 3443 , 'Protons' : 58 , 'Neutrons' : 82 , 'Binary': "111010"},
    {'Name': 'Praseodymium', 'Symbol': 'Pr', 'Atomic mass (u)': 140.90765 , 'Density (when liquid at melting point) (g/cm3)': 6.50 , 'Melting (°C)' : 931 , 'Boiling (°C)' : 3511.85 , 'Protons' : 59 , 'Neutrons' : 82 , 'Binary': "111011"},
    {'Name': 'Neodymium', 'Symbol': 'Nd', 'Atomic mass (u)': 144.242 , 'Density (when liquid at melting point) (g/cm3)': 6.89 , 'Melting (°C)' : 1016 , 'Boiling (°C)' : 3073.85 , 'Protons' : 60 , 'Neutrons' : 84 , 'Binary': "111100"},
    {'Name': 'Promethium', 'Symbol': 'Pm', 'Atomic mass (u)': 145 , 'Density (when liquid at melting point) (g/cm3)': 7.26 , 'Melting (°C)' : 1042 , 'Boiling (°C)' : 2999.85 , 'Protons' : 61 , 'Neutrons' : 84 , 'Binary': "111101"},
    {'Name': 'Samarium', 'Symbol': 'Sm', 'Atomic mass (u)': 150.36 , 'Density (when liquid at melting point) (g/cm3)': 7.16 , 'Melting (°C)' : 1072 , 'Boiling (°C)' : 1793.85 , 'Protons' : 62 , 'Neutrons' : 88 , 'Binary': "111110"},
    {'Name': 'Europium', 'Symbol': 'Eu', 'Atomic mass (u)': 151.964 , 'Density (when liquid at melting point) (g/cm3)': 5.13 , 'Melting (°C)' : 826 , 'Boiling (°C)' : 1529 , 'Protons' : 63, 'Neutrons' : 89 , 'Binary': "111111"},
    {'Name': 'Gadolinium', 'Symbol': 'Gd', 'Atomic mass (u)': 157.25 , 'Density (when liquid at melting point) (g/cm3)': 7.4 , 'Melting (°C)' : 1313 , 'Boiling (°C)' : 3271.85 , 'Protons' : 64 , 'Neutrons' : 93 , 'Binary': "1000000"},
    {'Name': 'Terbium', 'Symbol': 'Tb', 'Atomic mass (u)': 158.92535 , 'Density (when liquid at melting point) (g/cm3)': 7.65 , 'Melting (°C)' : 1356 , 'Boiling (°C)' : 3226.85 , 'Protons' : 65 , 'Neutrons' : 94 , 'Binary': "1000001"},
    {'Name': 'Dysprosium', 'Symbol': 'Dy', 'Atomic mass (u)': 162.5 , 'Density (when liquid at melting point) (g/cm3)': 8.37 , 'Melting (°C)' : 1412 , 'Boiling (°C)' : 2566.85 , 'Protons' :  66 , 'Neutrons' : 97 , 'Binary': "1000010"},
    {'Name': 'Holmium', 'Symbol': 'Ho', 'Atomic mass (u)': 164.93032 , 'Density (when liquid at melting point) (g/cm3)': 8.34 , 'Melting (°C)' : 1472 , 'Boiling (°C)' : 2694.85 , 'Protons' : 67 , 'Neutrons' : 98 , 'Binary': "1000011"},
    {'Name': 'Erbium', 'Symbol': 'Er', 'Atomic mass (u)': 167.259 , 'Density (when liquid at melting point) (g/cm3)': 8.86 , 'Melting (°C)' : 1529 , 'Boiling (°C)' : 2866.85 , 'Protons' : 68 , 'Neutrons' : 99 , 'Binary': "1000100"},
    {'Name': 'Thulium', 'Symbol': 'Tm', 'Atomic mass (u)': 168.93421 , 'Density (when liquid at melting point) (g/cm3)': 8.56 , 'Melting (°C)' : 1545 , 'Boiling (°C)' : 1730 , 'Protons' : 69 , 'Neutrons' : 100 , 'Binary': "1000101"},
    {'Name': 'Ytterbium', 'Symbol': 'Yb', 'Atomic mass (u)': 173.04 , 'Density (when liquid at melting point) (g/cm3)': 6.21 , 'Melting (°C)' : 824 , 'Boiling (°C)' : 1195.85 , 'Protons' : 70 , 'Neutrons' : 103 , 'Binary': "1000110"},
    {'Name': 'Lutetium', 'Symbol': 'Lu', 'Atomic mass (u)': 174.967 , 'Density (when liquid at melting point) (g/cm3)': 9.3 , 'Melting (°C)' : 1663 , 'Boiling (°C)' : 3394.85 , 'Protons' : 71 , 'Neutrons' : 104 , 'Binary': "1000111"},
    {'Name': 'Hafnium', 'Symbol': 'Hf', 'Atomic mass (u)': 178.49 , 'Density (when liquid at melting point) (g/cm3)': 13.28 , 'Melting (°C)' : 2232.85 , 'Boiling (°C)' : 4601.85 , 'Protons' : 72 , 'Neutrons' : 106 , 'Binary': "1001000"},
    {'Name': 'Tantalum', 'Symbol': 'Ta', 'Atomic mass (u)': 180.94788 , 'Density (when liquid at melting point) (g/cm3)': 15 , 'Melting (°C)' : 3017 , 'Boiling (°C)' : 5456.85 , 'Protons' : 73 , 'Neutrons' : 108 , 'Binary': "1001001"},
    {'Name': 'Tungsten', 'Symbol': 'W', 'Atomic mass (u)': 183.84 , 'Density (when liquid at melting point) (g/cm3)': 17.6 , 'Melting (°C)' : 3422 , 'Boiling (°C)' : 5555 , 'Protons' : 74 , 'Neutrons' : 110 , 'Binary': "1001010"},
    {'Name': 'Rhenium', 'Symbol': 'Ru', 'Atomic mass (u)': 101.07 , 'Density (when liquid at melting point) (g/cm3)': 10.65 , 'Melting (°C)' : 2334 , 'Boiling (°C)' : 4150 , 'Protons' : 75 , 'Neutrons' : 111 , 'Binary': "1001011"},
    {'Name': 'Osmium', 'Symbol': 'Os', 'Atomic mass (u)': 190.23 , 'Density (when liquid at melting point) (g/cm3)': 20 , 'Melting (°C)' : 3033 , 'Boiling (°C)' : 5026.85 , 'Protons' : 76 , 'Neutrons' : 114 , 'Binary': "1001100"},
    {'Name': 'Iridium', 'Symbol': 'Ir', 'Atomic mass (u)': 192.217 , 'Density (when liquid at melting point) (g/cm3)': 19 , 'Melting (°C)' : 2466 , 'Boiling (°C)' : 4130 , 'Protons' : 77 , 'Neutrons' : 115 , 'Binary': "1001101"},
    {'Name': 'Platinum', 'Symbol': 'Pt', 'Atomic mass (u)': 195.084 , 'Density (when liquid at melting point) (g/cm3)': 19.77 , 'Melting (°C)' : 1768.3 , 'Boiling (°C)' : 3825 , 'Protons' : 78 , 'Neutrons' : 117 , 'Binary': "1001110"},
    {'Name': 'Gold', 'Symbol': 'Au', 'Atomic mass (u)': 196.966569 , 'Density (when liquid at melting point) (g/cm3)': 17.31 , 'Melting (°C)' : 1064.18 , 'Boiling (°C)' : 2700 , 'Protons' : 79 , 'Neutrons' : 118 , 'Binary': "1001111"},
    {'Name': 'Gold', 'Symbol': 'Au', 'Atomic mass (u)': 196.966569 , 'Density (when liquid at melting point) (g/cm3)': 17.31 , 'Melting (°C)' : 1064.18 , 'Boiling (°C)' : 2700 , 'Protons' : 79 , 'Neutrons' : 118 , 'Binary': "1010000"},
    {'Name': 'Thallium', 'Symbol': 'Tl', 'Atomic mass (u)': 204.3833 , 'Density (when liquid at melting point) (g/cm3)': 11.22 , 'Melting (°C)' : 304 , 'Boiling (°C)' : 1472.85 , 'Protons' : 81 , 'Neutrons' : 123 , 'Binary': "1010001"},
    {'Name': 'Lead', 'Symbol': 'Pb', 'Atomic mass (u)': 207.2 , 'Density (when liquid at melting point) (g/cm3)': 10.66 , 'Melting (°C)' : 327.5 , 'Boiling (°C)' : 1749 , 'Protons' : 82 , 'Neutrons' : 125 , 'Binary': "1010010"},
    {'Name': 'Bismuth', 'Symbol': 'Bi', 'Atomic mass (u)': 208.98040 , 'Density (when liquid at melting point) (g/cm3)': 10.05 , 'Melting (°C)': 271.406 , 'Boiling (°C)' : 1563.85 , 'Protons' : 83 , 'Neutrons' : 126 , 'Binary': "1010011"},
    {'Name': 'Polonium', 'Symbol': 'Po', 'Atomic mass (u)': 209 , 'Density (when liquid at melting point) (g/cm3)': 9.398 , 'Melting (°C)': 254 , 'Boiling (°C)' : 962 , 'Protons' : 84 , 'Neutrons' : 125 , 'Binary': "1010100"},
    {'Name': 'Astatine', 'Symbol': 'At', 'Atomic mass (u)': 210 , 'Melting (°C)': 302 , 'Boiling (°C)' : 336.85 , 'Protons' : 85 , 'Neutrons' : 125 , 'Binary': "1010101"},
    {'Name': 'Radon', 'Symbol': 'Rn', 'Atomic mass (u)': 222 , 'Density (when liquid at melting point) (g/cm3)': 4.4 , 'Melting (°C)': -71 , 'Boiling (°C)' : -61.7 , 'Protons' : 86 , 'Neutrons' : 136 , 'Binary': "1010110"},
    {'Name': 'Francium', 'Symbol': 'Fr', 'Atomic mass (u)': 223 , 'Melting (°C)': 27  , 'Boiling (°C)' : 676.85 , 'Protons' : 87 , 'Neutrons' : 136 , 'Binary': "1010111"},
    {'Name': 'Radium', 'Symbol': 'Ra', 'Atomic mass (u)': 226 , 'Density (when liquid at melting point) (g/cm3)': 5.5 , 'Melting (°C)': 700 , 'Boiling (°C)' : 1737 , 'Protons' : 88 , 'Neutrons' : 138 , 'Binary': "1011000"},
    {'Name': 'Actinium', 'Symbol': 'Ac', 'Atomic mass (u)': 227 , 'Density (when liquid at melting point) (g/cm3)': 10 , 'Melting (°C)': 1050 , 'Boiling (°C)' : 3196.85 , 'Protons' : 89 , 'Neutrons' : 138 , 'Binary': "1011001"},
    {'Name': 'Thorium', 'Symbol': 'Th', 'Atomic mass (u)': 232.03806 , 'Density (when liquid at melting point) (g/cm3)': 11.7 , 'Melting (°C)': 1750 , 'Boiling (°C)' : 4786.85 , 'Protons' : 90 , 'Neutrons' : 142 , 'Binary': "1011010"},
    {'Name': 'Protactinium', 'Symbol': 'Pa', 'Atomic mass (u)': 231.03588 , 'Density (when liquid at melting point) (g/cm3)': 15.37 , 'Melting (°C)': 1568 , 'Boiling (°C)' : 4026.85 , 'Protons' : 91 , 'Neutrons' : 140 , 'Binary': "1011011"},
    {'Name': 'Uranium', 'Symbol': 'U', 'Atomic mass (u)': 238.02891 , 'Density (when liquid at melting point) (g/cm3)': 17.3 , 'Melting (°C)': 1132.2 , 'Boiling (°C)' : 4131 , 'Protons' : 92 , 'Neutrons' : 146 , 'Binary': "1011100"},
    {'Name': 'Neptunium', 'Symbol': 'Np', 'Atomic mass (u)': 237.0482 , 'Density (when liquid at melting point) (g/cm3)': 19.38 , 'Melting (°C)': 644 , 'Boiling (°C)' : 3901.85 , 'Protons' : 93 , 'Neutrons' : 144 , 'Binary': "1011101"},
    {'Name': 'Plutonium', 'Symbol': 'Pu', 'Atomic mass (u)': 244 , 'Density (when liquid at melting point) (g/cm3)': 16.63 , 'Melting (°C)': 639.4 , 'Boiling (°C)' : 3231.85 , 'Protons' : 94 , 'Neutrons' : 150 , 'Binary': "1011110"},
    {'Name': 'Americium', 'Symbol': 'Am', 'Atomic mass (u)': 243 , 'Melting (°C)': 1176 , 'Boiling (°C)' : 2606.85 , 'Protons' : 95 , 'Neutrons' : 148 , 'Binary': "1011111"},
    {'Name': 'Curium', 'Symbol': 'Cm', 'Atomic mass (u)': 247 , 'Density (when liquid at melting point) (g/cm3)': 13.51 , 'Melting (°C)': 1345 , 'Boiling (°C)' : 3109.85 , 'Protons' : 96 , 'Neutrons' : 151 , 'Binary': "1100000"},
    {'Name': 'Berkelium', 'Symbol': 'Bk', 'Atomic mass (u)': 247 , 'Melting (°C)': 986 , 'Boiling (°C)' : 2627 , 'Protons' : 97 , 'Neutrons' : 150 , 'Binary': "1100001"},
    {'Name': 'Californium', 'Symbol': 'Cf', 'Atomic mass (u)': 251 , 'Melting (°C)': 900 , 'Boiling (°C)' : 1472 , 'Protons' : 98 , 'Neutrons' : 153 , 'Binary': "1100010"},
    {'Name': 'Einsteinium', 'Symbol': 'Es', 'Atomic mass (u)': 252 , 'Density (when liquid at melting point) (g/cm3)': 8.84 , 'Melting (°C)': 860 , 'Protons' : 99 , 'Neutrons' : 153 , 'Binary': "1100011"},
    {'Name': 'Fermium', 'Symbol': 'Fm', 'Atomic mass (u)': 257 ,  'Melting (°C)': 1527 , 'Protons' : 100 , 'Neutrons' : 157 , 'Binary': "1100100"},
    {'Name': 'Mendelevium', 'Symbol': 'Md', 'Atomic mass (u)': 258 , 'Melting (°C)': 827 , 'Protons' : 101 , 'Neutrons' : 157 , 'Binary': "1100101"},
    {'Name': 'Nobelium', 'Symbol': 'No', 'Atomic mass (u)': 259 ,  'Melting (°C)': 827 , 'Protons' : 102 , 'Neutrons' : 157 , 'Binary': "1100110"},
    {'Name': 'Lawrencium', 'Symbol': 'Lr', 'Atomic mass (u)': 262 ,  'Melting (°C)': 1626.85 , 'Protons' : 103 , 'Neutrons' : 159, 'Binary': "1100111"},
    {'Name': 'Rutherfordium', 'Symbol': 'Rf', 'Atomic mass (u)': 261 , 'Protons' : 104 , 'Neutrons' : 157 , 'Binary': "1101000"},
    {'Name': 'Dubnium', 'Symbol': 'Db', 'Atomic mass (u)': 262 , 'Protons' : 105 , 'Neutrons' : 157 , 'Binary': "1101001"},
    {'Name': 'Seaborgium', 'Symbol': 'Sg' ,'Atomic mass (u)': 0 , 'Protons': 106 , 'Neutrons' : 157 , 'Binary': "1101010"},
    {'Name': 'Bohrium', 'Symbol': 'Bh', 'Atomic mass (u)': 264 , 'Protons': 107 , 'Neutrons' : 157 , 'Binary': "1101011"},
    {'Name': 'Hassium', 'Symbol': 'Hs', 'Atomic mass (u)': 277 , 'Protons': 108 , 'Neutrons' : 157 , 'Binary': "1101100"},
    {'Name': 'Meitnerium', 'Symbol': 'Mt', 'Atomic mass (u)': 278 , 'Protons': 109 , 'Neutrons' : 159 , 'Binary': "1101101"},
    {'Name': 'Darmstadtium', 'Symbol': 'Ds', 'Atomic mass (u)': 281 , 'Protons' : 110 , 'Neutrons' : 171 , 'Binary': "1101110"},
    {'Name': 'Roentgenium', 'Symbol': 'Rg', 'Atomic mass (u)': 272 , 'Protons' : 111 , 'Neutrons' : 162 , 'Binary': "1101111"},
    {'Name': 'Copernicium', 'Symbol': 'Cn', 'Atomic mass (u)': 285 , 'Protons' : 112 , 'Neutrons' : 165 , 'Binary': "1110000"},
    {'Name': 'Nihonium', 'Symbol': 'Nh', 'Atomic mass (u)': 286 , 'Protons' : 113 , 'Neutrons' : 170 , 'Binary': "1110001"},
    {'Name': 'Flerovium', 'Symbol': 'Fl', 'Atomic mass (u)': 289 , 'Protons' : 114 , 'Neutrons' : 171 , 'Binary': "1110010"},
    {'Name': 'Moscovium', 'Symbol': 'Mc', 'Atomic mass (u)': 288 , 'Protons' : 115 , 'Neutrons' : 172 , 'Binary': "1110011"},
    {'Name': 'Livermorium', 'Symbol': 'Lv', 'Atomic mass (u)': 292 , 'Protons' : 116 , 'Neutrons' : 173 , 'Binary': "1110100"},
    {'Name': 'Tennessine', 'Symbol': 'Ts' ,'Atomic mass (u)': 0 , 'Protons' : 117 , 'Neutrons' : 0 , 'Binary': "1110101"},
    {'Name': 'Oganesson', 'Symbol': 'Og' , 'Atomic mass (u)': 294 , 'Protons' : 118 , 'Neutrons' : 175 , 'Binary': "1110110"}]

#· Estandar Model 
indexsubelements = {"Up": 0, "Charm": 1, "Top": 2, "Down": 3, "Strange": 4,
    "Bottom": 5, "Antiup": 6, "Anticharm": 7, "Antitop": 8, "Antidown": 9,
    "Antistrange": 10, "Antibottom": 11, "Electron": 12, "Muon": 13, "Tau": 14,
    "Electronneutrino": 15, "Muonneutrino": 16, "Tauneutrino": 17, "Positron": 18,
    "Antimuon": 19, "Antitau": 20, "Electronantineutrino": 21, "Muonantineutrino": 22,
    "Tauantineutrino": 23, "Gluon": 24, "Photon": 25, "BosonZ": 26, "BosonWplus": 27,
    "BosonWless": 28, "Graviton": 29, "Higgs": 30}
     
subelements = [
    #Quarks
    {'Name': 'Up', 'mass MeVC2' : 2.2 , 'charge' : 2/3 , 'spin' : 1/2 , 'Family' : 'Quark', 'Binary': "00000000", 'Color_name' : '\033[92mUp\033[0m', 'Color_binary' : '\033[92m00000000\033[0m'},
    {'Name': 'Charm', 'mass GeVC2' : 1.28 , 'charge' : 2/3 , 'spin' : 1/2 , 'Family' : 'Quark', 'Binary': "00000001", 'Color_name' : '\033[92mCharm\033[0m', 'Color_binary' : '\033[92m00000001\033[0m'},
    {'Name': 'Top', 'mass GeVC2' : 173.1 , 'charge' : 2/3 , 'spin' : 1/2 , 'Family' : 'Quark', 'Binary': "00000010", 'Color_name' : '\033[92mTop\033[0m', 'Color_binary' : '\033[92m00000010\033[0m'},
    {'Name': 'Down', 'mass MeVC2' : 4.7 , 'charge' : -1/3 , 'spin' : 1/2 , 'Family' : 'Quark', 'Binary': "00000011", 'Color_name' : '\033[92mDown\033[0m', 'Color_binary' : '\033[92m00000011\033[0m'},
    {'Name': 'Strange', 'mass MeVC2' : 96 , 'charge' : -1/3 , 'spin' : 1/2 , 'Binary': "00000100", 'Color_name' : '\033[92mStrange\033[0m', 'Color_binary' : '\033[92m00000100\033[0m'},
    {'Name': 'Bottom', 'mass GeVC2' : 4.18 , 'charge' : -1/3 , 'spin' : 1/2 , 'Family' : 'Quark', 'Binary': "00000101", 'Color_name' : '\033[92mBottom\033[0m', 'Color_binary' : '\033[92m00000101\033[0m'},
    # Antiquarks
    {'Name': 'Antiup', 'mass MeVC2' : 2.2 , 'charge' : -2/3 , 'spin' : 1/2 , 'Family' : 'Antiquark', 'Binary': "00000110", 'Color_name' : '\033[94mAntiup\033[0m', 'Color_binary' : '\033[94m00000110\033[0m'},
    {'Name': 'Anticharm', 'mass GeVC2' : 1.28 , 'charge' : -2/3 , 'spin' : 1/2 , 'Family' : 'Antiquark', 'Binary': "00000111", 'Color_name' : '\033[94mAnticharm\033[0m', 'Color_binary' : '\033[94m00000111\033[0m'},
    {'Name': 'Antitop', 'mass GeVC2' : 173.1 , 'charge' : -2/3 , 'spin' : 1/2 , 'Family' : 'Antiquark', 'Binary': "00001000", 'Color_name' : '\033[94mAntitop\033[0m', 'Color_binary' : '\033[94m00001000\033[0m'},
    {'Name': 'Antidown', 'mass MeVC2' : 4.7 , 'charge' : 1/3 , 'spin' : 1/2 , 'Family' : 'Antiquark', 'Binary': "00001001", 'Color_name' : '\033[94mAntidown\033[0m', 'Color_binary' : '\033[94m00001001\033[0m'},
    {'Name': 'Antistrange', 'mass MeVC2' : 96 , 'charge' : 1/3 , 'spin' : 1/2 , 'Family' : 'Antiquark', 'Binary': "00001010", 'Color_name' : '\033[94mAntistrange\033[0m', 'Color_binary' : '\033[94m00001010\033[0m'},
    {'Name': 'Antibottom', 'mass GeVC2' : 4.18 , 'charge' : 1/3 , 'spin' : 1/2 , 'Family' : 'Antiquark', 'Binary': "00001011", 'Color_name' : '\033[94mAntibottom\033[0m', 'Color_binary' : '\033[94m00001011\033[0m'},
    # Leptons
    {'Name': 'Electron', 'mass MeVC2' : 0.511 , 'charge' : -1 , 'spin' : 1/2 , 'Family' : 'Lepton', 'Binary': "00001100", 'Color_name' : '\033[95mElectron\033[0m', 'Color_binary' : '\033[95m00001100\033[0m'},
    {'Name': 'Muon', 'mass MeVC2' : 105.66 , 'charge' : -1 , 'spin' : 1/2 , 'Family' : 'Lepton', 'Binary': "00001101", 'Color_name' : '\033[95mMuon\033[0m', 'Color_binary' : '\033[95m00001101\033[0m'},
    {'Name': 'Tau', 'mass GeVC2' : 1.7768 , 'charge' : -1 , 'spin' : 1/2 , 'Family' : 'Lepton', 'Binary': "00001110", 'Color_name' : '\033[95mTau\033[0m', 'Color_binary' : '\033[95m00001110\033[0m'},
    {'Name': 'Electronneutrino', 'mass MeVC2' : 2.2 , 'charge' : 0 , 'spin' : 1/2 , 'Family' : 'Lepton', 'Binary': "00001111", 'Color_name' : '\033[95mElectronneutrino\033[0m', 'Color_binary' : '\033[95m00001111\033[0m'},
    {'Name': 'Muonneutrino', 'mass MeVC2' : 1.7 , 'charge' : 0 , 'spin' : 1/2 , 'Family' : 'Lepton', 'Binary': "00010000", 'Color_name' : '\033[95mMuonneutrino\033[0m', 'Color_binary' : '\033[95m00010000\033[0m'},
    {'Name': 'Tauneutrino', 'mass MeVC2' : 15.5 , 'charge' : 0 , 'spin' : 1/2 , 'Family' : 'Lepton', 'Binary': "00010001", 'Color_name' : '\033[95mTauneutrino\033[0m', 'Color_binary' : '\033[95m00010001\033[0m'},
    # Antileptons
    {'Name': 'Positron', 'mass MeVC2' : 0.511 , 'charge' : 1 , 'spin' : 1/2 , 'Family' : 'Antilepton', 'Binary': "00010010", 'Color_name' : '\033[96mPositron\033[0m', 'Color_binary' : '\033[96m00010010\033[0m'},
    {'Name': 'Antimuon', 'mass MeVC2' : 105.66 , 'charge' : 1 , 'spin' : 1/2 , 'Family' : 'Antilepton', 'Binary': "00010011", 'Color_name' : '\033[96mAntimuon\033[0m', 'Color_binary' : '\033[96m00010011\033[0m'},
    {'Name': 'Antitau', 'mass GeVC2' : 1.7768 , 'charge' : 1 , 'spin' : 1/2 , 'Family' : 'Antilepton', 'Binary': "00010100", 'Color_name' : '\033[96mAntitau\033[0m', 'Color_binary' : '\033[96m00010100\033[0m'},
    {'Name': 'Electronantineutrino', 'mass MeVC2' : 2.2 , 'charge' : 0 , 'spin' : 1/2 , 'Family' : 'Antilepton', 'Binary': "00010101", 'Color_name' : '\033[96mElectronantineutrino\033[0m', 'Color_binary' : '\033[96m00010101\033[0m'},
    {'Name': 'Muonantineutrino', 'mass MeVC2' : 1.7 , 'charge' : 0 , 'spin' : 1/2 , 'Family' : 'Antilepton', 'Binary': "00010110", 'Color_name' : '\033[96mMuonantineutrino\033[0m', 'Color_binary' : '\033[96m00010110\033[0m'},
    {'Name': 'Tauantineutrino', 'mass MeVC2' : 15.5 , 'charge' : 0 , 'spin' : 1/2 , 'Family' : 'Antilepton', 'Binary': "00010111", 'Color_name' : '\033[96mTauantineutrino\033[0m', 'Color_binary' : '\033[96m00010111\033[0m'},
    # Gauge Bosons
    {'Name': 'Gluon', 'mass MeVC2' : 0 , 'charge' : 0 , 'spin' : 1 , 'Family' : 'Gauge Boson', 'Binary': "00011000", 'Color_name' : '\033[101mGluon\033[0m', 'Color_binary' : '\033[101m00011000\033[0m'},
    {'Name': 'Photon', 'mass MeVC2' : 0 , 'charge' : 0 , 'spin' : 1 , 'Family' : 'Gauge Boson', 'Binary': "00011001", 'Color_name' : '\033[101mPhoton\033[0m', 'Color_binary' : '\033[101m00011001\033[0m'},
    {'Name': 'BosonZ', 'mass GeVC2' : 91.19 , 'charge' : 0 , 'spin' : 1 , 'Family' : 'Gauge Boson', 'Binary': "00011010", 'Color_name' : '\033[101mBosonZ\033[0m', 'Color_binary' : '\033[101m00011010\033[0m'},
    {'Name': 'BosonWplus', 'mass GeVC2' : 80.39 , 'charge' : 1 , 'spin' : 1 , 'Family' : 'Gauge Boson', 'Binary': "00011011", 'Color_name' : '\033[101mBosonWplus\033[0m', 'Color_binary' : '\033[101m00011011\033[0m'},
    {'Name': 'BosonWless', 'mass MeVC2' : 80.39 , 'charge' : -1 , 'spin' : 1 , 'Family' : 'Gauge Boson', 'Binary': "00011100", 'Color_name' : '\033[101mBosonWless\033[0m', 'Color_binary' : '\033[101m00011100\033[0m'},
    {'Name': 'Graviton', 'mass GeVC2' : 0 , 'charge' : 0 , 'spin' : 0 , 'Family' : 'Gauge Boson', 'Binary': "00011101", 'Color_name' : '\033[101mGraviton\033[0m', 'Color_binary' : '\033[101m00011101\033[0m'},
    # Scalar Bosons
    {'Name': 'Higgs', 'mass GeVC2' : 125.09 , 'charge' : 0 , 'spin' : 0 , 'Family' : 'Scalar Boson', 'Binary': "00011110", 'Color_name' : '\033[102mHiggs\033[0m', 'Color_binary' : '\033[102m00011110\033[0m'},]

while True:
    print("""
                    Atomic World
                [0]
                    1] Periodic Table
                    2] Standard Model
    """)

    option1 = input("Please select a option: ")

    if option1 == "1":
        print("""
                                        Periodic Table

            01. Hydrogen        02. Helium          03. Lithium         04. Beryllium
            05. Boron           06. Carbon          07. Nitrogen        08. Oxygen
            09. Fluorine        10. Neon            11. Sodium          12. Magnesium
            13. Aluminium       14. Silicon         15. Phosphorus      16. Sulfur
            17. Chlorine        18. Argon           19. Potassium       20. Calcium
            21. Scandium        22. Titanium        23. Vanadium        24. Chromium
            25. Manganese       26. Iron            27. Cobalt          28. Nickel
            29. Copper          30. Zinc            31. Gallium         32. Germanium
            33. Arsenic         34. Selenium        35. Bromine         36. Krypton
            37. Rubidium        38. Strontium       39. Yttrium         40. Zirconium
            41. Niobium         42. Molybdenum      43. Technetium      44. Ruthenium
            45. Rhodium         46. Palladium       47. Silver          48. Cadmium
            49. Indium          50. Tin             51. Antimony        52. Tellurium
            53. Iodine          54. Xenon           55. Caesium         56. Barium
            57. Lanthanum       58. Cerium          59. Praseodymium    60. Neodymium
            61. Promethium      62. Samarium        63. Europium        64. Gadolinium
            65. Terbium         66. Dysprosium      67. Holmium         68. Erbium
            69. Thulium         70. Ytterbium       71. Lutetium        72. Hafnium
            73. Tantalum        74. Tungsten        75. Rhenium         76. Osmium
            77. Iridium         78. Platinum        79. Gold            80. Mercury
            81. Thallium        82. Lead            83. Bismuth         84. Polonium
            85. Astatine        86. Radon           87. Francium        88. Radium
            89. Actinium        90. Thorium         91. Protactinium    92. Uranium
            93. Neptunium       94. Plutonium       95. Americium       96. Curium
            97. Berkelium       98. Californium     99. Einsteinium     100. Fermium
            101. Mendelevium    102. Nobelium       103. Lawrencium     104. Rutherfordium
            105. Dubnium        106. Seaborgium     107. Bohrium        108. Hassium
            109. Meitnerium     110. Darmstadtium   111. Roentgenium    112. Copernicium
            113. Nihonium       114. Flerovium      115. Moscovium      116. Livermorium
            117. Tennessine     118. Oganesson

            [0]
                1] Calculate the atoms of a molecule 
        """)
        option2 = input("Please select a option: ")
        if option2 == "1":
            lenght = int(input('How many elements is the molecule made of?: '))

            if lenght == 0:
                print("I can't make a molecule.")
            elif lenght == 1:
                element = str(input('What is the name of the element?: '))
                a = indexelements[element]
                subscript = int(input('What is the subscript of the element?: '))        
                print(elements[a]['Symbol'], subscript)

                atomicweight = elements[a]['Atomic mass (u)'] * subscript
                print(atomicweight, "the atomic weight of", elements[a]['Symbol'], subscript)
                weight = float(input("What is physical weight in grams?: "))

                print("\nMoles:\n")
                mol = 1
                moles = weight * mol / atomicweight
                print(moles, "moles are in the molecule", elements[a]['Symbol'], subscript)

                print("\nMolecules:\n")
                avogadro = 6.022 * 10 ** 23 
                molecules = moles * avogadro / mol
                print(molecules, "molecules are in the molecule", elements[a]['Symbol'], subscript)

                print("\nAtoms:\n")
                molecule = 1
                atomsa = molecules * subscript / molecule
                print(atomsa, "atoms are in the element", elements[a]['Name'], "of the molecule", elements[a]['Symbol'], subscript)
                
                print("\nProtons and neutrons:\n")
                atom = 1
                protonsa = atomsa * elements[a]['Protons'] / atom
                neutronsa = atomsa * elements[a]['Neutrons'] / atom
                print(protonsa, "protons are in the element", elements[a]['Name'], "of the molecule", elements[a]['Symbol'], subscript)
                print(neutronsa, "neutrons are in the element", elements[a]['Name'], "of the molecule", elements[a]['Symbol'], subscript)

                print("\n\033[92mSub\033[0m\033[94ma\033[0m\033[95mto\033[0m\033[96mmic\033[0m \033[104mWo\033[0m\033[101mrld\033[0m\n")
                print("\nQuarks \033[92mUp\033[0m and \033[92mDown\033[0m are in protons and neutrons of each element:\n")
                proton = 1
                quarksupareinprotons = 2
                quarksdownareinprotons = 1
                neutron = 1
                quarksupareinneutrons = 1
                quarksdownareinneutrons = 2

                quarksupprotonsa = quarksupareinprotons * protonsa / proton
                quarksdownprotonsa = quarksdownareinprotons * protonsa / proton
                quarksupneutronsa = quarksupareinneutrons * protonsa / proton
                quarksdownneutronsa = quarksdownareinneutrons * protonsa / proton
                print(quarksupprotonsa, "quarks \033[92mUp\033[0m are in protons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript)
                print(quarksdownprotonsa, "quarks \033[92mDown\033[0m are in protons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript)
                
                print(quarksupneutronsa, "quarks \033[92mUp\033[0m are in neutrons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript)
                print(quarksdownneutronsa, "quarks \033[92mDown\033[0m are in neutrons of in the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript)

                print("\nMass MeVC2 of the \033[92mUp\033[0m and \033[92mDown\033[0m quarks are in the protons and neutrons of each element:\n")
                u = indexsubelements['Up']
                d = indexsubelements['Down']
                massquarksupprotonsa = subelements[u]['mass MeVC2'] * quarksupprotonsa
                massquarksdownprotonsa = subelements[d]['mass MeVC2'] * quarksdownprotonsa
                massquarksupneutronsa = subelements[u]['mass MeVC2'] * quarksupneutronsa
                massquarksdownneutronsa = subelements[d]['mass MeVC2'] * quarksdownneutronsa

                print(massquarksupprotonsa, "mass quarks \033[92mUp\033[0m are in protons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript)
                print(massquarksdownprotonsa, "mass quarks \033[92mDown\033[0m are are in protons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript)
                
                print(massquarksupneutronsa, "mass quarks \033[92mUp\033[0m are in neutrons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript)
                print(massquarksdownneutronsa, "mass quarks \033[92mDown\033[0m are are in neutrons of in the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript)
            elif lenght == 2:
                element = str(input('What is the name of the first element?: '))
                a = indexelements[element]
                subscript = int(input('What is the subscript of the first element?: '))
                element2 = str(input('What is the name of the second element?: '))
                b = indexelements[element2]
                subscript2 = int(input('What is the subscript of the second element?: '))
                print(elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)

                if element == element2:
                    print("Is not posible.")
                elif element != element2:
                    atomicweight = elements[a]['Atomic mass (u)'] * subscript + elements[b]['Atomic mass (u)'] * subscript2
                    print(atomicweight, "the atomic weight of", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)
                    weight = float(input("What is physical weight in grams?: "))

                    print("\nMoles:\n")
                    mol = 1
                    moles = weight * mol / atomicweight
                    print(moles, "moles are in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)

                    print("\nMolecules:\n")
                    avogadro = 6.022 * 10 ** 23 
                    molecules = moles * avogadro / mol
                    print(molecules, "molecules are in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)
                    
                    print("\nAtoms:\n")
                    molecule = 1
                    atomsa = molecules * subscript / molecule
                    atomsb = molecules * subscript2 / molecule
                    print(atomsa, "atoms are in the element", elements[a]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)
                    print(atomsb, "atoms are in the element", elements[b]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)
                    
                    print("\nProtons and neutrons:\n")
                    atom = 1
                    protonsa = atomsa * elements[a]['Protons'] / atom
                    neutronsa = atomsa * elements[a]['Neutrons'] / atom
                    protonsb = atomsb * elements[b]['Protons'] / atom
                    neutronsb = atomsb * elements[b]['Neutrons'] / atom

                    print(atomsa, "protons are in the element", elements[a]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)
                    print(neutronsa, "neutrons are in the element", elements[a]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)
                    print(atomsb, "protons are in the element", elements[b]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)
                    print(neutronsb, "neutrons are in the element", elements[b]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)

                    print("\n\033[92mSub\033[0m\033[94ma\033[0m\033[95mto\033[0m\033[96mmic\033[0m \033[104mWo\033[0m\033[101mrld\033[0m\n")
                    print("\nQuarks \033[92mUp\033[0m and \033[92mDown\033[0m are in protons and neutrons of each element:\n")
                    proton = 1
                    quarksupareinprotons = 2
                    quarksdownareinprotons = 1
                    neutron = 1
                    quarksupareinneutrons = 1
                    quarksdownareinneutrons = 2

                    quarksupprotonsa = quarksupareinprotons * protonsa / proton
                    quarksdownprotonsa = quarksdownareinprotons * protonsa / proton
                    quarksupneutronsa = quarksupareinneutrons * protonsa / proton
                    quarksdownneutronsa = quarksdownareinneutrons * protonsa / proton
                    quarksupprotonsb = quarksupareinprotons * protonsb / proton
                    quarksdownprotonsb = quarksdownareinprotons * protonsb / proton
                    quarksupneutronsb = quarksupareinneutrons * protonsb / proton
                    quarksdownneutronsb = quarksdownareinneutrons * protonsb / proton

                    print(quarksupprotonsa, "quarks \033[92mUp\033[0m are in protons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)
                    print(quarksdownprotonsa, "quarks \033[92mDown\033[0m are in protons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)
                    
                    print(quarksupneutronsa, "quarks \033[92mUp\033[0m are in neutrons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)
                    print(quarksdownneutronsa, "quarks \033[92mDown\033[0m are in neutrons of in the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)

                    print(quarksupprotonsb, "quarks \033[92mUp\033[0m are in protons of the element", elements[b]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)
                    print(quarksdownprotonsb, "quarks \033[92mDown\033[0m are in protons of the element", elements[b]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)
                    
                    print(quarksupneutronsb, "quarks \033[92mUp\033[0m are in neutrons of the element", elements[b]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)
                    print(quarksdownneutronsb, "quarks \033[92mDown\033[0m are in neutrons of in the element", elements[b]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)

                    print("\nMass MeVC2 of the \033[92mUp\033[0m and \033[92mDown\033[0m quarks are in the protons and neutrons of each element:\n")
                    u = indexsubelements['Up']
                    d = indexsubelements['Down']
                    massquarksupprotonsa = subelements[u]['mass MeVC2'] * quarksupprotonsa
                    massquarksdownprotonsa = subelements[d]['mass MeVC2'] * quarksdownprotonsa
                    massquarksupneutronsa = subelements[u]['mass MeVC2'] * quarksupneutronsa
                    massquarksdownneutronsa = subelements[d]['mass MeVC2'] * quarksdownneutronsa

                    massquarksupprotonsb = subelements[u]['mass MeVC2'] * quarksupprotonsb
                    massquarksdownprotonsb = subelements[d]['mass MeVC2'] * quarksdownprotonsb
                    massquarksupneutronsb = subelements[u]['mass MeVC2'] * quarksupneutronsb
                    massquarksdownneutronsb = subelements[d]['mass MeVC2'] * quarksdownneutronsb

                    print(massquarksupprotonsa, "mass quarks \033[92mUp\033[0m are in protons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)
                    print(massquarksdownprotonsa, "mass quarks \033[92mDown\033[0m are are in protons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)
                    
                    print(massquarksupneutronsa, "mass quarks \033[92mUp\033[0m are in neutrons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)
                    print(massquarksdownneutronsa, "mass quarks \033[92mDown\033[0m are are in neutrons of in the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)

                    print(massquarksupprotonsb, "mass quarks \033[92mUp\033[0m are in protons of the element", elements[b]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)
                    print(massquarksdownprotonsb, "mass quarks \033[92mDown\033[0m are are in protons of the element", elements[b]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)
                    
                    print(massquarksupneutronsb, "mass quarks \033[92mUp\033[0m are in neutrons of the element", elements[b]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)
                    print(massquarksdownneutronsb, "mass quarks \033[92mDown\033[0m are are in neutrons of in the element", elements[b]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2)
            elif lenght == 3:
                element = str(input('What is the name of the first element?: '))
                a = indexelements[element]
                subscript = int(input('What is the subscript of the first element?: '))
                element2 = str(input('What is the name of the second element?: '))
                b = indexelements[element2]
                subscript2 = int(input('What is the subscript of the second element?: '))
                element3 = str(input('What is the name of the third element?: '))
                c = indexelements[element3]
                subscript3 = int(input('What is the subscript of the third element?: '))
                print(elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)

                if element == element2 or element2 == element3 or element == element3:
                    print("Is not posible.")
                elif element != element2 or element2 != element3 or element != element3:
                    atomicweight = elements[a]['Atomic mass (u)'] * subscript + elements[b]['Atomic mass (u)'] * subscript2 + elements[c]['Atomic mass (u)'] * subscript3
                    print(atomicweight, "the atomic weight of", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    weight = float(input("What is physical weight in grams?: "))

                    print("\nMoles:\n")
                    mol = 1
                    moles = weight * mol / atomicweight
                    print(moles, "moles are in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)

                    print("\nMolecules:\n")
                    avogadro = 6.022 * 10 ** 23 
                    molecules = moles * avogadro / mol
                    print(molecules, "molecules are in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)

                    print("\nAtoms:\n")
                    molecule = 1
                    atomsa = molecules * subscript / molecule
                    atomsb = molecules * subscript2 / molecule
                    atomsc = molecules * subscript2 / molecule
                    print(atomsa, "atoms are in the element", elements[a]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    print(atomsb, "atoms are in the element", elements[b]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    print(atomsc, "atoms are in the element", elements[c]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)

                    print("\nProtons and neutrons:\n")
                    atom = 1
                    protonsa = atomsa * elements[a]['Protons'] / atom
                    neutronsa = atomsa * elements[a]['Neutrons'] / atom
                    protonsb = atomsb * elements[b]['Protons'] / atom
                    neutronsb = atomsb * elements[b]['Neutrons'] / atom
                    protonsc = atomsc * elements[c]['Protons'] / atom
                    neutronsc = atomsc * elements[c]['Neutrons'] / atom

                    print(atomsa, "protons are in the element", elements[a]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    print(neutronsa, "neutrons are in the element", elements[a]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    print(atomsb, "protons are in the element", elements[b]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    print(neutronsb, "neutrons are in the element", elements[b]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    print(atomsc, "protons are in the element", elements[c]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    print(neutronsc, "neutrons are in the element", elements[c]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)

                    print("\n\033[92mSub\033[0m\033[94ma\033[0m\033[95mto\033[0m\033[96mmic\033[0m \033[104mWo\033[0m\033[101mrld\033[0m\n")
                    print("\nQuarks \033[92mUp\033[0m and \033[92mDown\033[0m are in protons and neutrons of each element:\n")
                    proton = 1
                    quarksupareinprotons = 2
                    quarksdownareinprotons = 1
                    neutron = 1
                    quarksupareinneutrons = 1
                    quarksdownareinneutrons = 2

                    quarksupprotonsa = quarksupareinprotons * protonsa / proton
                    quarksdownprotonsa = quarksdownareinprotons * protonsa / proton
                    quarksupneutronsa = quarksupareinneutrons * protonsa / proton
                    quarksdownneutronsa = quarksdownareinneutrons * protonsa / proton
                    quarksupprotonsb = quarksupareinprotons * protonsb / proton
                    quarksdownprotonsb = quarksdownareinprotons * protonsb / proton
                    quarksupneutronsb = quarksupareinneutrons * protonsb / proton
                    quarksdownneutronsb = quarksdownareinneutrons * protonsb / proton
                    quarksupprotonsc = quarksupareinprotons * protonsc / proton
                    quarksdownprotonsc = quarksdownareinprotons * protonsc / proton
                    quarksupneutronsc = quarksupareinneutrons * protonsc / proton
                    quarksdownneutronsc = quarksdownareinneutrons * protonsc / proton

                    print(quarksupprotonsa, "quarks \033[92mUp\033[0m are in protons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    print(quarksdownprotonsa, "quarks \033[92mDown\033[0m are in protons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    
                    print(quarksupneutronsa, "quarks \033[92mUp\033[0m are in neutrons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3 )
                    print(quarksdownneutronsa, "quarks \033[92mDown\033[0m are in neutrons of in the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)

                    print(quarksupprotonsb, "quarks \033[92mUp\033[0m are in protons of the element", elements[b]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    print(quarksdownprotonsb, "quarks \033[92mDown\033[0m are in protons of the element", elements[b]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    
                    print(quarksupneutronsb, "quarks \033[92mUp\033[0m are in neutrons of the element", elements[b]['Name'], "in the molecule",  elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    print(quarksdownneutronsb, "quarks \033[92mDown\033[0m are in neutrons of in the element", elements[b]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)

                    print(quarksupprotonsc, "quarks \033[92mUp\033[0m are in protons of the element", elements[c]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    print(quarksdownprotonsc, "quarks \033[92mDown\033[0m are in protons of the element", elements[c]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    
                    print(quarksupneutronsc, "quarks \033[92mUp\033[0m are in neutrons of the element", elements[c]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    print(quarksdownneutronsc, "quarks \033[92mDown\033[0m are in neutrons of in the element", elements[c]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)

                    print("\nMass MeVC2 of the \033[92mUp\033[0m and \033[92mDown\033[0m quarks are in the protons and neutrons of each element:\n")
                    u = indexsubelements['Up']
                    d = indexsubelements['Down']
                    massquarksupprotonsa = subelements[u]['mass MeVC2'] * quarksupprotonsa
                    massquarksdownprotonsa = subelements[d]['mass MeVC2'] * quarksdownprotonsa
                    massquarksupneutronsa = subelements[u]['mass MeVC2'] * quarksupneutronsa
                    massquarksdownneutronsa = subelements[d]['mass MeVC2'] * quarksdownneutronsa

                    massquarksupprotonsb = subelements[u]['mass MeVC2'] * quarksupprotonsb
                    massquarksdownprotonsb = subelements[d]['mass MeVC2'] * quarksdownprotonsb
                    massquarksupneutronsb = subelements[u]['mass MeVC2'] * quarksupneutronsb
                    massquarksdownneutronsb = subelements[d]['mass MeVC2'] * quarksdownneutronsb

                    massquarksupprotonsc = subelements[u]['mass MeVC2'] * quarksupprotonsc
                    massquarksdownprotonsc = subelements[d]['mass MeVC2'] * quarksdownprotonsc
                    massquarksupneutronsc = subelements[u]['mass MeVC2'] * quarksupneutronsc
                    massquarksdownneutronsc = subelements[d]['mass MeVC2'] * quarksdownneutronsc

                    print(massquarksupprotonsa, "mass quarks \033[92mUp\033[0m are in protons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    print(massquarksdownprotonsa, "mass quarks \033[92mDown\033[0m are are in protons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    
                    print(massquarksupneutronsa, "mass quarks \033[92mUp\033[0m are in neutrons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    print(massquarksdownneutronsa, "mass quarks \033[92mDown\033[0m are are in neutrons of in the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)

                    print(massquarksupprotonsb, "mass quarks \033[92mUp\033[0m are in protons of the element", elements[b]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    print(massquarksdownprotonsb, "mass quarks \033[92mDown\033[0m are are in protons of the element", elements[b]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    
                    print(massquarksupneutronsb, "mass quarks \033[92mUp\033[0m are in neutrons of the element", elements[b]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    print(massquarksdownneutronsb, "mass quarks \033[92mDown\033[0m are are in neutrons of in the element", elements[b]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)

                    print(massquarksupprotonsc, "mass quarks \033[92mUp\033[0m are in protons of the element", elements[c]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    print(massquarksdownprotonsc, "mass quarks \033[92mDown\033[0m are are in protons of the element", elements[c]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    
                    print(massquarksupneutronsc, "mass quarks \033[92mUp\033[0m are in neutrons of the element", elements[c]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    print(massquarksdownneutronsc, "mass quarks \033[92mDown\033[0m are are in neutrons of in the element", elements[c]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
            elif lenght == 4:
                element = str(input('What is the name of the first element?: '))
                a = indexelements[element]
                subscript = int(input('What is the subscript of the first element?: '))
                element2 = str(input('What is the name of the second element?: '))
                b = indexelements[element2]
                subscript2 = int(input('What is the subscript of the second element?: '))
                element3 = str(input('What is the name of the third element?: '))
                c = indexelements[element3]
                subscript3 = int(input('What is the subscript of the third element?: '))
                element4 = str(input('What is the name of the fourth element?: '))
                z = indexelements[element4]
                subscript4 = int(input('What is the subscript of the fourth element?: '))
                print(elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)

                if element == element2 or element == element3 or element == element4 or element2 == element3 or element2 == element4 or element3 == element4:
                    print("Is not posible.")
                elif element != element2 or element != element3 or element != element4 or element2 != element3 or element2 != element4 or element3 != element4:
                    atomicweight = elements[a]['Atomic mass (u)'] * subscript + elements[b]['Atomic mass (u)'] * subscript2 + elements[c]['Atomic mass (u)'] * subscript3 + elements[z]['Atomic mass (u)'] * subscript4
                    print(atomicweight, "the atomic weight of", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    weight = float(input("What is physical weight in grams?: "))

                    print("\nMoles:\n")
                    mol = 1
                    moles = weight * mol / atomicweight
                    print(moles, "moles are in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)

                    print("\nMolecules:\n ")
                    avogadro = 6.022 * 10 ** 23 
                    molecules = moles * avogadro / mol
                    print(molecules, "molecules are in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)

                    print("\nAtoms:\n")
                    molecule = 1
                    atomsa = molecules * subscript / molecule
                    atomsb = molecules * subscript2 / molecule
                    atomsc = molecules * subscript3 / molecule
                    atomsd = molecules * subscript4 / molecule
                    print(atomsa, "atoms are in the element", elements[a]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(atomsb, "atoms are in the element", elements[b]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(atomsc, "atoms are in the element", elements[c]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(atomsd, "atoms are in the element", elements[z]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)


                    print("\nProtons and neutrons:\n")
                    atom = 1
                    protonsa = atomsa * elements[a]['Protons'] / atom
                    neutronsa = atomsa * elements[a]['Neutrons'] / atom
                    protonsb = atomsb * elements[b]['Protons'] / atom
                    neutronsb = atomsb * elements[b]['Neutrons'] / atom
                    protonsc = atomsc * elements[c]['Protons'] / atom
                    neutronsc = atomsc * elements[c]['Neutrons'] / atom
                    protonsd = atomsd * elements[z]['Protons'] / atom
                    neutronsd = atomsd * elements[z]['Neutrons'] / atom

                    print(atomsa, "protons are in the element", elements[a]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(neutronsa, "neutrons are in the element", elements[a]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(atomsb, "protons are in the element", elements[b]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(neutronsb, "neutrons are in the element", elements[b]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(atomsc, "protons are in the element", elements[c]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(neutronsc, "neutrons are in the element", elements[c]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(atomsd, "protons are in the element", elements[z]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(neutronsd, "neutrons are in the element", elements[z]['Name'], "of the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)


                    print("\n\033[92mSub\033[0m\033[94ma\033[0m\033[95mto\033[0m\033[96mmic\033[0m \033[104mWo\033[0m\033[101mrld\033[0m\n")
                    print("\nQuarks \033[92mUp\033[0m and \033[92mDown\033[0m are in protons and neutrons of each element:\n")
                    proton = 1
                    quarksupareinprotons = 2
                    quarksdownareinprotons = 1
                    neutron = 1
                    quarksupareinneutrons = 1
                    quarksdownareinneutrons = 2

                    quarksupprotonsa = quarksupareinprotons * protonsa / proton
                    quarksdownprotonsa = quarksdownareinprotons * protonsa / proton
                    quarksupneutronsa = quarksupareinneutrons * protonsa / proton
                    quarksdownneutronsa = quarksdownareinneutrons * protonsa / proton
                    quarksupprotonsb = quarksupareinprotons * protonsb / proton
                    quarksdownprotonsb = quarksdownareinprotons * protonsb / proton
                    quarksupneutronsb = quarksupareinneutrons * protonsb / proton
                    quarksdownneutronsb = quarksdownareinneutrons * protonsb / proton
                    quarksupprotonsc = quarksupareinprotons * protonsc / proton
                    quarksdownprotonsc = quarksdownareinprotons * protonsc / proton
                    quarksupneutronsc = quarksupareinneutrons * protonsc / proton
                    quarksdownneutronsc = quarksdownareinneutrons * protonsc / proton
                    quarksupprotonsd = quarksupareinprotons * protonsd / proton
                    quarksdownprotonsd = quarksdownareinprotons * protonsd / proton
                    quarksupneutronsd = quarksupareinneutrons * protonsd / proton
                    quarksdownneutronsd = quarksdownareinneutrons * protonsd / proton

                    print(quarksupprotonsa, "quarks \033[92mUp\033[0m are in protons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(quarksdownprotonsa, "quarks \033[92mDown\033[0m are in protons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    
                    print(quarksupneutronsa, "quarks \033[92mUp\033[0m are in neutrons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(quarksdownneutronsa, "quarks \033[92mDown\033[0m are in neutrons of in the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)

                    print(quarksupprotonsb, "quarks \033[92mUp\033[0m are in protons of the element", elements[b]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(quarksdownprotonsb, "quarks \033[92mDown\033[0m are in protons of the element", elements[b]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    
                    print(quarksupneutronsb, "quarks \033[92mUp\033[0m are in neutrons of the element", elements[b]['Name'], "in the molecule",  elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3)
                    print(quarksdownneutronsb, "quarks \033[92mDown\033[0m are in neutrons of in the element", elements[b]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)

                    print(quarksupprotonsc, "quarks \033[92mUp\033[0m are in protons of the element", elements[c]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(quarksdownprotonsc, "quarks \033[92mDown\033[0m are in protons of the element", elements[c]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    
                    print(quarksupneutronsc, "quarks \033[92mUp\033[0m are in neutrons of the element", elements[c]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(quarksdownneutronsc, "quarks \033[92mDown\033[0m are in neutrons of in the element", elements[c]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    
                    print(quarksupprotonsd, "quarks \033[92mUp\033[0m are in protons of the element", elements[z]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(quarksdownprotonsc, "quarks \033[92mDown\033[0m are in protons of the element", elements[z]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    
                    print(quarksupneutronsd, "quarks \033[92mUp\033[0m are in neutrons of the element", elements[z]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(quarksdownneutronsd, "quarks \033[92mDown\033[0m are in neutrons of in the element", elements[z]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)  

                    print("\nMass MeVC2 of the \033[92mUp\033[0m and \033[92mDown\033[0m quarks are in the protons and neutrons of each element:\n")
                    u = indexsubelements['Up']
                    d = indexsubelements['Down']
                    massquarksupprotonsa = subelements[u]['mass MeVC2'] * quarksupprotonsa
                    massquarksdownprotonsa = subelements[d]['mass MeVC2'] * quarksdownprotonsa
                    massquarksupneutronsa = subelements[u]['mass MeVC2'] * quarksupneutronsa
                    massquarksdownneutronsa = subelements[d]['mass MeVC2'] * quarksdownneutronsa

                    massquarksupprotonsb = subelements[u]['mass MeVC2'] * quarksupprotonsb
                    massquarksdownprotonsb = subelements[d]['mass MeVC2'] * quarksdownprotonsb
                    massquarksupneutronsb = subelements[u]['mass MeVC2'] * quarksupneutronsb
                    massquarksdownneutronsb = subelements[d]['mass MeVC2'] * quarksdownneutronsb

                    massquarksupprotonsc = subelements[u]['mass MeVC2'] * quarksupprotonsc
                    massquarksdownprotonsc = subelements[d]['mass MeVC2'] * quarksdownprotonsc
                    massquarksupneutronsc = subelements[u]['mass MeVC2'] * quarksupneutronsc
                    massquarksdownneutronsc = subelements[d]['mass MeVC2'] * quarksdownneutronsc

                    massquarksupprotonsd = subelements[u]['mass MeVC2'] * quarksupprotonsd
                    massquarksdownprotonsd = subelements[d]['mass MeVC2'] * quarksdownprotonsd
                    massquarksupneutronsd = subelements[u]['mass MeVC2'] * quarksupneutronsd
                    massquarksdownneutronsd = subelements[d]['mass MeVC2'] * quarksdownneutronsd

                    print(massquarksupprotonsa, "mass quarks \033[92mUp\033[0m are in protons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(massquarksdownprotonsa, "mass quarks \033[92mDown\033[0m are are in protons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    
                    print(massquarksupneutronsa, "mass quarks \033[92mUp\033[0m are in neutrons of the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(massquarksdownneutronsa, "mass quarks \033[92mDown\033[0m are are in neutrons of in the element", elements[a]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)

                    print(massquarksupprotonsb, "mass quarks \033[92mUp\033[0m are in protons of the element", elements[b]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(massquarksdownprotonsb, "mass quarks \033[92mDown\033[0m are are in protons of the element", elements[b]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    
                    print(massquarksupneutronsb, "mass quarks \033[92mUp\033[0m are in neutrons of the element", elements[b]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(massquarksdownneutronsb, "mass quarks \033[92mDown\033[0m are are in neutrons of in the element", elements[b]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)

                    print(massquarksupprotonsc, "mass quarks \033[92mUp\033[0m are in protons of the element", elements[c]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(massquarksdownprotonsc, "mass quarks \033[92mDown\033[0m are are in protons of the element", elements[c]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    
                    print(massquarksupneutronsc, "mass quarks \033[92mUp\033[0m are in neutrons of the element", elements[c]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(massquarksdownneutronsc, "mass quarks \033[92mDown\033[0m are are in neutrons of in the element", elements[c]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)

                    print(massquarksupprotonsd, "mass quarks \033[92mUp\033[0m are in protons of the element", elements[z]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(massquarksdownprotonsd, "mass quarks \033[92mDown\033[0m are are in protons of the element", elements[z]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    
                    print(massquarksupneutronsd, "mass quarks \033[92mUp\033[0m are in neutrons of the element", elements[z]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
                    print(massquarksdownneutronsd, "mass quarks \033[92mDown\033[0m are are in neutrons of in the element", elements[z]['Name'], "in the molecule", elements[a]['Symbol'], subscript, elements[b]['Symbol'], subscript2, elements[c]['Symbol'], subscript3, elements[z]['Symbol'], subscript4)
            else:
                print("I can't make a molecule.")
        elif option2 == "0":
            print("Until next time.")
            break
        else:
            print("Invalid option.")        
    elif option1 == "2":
        print("""
                                            Standard Model
                                            \033[92mS\033[0m\033[94mtan\033[0m\033[95mdar\033[0m\033[96md\033[0m \033[104mMo\033[0m\033[101mdel\033[0m                                       

            00. \033[92mUp\033[0m                        01. \033[92mCharm\033[0m                         02. \033[92mTop\033[0m
            03. \033[92mDown\033[0m                      04. \033[92mStrange\033[0m                       05. \033[92mBottom\033[0m
            06. \033[94mAntiup\033[0m                    07. \033[94mAnticharm\033[0m                     08. \033[94mAntitop\033[0m
            09. \033[94mAntidown\033[0m                  10. \033[94mAntistrange\033[0m                   11. \033[94mAntibottom\033[0m
            12. \033[95mElectron\033[0m                  13. \033[95mMuon\033[0m                          14. \033[95mTau\033[0m
            15. \033[95mElectron neutrino\033[0m         16. \033[95mMuon neutrino\033[0m                 17. \033[95mTau neutrino\033[0m
            18. \033[96mPositron\033[0m                  19. \033[96mAntimuon\033[0m                      20. \033[96mAntitau\033[0m
            21. \033[96mElectron neutrino\033[0m         22. \033[96mMuon neutrino\033[0m                 23. \033[96mTau neutrino\033[0m
            24. \033[101mGluon\033[0m                     25. \033[101mPhoton\033[0m                        26. \033[101mBosonZ\033[0m
            27. \033[101mBosonWplus\033[0m                28. \033[101mBosonWless\033[0m                    29. \033[101mGraviton\033[0m
            30. \033[102mHiggs\033[0m                     

            [key]
            \033[92mQuarks\033[0m                   \033[94mAntiquarks\033[0m               \033[95mLeptons\033[0m
            \033[96mAntileptons\033[0m              \033[101mGauge Bosons\033[0m            \033[102mScalar Bosons\033[0m

            [0]
                1] Create a simple Big Bang 
        """)
        option2 = input("What do you want to do? ")
        if option2 == "1":
            bits = ['0','1']

            n = int(input("Enter the number of bits you want to generate: "))
            total_bytes = n/8

            # Generate random bits in a string.
            bits_string = ''.join(random.choice(bits) for i in range(n))

            # Every eight bits we generate a byte, separate it with : and store it in a string.
            bytes_string = ':'.join(bits_string[i:i+8] for i in range(0, len(bits_string), 8))

            print("\n[ 8 bits = 1 byte ]")
            print("I show you the bytes that have coincided with some subelement:\n")
                        
            for byte in bytes_string.split(':'):
                for subelement in subelements:
                    if subelement['Binary'] == byte:
                        # Cambiamos todos los bytes por los bytes coloreados
                        bytes_string = bytes_string.replace(byte, subelement['Color_binary'])
                        # Cambiamos el nombre del subelemento por el coloreado
            print(bytes_string)

            print("\nI show you the name of the subelement that has matched:\n")
            for byte_colored in range(len(bytes_string.split(':'))):
                for subelement in subelements:
                    if subelement['Color_binary'] in bytes_string.split(':')[byte_colored]:
                        # We change the colored byte for the colored name.
                        bytes_string = bytes_string.replace(bytes_string.split(':')[byte_colored], subelement['Color_name'])
            print(bytes_string)

            print("\nI have created", total_bytes, "bytes.")
         
            while True:
                print("""
                        [0]
                            1] Show me the time it takes to generate each bit.
                            2] Reverse the zeros for ones, and vice versa.
                            3] Reverse the bit string.
                            4] Change zeros to ones and flip the bit string.
                """)

                option = int(input("Enter the option you want to do: "))

                if option == 0:
                    print("Bye!")
                    exit()
                elif option == 1:
                    # Show me the time it takes to generate each bit.
                    print("\nTime to generate each bit: \n")
                    for i in bits_string:
                        print("The bit", i, "it has taken", time.time(), "milliseconds to generate.")
                elif option == 2:
                    # Convert the string to a list of bits.
                    bits_list = list(bits_string)
                    # We invert the zeros for ones and the ones for zeros.
                    bits_list = [1 if x == '0' else 0 for x in bits_list]
                    # We convert the list of bits to a string.
                    bits_flipped_string = ''.join(str(x) for x in bits_list)
                    # Every eight bits we generate a byte, separate it with : and store it in a string.
                    bytes_flipped_string = ':'.join(bits_flipped_string[i:i+8] for i in range(0, len(bits_flipped_string), 8))

                    print("\n[ 8 bits = 1 byte ]")
                    print("I show you the bytes flipped from zeros to ones that have coincided with some subelement:\n")
                                
                    for byte in bytes_flipped_string.split(':'):
                        for subelement in subelements:
                            if subelement['Binary'] == byte:
                                # Cambiamos todos los bytes por los bytes coloreados
                                bytes_flipped_string = bytes_flipped_string.replace(byte, subelement['Color_binary'])
                                # Cambiamos el nombre del subelemento por el coloreado
                    print(bytes_flipped_string)

                    print("\nI show you the name of the subelement that has matched:\n")
                    for byte_colored in range(len(bytes_flipped_string.split(':'))):
                        for subelement in subelements:
                            if subelement['Color_binary'] in bytes_flipped_string.split(':')[byte_colored]:
                                # We change the colored byte for the colored name.
                                bytes_flipped_string = bytes_flipped_string.replace(bytes_flipped_string.split(':')[byte_colored], subelement['Color_name'])
                                break
                    print(bytes_flipped_string)

                    print("\nI have created", total_bytes, "bytes.")
                elif option == 3:
                    # We invert the bits so that they are in reverse order.
                    bits_reverse_string = bits_string[::-1]

                    # Every eight bits we generate a byte, separate it with : and store it in a string.
                    bytes_reverse_string = ':'.join(bits_reverse_string[i:i+8] for i in range(0, len(bits_reverse_string), 8))
                    print("\n[ 8 bits = 1 byte ]")
                    print("I show you the bytes reversed that have coincided with some subelement:\n")
                                
                    for byte in bytes_reverse_string.split(':'):
                        for subelement in subelements:
                            if subelement['Binary'] == byte:
                                # Cambiamos todos los bytes por los bytes coloreados
                                bytes_reverse_string = bytes_reverse_string.replace(byte, subelement['Color_binary'])
                                # Cambiamos el nombre del subelemento por el coloreado
                    print(bytes_reverse_string)

                    print("\nI show you the name of the subelement that has matched:\n")
                    for byte_colored in range(len(bytes_reverse_string.split(':'))):
                        for subelement in subelements:
                            if subelement['Color_binary'] in bytes_reverse_string.split(':')[byte_colored]:
                                # We change the colored byte for the colored name.
                                bytes_reverse_string = bytes_reverse_string.replace(bytes_reverse_string.split(':')[byte_colored], subelement['Color_name'])
                                break
                    print(bytes_reverse_string)

                    print("\nI have created", total_bytes, "bytes.")
                elif option == 4:
                    print("\nString of bits ordered from end to begin with the zeros inverted by ones: \n")
                    # We invert the bits so that they are in reverse order.
                    bits_inverted_string = bits_string[::-1]
                    # We convert the string into a list of bits.
                    bits_inverted_list = list(bits_inverted_string)
                    # We invert the zeros for ones and the ones for zeros.
                    bits_inverted_list = [1 if x == '0' else 0 for x in bits_inverted_list]
                    # We convert the list of bits to a string.
                    bits_inverted_string = ''.join(str(x) for x in bits_inverted_list)

                    # Every eight bits we generate a byte, separate it with : and store it in a string.
                    bytes_inverted_string = ':'.join(bits_inverted_string[i:i+8] for i in range(0, len(bits_inverted_string), 8))
                    print("\n[ 8 bits = 1 byte ]")
                    print("I show you the bytes ordered from end to begin with the zeros inverted by ones that have coincided with some subelement:\n")
                                
                    for byte in bytes_inverted_string.split(':'):
                        for subelement in subelements:
                            if subelement['Binary'] == byte:
                                # Cambiamos todos los bytes por los bytes coloreados
                                bytes_inverted_string = bytes_inverted_string.replace(byte, subelement['Color_binary'])
                                # Cambiamos el nombre del subelemento por el coloreado
                    print(bytes_inverted_string)

                    print("\nI show you the name of the subelement that has matched:\n")
                    for byte_colored in range(len(bytes_inverted_string.split(':'))):
                        for subelement in subelements:
                            if subelement['Color_binary'] in bytes_inverted_string.split(':')[byte_colored]:
                                # We change the colored byte for the colored name.
                                bytes_inverted_string = bytes_inverted_string.replace(bytes_inverted_string.split(':')[byte_colored], subelement['Color_name'])
                                break
                    print(bytes_inverted_string)

                    print("\nI have created", total_bytes, "bytes.")
                else:
                    print("\nOption not valid, try again.")
        elif option2 == "0":
            print("Until next time.")
            break
        else:
            print("Invalid option.")
    elif option1 == "0":
        print("Until next time.")
        break
    else:
        print("Invalid option.")
# A!Ü$KA
