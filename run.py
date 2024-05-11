from argparse import ArgumentParser
from app.view import RootView
from test import test_tokenization

def setup():
    mode = ArgumentParser(description="Utility to control application execution with various options.")

    mode.add_argument("-t", "--test", action="store_true", help="test the functionality of the application")

    if mode.parse_args().test:
        return test_tokenization()
    
    else:
        return RootView()

if __name__ == "__main__":
    setup()

