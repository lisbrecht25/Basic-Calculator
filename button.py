import customtkinter

# Last Updated: 11/10/2025

# The button class made for building a calculator. Contaions only a function to spawn the button
# onto the grid of customtkinter and the listener to go with it.
class Button():
    def __init__(self, root, text,  textbox):
        self.root = root
        self.text = text
        self.textbox = textbox
        
    # This is the function that is called when a button of this class is clicked. This listening
    # function is specific for a calculator where it checks what button was pressed by using its
    # text and executes something basde off of that.
    def buttonListener(self):
        # If the button is an equals button it will attmempt to evaluate the expression. If something
        # goes wrong it will give the user an error.
        if self.text == "=":
            try:
                self.textbox.configure(state="normal")
                expression = self.textbox.get("1.0", "end-1c")
                result = eval(expression, {"__builtins__": None}, {})
                self.textbox.delete("1.0", "end-1c")
                self.textbox.insert(customtkinter.END, str(result), "right_align")
                self.textbox.configure(state="disabled")
            except Exception:
                self.textbox.configure(state="normal")
                self.textbox.delete("1.0", "end-1c")
                self.textbox.insert(customtkinter.END, "ERROR", "right_align")
                self.textbox.configure(state="disabled")
        # If the button is the clear button the text in the textbox will be erased.
        elif self.text == "C":
            self.textbox.configure(state="normal")
            self.textbox.delete("1.0", "end-1c")
            self.textbox.configure(state="disabled")
        #If the button is neither equals or clear it will just add the text to the textbox.
        else:
            self.textbox.configure(state="normal")
            self.textbox.insert(customtkinter.END, self.text, "right_align")
            self.textbox.configure(state="disabled")
    
    # Creates button in customtkinter. Gives user ability to customize button with many different
    # parameters that are optional. ONLY WORKS FOR BUTTONS IN A GRID. Uses the function buttonListener()
    # as the function called when the button is clicked.
    def spawnButton(self, rowNum, colNum, color = "orange", width = 100, height = 70, font = "Arial", fontSize = 20):
        self.button = customtkinter.CTkButton(
            master = self.root,
            text = self.text,
            fg_color = color,
            width = width,
            height = height,
            font = (font, fontSize),
            command = self.buttonListener
        )
        self.button.grid(row = rowNum, column = colNum, pady = 10)