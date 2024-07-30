from unittest.mock import MagicMock

from tkinter_example.model import Model, ModelProtocol


def test_supports_protocol():
    model = Model()
    assert isinstance(model, ModelProtocol)


def test_increment():
    model = Model()
    model.increment()
    assert model.get_count() == 1


def test_decrement():
    model = Model()
    model.decrement()
    assert model.get_count() == -1


def test_notify():
    mock = MagicMock()

    model = Model()
    model.add_observer(mock)

    model.increment()
    model.decrement()

    assert mock.call_count == 2
