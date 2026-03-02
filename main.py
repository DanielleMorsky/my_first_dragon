from enum import Enum
from typing import List, Any
import typer


class AnimalsTypes(str, Enum):
    """define all the animal possible types"""

    dog = "dog"
    cat = "cat"
    horse = "horse"


class Animal:
    """define an animal and its actions"""

    choices = (
        "Choose one of the following options:"
        "\n~\teat"
        "\n~\tplay"
        "\n~\tsleep"
        "\n~\tbite"
        "\n~\towner"
        "\n~\texit"
        "\nyour choice"
    )

    def __init__(self, kind: str, name: str, owner="Danielle") -> None:
        """define the class variables"""
        self.kind = kind
        self.name = name
        self.owner = owner
        self.hunger = 0
        self.happiness = 0
        self.energy = 0
        self.points = 0
        self.history: List[str] = []

    def eat(self) -> None:
        """update animal values if it eats"""
        params_values = {"energy": 10, "hunger": -10, "happiness": 0}
        if self.update_values_if_right(params_values):
            self.default_actions("eat")

    def play(self) -> None:
        """update animal values if it plays"""
        params_values = {"energy": -20, "hunger": 10, "happiness": 25}
        if self.update_values_if_right(params_values):
            self.default_actions("play")

    def sleep(self) -> None:
        """update animal values if it sleeps"""
        params_values = {"energy": 10, "hunger": 5, "happiness": 0}
        if self.update_values_if_right(params_values):
            self.default_actions("sleep")

    def bite_someone(self) -> None:
        """delete points to the animal if it bites"""
        self.default_actions("bite_someone")

    def change_owner(self) -> None:
        """change the owner of the animal"""
        owner = self.owner
        while not owner.isalpha():
            owner = input("Please enter the name of the new owner: ")
        self.owner = owner
        params_values = {"energy": 0, "hunger": 0, "happiness": -10}
        if self.update_values_if_right(params_values):
            self.default_actions("change_owner")

    def default_actions(self, source_action) -> None:
        """do the default actions with specific values per actions"""
        actions_values = {
            "eat": {"points": 5, "msg": f"{self.name} eats"},
            "play": {"points": 10, "msg": f"{self.name} plays"},
            "sleep": {"points": 7, "msg": f"{self.name} sleeps"},
            "bite_someone": {"points": -11, "msg": f"{self.name} bites"},
            "change_owner": {
                "points": -5,
                "msg": f"{self.name}'s owner changed",
            },
        }
        points_amount: Any = actions_values[source_action]["points"]
        self.points += points_amount
        if self.points < 0:
            self.points = 0
        text: Any = actions_values[source_action]["msg"]
        self.history.append(text)
        print("~~~" + text + "~~~")

    def update_values_if_right(self, params_values) -> bool:
        """make sure the values are between 0-100"""
        energy = params_values["energy"] + self.energy
        hunger = params_values["hunger"] + self.hunger
        happiness = params_values["happiness"] + self.happiness
        params = [energy, hunger, happiness]
        for value in params:
            if value > 100 or value < 0:
                print("Can't do this action...  :(")
                return False
        self.energy = energy
        self.hunger = hunger
        self.happiness = happiness
        return True

    def exit_loop(self) -> bool:
        """return false to exit the loop"""
        return False

    def print_params(self) -> None:
        """print the parameters of the animal"""
        print(
            "Current status: "
            f"\n\thappiness: {self.happiness}"
            f"\n\thunger: {self.hunger}"
            f"\n\tenergy: {self.energy}"
            f"\n\thistory: {self.history}"
        )

    def get_user_choice(self) -> str:
        """check that the user entered an action from the options"""
        actions = ["eat", "play", "sleep", "bite", "owner", "exit"]
        user_choice = ""
        while user_choice not in actions:
            user_choice = typer.prompt(self.choices, type=str)
        return user_choice

    def choose_actions(self) -> None:
        """keep allow choosing action until exit, also if input is wrong"""
        keep_choose = True
        while keep_choose:
            user_choice = self.get_user_choice()
            choice_to_action = {
                "eat": self.eat,
                "play": self.play,
                "sleep": self.sleep,
                "bite": self.bite_someone,
                "owner": self.change_owner,
            }
            if user_choice == "exit":
                keep_choose = self.exit_loop()
                print(f"Params average is: {self.final_calculate()}")
                print("goodbye :)")
            else:
                choice_to_action[user_choice]()
            self.print_params()

    def final_calculate(self) -> float:
        """calculate the average of all the parameters of the animal"""
        params = [self.happiness, self.energy, self.hunger]
        return sum(params) / len(params)


def main(animal_type: AnimalsTypes, animal_name: str):
    """create and define a new animal"""
    print(f"Hello {animal_type} {animal_name}")
    my_animal = Animal(animal_type, animal_name)
    my_animal.choose_actions()


if __name__ == "__main__":
    typer.run(main)
