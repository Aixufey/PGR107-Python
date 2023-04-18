class Compose:
    def __init__(self, letter_from, letter_to):
        self.letter_from = letter_from
        self.letter_to = letter_to
        self.line = ''

    def add_newline(self, line):
        self.line = self.line + f"{line}\n"

    def output(self):
        text = f"Dear {self.letter_to}: \n\n"
        text = text + self.line
        text = text + f"\nSincerely,\n\n{self.letter_from}"
        print(text)


c = Compose('John', 'Mary')
c.add_newline('I am sorry we must part.')
c.add_newline('I wish you all the best.')
c.output()
