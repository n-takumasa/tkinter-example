import tkinter as tk

from controller import Controller
from model import Model
from view import View


def main():
    root = tk.Tk()
    model = Model()
    view = View(root)

    app = Controller(model, view)
    app.mainloop()


if __name__ == "__main__":
    main()
