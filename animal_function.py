from typing import Any, Dict, Union
import logging
import typer

ANIMAL_TYPES = ["dog", "cat", "horse"]


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
    BITE_ENERGY = -10
    DEFAULT = 0

    PARAM_MAX = 100
    PARAM_MIN = 0

    ENERGY_IDX = 0
    HUNGER_IDX = 1
    HAPPINESS_IDX = 2

    def __init__(self, kind: str, name: str, owner="danielle") -> None:
        """define the class variables"""
        self.kind = kind
        self.name = name
        self.owner = owner
        self.hunger = 0
        self.happiness = 20
        self.energy = 10
        self.points = 0
        self.history_path = kind + "_" + name + ".txt"
        self.last_action = ""
        self.logger:Any = None

    def append_history(self):
        """create a logger that use for update history file"""
        self.logger = logging.getLogger(self.kind + "_" + self.name)
        fh = logging.FileHandler(self.history_path)
        log_format = logging.Formatter("%(asctime)s %(levelname)s: %(message)s")
        fh.setFormatter(log_format)
        self.logger.setLevel(logging.DEBUG)
        self.logger.addHandler(fh)

    def eat(self) -> None:
        """update animal values if it eats"""
        self.energy += self.EAT_ENERGY
        self.hunger += self.EAT_HUNGER
        self.keep_params_in_range()
        self.default_actions("eat")

    def play(self) -> None:
        """update animal values if it plays"""
        self.energy += self.PLAY_ENERGY
        self.hunger += self.PLAY_HUNGER
        self.happiness += self.PLAY_HAPPINESS
        self.keep_params_in_range()
        self.default_actions("play")

    def sleep(self) -> None:
        """update animal values if it sleeps"""
        self.energy += self.SLEEP_ENERGY
        self.hunger += self.SLEEP_HUNGER
        self.keep_params_in_range()
        self.default_actions("sleep")

    def bite(self) -> None:
        """delete points to the animal if it bites"""
        self.energy += self.BITE_ENERGY
        self.keep_params_in_range()
        self.default_actions("bite")

    def check_owner_name(self, owner):
        """check if the owner name is ok"""
        if len(owner) > 0:
            if owner.isalpha() and owner.islower():
                return True
        return False

    def change_owner(self, owner) -> None:
        """change the owner of the animal"""
        if self.check_owner_name(owner):
            self.owner = owner
            self.happiness += self.OWNER_HAPPINESS
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
            self.last_action = source_action
            if self.logger is None:
                self.append_history()
            self.logger.info(text)

    def keep_params_in_range(self) -> None:
        """make sure the values are between 0-100"""
        params = [self.energy, self.hunger, self.happiness]
        for i in range(len(params)):
            if params[i] > self.PARAM_MAX:
                params[i] -= params[i] - self.PARAM_MAX
            elif params[i] < self.PARAM_MIN:
                params[i] += self.PARAM_MIN - params[i]
        self.energy = params[self.ENERGY_IDX]
        self.hunger = params[self.HUNGER_IDX]
        self.happiness = params[self.HAPPINESS_IDX]

    def exit_loop(self) -> bool:
        """return false to exit the loop"""
        return False

    def print_params(self) -> Dict:
        """print the parameters of the animal"""
        return {
            "happiness": self.happiness,
            "hunger": self.hunger,
            "energy": self.energy,
            "last_action": self.last_action,
            "animal_stat": self.final_calculate(),
            "total_points": self.points,
            "owner": self.owner,
        }

    def choose_actions(self, user_choice, params: Union[str, None]) -> Dict:
        """keep allow choosing action until exit, also if input is wrong"""
        choice_to_action = {
            "eat": self.eat,
            "play": self.play,
            "sleep": self.sleep,
            "bite": self.bite,
            "owner": self.change_owner,
        }
        if params is None:
            choice_to_action[user_choice]()
        else:
            choice_to_action[user_choice](params)
        return self.print_params()

    def final_calculate(self) -> float:
        """calculate the average of all the parameters of the animal"""
        params = [self.happiness, self.energy, self.hunger]
        return sum(params) / len(params)


def name_confirm(value):
    """check that the name is ok"""
    if len(value) > 0:
        if value.isalpha() and value.islower():
            return value
    raise ValueError("Name should contain only lowercase")


def kind_confirm(kind):
    """make sure the input kind exists"""
    if kind in ANIMAL_TYPES:
        return kind
    raise ValueError("The type of the animal is wrong")


def create_animal(animal_type: str, animal_name: str):
    """create and define a new animal"""
    name_confirm(animal_name)
    kind_confirm(animal_type)
    my_animal = Animal(animal_type, animal_name)
    my_animal.append_history()
    return my_animal


if __name__ == "__main__":
    create_animal("cat", "da")
