"""Useful functions."""

TEST_FILENAME = 'small_input'
TASK_FILENAME = 'input'

def read_file(name: str) -> list[str]:
    """Reads the whole file and returns list of strings."""
    with open(name) as f:
        return f.readlines()
