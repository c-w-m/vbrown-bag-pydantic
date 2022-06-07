import fastapi.responses
import uvicorn as uvicorn
from fastapi import FastAPI
from models.people import Address, Person

app = FastAPI()


@app.get("/")
def index():
    return fastapi.responses.HTMLResponse("<h1>SUPER simple API site</h1>Try it: <a href='/api'>/api</a>")


@app.post('/api', response_model=Address)
def api(person: Person):
    print(person)
    return person.address


if __name__ == '__main__':
    uvicorn.run(app)
