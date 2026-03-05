import html
import animal_function
import ctypes


class WebAnimal:
    def __init__(self):
        self.animal_objects = {}

    def full_html(self, specific_site_content):
        html_base_content = f"""
            <html>
            <head>
                <title>Some HTML in here</title>
            </head>
            <body>
                {specific_site_content}
            </body>
            </html>
            """
        return html_base_content


    def home_screen(self):
        text = """
        <h2 style='text-align:center'>Welcome to animal viewing :)</h2>
        <br>
        <a href="http://127.0.0.1:8000/status"><h3 style='text-align:center'>press here to get to status page</h3></a>
        """
        return self.full_html(text)

    def new_animal(self, animal_kind, animal_name):
        try:
            animal = animal_function.create_animal(animal_kind, animal_name)
            text = f"<h1 style='text-align:center'>A {animal_kind} name {animal_name} is exist</h1>"
            if animal_kind + "_" + animal_name not in self.animal_objects:
                self.animal_objects[animal_kind + "_" + animal_name] = animal
                text = f"<h1 style='text-align:center'>A {animal_kind} name {animal_name} was created</h1>"
            return text
            # call this function from the one that contains the whole page of bottoms
        except Exception:
            text = "<h1 style='text-align:center'>Error: wrong parameters</h1>"
            return text

    def show_bottoms(self, animal_kind, animal_name):
        animal_text = self.new_animal(animal_kind, animal_name)
        if "Error" in animal_text:
            return self.full_html(animal_text)
        text = f"""
        <a href="http://127.0.0.1:8000/eat?animal_description={animal_kind + "_" + animal_name}"><button>make the animal eat</button></a>
        <button onlink='window.location.href="http://127.0.0.1:8000/sleep"'>make the animal sleep</button>
        <button onlink='window.location.href="http://127.0.0.1:8000/play"'>make the animal play</button>
        
        <h1>{animal_function.Animal.print_params(self.animal_objects[animal_kind + "_" + animal_name])}</h1>
        """
        print(animal_function.Animal.print_params(self.animal_objects[animal_kind + "_" + animal_name]))
        # text = f"{id(animal)}"
        return animal_text + "\n" + text

    def do_action(self, action, animal_description):
        animal_obj = self.animal_objects[animal_description]
        animal_function.Animal.choose_actions(animal_obj, action)
        # TODO redirect instead of return
        return self.full_html(f"{animal_function.Animal.print_params(animal_obj)}")
