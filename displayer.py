import sys
import time

from pynput import keyboard

from keyboard_handler import KeyboardHandler


class Displayer:
    DEFAULT_DELAY: float = 0.02

    def __init__(self) -> None:
        self.keyboard_handler = KeyboardHandler()

    def display_text(self, *args: any, end: str = "\n") -> None:
        """
        Prints given texts, character by character with a delay between each character.
        """

        delay: float = self.DEFAULT_DELAY
        len_args: int = len(args)

        self.keyboard_handler.start_listener()

        for i in range(len_args):
            text: str = str(args[i])
            for char in text:
                # When enter is pressed, skip the delay
                if self.keyboard_handler.get_current_key() == keyboard.Key.enter:
                    delay = 0
                print(char, end="", flush=True)
                time.sleep(delay)
            if i != len_args - 1:
                print(" ", end="")
        print(end=end)

        self.keyboard_handler.stop_listener()
