from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import design_web
app = FastAPI()


@app.get("/")
def read_root():
    return HTMLResponse(content=design_web.home_screen(), status_code=200)


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}
