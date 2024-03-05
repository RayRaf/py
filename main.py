from fastapi import FastAPI



app = FastAPI()


@app.get("/")
async def main_page():
    return "Main page from main branch!"

@app.get("/home")
async def get_home():
    return "Hello World"


@app.get("/about")
def get_home():
    return "About message"

@app.get("/hello")
def get_home():
    return "Hello from main branch"
