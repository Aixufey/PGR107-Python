"""
    We want to add a button to the tally counter in previous lecture that allows an operator to undo an
    accidental button click. Provide a method
    def undo (self)
    that simulates such a button. As an added precaution, make sure that the operator cannot click the undo
    button more often than the count button.
"""


class TallyCounter:

    def __init__(self):
        self.temp = None
        self.value = 0

    def click(self):
        self.temp = self.value
        self.value = self.value + 1

    def undo(self):
        if self.temp < self.value:
            self.value = self.temp
        else:
            print("Can't undo")

    def reset(self):
        if self.value > 0:
            self.value = 0
        else:
            print('Already 0')

    def __str__(self):
        return f"The value is: {self.value}"


result = TallyCounter()
result.click()
result.click()
result.click()

result.undo()
print(result)
