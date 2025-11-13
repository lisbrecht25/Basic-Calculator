import customtkinter
import button # From button.py

# Last Updated on 11/12/2025

customtkinter.set_appearance_mode("dark")

# Create customtkinter window for GUI
root = customtkinter.CTk()
root.geometry("500x550")
root.title("Basic Calculator")

# Add textbox to the GUI. Have text aligned to right and doesn't allow users to type in box.
textbox = customtkinter.CTkTextbox(root, width = 480, height = 75, font = ("Arial", 30), pady=25)
textbox.tag_config("right_align", justify="right")
textbox.configure(state="disabled")
textbox.grid(row = 0, column = 0, pady = 20, padx = 10, columnspan = 4, sticky = "ns")

# Create objects for numbers 0 to 9 using button class from button.py
buttonZero = button.Button(root, "0", textbox)
buttonOne = button.Button(root, "1", textbox)
buttonTwo = button.Button(root, "2", textbox)
buttonThree = button.Button(root, "3", textbox)
buttonFour = button.Button(root, "4", textbox)
buttonFive = button.Button(root, "5", textbox)
buttonSix = button.Button(root, "6", textbox)
buttonSeven = button.Button(root, "7", textbox)
buttonEight = button.Button(root, "8", textbox)
buttonNine = button.Button(root, "9", textbox)

# Create objects for operational buttons
sumButton = button.Button(root, "+", textbox)
subtractButton = button.Button(root, "-", textbox)
divideButton = button.Button(root, "/", textbox)
mulitplicationButton = button.Button(root, "*", textbox)
clearButton = button.Button(root, "C", textbox)
equalsButton = button.Button(root, "=", textbox)

# Spawn all of the buttons onto the GUI by giving the row and coloumn they should be located in.
# Both row and cloumn start at 0 but textbox take up entirity of row 0.
buttonZero.spawnButton(4, 1)
buttonOne.spawnButton(3, 0)
buttonTwo.spawnButton(3, 1)
buttonThree.spawnButton(3, 2)
buttonFour.spawnButton(2, 0)
buttonFive.spawnButton(2, 1)
buttonSix.spawnButton(2, 2)
buttonSeven.spawnButton(1, 0)
buttonEight.spawnButton(1, 1)
buttonNine.spawnButton(1, 2)
sumButton.spawnButton(1, 3)
subtractButton.spawnButton(2, 3)
divideButton.spawnButton(4, 3)
mulitplicationButton.spawnButton(3, 3)
clearButton.spawnButton(4, 0)
equalsButton.spawnButton(4, 2)

# Create customtkinter loop to show GUI
root.mainloop()

