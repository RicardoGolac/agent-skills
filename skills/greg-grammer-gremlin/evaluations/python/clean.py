def select_label(value):
    """Use the fallback for every falsy value, including zero and empty text."""
    return value or "fallback"


def wire_value(l):  # noqa: E741 - Public keyword matches the wire field name.
    return l
