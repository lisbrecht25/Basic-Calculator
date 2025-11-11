import customtkinter

class Button():
    def __init__(self, frame, num):
        self.number = num
        self.frame = frame

    def buttonAction(self):
        textbox.configure(state="normal")
        textbox.insert(customtkinter.END, self.number, "right_align")
        textbox.configure(state="disabled")

    def createNumberButton(self, rowNum, columnNum):
        self.button = customtkinter.CTkButton(
            master = self.frame,
            text = self.number,
            fg_color = "orange",
            width = 100,
            height = 70,
            font = ("Arial", 20),
            command = self.buttonAction
        )
        self.button.grid(row = rowNum, column = columnNum, pady = 10)

class operationButton():
    def __init__(self, root, operation, num1):
        self.root = root
        self.operation = operation
        self.num1 = num1

    def operationButtonAction(self):
        self.num1 = textbox.get("0.0", customtkinter.END)
        textbox.configure(state="normal")
        textbox.insert(customtkinter.END, self.operation, "right_align")
        textbox.configure(state="disabled")
        match self.operation:
            case "+":
                print(self.num1)
                return self.num1


    def createOperationalButton(self, rowNum, columnNum):
        self.button = customtkinter.CTkButton(
            master = self.root,
            text = self.operation,
            fg_color = "orange",
            width = 100,
            height = 70,
            font = ("Arial", 20),
            command = self.operationButtonAction
        )
        self.button.grid(row = rowNum, column = columnNum, pady = 10)
    

customtkinter.set_appearance_mode("dark")


root = customtkinter.CTk()
root.geometry("500x550")

textbox = customtkinter.CTkTextbox(root, width = 480, height = 75, font = ("Arial", 30), pady=25)
textbox.tag_config("right_align", justify="right")
textbox.configure(state="disabled")
textbox.grid(row = 0, column = 0, pady = 20, padx = 10, columnspan = 4, sticky = "ns")

num1 = 0
num2 = 0

buttonZero = Button(root, "0")
buttonZero.createNumberButton(4, 1)
buttonOne = Button(root, "1")
buttonOne.createNumberButton(3, 0)
buttonTwo = Button(root, "2")
buttonTwo.createNumberButton(3, 1)
buttonThree = Button(root, "3")
buttonThree.createNumberButton(3, 2)
buttonFour = Button(root, "4")
buttonFour.createNumberButton(2, 0)
buttonFive = Button(root, "5")
buttonFive.createNumberButton(2, 1)
buttonSix = Button(root, "6")
buttonSix.createNumberButton(2, 2)
buttonSeven = Button(root, "7")
buttonSeven.createNumberButton(1, 0)
buttonEight = Button(root, "8")
buttonEight.createNumberButton(1, 1)
buttonNine = Button(root, "9")
buttonNine.createNumberButton(1, 2)

plusButton = operationButton(root, "+", num1)
num1 = plusButton.createOperationalButton(1, 3)
minusButton = operationButton(root, "-", num1)
minusButton.createOperationalButton(2, 3)
divisionButton = operationButton(root, "/", num1)
divisionButton.createOperationalButton(3, 3)
productButton = operationButton(root, "X", num1)
productButton.createOperationalButton(4, 3)
clearButton = operationButton(root, "CLEAR", num1)
clearButton.createOperationalButton(4, 0)
equalButton = operationButton(root, "=", num1)
equalButton.createOperationalButton(4, 2)


root.mainloop()

