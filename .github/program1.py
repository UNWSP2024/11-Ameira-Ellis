import tkinter as tk

class GUI:
    def __init__(self):
        #Main window setup
        self.main_window = tk.Tk()
        self.main_window.title("Favorite Saying")

        # Set window size
        self.main_window.geometry("400x200")

        saying_label = tk.Label(self.main_window, 
            text='"If the Stars were Made to Worship, So Will I"', fg = ("Magenta"), font=("Helvetica", 24))
        saying_label.pack(pady=10)

        # Start the GUI event loop
        self.main_window.mainloop()
if __name__ == "__main__":
    gui = GUI()