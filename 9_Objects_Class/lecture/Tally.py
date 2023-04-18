class Tally:
    def __init__(self):
        self.value = 0

    def click(self):
        self.value += 1

    def reset(self):
        self.value = 0

    # Default printing toString method
    def __str__(self):
        return "Value: " + str(self.value)


t = Tally()
t.click()
t.click()
t.click()

print(t)
