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
        Animal Kind: <input type="text" id="kind_text" value="">
        Animal Name: <input type="text" id="name_text" value="">
        <button onclick="myFunction()">create link</button>
        <h3 style='text-align:center'><a id="aLink"></a></h3>
        <script>
        function myFunction() {
          var kind = document.getElementById("kind_text").value;
          var name = document.getElementById("name_text").value;
          let link = document.getElementById('aLink');
          link.href = "http://127.0.0.1:8000/status/" + kind + "/" + name;
          link.innerText = 'Press here to get to the animal status page';
        }
        </script>
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
        animal_obj = self.animal_objects[animal_kind + "_" + animal_name]
        text = f"""
        <a href="http://127.0.0.1:8000/eat?animal_kind={animal_kind}&animal_name={animal_name}"><button>make the animal eat</button></a>
        <a href="http://127.0.0.1:8000/sleep?animal_kind={animal_kind}&animal_name={animal_name}"><button>make the animal sleep</button></a>
        <a href="http://127.0.0.1:8000/play?animal_kind={animal_kind}&animal_name={animal_name}"><button>make the animal play</button></a>
        <h1 style='text-align:center'>Basic Parameters</h1>
        <h2 style='text-align:center'>Happiness -- {animal_function.Animal.print_params(animal_obj)["happiness"]}</h2>
        <h2 style='text-align:center'>Hunger -- {animal_function.Animal.print_params(animal_obj)["hunger"]}</h2>
        <h2 style='text-align:center'>Energy -- {animal_function.Animal.print_params(animal_obj)["energy"]}</h2>
        <br>
        <h1 style='text-align:center'>More Parameters</h1>
        <h2 style='text-align:center'>Last Action -- {animal_function.Animal.print_params(animal_obj)["last_action"]}</h2>
        <h2 style='text-align:center'>Animal Status -- {animal_function.Animal.print_params(animal_obj)["animal_stat"]}</h2>
        <br>
        <h3 style='text-align:center'><a href="http://127.0.0.1:8000/">Press here to get to the animal status page</a></h3>
        """
        return animal_text + "\n" + text

    def do_action(self, action, animal_kind, animal_name):
        animal_obj = self.animal_objects[animal_kind + "_" + animal_name]
        animal_function.Animal.choose_actions(animal_obj, action)
