import customtkinter

class Interface :

    def __init__(self) -> None:
        self.app=customtkinter.CTk()
        self.app.geometry("800x500")
        self.app.resizable(0,0)
        self.app.title('Pd control panel')


        if __name__ == "__main__":
            self.run()
    



    def run(self):
        self.app.mainloop()

Interface()
