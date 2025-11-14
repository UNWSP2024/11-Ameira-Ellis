import tkinter as tk

class GUI:
    def __init__(self):
        #Main window setup
        self.main_window = tk.Tk()
        self.main_window.title("My info")

        # Set window size
        self.main_window.geometry("400x200")

        self.button = tk.Button(self.main_window, text="Show Info", command=self.show_info)
        self.button.pack(pady=10)
        # add a Quit button that closes the window
        self.quit_button = tk.Button(self.main_window, text="Quit", command=self.main_window.quit)
        self.quit_button.pack(pady=5)
    def quit(self):
        exit_label = tk.Label(self.main_window,
            text="Exiting the program...", fg="Red", font=("Helvetica", 16))
        exit_label.pack(pady=10)    

    def show_info(self):
        info_label = tk.Label(self.main_window, 
            text="Name: Ameira Ellis \nAge: 17\nAddress: 201 3rd St. NW Saint Michael 55376", 
            fg = "Blue", font=("Helvetica", 16))

        # display the label
        info_label.pack(pady=10)
if __name__ == "__main__":
    gui = GUI()

    gui.main_window.mainloop()