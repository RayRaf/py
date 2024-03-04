from fastapi import FastAPI


app = FastAPI()


@app.get("/home")
async def get_home():
    return "Hello World"


@app.get("/about")
def get_home():
    return "About message"

