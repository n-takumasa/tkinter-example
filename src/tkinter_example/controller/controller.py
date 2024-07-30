from ..model import ModelProtocol
from ..view import View


class Controller:
    def __init__(self, model: ModelProtocol, view: View):
        self.model = model
        self.view = view

        self.setup_model()
        self.setup_view()

    def setup_model(self):
        self.model.add_observer(self.update_view)

    def setup_view(self):
        self.view.increment_button.config(command=self.increment)
        self.view.decrement_button.config(command=self.decrement)

    def mainloop(self):
        self.view.frame.master.mainloop()

    def increment(self):
        # TODO: ここでViewとModelの縁切り
        self.model.increment()

    def decrement(self):
        # TODO: ここでViewとModelの縁切り
        self.model.decrement()

    def update_view(self):
        count = self.model.get_count()
        self.view.label.config(text=str(count))
