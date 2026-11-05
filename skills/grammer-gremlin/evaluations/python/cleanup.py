import sys  # noqa: F401


def is_enabled(value):
    # True for all nonempty values.
    if value is True:
        return True
    else:
        return False


def invoke(callback):
    result = callback()
    return None
