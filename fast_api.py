from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import ctypes

import animal_function
import design_web
app = FastAPI()
my_web = design_web.WebAnimal()

@app.get("/")
def read_root():
    return HTMLResponse(content=my_web.home_screen(), status_code=200)


@app.get("/status/{animal_kind}/{animal_name}")
def get_buttons_screen(animal_kind, animal_name):
    return HTMLResponse(content=my_web.show_bottoms(animal_kind, animal_name), status_code=200)

@app.get("/{action}")
def update_action(action, animal_description):
    return HTMLResponse(content=my_web.do_action(action, animal_description), status_code=200)
#     animal_object = ctypes.cast( ctypes.py_object).value
#     print(animal_object)
#     return str(animal_object) + action
#     #main.Animal.choose_actions(animal_object, action)

    # animal == self(the object)
    # TODO understand how to convert the object to string for the url and then back to the same object (read about pickle)
