from api import MainWindow


def test_main_windo():
    mw = MainWindow()
    assert isinstance(mw, MainWindow)