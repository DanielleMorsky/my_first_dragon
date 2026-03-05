from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse, RedirectResponse
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
def update_action(action, animal_kind, animal_name):
    my_web.do_action(action, animal_kind, animal_name)
    return RedirectResponse(f"http://127.0.0.1:8000/status/{animal_kind}/{animal_name}", status_code=status.HTTP_303_SEE_OTHER)

