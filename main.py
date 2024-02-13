import tkinter as tk
from PIL import Image, ImageTk
import random


class GuessingGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Number Guessing Game")
        self.geometry("600x350")

        # Load background image
        bg_image = Image.open("photo.jpg")
        bg_image = bg_image.resize((600, 350))
        self.background_image = ImageTk.PhotoImage(bg_image)
        self.background_label = tk.Label(self, image=self.background_image)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.random_number = random.randint(0, 100)

        self.label = tk.Label(self, text="Enter your guess (0-100):", font=("Arial", 12), bg='white')
        self.label.place(relx=0.5, rely=0.3, anchor="center")

        self.entry = tk.Entry(self)
        self.entry.place(relx=0.5, rely=0.4, anchor="center")

        self.submit_button = tk.Button(self, text="Submit", command=self.check_guess)
        self.submit_button.place(relx=0.5, rely=0.5, anchor="center")

        self.result_label = tk.Label(self, text="", font=("Arial", 14), bg='white')
        self.result_label.place(relx=0.5, rely=0.6, anchor="center")

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            if guess == self.random_number:
                self.result_label.config(text="Congratulations! You guessed the number.")
            elif guess < self.random_number:
                self.result_label.config(text="Too small! Try again.")
            else:
                self.result_label.config(text="Too large! Try again.")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a number.")


if __name__ == "__main__":
    app = GuessingGame()
    app.mainloop()
