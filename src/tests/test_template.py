# from ..template import hello_world works too,
# But we try to avoid relative imports.
from src.template import hello_world


def test_hello_world():
    result = hello_world()
    assert result.startswith("Hello World ! It's")
