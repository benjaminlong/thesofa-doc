# Here import your needed dep
# Ex:
# import pytest
# from datetime import date, datetime
from datetime import datetime


# Here define your class/methods
def hello_world():
    msg = f"Hello World ! It's {datetime.now()}"
    print(msg)
    return msg


# This if statement is executed only if you call directly
# python3 path/to/this/template.py
if __name__ == '__main__':
    # Execute when the module is not initialized from an import statement.
    hello_world()
