# AtomicWorld 👨‍🏫
This application has two options:

   __1.__ Calculate the atoms of each element in a molecule.

   __2.__ "simulate" a Big Bang.

# Development of the program: ⚠️
The program has been developed using the Python programming language. The following libraries have been used:

**'random'**: Used to generate random numbers in the program.

**'colorama'**: Used for the color format in the program output.

**'time'**: Used to calculate the execution of the program at certain points for a better user experience.

# Option 1: Description: 🤓
The AtomicWorld program is a tool that allows you to calculate various properties of a molecule composed of up to four chemical elements. The user can enter the names and subscripts of the elements that make up the molecule, as well as their physical weight in grams, and the program will calculate and display detailed information about the composition of the molecule, including the number of moles, the number of molecules, the number of atoms, the number of protons and neutrons, as well as the mass in MeV/c^2 of the Up and Down quarks present in the protons and neutrons of each element.

# Option 1: Main Features: 🧠

   __·__ Calculation of the number of moles in the molecule.

   __·__ Calculation of the number of molecules in the molecule.

   __·__ Calculation of the number of atoms of each element in the molecule.

   __·__ Calculation of the number of protons and neutrons of each element in the molecule.

   __·__ Calculation of the mass in MeV/c^2 of the Up and Down quarks present in the protons and neutrons of each element.

# Option 1: Logic Used: 💭
The program uses a series of formulas and calculations based on the information provided about the chemical elements, including their atomic mass, number of protons and neutrons, as well as the mass in MeV/c^2 of the Up and Down quarks.

# Option 2: Description: 🤓
Aims to generate a visual representation of random bytes and display the names of sub-elements that match the generated bytes. The program offers several options to manipulate and display the generated bytes.

# Option 2: Main Features: 🧠
The program generates a random sequence of bits and converts it to bytes, then displays the generated bytes and their corresponding sub-element names. It also allows the user to perform various operations on the generated bits, such as inverting them, displaying the generation time of each bit, among other options.

# Option 2: Logic Used: 💭
The program uses the following logic to generate and manipulate the bits and bytes:

1. The **'random.choice'** function is used to generate a random sequence of bits.
2. The sequence of bits is converted to bytes by concatenating every 8 bits into a byte and separating the bytes with ":".
3. The generated bytes are compared to a list of predefined sub-elements.
4. If a byte matches the binary byte of a subitem, the colored name of the subitem is displayed.
5. Various options are offered to manipulate the generated bits, such as inverting them, inverting zeros to ones, etc.

# Developer 🌎
This program has been developed by [Alexei Barberà Roca] and is available for use and collaboration in  [https://github.com/aluskabarbera/AtomicWorld].
