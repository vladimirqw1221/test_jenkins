import pytest


@pytest.fixture(scope="function")
def set_up():
    print("Start test")
    yield
    print("Finish test")
