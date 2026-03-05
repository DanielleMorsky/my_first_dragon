import html
import animal_function


def full_html(specific_site_content):
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


def home_screen():
    text = """
    <h2 style='text-align:center'>Welcome to animal viewing :)</h2>
    <br>
    <a href="http://127.0.0.1:8000/status"><h3 style='text-align:center'>press here to get to status page</h3></a>
    """
    return full_html(text)


def new_animal(animal_kind, animal_name):
    try:
        animal = animal_function.create_animal(animal_kind, animal_name)
        return animal
        # call this function from the one that contains the whole page of bottoms
    except Exception:
        text = "<h1 style='text-align:center'>wrong parameters</h1>"
        return full_html(text)


def show_bottoms(animal_kind, animal_name):
    animal = new_animal(animal_kind, animal_name)
    if type(animal) == str:
        return animal
    text = f"""
    <button onlink={animal_function.Animal.choose_actions(animal, "eat")}">Set bottom position to 100 px</a>
    """
    text = f"{id(animal)}"
    return text
