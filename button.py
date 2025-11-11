import customtkinter

class Button():
    def __init__(self, root, text,  textbox):
        self.root = root
        self.text = text
        self.textbox = textbox
        
    def buttonListener(self):
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
        elif self.text == "C":
            self.textbox.configure(state="normal")
            self.textbox.delete("1.0", "end-1c")
            self.textbox.configure(state="disabled")
        else:
            self.textbox.configure(state="normal")
            self.textbox.insert(customtkinter.END, self.text, "right_align")
            self.textbox.configure(state="disabled")
    
    def spawnButton(self, rowNum, colNum):
        self.button = customtkinter.CTkButton(
            master = self.root,
            text = self.text,
            fg_color = "orange",
            width = 100,
            height = 70,
            font = ("Arial", 20),
            command = self.buttonListener
        )
        self.button.grid(row = rowNum, column = colNum, pady = 10)