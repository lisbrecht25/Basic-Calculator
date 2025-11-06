import customtkinter

class Button():
    def __init__(self, root, num):
        self.number = num
        self.root = root

    def buttonAction(self):
        print("Button number is", self.number)

    def createNumberButton(self):
        self.button = customtkinter.CTkButton(
            master = self.root,
            text = self.number,
            fg_color="orange",
            command = self.buttonAction
        )
        self.button.pack(padx=20,pady=20)
    

customtkinter.set_appearance_mode("dark")


root = customtkinter.CTk()
root.geometry("500x350")


frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

buttonOne = Button(root, "2")
buttonOne.createNumberButton()

root.mainloop()

