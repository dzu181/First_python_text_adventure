import sys
import time


def display_text(*args: any, end: str = '\n') -> None:
    """
    Prints given texts, character by character with a delay between each character.
    """
    DELAY: float = 0.05
    len_args: int = len(args)
    for i in range(len_args):
        text: str = str(args[i])
        for char in text:
            print(char, end='')
            sys.stdout.flush()
            time.sleep(DELAY)
        if i != len_args - 1:
            print(' ', end='')
    print(end=end)
