from enum import Enum
import typer


class AnimalsTypes(str, Enum):
    dog = "dog"
    cat = "cat"
    horse = "horse"


class Animal:
    def __init__(self, animal_type: str, animal_name: str):
        self.animal_type = animal_type
        self.animal_name = animal_name
        self.hunger = 0
        self.happiness = 0
        self.energy = 0
        self.points = 0
        self.history = []

    def eat(self):
        self.default_actions("eat")
        params_values = {"energy": 10, "hunger": -10, "happiness": 0}
        return self.check_values(params_values)

    def play(self):
        self.default_actions("play")
        params_values = {"energy": -20, "hunger": 10, "happiness": 25}
        return self.check_values(params_values)

    def sleep(self):
        self.default_actions("sleep")
        params_values = {"energy": 10, "hunger": 5, "happiness": 0}
        return self.check_values(params_values)

    def default_actions(self, source_action) -> None:
        actions_values = {
            "eat": {
                "points": 5,
                "msg": f"{self.animal_name} eats"
            },
            "play": {
                "points": 10,
                "msg": f"{self.animal_name} plays"
            },
            "sleep": {
                "points": 7,
                "msg": f"{self.animal_name} sleeps"
            }
        }
        self.points += actions_values[source_action]["points"]
        text = actions_values[source_action]["msg"]
        self.history.append(text)
        print(text)

    def check_values(self, params_values):
        energy = params_values["energy"] + self.energy
        hunger = params_values["hunger"] + self.hunger
        happiness = params_values["happiness"] + self.happiness
        params = [energy, hunger, happiness]
        for value in params:
            if value > 100 or value < 0:
                return False
        self.energy = energy
        self.hunger = hunger
        self.happiness = happiness
        return True


def main(animal_type: AnimalsTypes, animal_name: str):
    print(f"Hello {animal_type} {animal_name}")
    my_animal = Animal(animal_type, animal_name)
    # get_value = typer.prompt("Please enter", type=int)
    my_animal.default_actions("sleep")


if __name__ == "__main__":
    typer.run(main)
