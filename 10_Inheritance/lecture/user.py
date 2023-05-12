class User:
    def sign_in(self):
        print("Logged in")


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power {self.power}")


class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f"Remaining arrows {self.arrows}")

    def sprint(self):
        print("Sprint for 10 seconds.")


class HybridClass(Wizard, Archer):
    # Constructor of Hybrid should include ALL arguments for Parents classes
    def __init__(self, name, power, arrows=None):
        Wizard.__init__(self, name, power)
        self.arrows = arrows


myhybrid = HybridClass("Borgin", 50, 20)
myhybrid.sign_in()
myhybrid.sprint()
myhybrid.check_arrows()
myhybrid.attack()
