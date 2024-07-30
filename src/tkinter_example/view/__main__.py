import tkinter as tk

from .view_impl import View

if __name__ == "__main__":
    root = tk.Tk()
    v = View(root)
    root.mainloop()
