class InputHandler:
    @staticmethod
    def input(prompt: str = ''):
        print(prompt, end='')

        s: str = ''
        while len(s) == 0:
            s = input()
        return s
