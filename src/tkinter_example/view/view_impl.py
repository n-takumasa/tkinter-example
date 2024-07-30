from tkinter import ttk


class View:
    def __init__(self, master=None):
        frame = ttk.Frame(master)
        self.style = ttk.Style()
        frame.grid(sticky="NSEW")
        frame.master.columnconfigure(0, weight=1)
        frame.master.rowconfigure(0, weight=1)

        self.create_widgets(frame)

        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(0, weight=1)
        self.frame = frame

    def create_widgets(self, frame) -> None:
        self.label = ttk.Label(frame, text="0", anchor="center")
        self.label.grid(row=0, sticky="NSEW")

        self.increment_button = ttk.Button(frame, text="Increment")
        self.increment_button.grid(row=1, sticky="NSEW")

        self.decrement_button = ttk.Button(frame, text="Decrement")
        self.decrement_button.grid(row=2, sticky="NSEW")

        self.theme_combo = ttk.Combobox(frame)
        self.theme_combo.config(
            values=ttk.Style().theme_names(),
            state="readonly",
        )
        self.theme_combo.bind("<<ComboboxSelected>>", self.change_theme)
        self.theme_combo.grid(row=3, sticky="NSEW")

    def change_theme(self, _event):
        selected = self.theme_combo.get()
        self.style.theme_use(selected)
