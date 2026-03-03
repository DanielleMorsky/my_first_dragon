from enum import Enum

from typing import Any
import logging
import typer


class AnimalsTypes(str, Enum):
    """define all the animal possible types"""

    DOG = "dog"
    CAT = "cat"
    HORSE = "horse"


class Animal:
    """define an animal and its actions"""

    EAT_ENERGY = 10
    EAT_HUNGER = -10
    PLAY_ENERGY = -20
    PLAY_HUNGER = 10
    PLAY_HAPPINESS = 25
    SLEEP_ENERGY = 10
    SLEEP_HUNGER = 5
    OWNER_HAPPINESS = -10
    DEFAULT = 0

    PARAM_MAX = 100
    PARAM_MIN = 0
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
        self.hunger = [0]
        self.happiness = [0]
        self.energy = [0]
        self.points = 0
        self.history_path = "history.txt"
        self.logger: Any = None

    def eat(self) -> None:
        """update animal values if it eats"""
        self.energy[0] += self.EAT_ENERGY
        self.hunger[0] += self.EAT_HUNGER
        self.keep_params_in_range()
        self.default_actions("eat")

    def play(self) -> None:
        """update animal values if it plays"""
        self.energy[0] += self.PLAY_ENERGY
        self.hunger[0] += self.PLAY_HUNGER
        self.happiness[0] += self.PLAY_HAPPINESS
        self.keep_params_in_range()
        self.default_actions("play")

    def sleep(self) -> None:
        """update animal values if it sleeps"""
        self.energy[0] += self.SLEEP_ENERGY
        self.hunger[0] += self.SLEEP_HUNGER
        self.keep_params_in_range()
        self.default_actions("sleep")

    def bite_someone(self) -> None:
        """delete points to the animal if it bites"""
        self.default_actions("bite")

    def get_owner_name(self):
        right_input = False
        owner = self.owner
        while not right_input:
            owner = typer.prompt(
                "Enter the name of the new owner (only lowercase)", type=str
            )
            if len(owner) > 0:
                if owner.isalpha() and owner.islower():
                    right_input = True
        return owner

    def change_owner(self) -> None:
        """change the owner of the animal"""
        self.owner = self.get_owner_name()
        self.happiness[0] = self.OWNER_HAPPINESS
        self.keep_params_in_range()
        self.default_actions("change_owner")

    def default_actions(self, source_action) -> None:
        """do the default actions with specific values per actions"""
        actions_values = {
            "eat": {"points": 5, "msg": f"{self.kind} {self.name} eats"},
            "play": {"points": 10, "msg": f"{self.kind} {self.name} plays"},
            "sleep": {"points": 7, "msg": f"{self.kind} {self.name} sleeps"},
            "bite": {"points": -11, "msg": f"{self.kind} {self.name} bites"},
            "change_owner": {
                "points": -5,
                "msg": f"{self.kind} {self.name}'s owner changed",
            },
        }
        if source_action in actions_values:
            self.points += actions_values[source_action]["points"]
            if self.points < 0:
                self.points = 0
            text = actions_values[source_action]["msg"]
            self.logger.info(text)
            print("~~~" + text + "~~~")
        else:
            print("There isn't such an action")

    def append_history(self):
        logging.basicConfig(
            filename=self.history_path,
            format="%(asctime)s %(levelname)s: %(message)s",
            filemode="a",
        )
        self.logger = logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        self.logger.info(("~" * 5) + "New Run" + ("~" * 5))

    def keep_params_in_range(self) -> None:
        """make sure the values are between 0-100"""
        params = [self.energy, self.hunger, self.happiness]
        for i in range(len(params)):
            if params[i][0] > self.PARAM_MAX:
                params[i][0] = self.PARAM_MAX
            elif params[i][0] < self.PARAM_MIN:
                params[i][0] = self.PARAM_MIN

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
        params = [self.happiness[0], self.energy[0], self.hunger[0]]
        return sum(params) / len(params)


def name_confirm(value):
    if len(value) > 0:
        if value.isalpha() and value.islower():
            return value
    raise Exception("Name should contains only lowercase")


def main(animal_type: AnimalsTypes, animal_name: str):
    """create and define a new animal"""
    name_confirm(animal_name)
    print(f"Hello {animal_type} {animal_name}")
    my_animal = Animal(animal_type, animal_name)
    my_animal.append_history()
    my_animal.choose_actions()


if __name__ == "__main__":
    typer.run(main)
