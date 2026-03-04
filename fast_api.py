from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import design_web
app = FastAPI()


@app.get("/")
def read_root():
    return HTMLResponse(content=design_web.home_screen(), status_code=200)


@app.get("/status")
def read_item():
    return HTMLResponse(content=design_web.new_animal(), status_code=200)
