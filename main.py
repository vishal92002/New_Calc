""" content of test_sample.py#"""


def inc(x_value):
    """Increment the function adds one to the x_value"""

    return x_value + 1


def test_answer():
    """This test the function"""

    assert inc(4) == 5
