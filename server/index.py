from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from routers.splendor.router import router as splendor_router


app = FastAPI()
# https://stackoverflow.com/questions/73917396/why-doesnt-uvicorn-pick-up-changes-to-css-files
app.mount(
    "/css",
    StaticFiles(directory=Path(__file__).parent.parent.absolute() / "css"),
    name="css",
)

app.include_router(splendor_router)


@app.get("/", response_class=RedirectResponse)
def redirect_splendor(request: Request):
    return RedirectResponse("/splendor/new-waiting-room")


# TODO:
# File "/Users/mattzhang/Projects/splendor_bot/server/index.py", line 6, in <module>
    # from routers import splendor_router
# ModuleNotFoundError: No module named 'routers'
