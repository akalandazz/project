from api import MainWindow, SendDialog


def test_main_windo():
    mw = MainWindow()
    assert isinstance(mw, MainWindow)


def test_send_dialog():
    mw = MainWindow()
    sd = SendDialog(mw)
    assert isinstance(sd, SendDialog)
    
def test_addition():
    expresion = 1 + 1
    assert expresion == 2
