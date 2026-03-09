from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse, RedirectResponse
import design_web

app = FastAPI()
my_web = design_web.WebAnimal()
IP = "127.0.0.1"
PORT = 8000
my_url = f"http://{IP}:{PORT}/"


@app.get("/")
def read_root():
    """display the home screen"""
    return HTMLResponse(content=my_web.home_screen(), status_code=200)


@app.get("/status/{animal_kind}/{animal_name}")
def get_buttons_screen(animal_kind, animal_name):
    """display a status screen of specific animal"""
    con = my_web.get_status_screen(animal_kind, animal_name)
    return HTMLResponse(content=con, status_code=200)


@app.get("/{action}")
def update_action(action, animal_kind, animal_name, params=None):
    """update animal properties by the specific action"""
    con = my_web.do_action(action, animal_kind, animal_name, params)
    # redirect = f"window.location.href=/status/{animal_kind}/{animal_name}"
    # return RedirectResponse(redirect, status_code=status.HTTP_303_SEE_OTHER)
    return HTMLResponse(content=con, status_code=200)