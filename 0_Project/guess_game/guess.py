"""
Project description
Number Guessing Game
This project uses random module in Python to randomly generate an integer between 1 and 1000. Note that
the number is unknown to the user, and he/she should guess what that number is in a maximum of 5 guesses.
If the user’s guess is wrong, the program should provide some sort of indication as to how wrong (e.g., The
number is too high or too low). After each wrong guess, the program should also print how many attempts are
left for the user to guess the number again. If the user cannot guess the correct number in five attempts, the
program should print the message “Sorry!! You did not manage to guess the number. You have reached
the guessing limit” and prints the number itself. If the user guesses correctly (in maximum five attempts),
the program  should print the message “Congratulation! You guessed the number in ** attempt(s)” (the
number of attempts used to guess the number should be printed instead of **). The program should also print
the number itself in the end. Finally, the program should ask the user if he/she wants to play the game again.
If the answer is “YES”, the user must be able to play the game (a new game) again and has 5 attempts to guess
a new number randomly generated by the program. The program should be repeated as long as the user wants
to play the game again and again.
"""
import csv
import random
import sys
import uuid


class User:
    def __init__(self, name, attempt):
        self.id = str(uuid.uuid4()).split("-")[0]
        self.name = name
        self.attempt = attempt

    def __str__(self):
        return f"user: {self.name}, score: {self.attempt}"


class Game:
    def __init__(self):
        self.current_user = None
        self.users = []
        self.random_number = None
        self.attempts = None

    def login(self):
        try:
            self.read_user_csv()
            usr = input("Enter user: ").strip().lower()
            for user in self.users:
                if user.name == usr:
                    print(f"Welcome back, {user.name}")
                    self.current_user = user
                    self.show_menu()
                    print()
            else:
                raise Exception(f"{usr} not found!\r\nCreate a new user? y/n")
        except Exception as e:
            print(e)
            choice = input("Enter choice: ").strip()
            if choice == "y":
                new_user = self.create_user()
                self.save_user_csv(new_user)
                print(f"Welcome, {new_user.name}!")
                self.current_user = new_user
                self.show_menu()
            else:
                print("Goodbye")
                sys.exit(0)

    def display_menu_option(self):
        print("\r\n" + "=" * 20)
        menu = [
            "1 - Show users",
            "2 - Show high scores",
            "3 - Play game",
            "4 - Exit",
        ]
        for item in menu:
            print(item)
        print("=" * 20 + "\r\n")

    def show_menu(self):
        self.display_menu_option()
        while True:
            choice = input("Enter choice: ")
            if choice == "1":
                self.show_users()
            elif choice == "2":
                self.show_high_scores()
            elif choice == "3":
                self.handle_game(self.current_user)
                self.display_menu_option()
            else:
                print("Goodbye")
                sys.exit(0)

    def prepare_game(self):
        self.random_number = random.randint(1, 1000)
        self.attempts = 5

        msg = """
                Select difficulty level:
                1 - Easy (5 attempts)
                2 - Medium (3 attempts)
                3 - Hard (1 attempt)
        """
        print(msg)
        while True:
            choice = input("Enter choice: ").strip().lower()
            if choice == "1":
                self.attempts = 5
            elif choice == "2":
                self.attempts = 3
                self.random_number = random.randint(1, 500)
            else:
                self.attempts = 1
                self.random_number = random.randint(1, 100)
            return

    def handle_game(self, player):

        self.prepare_game()
        msg = f"""
        Welcome to the Number Guessing Game!\r\n
        You have {self.attempts} {'attempt' if self.attempts == 1 else 'attempts'} to guess a number {'between 1 - 100' if self.attempts == 1 else 'between 1 - 500' if self.attempts == 3 else 'between 1 - 1000'} \r\n
        Let's begin? \r\n"""
        print(msg)
        prompt = input("Press any key to continue or 'q' to quit: ").strip().lower()
        if prompt != "q".strip().lower():
            tries = 0
            try:
                while True:
                    guess = input("Guess the number: ").strip()
                    if guess.isdigit() and guess != "":
                        tries += 1
                        message = f"You have {self.attempts - tries} " \
                                  f"{'try' if self.attempts - tries == 1 else 'tries'} left."
                        if int(guess) == self.random_number:
                            print(f"{self.random_number} is the correct number!")
                            print(
                                f"Congratulation! You guessed the number in {tries} "
                                f"{'attempt' if tries == 1 else 'attempts'}")
                            # Only update high score if tries is less than current high score
                            self.update_user_csv(player, tries)
                            return
                        elif int(guess) > self.random_number:
                            print(f"{guess} is too high!")
                        else:
                            print(f"{guess} is too low!")

                        print(message)

                        if tries == self.attempts:
                            print(f"Ouch! You are out of tries.")
                            print(f"The number was {self.random_number}")
                            print("Do you want to play again? y/n")
                            choice = input("Enter choice: ").strip().lower()
                            if choice == "y":
                                self.handle_game(player)
                            return
                    else:
                        print(f"{player.name}, please enter a number! {guess} is not a number.")
            except ValueError as e:
                print(e)

        else:
            sys.exit(0)

    def create_user(self):
        name = input("Enter your name: ").strip().lower()
        exist = self.user_authenticate(name)
        if exist is not None:
            print("User already exists")
            return exist
        else:
            self.users.append(User(name, 0))
            self.save_user_csv(User(name, 0))

    def user_authenticate(self, user):
        self.read_user_csv()
        for u in self.users:
            if u.name == user:
                return u
        return None

    def save_user_csv(self, user):
        with open("users.csv", "a", newline='') as csvFile:
            writer = csv.writer(csvFile)
            if csvFile.tell() == 0:
                writer.writerow(["id", "name", "attempt"])
            writer.writerow([user.id, user.name, user.attempt])

    def read_user_csv(self):
        with open("users.csv", "r") as csvFile:
            reader = csv.reader(csvFile)
            next(reader)  # skip header row
            for row in reader:
                dto = User(row[1], row[2])
                self.users.append(dto)

    def update_user_csv(self, user, high_score):
        with open("users.csv", "r") as csvFile:
            reader = csv.reader(csvFile)
            rows = [row for row in reader]
        for row in rows:
            if row[1] == user.name:
                row[2] = high_score
                break
        with open("users.csv", "w", newline="") as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(rows)

    def show_users(self):
        for user in self.users:
            print(f"User:\t{user.name} ")

    def show_high_scores(self):
        for user in self.users:
            print("%s\t\t%s" % (user.name, user.attempt))


if __name__ == "__main__":
    game = Game()
    game.login()
