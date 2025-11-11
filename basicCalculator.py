import customtkinter
import button

customtkinter.set_appearance_mode("dark")


root = customtkinter.CTk()
root.geometry("500x550")

textbox = customtkinter.CTkTextbox(root, width = 480, height = 75, font = ("Arial", 30), pady=25)
textbox.tag_config("right_align", justify="right")
textbox.configure(state="disabled")
textbox.grid(row = 0, column = 0, pady = 20, padx = 10, columnspan = 4, sticky = "ns")

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

sumButton = button.Button(root, "+", textbox)
subtractButton = button.Button(root, "-", textbox)
divideButton = button.Button(root, "/", textbox)
mulitplicationButton = button.Button(root, "X", textbox)
clearButton = button.Button(root, "C", textbox)
equalsButton = button.Button(root, "=", textbox)

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


root.mainloop()

