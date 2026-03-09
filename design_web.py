import animal_function


class WebAnimal:
    IP = "127.0.0.1"
    PORT = 8000

    def __init__(self):
        """define class variables"""
        self.animal_objects = {}
        self.url = f"http://{self.IP}:{self.PORT}/"

    def full_html(self, specific_site_content):
        """define basic structure of html page"""
        html_base_content = f"""
            <html>
            <style>
            body{{
                color: #de526c;
                background-color: #f0aab7;
            }}
            </style>
            <head>
                <title>My Animal</title>
            </head>
            <body>
                {specific_site_content}
            </body>
            </html>
            """
        return html_base_content

    def home_screen(self):
        # """create the home screen"""
        text = """
        <h2 style='text-align:center'>Welcome to animal viewing :)</h2>
        <br>
        <div style="text-align:center">
            Animal Kind: <input type="text" id="kind_text" value="">
            <br><br>
            Animal Name: <input type="text" id="name_text" value="">
            <br><br>
            <button onclick="myFunction()">animal status page</button>
            <script>
            function myFunction(){
                var kind = document.getElementById("kind_text").value;
                var name = document.getElementById("name_text").value;
                window.location.href = "/status/" + kind + "/" + name;
            }
            </script>
        </div>
        """
        return self.full_html(text)

    def new_animal(self, animal_kind, animal_name):
        """create new object of an animal"""
        if animal_kind + "_" + animal_name not in self.animal_objects:
            try:
                animal = animal_function.create_animal(animal_kind, animal_name)
                self.animal_objects[animal_kind + "_" + animal_name] = animal
                text = (
                    f"<h1 style='text-align:center'>"
                    f"A {animal_kind} name {animal_name} was created"
                    f"</h1>"
                )
            except ValueError:
                text = "<h1 style='text-align:center'>Error: wrong parameters</h1>"
        else:
            text = (
                f"<h1 style='text-align:center'>"
                f"A {animal_kind} name {animal_name} is exist"
                f"</h1>"
            )
        return text

    def show_buttons(self, animal_prop):
        """create the action buttons"""
        eat_button = f'<button onclick=window.location.href="/eat?{animal_prop}">the animal eats</button>'
        sleep_button = f'<button onclick=window.location.href="/sleep?{animal_prop}">the animal sleeps</button>'
        play_button = f'<button onclick=window.location.href="/play?{animal_prop}">the animal plays</button>'
        bite_button = f'<button onclick=window.location.href="/bite?{animal_prop}">the animal bites</button>'
        full_text = f"{eat_button}{sleep_button}{play_button}{bite_button}"
        return full_text

    def owner_button(self, animal_prop):
        """create the button of change owner"""
        owner_html = f"""
            Owner Name: <input type="text" id="owner_name" value="">
            <button onclick="myFunction()">change owner</button>
            <script>
            function myFunction() {{
              var owner = document.getElementById("owner_name").value;
              let link = document.getElementById('aLink');
              window.location.href = "/owner?{animal_prop}&params=" + owner;
            }}
            </script>
            """
        return owner_html

    def show_status(self, params_values):
        """display the current status of the animal"""
        text_status = f"""
            <h1>Basic Parameters</h1>
            <h2>Happiness -- {params_values["happiness"]}</h2>
            <h2>Hunger -- {params_values["hunger"]}</h2>
            <h2>Energy -- {params_values["energy"]}</h2>
            <br>
            <h1>More Parameters</h1>
            <h2>Last Action -- {params_values["last_action"]}</h2>
            <h2>Animal Status -- {params_values["animal_stat"]}</h2>
            <h2>Animal Total Points -- {params_values["total_points"]}</h2>
            <h2>Animal Owner -- {params_values["owner"]}</h2>
            <br>
            <h3><a href="{self.url}">Press to get animal status page</a></h3>
            """
        return text_status

    def get_status_screen(self, animal_kind, animal_name):
        """combine all the functions of this page and return the total page"""
        animal_text = self.new_animal(animal_kind, animal_name)
        if "Error" in animal_text:
            return self.full_html(animal_text)
        animal_prop = f"animal_kind={animal_kind}&animal_name={animal_name}"
        animal_obj = self.animal_objects[animal_kind + "_" + animal_name]
        params_values = animal_function.Animal.print_params(animal_obj)
        text_buttons = self.show_buttons(animal_prop)
        text_owner = self.owner_button(animal_prop)
        text_status = self.show_status(params_values)
        total_screen = f"""
        <div style="text-align:center">
            {text_buttons}
            <br><br>
            {text_owner}
            <br><br>
            {text_status}
        </div>
        """
        sum_text = animal_text + "\n" + total_screen
        return self.full_html(sum_text)

    def do_action(self, action, animal_kind, animal_name, params):
        """do specific action and change its properties"""
        animal_obj = self.animal_objects[animal_kind + "_" + animal_name]
        animal_function.Animal.choose_actions(animal_obj, action, params)
