from .type import ObserverT


class Model:
    def __init__(self):
        self._count = 0
        self._observers: list[ObserverT] = []

    def get_count(self):
        return self._count

    def increment(self):
        self._count += 1
        self._notify()

    def decrement(self):
        self._count -= 1
        self._notify()

    def _notify(self):
        for observer in self._observers:
            observer()

    def add_observer(self, observer: ObserverT):
        self._observers.append(observer)
