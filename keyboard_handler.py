import sys

from pynput import keyboard


class KeyboardHandler:

    def __init__(self) -> None:
        self.listener = None
        self.controller = keyboard.Controller()
        self.current_key = None

    def on_press(self, key):
        if keyboard.Key.backspace != key:
            self.current_key = key
            self.controller.press(keyboard.Key.backspace)

    def start_listener(self):
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()  # start to listen on a separate thread

    def run_listener(self):
        self.listener.run()
        self.listener.wait()

    def stop_listener(self):
        self.listener.stop()

    def is_listener_alive(self):
        return self.listener.is_alive()

    def get_current_key(self) -> keyboard.Key:
        temp = self.current_key
        self.current_key = None
        return temp
